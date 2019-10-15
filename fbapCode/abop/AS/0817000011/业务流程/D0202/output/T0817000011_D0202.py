# -*- coding: gbk -*-
'''
----------------------------------------------------------------
�ڲ����ƣ�AS
˵    �����������������
��    �ߣ�
��    ע����ͬ�Ƽ�AFA������V3.7.0.2_test 
�������꣺
    1. __REQ__   ---> ����������������������
    2. __RSP__   ---> ���׷�����������������
    3. __SND__   ---> �ͻ��˷�����������������
    4. __RCV__   ---> �ͻ��˽�����������������
    5. __TC__    ---> ���״���
    6. __MC__    ---> ��Ŀ����
----------------------------------------------------------------
'''


'''
import sys function:
'''
from copy      import deepcopy;
from types     import FunctionType;
from traceback import format_exc;

#import Logger function
from AFABuiltIn import LoggerDebug as AFALoggerDebug;
from AFABuiltIn import LoggerTrace as AFALoggerTrace;
from AFABuiltIn import LoggerInfor as AFALoggerInfor;
from AFABuiltIn import LoggerDump  as AFALoggerDump;
from AFABuiltIn import LoggerError as AFALoggerError;

#import BuiltIn function
from AFABuiltIn import ACMP_Builtin_Object2Str;
from AFABuiltIn import ACMP_Builtin_LoggerVar;
from AFABuiltIn import ACMP_Builtin_SetGlobalError;
from AFABuiltIn import ACMP_Builtin_CheckRequest;
from AFABuiltIn import ACMP_Builtin_CheckResponse;
from AFABuiltIn import ACMP_Builtin_GetDefaultExceptNode;
from AFABuiltIn import ACMP_Builtin_SetDefaultExceptNode;
from AFABuiltIn import ACMP_Builtin_TradeInitialize;
from AFABuiltIn import ACMP_Builtin_BoolFrame;
from AFABuiltIn import ACMP_Builtin_DefaultErrorHolder;
from AFABuiltIn import ACMP_Builtin_SwitchCaseFrame;
from AFABuiltIn import ACMP_Builtin_SetValueToContext;
from AFABuiltIn import ACMP_Builtin_SetErrorToGlobal;
from AFABuiltIn import ACMP_Builtin_GetGlobalErrorToDict;
from AFABuiltIn import ACMP_Builtin_SwitchToAsyncMode;

#import dependent components
from B_ABOP_Trade import B_SetTradeFaild as B_ABOP_Trade_B_SetTradeFaild;
from B_ABOP_Trade import B_TradeSuccess as B_ABOP_Trade_B_TradeSuccess;
from B_ABOP_DB import B_DBDMLUpd as B_ABOP_DB_B_DBDMLUpd;
from B_ABOP_File import B_DealOneLineSeparativeSignInfo as B_ABOP_File_B_DealOneLineSeparativeSignInfo;
from B_ABOP_File import B_CloseTheFile as B_ABOP_File_B_CloseTheFile;
from B_ABOP_File import B_GetOneLineFromFile as B_ABOP_File_B_GetOneLineFromFile;
from B_ABOP_File import B_OpenTheFile as B_ABOP_File_B_OpenTheFile;
from B_ABOP_Dictionary import B_dict_setvalue as B_ABOP_Dictionary_B_dict_setvalue;
from B_ABOP_DB import B_DBDMLSelForPlaceholder as B_ABOP_DB_B_DBDMLSelForPlaceholder;
from B_ABOP_BatchCheck import B_CheckTheChoiceableField as B_ABOP_BatchCheck_B_CheckTheChoiceableField;
from B_ABOP_BatchCheck import B_IndispensableFieldCheck as B_ABOP_BatchCheck_B_IndispensableFieldCheck;
from B_ABOP_Time import B_time_get as B_ABOP_Time_B_time_get;



'''
--------------------------- ��Ŀ���� ---------------------------
��    �ƣ�0817000011
��    �����ϲ�һ��ͨ��������
----------------------------------------------------------------
'''


def TD0202_STEP1_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0202_STEP1_NODE2;

def TD0202_STEP1_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0202_STEP1_NODE6);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0202_STEP1_NODE6 �ڵ�");

    return TD0202_STEP1_NODE3;

