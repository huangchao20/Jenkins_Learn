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
from B_ABOP_Socket import B_CreatTCPSocketClint as B_ABOP_Socket_B_CreatTCPSocketClint;
from B_ABOP_DB import B_db_sequence as B_ABOP_DB_B_db_sequence;
from B_ABOP_Dict import B_InitReqBody as B_ABOP_Dict_B_InitReqBody;
from B_SCNX_MapDefine import B_GetSystemCfg as B_SCNX_MapDefine_B_GetSystemCfg;
from B_SCNX_MapDefine import B_ABOPClientModleUnPack as B_SCNX_MapDefine_B_ABOPClientModleUnPack;
from B_SCNX_MapDefine import B_RteunCommonDict as B_SCNX_MapDefine_B_RteunCommonDict;
from B_ABOP_Socket import B_ABOP_Socket_Reacv as B_ABOP_Socket_B_ABOP_Socket_Reacv;
from B_ABOP_Socket import B_ABOP_SocketSent as B_ABOP_Socket_B_ABOP_SocketSent;
from B_ABOP_DB import B_DBDMLSelForPlaceholder as B_ABOP_DB_B_DBDMLSelForPlaceholder;
from B_SCNX_MapDefine import B_ABOPClientModlePack as B_SCNX_MapDefine_B_ABOPClientModlePack;
from B_ABOP_File import B_CheckFileExistAndIsFile as B_ABOP_File_B_CheckFileExistAndIsFile;
from B_SCNX_CFG import B_GetCoreCfg as B_SCNX_CFG_B_GetCoreCfg;
from B_ABOP_Commom_Auto import B_GetTheOverallSituationCfg as B_ABOP_Commom_Auto_B_GetTheOverallSituationCfg;
from B_ABOP_Time import B_GetMicrosecondTime as B_ABOP_Time_B_GetMicrosecondTime;
from B_ABOP_BatchCheck import B_IndispensableFieldCheck as B_ABOP_BatchCheck_B_IndispensableFieldCheck;



'''
--------------------------- ��Ŀ���� ---------------------------
��    �ƣ�0817000011
��    �����ϲ�һ��ͨ��������
----------------------------------------------------------------
'''


def TD0206_STEP1_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0206_STEP1_NODE2;

def TD0206_STEP1_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0206_STEP1_NODE6);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0206_STEP1_NODE6 �ڵ�");

    return TD0206_STEP1_NODE3;

def TD0206_STEP1_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0206_STEP1_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP1_NODE6);

def TD0206_STEP1_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0206_STEP1_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP1_NODE6);

def TD0206_STEP1_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0206_STEP1_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP1_NODE6);

def TD0206_STEP1_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0206_STEP1_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0206_STEP1_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 1 ���� ���ݺϷ�У��");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0206_STEP1_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0206_STEP2_IMPL;
        else:
            return TD0206_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0206_STEP2_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0206_STEP2_NODE6;

def TD0206_STEP2_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ļ�·��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostBatchFilePath";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["MsgSystemDict"]["ReqSucPath"]+__REQ__["__BODY__"]["BranchID"][:2]+"/"+__REQ__["__BODY__"]["BranchID"]+"/";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP2_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

def TD0206_STEP2_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���������ļ�����");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostBatchFileName";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["__BODY__"]["HostFileName"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP2_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

def TD0206_STEP2_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0206_STEP2_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0206_STEP2_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0206_STEP2_NODE4);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0206_STEP2_NODE4 �ڵ�");

    return TD0206_STEP2_NODE7;

def TD0206_STEP2_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0206_STEP2_NODE2;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

