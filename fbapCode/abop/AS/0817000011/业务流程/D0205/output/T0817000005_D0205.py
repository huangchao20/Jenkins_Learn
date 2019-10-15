# -*- coding: gbk -*-
'''
----------------------------------------------------------------
�ڲ����ƣ�OP
˵    ������������ɷ���
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
from B_ABOP_File import B_RenameFIle as B_ABOP_File_B_RenameFIle;
from B_ABOP_DB import B_ABOP_GetTheTableCircleCursor as B_ABOP_DB_B_ABOP_GetTheTableCircleCursor;
from B_ABOP_DB import B_ABOP_FetchOneRecord as B_ABOP_DB_B_ABOP_FetchOneRecord;
from B_ABOP_File import B_WriteOneLine as B_ABOP_File_B_WriteOneLine;
from B_ABOP_File import B_OpenTheFile as B_ABOP_File_B_OpenTheFile;
from B_ABOP_File import B_WriteHeadToSrcFile as B_ABOP_File_B_WriteHeadToSrcFile;
from B_ABOP_DB import B_SearchLinesIntoDelFile as B_ABOP_DB_B_SearchLinesIntoDelFile;
from B_ABOP_Dictionary import B_dict_setvalue as B_ABOP_Dictionary_B_dict_setvalue;
from B_ABOP_File import B_CloseTheFile as B_ABOP_File_B_CloseTheFile;
from B_ABOP_File import B_GetOneLineFromDelFile as B_ABOP_File_B_GetOneLineFromDelFile;
from B_ABOP_Commom_Auto import B_GetSysPath as B_ABOP_Commom_Auto_B_GetSysPath;
from B_ABOP_DB import B_DBDMLSel as B_ABOP_DB_B_DBDMLSel;
from B_ABOP_DB import B_DBDMLUpd as B_ABOP_DB_B_DBDMLUpd;
from B_ABOP_DB import B_db_sequence as B_ABOP_DB_B_db_sequence;
from B_ABOP_File import B_CreatePath as B_ABOP_File_B_CreatePath;
from B_ABOP_DB import B_DBDMLSelForPlaceholder as B_ABOP_DB_B_DBDMLSelForPlaceholder;
from B_SCNX_CFG import B_GetCoreCfg as B_SCNX_CFG_B_GetCoreCfg;
from B_ABOP_Commom_Auto import B_GetSysParameterValue as B_ABOP_Commom_Auto_B_GetSysParameterValue;
from B_ABOP_Commom_Auto import B_GetTheOverallSituationCfg as B_ABOP_Commom_Auto_B_GetTheOverallSituationCfg;
from B_ABOP_Time import B_GetMicrosecondTime as B_ABOP_Time_B_GetMicrosecondTime;
from B_ABOP_BatchCheck import B_IndispensableFieldCheck as B_ABOP_BatchCheck_B_IndispensableFieldCheck;



'''
--------------------------- ��Ŀ���� ---------------------------
��    �ƣ�0817000005
��    ������¤��Դˮ�Ѵ���
----------------------------------------------------------------
'''


def TD0205_STEP1_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0205_STEP1_NODE2;

def TD0205_STEP1_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0205_STEP1_NODE6);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0205_STEP1_NODE6 �ڵ�");

    return TD0205_STEP1_NODE3;

def TD0205_STEP1_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ֶκϷ��Լ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [ ["REQBODY","AppType","STRING",20], ["REQBODY","AppID","STRING",20], ["REQBODY","BranchID","STRING",10], ["REQBODY","ChannelID","STRING",10], ["REQBODY","SysBatchID","CHAR",16], ["REQBODY","HostCfgID","CHAR",8], ["REQBODY","HostExcuteType","CHAR",1], ["REQBODY","IsBatchClear","CHAR",1], ["REQBODY","RuleModeID","CHAR",10], ["REQBODY","PropertyValue","STRING",512], ["REQBODY","HostBatchID","CHAR",16], ["REQBODY","IsUrgent","CHAR",1], ["REQBODY","IsRealTimeDeal","CHAR",1], ["REQBODY","CurrentSeries","CHAR",1], ["REQBODY","HostType","CHAR",2], ["REQBODY","HostID","CHAR",4], ["REQBODY","BatchType","CHAR",1], ["REQBODY","ExcuteStatus","CHAR",2], ["REQBODY","OnLineMsgStatus","CHAR",2], ["REQBODY","HostFileDealStatus","CHAR",2], ["REQBODY","HostFilePath","STRING",128], ["REQBODY","HostFileName","STRING",128], ["REQBODY","HostRsltFilePath","STRING",128], ["REQBODY","HostRsltFileName","STRING",128], ["REQBODY","NearOperateDate","CHAR",8], ["REQBODY","NearOperateTime","CHAR",6], ["REQBODY","ErrorCode","CHAR",6], ["REQBODY","ErrorMsg","STRING",256] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_BatchCheck_B_IndispensableFieldCheck(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP1_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP1_NODE6);

def TD0205_STEP1_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ���뼶ϵͳʱ��");


        _Result_ = B_ABOP_Time_B_GetMicrosecondTime();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["CurrentDate"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["CurrentDate"]);
            __REQ__["CurrentTime"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["CurrentTime"]);
            __REQ__["CurrentMSecond"] = _RTVAL_[2];
            ACMP_Builtin_LoggerVar(4,"O2",__REQ__["CurrentMSecond"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP1_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP1_NODE6);

def TD0205_STEP1_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡ������ر�ʶ");


        _Result_ = B_ABOP_Commom_Auto_B_GetTheOverallSituationCfg();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["LocalHost_Cfg"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["LocalHost_Cfg"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP1_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP1_NODE6);

def TD0205_STEP1_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0205_STEP1_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0205_STEP1_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 1 ���� ���ݺϷ���У��");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0205_STEP1_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0205_STEP2_IMPL;
        else:
            return TD0205_STEP8_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0205_STEP2_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0205_STEP2_NODE3;

def TD0205_STEP2_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡϵͳ������ֵ");

        _Arg0_ = "TheRecordThresholdForLoad";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_Commom_Auto_B_GetSysParameterValue(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TheRecordThresholdForLoad"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TheRecordThresholdForLoad"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP2_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP2_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP2_NODE5);

def TD0205_STEP2_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0205_STEP2_NODE5);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0205_STEP2_NODE5 �ڵ�");

    return TD0205_STEP2_NODE2;

def TD0205_STEP2_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0205_STEP2_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0205_STEP2_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 2 ���� ����ֵ��ȡ");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0205_STEP2_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0205_STEP3_IMPL;
        else:
            return TD0205_STEP8_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0205_STEP3_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0205_STEP3_NODE2;

def TD0205_STEP3_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0205_STEP3_NODE9);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0205_STEP3_NODE9 �ڵ�");

    return TD0205_STEP3_NODE3;

def TD0205_STEP3_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡʵ�ʱ���");

        _Arg0_ = "select count(LineNo) from BPDM_OP_LZGasPayment where HostBatchID= ? and CurrentSeries = ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["HostBatchID"], __REQ__["__BODY__"]["CurrentSeries"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["Total"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["Total"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �жϱ����Ƿ�Ϊ0");

        _Arg0_ = __REQ__["Total"][0][0]!=0;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0205_STEP3_NODE5;
        elif(_Result_[0] == 1): 
            return TD0205_STEP3_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "���ݿ���ϵͳ���и��������¿ɲ�����¼��Ϊ0";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ɲ�����¼�Ƿ���ڷ�ֵ");

        _Arg0_ = __REQ__["Total"][0][0] > int(__REQ__["TheRecordThresholdForLoad"]);
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0205_STEP3_NODE7;
        elif(_Result_[0] == 1): 
            return TD0205_STEP3_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "CrtType";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "Fetch";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "CrtType";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "DBLoad";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0205_STEP3_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���кŲ���");

        _Arg0_ = "SEQ_HNHostNo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 5;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["SEQ_HNHostNo"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["SEQ_HNHostNo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ��Ч����");

        _Arg0_ = "select LineNo,  UserID, ArrearageMoney from BPDM_OP_LZGasPayment  where  HostBatchID='"+__REQ__["__BODY__"]["HostBatchID"]+"' and  RecordStatus!='E' and CurrentSeries = '"+__REQ__["__BODY__"]["CurrentSeries"]+ "' order by LineNo ASC";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 0;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_DBDMLSel(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["TMPLIST"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["TMPLIST"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE22;
        elif(_Result_[0] == 2): 
            return TD0205_STEP3_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ѯ�ڲ��˻���Ϣ");

        _Arg0_ = "select 	a.protocolno,	a.signbrno,	b.AgreementID,	b.BranchID,	b.BankIndoorAcct,	b.BankIndoorAcctName from afa_memy_protocolinfo a join ABOP_AppBatchIndoorAcctInfo b on a.protocolno = b.AgreementID where a.protocolstatus = ? and 	  a.protocolno = ? and 	  a.productcode = ? and 	  b.BankAccType = ? and 	  b.AppType = ? and 	  b.AppID = ? and 	  b.BranchID = ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = ["A2",__REQ__["__BODY__"]["AgreementID"],__REQ__["__BODY__"]["AppID"],"1",__REQ__["__BODY__"]["AppType"],__REQ__["__BODY__"]["AppID"],__REQ__["__BODY__"]["BranchID"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TEMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TEMP"]);
            __REQ__["AcctInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["AcctInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ļ�Ϊ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "CrtType";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "ISNULL";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE22;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ�����ļ���������");


        _Result_ = B_SCNX_CFG_B_GetCoreCfg();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["MsgSystemDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["MsgSystemDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ļ�·��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostBatchFilePath";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["MsgSystemDict"]["ReqPath"]+__REQ__["__BODY__"]["BranchID"][:2]+"/"+__REQ__["__BODY__"]["BranchID"]+"/";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE18;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���������ļ�����");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostBatchFile";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "ABOP_"+__REQ__["__BODY__"]["AppType"]+__REQ__["__BODY__"]["HostBatchID"]+__REQ__["__BODY__"]["CurrentSeries"]+".fbaptmp";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ׼�������ļ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostBatchFileNew";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["HostBatchFile"][:-8];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE23;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ʧ��������ϸ");

        _Arg0_ = "BPDM_OP_LZGasPayment";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["CurrentSeries","0"],["RecordStatus","E"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["HostBatchID","=",__REQ__["__BODY__"]["HostBatchID"],"and"], ["ErrorCode","=","FFFF",None]];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = True;
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = B_ABOP_DB_B_DBDMLUpd(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TEMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TEMP"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE11;
        elif(_Result_[0] == 2): 
            return TD0205_STEP3_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_NODE22(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0205_STEP3_NODE23(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����·��");

        _Arg0_ = __REQ__["HostBatchFilePath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_File_B_CreatePath(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP3_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP3_NODE9);

def TD0205_STEP3_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 3 ���� ȷ���ļ����ɷ�ʽ");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0205_STEP3_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0205_STEP4_IMPL;
        else:
            return TD0205_STEP8_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0205_STEP4_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0205_STEP4_NODE3;

def TD0205_STEP4_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ļ���ȡ�ķ�ʽ");

        _Arg0_ = __REQ__["CrtType"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "Fetch";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "DBLoad";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "ISNULL";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0205_STEP4_NODE5;
        elif(_Result_[0] == 1): 
            return TD0205_STEP4_NODE24;
        elif(_Result_[0] == 2): 
            return TD0205_STEP4_NODE4;
        elif(_Result_[0] == 3): 
            return TD0205_STEP4_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0205_STEP4_NODE7);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0205_STEP4_NODE7 �ڵ�");

    return TD0205_STEP4_NODE2;

def TD0205_STEP4_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡϵͳ��ʱ·��");

        _Arg0_ = "DBLoaderTmpPath";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["__BODY__"]["AppType"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["__BODY__"]["AppID"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = __REQ__["__BODY__"]["BranchID"];
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = B_ABOP_Commom_Auto_B_GetSysPath(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["DBLoaderTmpPath"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["DBLoaderTmpPath"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ����ڽ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "�����ļ��ķ�ʽֻ����Ϊ Fetch��DBload���ַ�ʽ";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡϵͳ��ʱ�ļ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostDBLoad";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["HostBatchFile"]+"HostDBLoad";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �رմ򿪵��ļ�");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "DbFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0205_STEP4_NODE13;
        elif(_Result_[0] == 1): 
            return TD0205_STEP4_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �������������ݵ��ļ�");

        _Arg0_ = "BPDM_OP_LZGasPayment";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ "LineNo", "UserID", "ArrearageMoney"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["HostBatchID","=",__REQ__["__BODY__"]["HostBatchID"],"and"], ["RecordStatus","!=","E","and"],["CurrentSeries","=",__REQ__["__BODY__"]["CurrentSeries"],None] ];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = __REQ__["DBLoaderTmpPath"];
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = __REQ__["HostDBLoad"];
        ACMP_Builtin_LoggerVar(4,"A4",_Arg4_);

        _Result_ = B_ABOP_DB_B_SearchLinesIntoDelFile(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ݿ��ļ���ȡһ����¼");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "DbFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_GetOneLineFromDelFile(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["Record"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["Record"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE12;
        elif(_Result_[0] == 2): 
            return TD0205_STEP4_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ݿ��ļ�");

        _Arg0_ = __REQ__["DBLoaderTmpPath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["HostDBLoad"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "r";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_OpenTheFile(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["DbFileDesc"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["DbFileDesc"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� Э����Ϣ���ѯ");

        _Arg0_ = "select  accno, accname, documenttype, documentno  from afa_memy_protocolinfo  where protocolstatus=? and productcode=?  and  productmaincode=? and signinfo=?";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = ["A2",__REQ__["__BODY__"]["AppID"],__REQ__["__BODY__"]["AppType"],__REQ__["Record"][1]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TEMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TEMP"]);
            __REQ__["protocolInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["protocolInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE27;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �رմ򿪵��ļ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0205_STEP4_NODE17;
        elif(_Result_[0] == 1): 
            return TD0205_STEP4_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� д�ļ�ͷ��ָ���ļ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["headInfor"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_WriteHeadToSrcFile(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE18;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �������ļ�");

        _Arg0_ = __REQ__["HostBatchFilePath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["HostBatchFile"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "w";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_OpenTheFile(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["HostFileDesc"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["HostFileDesc"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE16(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ļ�ͷ��ֵ");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [	["headInfor",__REQ__["HostBatchFileNew"]+"|#|"+				 "1"+"|#|"+				 "0"+"|#|"+				 "0"+"|#|"+				 str(__REQ__["TotalAmount"])+"|#|"+				 str(__REQ__["TotalMoney"])+"|#|"+				 "1104"+"|#|"+				 "01"+"|#|"+				 "12345678"+"|#|"+				 "200"+"|#|"+				 "��¤��Դˮ����������"+"|#|"+				 __REQ__["AcctInfo"][0][4]	]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE14;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0205_STEP4_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �رմ򿪵��ļ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "DbFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE21;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ָ���ļ���д��һ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = " ".ljust(180)+"\n";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_WriteOneLine(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE22;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ָ���ļ���д��һ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["TmpInfo"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_WriteOneLine(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE23;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE21(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �رմ򿪵��ļ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE22(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ʼ���ܱ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "TotalAmount";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE25;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE23(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ܱ����ۼ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "TotalAmount";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = int(__REQ__["TotalAmount"])+1;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE26;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE24(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0205_STEP4_NODE25(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ʼ���ܽ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "TotalMoney";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0.0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE26(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ܽ���ۼ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "TotalMoney";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = float(__REQ__["TotalMoney"])+float(__REQ__["Record"][2]);
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_NODE27(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ļ���ϸ��ֵ");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [	["TmpInfo",__REQ__["Record"][0] + "|#|" +			   __REQ__["protocolInfo"][0][0] + "|#|" +			   __REQ__["protocolInfo"][0][1] + "|#|" +               __REQ__["protocolInfo"][0][2] + "|#|" +               __REQ__["protocolInfo"][0][3] + "|#|" +               "0" + "|#|" +               __REQ__["Record"][2]	]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP4_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP4_NODE17);

def TD0205_STEP4_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 4 ���� ���������ļ�");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0205_STEP4_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0205_STEP5_IMPL;
        else:
            return TD0205_STEP8_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0205_STEP5_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0205_STEP5_NODE2;

def TD0205_STEP5_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0205_STEP5_NODE9);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0205_STEP5_NODE9 �ڵ�");

    return TD0205_STEP5_NODE3;

def TD0205_STEP5_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ļ���ȡ�ķ�ʽ");

        _Arg0_ = __REQ__["CrtType"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "Fetch";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "DBLoad";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "ISNULL";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0205_STEP5_NODE4;
        elif(_Result_[0] == 1): 
            return TD0205_STEP5_NODE10;
        elif(_Result_[0] == 2): 
            return TD0205_STEP5_NODE19;
        elif(_Result_[0] == 3): 
            return TD0205_STEP5_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ����ڽ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "�����ļ��ķ�ʽֻ����Ϊ Fetch��DBload���ַ�ʽ";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ָ���ļ���д��һ������");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = " ".ljust(180)+"\n";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_WriteOneLine(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ʼ���ܱ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "TotalAmount";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ʼ���ܽ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "TotalMoney";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0.0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡ��ѭ�����¼���α�");

        _Arg0_ = "select LineNo,  UserID, ArrearageMoney from BPDM_OP_LZGasPayment  where  HostBatchID='"+__REQ__["__BODY__"]["HostBatchID"]+"' and  RecordStatus!='E' and CurrentSeries = '"+__REQ__["__BODY__"]["CurrentSeries"]+ "' order by LineNo ASC";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_DB_B_ABOP_GetTheTableCircleCursor(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["DBCurr"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["DBCurr"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �رմ򿪵��ļ�");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0205_STEP5_NODE12;
        elif(_Result_[0] == 1): 
            return TD0205_STEP5_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �������ļ�");

        _Arg0_ = __REQ__["HostBatchFilePath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["HostBatchFile"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "w";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_OpenTheFile(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["HostFileDesc"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["HostFileDesc"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȡ��һ����¼");

        _Arg0_ = __REQ__["DBCurr"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_DB_B_ABOP_FetchOneRecord(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["Record"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["Record"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE14;
        elif(_Result_[0] == 2): 
            return TD0205_STEP5_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0205_STEP5_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ļ�ͷ��ֵ");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [	["headInfor",__REQ__["HostBatchFileNew"]+"|#|"+				 "1"+"|#|"+				 "0"+"|#|"+				 "0"+"|#|"+				 str(__REQ__["TotalAmount"])+"|#|"+				 str(__REQ__["TotalMoney"])+"|#|"+				 "1104"+"|#|"+				 "01"+"|#|"+				 "12345678"+"|#|"+				 "200"+"|#|"+				 "��¤��Դˮ����������"+"|#|"+				 __REQ__["AcctInfo"][0][4]	]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� Э����Ϣ���ѯ");

        _Arg0_ = "select  accno, accname, documenttype, documentno  from afa_memy_protocolinfo  where protocolstatus=? and productcode=?  and  productmaincode=? and signinfo=?";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = ["A2",__REQ__["__BODY__"]["AppID"],__REQ__["__BODY__"]["AppType"],__REQ__["Record"][1]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TEMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TEMP"]);
            __REQ__["protocolInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["protocolInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE22;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� д�ļ�ͷ��ָ���ļ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["headInfor"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_WriteHeadToSrcFile(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �رմ򿪵��ļ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ָ���ļ���д��һ������");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["TmpInfo"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_WriteOneLine(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0205_STEP5_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ܱ����ۼ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "TotalAmount";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = int(__REQ__["TotalAmount"])+1;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE21;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE21(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ܽ���ۼ�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "TotalMoney";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = float(__REQ__["TotalMoney"])+float(__REQ__["Record"][2]);
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_NODE22(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ļ���ϸ��ֵ");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [	["TmpInfo",__REQ__["Record"][0] + "|#|" +			   __REQ__["protocolInfo"][0][0] + "|#|" +			   __REQ__["protocolInfo"][0][1] + "|#|" +               __REQ__["protocolInfo"][0][2] + "|#|" +               __REQ__["protocolInfo"][0][3] + "|#|" +               "0" + "|#|" +               __REQ__["Record"][2]	]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP5_NODE18;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP5_NODE12);

def TD0205_STEP5_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 5 ���� ���������ļ�");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0205_STEP5_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0205_STEP6_IMPL;
        else:
            return TD0205_STEP8_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0205_STEP6_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0205_STEP6_NODE2;

def TD0205_STEP6_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0205_STEP6_NODE4);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0205_STEP6_NODE4 �ڵ�");

    return TD0205_STEP6_NODE7;

def TD0205_STEP6_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �޸�ָ���ļ�����");

        _Arg0_ = __REQ__["HostBatchFilePath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["HostBatchFile"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["HostBatchFileNew"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_RenameFIle(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP6_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP6_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP6_NODE4);

def TD0205_STEP6_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0205_STEP6_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ݸ���");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostFileDealStatus","11"], ["HostFilePath",__REQ__["HostBatchFilePath"]], ["HostFileName",__REQ__["HostBatchFileNew"]], ["NearOperateDate",__REQ__["CurrentDate"]], ["NearOperateTime",__REQ__["CurrentTime"]] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["HostBatchID","=",__REQ__["__BODY__"]["HostBatchID"],None] ];
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
            return TD0205_STEP6_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP6_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP6_NODE4);

def TD0205_STEP6_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0205_STEP6_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ļ���ȡ�ķ�ʽ");

        _Arg0_ = __REQ__["CrtType"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "Fetch";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "DBLoad";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "ISNULL";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0205_STEP6_NODE4;
        elif(_Result_[0] == 1): 
            return TD0205_STEP6_NODE3;
        elif(_Result_[0] == 2): 
            return TD0205_STEP6_NODE3;
        elif(_Result_[0] == 3): 
            return TD0205_STEP6_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP6_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP6_NODE4);

def TD0205_STEP6_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ݸ���");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["TotalRecords","0"],["TotalAmount","0.0"],["SucRecords","0"],["SucAmount","0.0"],["HostFileDealStatus","41"], ["HostFilePath",""], ["HostFileName",""], ["NearOperateDate",__REQ__["CurrentDate"]], ["NearOperateTime",__REQ__["CurrentTime"]] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["HostBatchID","=",__REQ__["__BODY__"]["HostBatchID"],None] ];
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
            return TD0205_STEP6_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP6_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP6_NODE4);

def TD0205_STEP6_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 6 ���� �޸�����״̬");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0205_STEP6_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0205_STEP7_IMPL;
        else:
            return TD0205_STEP8_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0205_STEP7_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0205_STEP7_NODE2;

def TD0205_STEP7_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0205_STEP7_NODE4);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0205_STEP7_NODE4 �ڵ�");

    return TD0205_STEP7_NODE3;

def TD0205_STEP7_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ý���ִ�гɹ�");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");

        _Result_ = B_ABOP_Trade_B_TradeSuccess(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0205_STEP7_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP7_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP7_NODE4);

def TD0205_STEP7_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0205_STEP7_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0205_STEP7_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 7 ���� ��������");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0205_STEP7_NODE1;
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

def TD0205_STEP8_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0205_STEP8_NODE2;

def TD0205_STEP8_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0205_STEP8_NODE5);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0205_STEP8_NODE5 �ڵ�");

    return TD0205_STEP8_NODE3;

def TD0205_STEP8_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡȫ�ִ����������ڽ���");

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
            return TD0205_STEP8_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP8_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP8_NODE5);

def TD0205_STEP8_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0205_STEP8_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP8_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0205_STEP8_NODE5);

def TD0205_STEP8_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0205_STEP8_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0205_STEP8_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 8 ���� �쳣����");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0205_STEP8_NODE1;
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
def MD0205_ENTRY(__REQ__,__RSP__):
    AFALoggerInfor("��ʼ���� D0205:ˮ�Ѵ��������ļ�����");

    __SND__ = {};
    __RCV__ = {};

    __REQ__["__TRADENAME__"] = "ˮ�Ѵ��������ļ�����";

    ACMP_Builtin_TradeInitialize(__REQ__,__RSP__,"KOP_SSK");

    _Result_ = None;
    _Method_ = TD0205_STEP1_IMPL;
    while(type(_Method_) is FunctionType):
        AFALoggerInfor(("Step "+getattr(_Method_,"__name__")));
        _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
        _Method_ = _Result_;

    __SND__.clear();
    __RCV__.clear();
    del __SND__;
    del __RCV__;

    ACMP_Builtin_CheckResponse(__REQ__,__RSP__);
    AFALoggerInfor("�������� D0205");

    return True;