def TD0202_STEP1_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ����ʱ��");


        _Result_ = B_ABOP_Time_B_time_get();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["CurrentDate"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["CurrentDate"]);
            __REQ__["CurrentTime"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["CurrentTime"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP1_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP1_NODE6);

def TD0202_STEP1_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ֶκϷ��Լ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [ ["REQBODY","AppType","STRING",20], ["REQBODY","AppID","STRING",20], ["REQBODY","AgreementID","STRING",20], ["REQBODY","CustBatchID","CHAR",16], ["REQBODY","IsUrgent","CHAR",1], ["REQBODY","IsRealTimeDeal","CHAR",1],["REQBODY","BankBranchID","STRING",10], ["REQBODY","ChannelID","STRING",10], ["REQBODY","ExcuteStatus","CHAR",2], ["REQBODY","Status","CHAR",1], ["REQBODY","IsBatchClear","CHAR",1], ["REQBODY","RuleModeID","STRING",10], ["REQBODY","BatchFilePath","STRING",128], ["REQBODY","BatchFileName","STRING",128], ["REQBODY","TotalRecord","STRING",10], ["REQBODY","TotalAmount","STRING",17], ["REQBODY","ScuRecord","STRING",10], ["REQBODY","ScuAmount","STRING",17], ["REQBODY","NearstDate","CHAR",8], ["REQBODY","NearstTime","CHAR",6] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_BatchCheck_B_IndispensableFieldCheck(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP1_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP1_NODE6);

def TD0202_STEP1_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ѡ���ֶ�У��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [ ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_BatchCheck_B_CheckTheChoiceableField(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP1_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP1_NODE6);

def TD0202_STEP1_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0202_STEP1_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0202_STEP1_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 1 ���� ����У��");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0202_STEP1_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0202_STEP2_IMPL;
        else:
            return TD0202_STEP6_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0202_STEP2_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ѯǩԼ��Ϣ");

        _Arg0_ = "select  protocolno from afa_memy_protocolinfo  where   protocolstatus=? and productmaincode=?  and productcode=? and clienttype=?  and protocolno=?";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = ["A2","AS","0817000011","0",__REQ__["__BODY__"]["AgreementID"],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TEMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TEMP"]);
            __REQ__["AgreeMentInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["AgreeMentInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP2_NODE8;
        elif(_Result_[0] == 2): 
            return TD0202_STEP2_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP2_NODE4);

def TD0202_STEP2_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "OP10";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "Э���У��δͨ��"+__REQ__["__BODY__"]["AgreementID"]+"!="+"�ܹ�˾Э��ţ�"+__REQ__["AgreementID"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP2_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP2_NODE4);

def TD0202_STEP2_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0202_STEP2_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0202_STEP2_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0202_STEP2_NODE7;

def TD0202_STEP2_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0202_STEP2_NODE4);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0202_STEP2_NODE4 �ڵ�");

    return TD0202_STEP2_NODE1;

def TD0202_STEP2_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������Ϣ��ʼ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [	["Count",0],	["Amount",0.00],	["LineNo",0]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP2_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP2_NODE4);

def TD0202_STEP2_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 2 ���� ����׼��");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0202_STEP2_NODE6;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0202_STEP3_IMPL;
        else:
            return TD0202_STEP6_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0202_STEP3_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0202_STEP3_NODE2;

def TD0202_STEP3_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0202_STEP3_NODE3);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0202_STEP3_NODE3 �ڵ�");

    return TD0202_STEP3_NODE5;

def TD0202_STEP3_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �رմ򿪵��ļ�");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "BatchFile";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0202_STEP3_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �������ļ�");

        _Arg0_ = __REQ__["__BODY__"]["BatchFilePath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["__BODY__"]["BatchFileName"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "r";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_OpenTheFile(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["BatchFile"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["BatchFile"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡһ������");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "BatchFile";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_GetOneLineFromFile(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["OneInfo"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["OneInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE8;
        elif(_Result_[0] == 2): 
            return TD0202_STEP3_NODE14;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ݷָ���б�");

        _Arg0_ = __REQ__["OneInfo"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "|";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_DealOneLineSeparativeSignInfo(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["OneInfoList"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["OneInfoList"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �кŵ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "LineNo";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["LineNo"]+1;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ϸ��ʽУ��");

        _Arg0_ = (len(__REQ__["OneInfoList"]) == 4) and(len(__REQ__["OneInfoList"][0])==10 and __REQ__["OneInfoList"][0].strip() != "") and (len(__REQ__["OneInfoList"][1])==18 and __REQ__["OneInfoList"][1].strip() != "") and ( __REQ__["OneInfoList"][3].strip() != "");
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0202_STEP3_NODE10;
        elif(_Result_[0] == 1): 
            return TD0202_STEP3_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "OP30";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "��"+str(__REQ__["LineNo"])+"�����ݸ�ʽ�������飡";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ѧУ�����Ƿ�����");

        _Arg0_ = int(__REQ__["__BODY__"]["AgreementID"]) == int(__REQ__["OneInfoList"][0]);
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0202_STEP3_NODE12;
        elif(_Result_[0] == 1): 
            return TD0202_STEP3_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "OP30";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "��"+str(__REQ__["LineNo"])+"������ѧУ����������飡";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������Ϣ�ۼ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [	["Count",__REQ__["Count"]+1],	["Amount","%.2f"%(float(__REQ__["Amount"])+float(__REQ__["OneInfoList"][3]))]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �رմ򿪵��ļ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "BatchFile";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� У����Ч���ݼ�¼");

        _Arg0_ = int(__REQ__["Count"]) <> 0;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0202_STEP3_NODE17;
        elif(_Result_[0] == 1): 
            return TD0202_STEP3_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "OP30";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "������Ч����Ϊ0�������飡";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "OP30";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "�����ļ��ܽ�����ܱ����������Ϣ����������飡";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP3_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� У����ܼ�¼");

        _Result_ = [1, None, None, []];

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0202_STEP3_NODE18;
        elif(_Result_[0] == 1): 
            return TD0202_STEP3_NODE21;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP3_NODE4);

def TD0202_STEP3_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0202_STEP3_NODE21(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0202_STEP3_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 3 ���� �ļ���ϢУ��");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0202_STEP3_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0202_STEP4_IMPL;
        else:
            return TD0202_STEP6_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0202_STEP4_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0202_STEP4_NODE2;

def TD0202_STEP4_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0202_STEP4_NODE4);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0202_STEP4_NODE4 �ڵ�");

    return TD0202_STEP4_NODE3;

def TD0202_STEP4_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������״̬");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["ExcuteStatus","21"], ["Status","1"], ["ErroCode","0000"], ["ErroMsg","�ļ�У��ɹ���"],["TotalRecords",str(__REQ__["Count"])],["TotalAmount",str(__REQ__["Amount"])],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["CustBatchID","=",__REQ__["__BODY__"]["CustBatchID"],None] ];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = True;
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = B_ABOP_DB_B_DBDMLUpd(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP4_NODE5;
        elif(_Result_[0] == 2): 
            return TD0202_STEP4_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP4_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP4_NODE4);

def TD0202_STEP4_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0202_STEP4_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0202_STEP4_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "��������״̬ʱ��������Ĵ���!Ӱ������μ�¼��Ϊ0";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP4_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP4_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP4_NODE4);

def TD0202_STEP4_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 4 ���� ����״̬����");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0202_STEP4_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0202_STEP5_IMPL;
        else:
            return TD0202_STEP6_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0202_STEP5_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0202_STEP5_NODE4;

def TD0202_STEP5_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0202_STEP5_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ý���ִ�гɹ�");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");

        _Result_ = B_ABOP_Trade_B_TradeSuccess(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP5_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP5_NODE2);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP5_NODE2);

def TD0202_STEP5_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0202_STEP5_NODE2);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0202_STEP5_NODE2 �ڵ�");

    return TD0202_STEP5_NODE3;

def TD0202_STEP5_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0202_STEP5_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 5 ���� ��������");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0202_STEP5_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        return (_Method_ == True);
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0202_STEP6_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0202_STEP6_NODE2;

def TD0202_STEP6_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0202_STEP6_NODE7);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0202_STEP6_NODE7 �ڵ�");

    return TD0202_STEP6_NODE9;

def TD0202_STEP6_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡȫ�ִ�������");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "ErrorType";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "ErrorCode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "ErrorMsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP6_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

def TD0202_STEP6_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �жϴ�����Ϣ����");

        _Arg0_ = len(__REQ__["ErrorMsg"])>127;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0202_STEP6_NODE6;
        elif(_Result_[0] == 1): 
            return TD0202_STEP6_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

def TD0202_STEP6_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������Ϣ��ֵ");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "ErrorMsg";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["ErrorMsg"][:127];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP6_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

def TD0202_STEP6_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ý���ִ��ʧ��");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");
        _Arg1_ = __REQ__["ErrorCode"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["ErrorMsg"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_Trade_B_SetTradeFaild(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP6_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

def TD0202_STEP6_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0202_STEP6_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0202_STEP6_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������״̬");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["ExcuteStatus","21"], ["Status","9"], ["ErroCode","FBAP"], ["ErroMsg","�ļ����鲻�ɹ�"],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["CustBatchID","=",__REQ__["__BODY__"]["CustBatchID"],None] ];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = True;
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = B_ABOP_DB_B_DBDMLUpd(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0202_STEP6_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0202_STEP6_NODE7);

def TD0202_STEP6_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 6 ���� �쳣����");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0202_STEP6_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        return (_Method_ == True);
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

'''
------------------------- ������ں��� -------------------------
'''
def MD0202_ENTRY(__REQ__,__RSP__):
    AFALoggerInfor("��ʼ���� D0202:�����ļ�У��");

    __SND__ = {};
    __RCV__ = {};

    __REQ__["__TRADENAME__"] = "�����ļ�У��";

    ACMP_Builtin_TradeInitialize(__REQ__,__RSP__,"KAS_SSK");

    _Result_ = None;
    _Method_ = TD0202_STEP1_IMPL;
    while(type(_Method_) is FunctionType):
        AFALoggerInfor(("Step "+getattr(_Method_,"__name__")));
        _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
        _Method_ = _Result_;

    __SND__.clear();
    __RCV__.clear();
    del __SND__;
    del __RCV__;

    ACMP_Builtin_CheckResponse(__REQ__,__RSP__);
    AFALoggerInfor("�������� D0202");

    return True;