def TD0206_STEP2_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ж��ļ��Ƿ����");

        _Arg0_ = __REQ__["HostBatchFilePath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["HostBatchFileName"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CheckFileExistAndIsFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0206_STEP2_NODE9;
        elif(_Result_[0] == 1): 
            return TD0206_STEP2_NODE9;
        elif(_Result_[0] == 2): 
            return TD0206_STEP2_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

def TD0206_STEP2_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ִ��1510����");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "gotoThird";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "0";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP2_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

def TD0206_STEP2_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ִ��1510����");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "gotoThird";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "1";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP2_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP2_NODE4);

def TD0206_STEP2_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 2 ���� ����׼��");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0206_STEP2_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0206_STEP3_IMPL;
        else:
            return TD0206_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0206_STEP3_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0206_STEP3_NODE3;

def TD0206_STEP3_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ִ��1510����(0N/1Y)");

        _Arg0_ = __REQ__["gotoThird"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "0";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "1";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
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

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE7;
        elif(_Result_[0] == 2): 
            return TD0206_STEP3_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0206_STEP3_NODE15);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0206_STEP3_NODE15 �ڵ�");

    return TD0206_STEP3_NODE2;

def TD0206_STEP3_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡƽ̨��ˮ��Ϣ");

        _Arg0_ = "SQ_PLATSEQNO";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 8;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["PlatformSeq"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["PlatformSeq"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ������Ա��Ϣ");

        _Arg0_ = "select  A.VMTELLETER, A.BRANCHID from ABOP_APPBATCHINDOORACCTINFO A   join AFA_MEMY_PROTOCOLINFO B on A.BRANCHID=B.signbrno where  A.APPTYPE=? and  A.APPID=? and  A.BankAccType=? and B.PROTOCOLSTATUS=? and B.PRODUCTCODE=? and  B.PROTOCOLNO=?";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [__REQ__["__BODY__"]["AppType"],__REQ__["__BODY__"]["AppID"],'1','A2',__REQ__["__BODY__"]["AppID"],__REQ__["__BODY__"]["AgreementID"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["Temp"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["Temp"]);
            __REQ__["OperatorInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["OperatorInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����TCPSocket�ͻ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "Socket";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["HostInfo"]["IP"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = __REQ__["HostInfo"]["Port"];
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4,"A4",_Arg4_);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);

        _Result_ = B_ABOP_Socket_B_CreatTCPSocketClint(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ִ�н���ж�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "gotoThird";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "0";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0206_STEP3_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ѷ�����ƴ��_ģ��");

        _Arg0_ = __REQ__["HostInfo"]["System"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["HostInfo"]["InterFace"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["CoreDict"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = __REQ__["AFADict"];
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = __REQ__["EsbDict"];
        ACMP_Builtin_LoggerVar(4,"A4",_Arg4_);

        _Result_ = B_SCNX_MapDefine_B_ABOPClientModlePack(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["SentMsg"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["SentMsg"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "CoreDict";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = { "__HEAD__"                   : {    "Opr_Tellr_Num"              : __REQ__["OperatorInfo"][0][0] ,    "Init_Ext_TX_Cd"             : "CH1510",    "Termn_Typ"                  : "01",    "Chnl_Seq_Num"               : __REQ__["PlatformSeq"],    "Chnl_Dt"                    : __REQ__["CurrentDate"],    "Ext_TX_Cd"                  : "CH1510",    "Org_ID"                     : __REQ__["OperatorInfo"][0][1],                                 }, "__BODY__"                   : {} };
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE14;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0206_STEP3_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ر��Ĺ�������");


        _Result_ = B_SCNX_MapDefine_B_RteunCommonDict();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["MsgCommonDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["MsgCommonDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� SOCKET��Ϣ����");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "Socket";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["SentMsg"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_Socket_B_ABOP_SocketSent(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0206_STEP3_NODE23;
        elif(_Result_[0] == 1): 
            return TD0206_STEP3_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� AFA����ͷ����");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "AFADict";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = {   "M_CustomerNo":__REQ__["MsgCommonDict"]["M_CustomerNo"],   "M_ServicerNo":" ",   "M_PackageType":__REQ__["MsgCommonDict"]["M_PackageType"],   "M_ServiceCode":" ",   "M_MesgSndDate":__REQ__["CurrentDate"],   "M_MesgSndTime":__REQ__["CurrentTime"],   "M_MesgId":__REQ__["PlatformSeq"],   "M_MesgRefId":" "};
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE18;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0206_STEP3_NODE16(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ���񷽶˿���Ϣ");

        _Arg0_ = "SC6000Z";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_SCNX_MapDefine_B_GetSystemCfg(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["SC6000ZCfg"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["SC6000ZCfg"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ϵͳSocket���Ľ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "Socket";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["SC6000ZCfg"]["TimeOut"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_Socket_B_ABOP_Socket_Reacv(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["RecvMsg"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["RecvMsg"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0206_STEP3_NODE23;
        elif(_Result_[0] == 1): 
            return TD0206_STEP3_NODE20;
        elif(_Result_[0] == 2): 
            return TD0206_STEP3_NODE23;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������Ϣ����");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "HostInfo";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = {  "System":"SC6000Z",  "InterFace":"CH1510",  "IP":__REQ__["SC6000ZCfg"]["IP"],  "Port":__REQ__["SC6000ZCfg"]["Port"]};
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ESB����ͷ����");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "EsbDict";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = {   "reqTime":__REQ__["CurrentDate"]+__REQ__["CurrentTime"],   "appId":"app100",   "transId":"FBAP"+__REQ__["PlatformSeq"],   "hostName":__REQ__["LocalHost_Cfg"]["Characteristic"],   "channelId":__REQ__["MsgCommonDict"]["ChannelID"],   "serviceTarget":__REQ__["HostInfo"]["InterFace"],   "serviceAddress":"business/payment/batCollPayFileUpd033_v1_0_0",};
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE21;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ѷ�Ӧ����_ģ��");

        _Arg0_ = __REQ__["HostInfo"]["System"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["HostInfo"]["InterFace"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["RecvMsg"][8:];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_SCNX_MapDefine_B_ABOPClientModleUnPack(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["RspDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["RspDict"]);
            __REQ__["AFADict"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["AFADict"]);
            __REQ__["SecretyInfo"] = _RTVAL_[2];
            ACMP_Builtin_LoggerVar(4,"O2",__REQ__["SecretyInfo"]);
            __REQ__["ESBRspDict"] = _RTVAL_[3];
            ACMP_Builtin_LoggerVar(4,"O3",__REQ__["ESBRspDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE22;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE21(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ʼ��������");

        _Arg0_ = __REQ__["CoreDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [   "Debt_Crdt_Ind",   "Open_Acct_Ind",   "AIO_Ind",   "Cur",   "Prod_Acct_Prod_Cd",   "Memo_Cd",   "Memo",   "Doc_Nm",   "Pwd" ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [   "1",   "0",   "0",   "01",   "1104",   "200",   "�ϲ�У԰һ��ͨ��������",   __REQ__["HostBatchFileName"],   "12345678"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_Dict_B_InitReqBody(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE22(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ִ�н���ж�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "gotoThird";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "2";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE23(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ִ�н���ж�");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "gotoThird";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "1";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP3_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP3_NODE15);

def TD0206_STEP3_NODE24(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0206_STEP3_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 3 ���� CH1510����");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0206_STEP3_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0206_STEP4_IMPL;
        else:
            return TD0206_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0206_STEP4_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0206_STEP4_NODE3;

def TD0206_STEP4_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ִ���ʽ�����(1N/2Y)");

        _Arg0_ = __REQ__["gotoThird"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "0";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "1";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "2";
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

        if(_Result_[0] == 1): 
            return TD0206_STEP4_NODE10;
        elif(_Result_[0] == 2): 
            return TD0206_STEP4_NODE8;
        elif(_Result_[0] == 3): 
            return TD0206_STEP4_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

def TD0206_STEP4_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0206_STEP4_NODE5);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0206_STEP4_NODE5 �ڵ�");

    return TD0206_STEP4_NODE2;

def TD0206_STEP4_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �ж�ESB������");

        _Arg0_ = __REQ__["ESBRspDict"]["errCode"]=="soaErr_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0206_STEP4_NODE11;
        elif(_Result_[0] == 1): 
            return TD0206_STEP4_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

def TD0206_STEP4_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0206_STEP4_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �жϺ��Ĵ�����");

        _Arg0_ = __REQ__["RspDict"]["__RSPHEAD__"]["Host_Stat"]=="0";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0206_STEP4_NODE9;
        elif(_Result_[0] == 1): 
            return TD0206_STEP4_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

def TD0206_STEP4_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������������Ϣ");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostFileDealStatus","21"], ["NearOperateDate",__REQ__["CurrentDate"]], ["NearOperateTime",__REQ__["CurrentTime"]],["ErrorCode","000000"],["ErrorMsg",""]];
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
            return TD0206_STEP4_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

def TD0206_STEP4_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������������Ϣ");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostFileDealStatus","11"], ["NearOperateDate",__REQ__["CurrentDate"]], ["NearOperateTime",__REQ__["CurrentTime"]],["ErrorCode","FFFF"],["ErrorMsg","CH1510ͨ��ʧ��"]];
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
            return TD0206_STEP4_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

def TD0206_STEP4_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������������Ϣ");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostFileDealStatus","11"], ["NearOperateDate",__REQ__["CurrentDate"]], ["NearOperateTime",__REQ__["CurrentTime"]],["ErrorCode",__REQ__["RspDict"]["__RSPHEAD__"]["Err_Cd"][-6:]],["ErrorMsg",__REQ__["RspDict"]["__RSPHEAD__"]["Host_Info"]]];
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
            return TD0206_STEP4_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

def TD0206_STEP4_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������������Ϣ");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostFileDealStatus","11"], ["NearOperateDate",__REQ__["CurrentDate"]], ["NearOperateTime",__REQ__["CurrentTime"]] ];
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
            return TD0206_STEP4_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

def TD0206_STEP4_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������������Ϣ");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostFileDealStatus","11"], ["NearOperateDate",__REQ__["CurrentDate"]], ["NearOperateTime",__REQ__["CurrentTime"]],["ErrorCode",__REQ__["ESBRspDict"]["errCode"][-6:]],["ErrorMsg",__REQ__["ESBRspDict"]["errMsg"]]];
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
            return TD0206_STEP4_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP4_NODE5);

def TD0206_STEP4_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0206_STEP4_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0206_STEP4_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 4 ���� CH1510�������");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0206_STEP4_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0206_STEP5_IMPL;
        else:
            return TD0206_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0206_STEP5_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0206_STEP5_NODE5;

def TD0206_STEP5_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0206_STEP5_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0206_STEP5_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ý���ִ�гɹ�");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");

        _Result_ = B_ABOP_Trade_B_TradeSuccess(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0206_STEP5_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP5_NODE2);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP5_NODE2);

def TD0206_STEP5_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0206_STEP5_NODE2);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0206_STEP5_NODE2 �ڵ�");

    return TD0206_STEP5_NODE4;

def TD0206_STEP5_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 5 ���� ��ȷ����");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0206_STEP5_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return None;
        else:
            return TD0206_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0206_STEP7_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0206_STEP7_NODE2;

def TD0206_STEP7_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0206_STEP7_NODE5);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0206_STEP7_NODE5 �ڵ�");

    return TD0206_STEP7_NODE6;

def TD0206_STEP7_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0206_STEP7_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP7_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP7_NODE5);

def TD0206_STEP7_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0206_STEP7_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0206_STEP7_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0206_STEP7_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP7_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0206_STEP7_NODE5);

def TD0206_STEP7_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 7 ���� �쳣����");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0206_STEP7_NODE1;
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
def MD0206_ENTRY(__REQ__,__RSP__):
    AFALoggerInfor("��ʼ���� D0206:���������ļ��ϴ�");

    __SND__ = {};
    __RCV__ = {};

    __REQ__["__TRADENAME__"] = "���������ļ��ϴ�";

    ACMP_Builtin_TradeInitialize(__REQ__,__RSP__,"KAS_SSK");

    _Result_ = None;
    _Method_ = TD0206_STEP1_IMPL;
    while(type(_Method_) is FunctionType):
        AFALoggerInfor(("Step "+getattr(_Method_,"__name__")));
        _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
        _Method_ = _Result_;

    __SND__.clear();
    __RCV__.clear();
    del __SND__;
    del __RCV__;

    ACMP_Builtin_CheckResponse(__REQ__,__RSP__);
    AFALoggerInfor("�������� D0206");

    return True;
