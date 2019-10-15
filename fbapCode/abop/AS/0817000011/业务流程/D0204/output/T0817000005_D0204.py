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
from B_ABOP_Time import B_time_get as B_ABOP_Time_B_time_get;
from B_ABOP_DB import B_DBDMLUpd as B_ABOP_DB_B_DBDMLUpd;
from B_ABOP_DB import B_DBDMLIns as B_ABOP_DB_B_DBDMLIns;
from B_ABOP_DB import B_ABOP_FetchManyRecord as B_ABOP_DB_B_ABOP_FetchManyRecord;
from B_ABOP_DB import B_db_sequence as B_ABOP_DB_B_db_sequence;
from B_ABOP_DB import B_ABOP_GetTheTableCircleCursor as B_ABOP_DB_B_ABOP_GetTheTableCircleCursor;
from B_ABOP_SysBatchEnqing import B_CheckBatchType as B_ABOP_SysBatchEnqing_B_CheckBatchType;
from B_ABOP_FeeRecv_Auto import B_CheckBatchIsRecvFee as B_ABOP_FeeRecv_Auto_B_CheckBatchIsRecvFee;
from B_ABOP_Commom_Auto import B_GetSysParameterValue as B_ABOP_Commom_Auto_B_GetSysParameterValue;
from B_EventDeal import B_ABOPEventUpdate as B_EventDeal_B_ABOPEventUpdate;
from B_ABOP_DB import B_DBDMLSelForPlaceholder as B_ABOP_DB_B_DBDMLSelForPlaceholder;
from B_ABOP_Commom_Auto import B_GetTheOverallSituationCfg as B_ABOP_Commom_Auto_B_GetTheOverallSituationCfg;
from B_ABOP_Time import B_GetMicrosecondTime as B_ABOP_Time_B_GetMicrosecondTime;
from B_ABOP_BatchCheck import B_IndispensableFieldCheck as B_ABOP_BatchCheck_B_IndispensableFieldCheck;



'''
--------------------------- ��Ŀ���� ---------------------------
��    �ƣ�0817000005
��    ������¤��Դˮ�Ѵ���
----------------------------------------------------------------
'''


def TD0204_STEP1_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0204_STEP1_NODE2;

def TD0204_STEP1_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0204_STEP1_NODE6);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0204_STEP1_NODE6 �ڵ�");

    return TD0204_STEP1_NODE3;

def TD0204_STEP1_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �����ֶκϷ��Լ��");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [ ["REQBODY","CustomerID","STRING",20], ["REQBODY","AppType","STRING",20], ["REQBODY","AppID","STRING",20], ["REQBODY","BranchID","STRING",10], ["REQBODY","ChannelID","STRING",10], ["REQBODY","CustBatchID","CHAR",16], ["REQBODY","AgreementID","STRING",20], ["REQBODY","IsBatchClear","CHAR",1], ["REQBODY","RuleModeID","STRING",10], ["REQBODY","PropertyValue","STRING",512], ["REQBODY","SysBatchID","CHAR",16], ["REQBODY","IsUrgent","CHAR",1], ["REQBODY","IsRealTimeDeal","CHAR",1], ["REQBODY","ExcuteStatus","CHAR",2], ["REQBODY","Status","CHAR",1], ["REQBODY","TotalRecords","STRING",10], ["REQBODY","TotalAmount","STRING",17], ["REQBODY","SucRecords","STRING",10], ["REQBODY","SucAmount","STRING",17], ["REQBODY","FreezeStatus","CHAR",1], ["REQBODY","FreezeAmount","STRING",17], ["REQBODY","UnFreezeAmount","STRING",17], ["REQBODY","TransStatus","CHAR",1], ["REQBODY","TransToBankAmount","STRING",17], ["REQBODY","TransToCustAmount","STRING",17], ["REQBODY","BatchFilePath","STRING",128], ["REQBODY","BatchFileName","STRING",128], ["REQBODY","IsCrtRspFile","CHAR",1], ["REQBODY","BatchFileRspPath","STRING",128], ["REQBODY","BatchFileRspName","STRING",128], ["REQBODY","ErrorCode","STRING",6], ["REQBODY","ErrorMsg","STRING",128], ["REQBODY","CapitalRecover","CHAR",1], ["REQBODY","NearOperateDate","CHAR",8], ["REQBODY","NearOperateTime","CHAR",6] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_BatchCheck_B_IndispensableFieldCheck(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP1_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP1_NODE6);

def TD0204_STEP1_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0204_STEP1_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP1_NODE6);

def TD0204_STEP1_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0204_STEP1_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP1_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP1_NODE6);

def TD0204_STEP1_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0204_STEP1_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0204_STEP1_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 1 ���� ����У��");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0204_STEP1_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0204_STEP2_IMPL;
        else:
            return TD0204_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0204_STEP2_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0204_STEP2_NODE3;

def TD0204_STEP2_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������ҵ����Ϣ");

        _Arg0_ = "select AppType,AppID,AppName,AppRemark from ABOP_AppInfo where AppType=? and AppID=?";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["AppType"], __REQ__["__BODY__"]["AppID"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["AppInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["AppInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE5;
        elif(_Result_[0] == 2): 
            return TD0204_STEP2_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0204_STEP2_NODE17);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0204_STEP2_NODE17 �ڵ�");

    return TD0204_STEP2_NODE2;

def TD0204_STEP2_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ����������ִ������");

        _Arg0_ = "select BatchType,MaxBatchSerials from ABOP_AppExecuteHostCfg where HostCfgID= ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["HostCfgID"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["HostExcute"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["HostExcute"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE9;
        elif(_Result_[0] == 2): 
            return TD0204_STEP2_NODE14;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ������������");

        _Arg0_ = "select HostType,HostID from ABOP_AppExecuteHostCfg where HostCfgID= ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["HostCfgID"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["HostInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["HostInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE7;
        elif(_Result_[0] == 2): 
            return TD0204_STEP2_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ϵͳ�¼��ϱ�");

        _Arg0_ = "S0303";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["AppType"], __REQ__["__BODY__"]["AppID"], __REQ__["AppInfo"][0][2], __REQ__["__BODY__"]["HostCfgID"], None, None,None,None,None,None, None,None,None,None,None ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["LocalHost_Cfg"]["Characteristic"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_EventDeal_B_ABOPEventUpdate(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0204_STEP2_NODE8;
        elif(_Result_[0] == 1): 
            return TD0204_STEP2_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ����������Ϣ");

        _Arg0_ = "select FileCutSwitch,MaxFileRecord from ABOP_HostServiceProperty where HostType= ? and HostID= ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["HostInfo"][0][0], __REQ__["HostInfo"][0][1] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["HostCtrl"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["HostCtrl"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE10;
        elif(_Result_[0] == 2): 
            return TD0204_STEP2_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ����ڽ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "����HostCfgID������������¼ʧ�ܡ����ܶ����¼����ɾ����";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡϵͳ������ֵ");

        _Arg0_ = "EnableHostBatchCycle";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_Commom_Auto_B_GetSysParameterValue(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["EnableHostBatchCycle"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["EnableHostBatchCycle"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ��δ�����¼��");

        _Arg0_ = "select count(LineNo) from BPDM_OP_LZGasPayment where SysBatchID= ? and RecordStatus= ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["SysBatchID"], 'D' ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["TotalRecord"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["TotalRecord"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ϵͳ�¼��ϱ�");

        _Arg0_ = "S0116";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["HostInfo"][0][0], __REQ__["HostInfo"][0][1], None,None,None, None,None,None,None,None, None,None,None,None,None ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["LocalHost_Cfg"]["Characteristic"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_EventDeal_B_ABOPEventUpdate(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0204_STEP2_NODE13;
        elif(_Result_[0] == 1): 
            return TD0204_STEP2_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡϵͳ������ֵ");

        _Arg0_ = "HostBatch_MaxCount";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_Commom_Auto_B_GetSysParameterValue(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["EnableHostBatchCycle"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["EnableHostBatchCycle"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE18;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ����ڽ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "����HostCfgID���ҵ��������������󶨵�HostType[%s],HostID[%s],���ø�ֵ�������������¼ʱʧ�ܡ����ܸ����������¼��ɾ����"%(__REQ__["HostInfo"][0][0],__REQ__["HostInfo"][0][1]);
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ϵͳ�¼��ϱ�");

        _Arg0_ = "S0117";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["HostCfgID"], None, None,None,None, None,None,None,None,None, None,None,None,None,None ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["LocalHost_Cfg"]["Characteristic"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_EventDeal_B_ABOPEventUpdate(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0204_STEP2_NODE16;
        elif(_Result_[0] == 1): 
            return TD0204_STEP2_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "����ϵͳ����������ҵ���¼ʧ�ܣ�����ϵ��������ά���ж�λ��";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE16(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ȫ�ִ����ڽ���");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "��ȡ���������� HostCfgID[%s]��ִ������ʧ�ܣ�������δ���á�"%(__REQ__["__BODY__"]["HostCfgID"]);
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP2_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP2_NODE17);

def TD0204_STEP2_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0204_STEP2_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0204_STEP2_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0204_STEP2_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 2 ���� ����׼��");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0204_STEP2_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0204_STEP3_IMPL;
        else:
            return TD0204_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0204_STEP3_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0204_STEP3_NODE2;

def TD0204_STEP3_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0204_STEP3_NODE6);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0204_STEP3_NODE6 �ڵ�");

    return TD0204_STEP3_NODE3;

def TD0204_STEP3_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������Ƿ����������");

        _Arg0_ = __REQ__["__BODY__"]["AppType"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["__BODY__"]["AppID"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "HostBatch";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = __REQ__["__BODY__"]["BranchID"];
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A4","__REQ__");

        _Result_ = B_ABOP_FeeRecv_Auto_B_CheckBatchIsRecvFee(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["IsRcvFee"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["IsRcvFee"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP3_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP3_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP3_NODE6);

def TD0204_STEP3_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ʽ�����жϣ��ڽ���");

        _Arg0_ = __REQ__["IsRcvFee"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0204_STEP3_NODE5;
        elif(_Result_[0] == 1): 
            return TD0204_STEP3_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP3_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP3_NODE6);

def TD0204_STEP3_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������ֵ���ڽ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "IsRecvFee";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "0";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP3_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP3_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP3_NODE6);

def TD0204_STEP3_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0204_STEP3_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������ֵ���ڽ���");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "IsRecvFee";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "1";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP3_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP3_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP3_NODE6);

def TD0204_STEP3_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0204_STEP3_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 3 ���� У���Ƿ���ȡ������");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0204_STEP3_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0204_STEP4_IMPL;
        else:
            return TD0204_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0204_STEP4_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0204_STEP4_NODE3;

def TD0204_STEP4_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� SWITCHʵ�ֿ�ܣ��ڽ���");

        _Arg0_ = __REQ__["HostExcute"][0][0];
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
            return TD0204_STEP4_NODE8;
        elif(_Result_[0] == 2): 
            return TD0204_STEP4_NODE13;
        elif(_Result_[0] == 3): 
            return TD0204_STEP4_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0204_STEP4_NODE24);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0204_STEP4_NODE24 �ڵ�");

    return TD0204_STEP4_NODE2;

def TD0204_STEP4_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ϵͳ��ǰ��������ģʽ");

        _Arg0_ = "select AppRunTactics,AppRunTactisData from ABOP_RunControlTable where AppType= ? and AppID= ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["AppType"], __REQ__["__BODY__"]["AppID"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["AppCtrl"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["AppCtrl"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE5;
        elif(_Result_[0] == 2): 
            return TD0204_STEP4_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���鵱ǰʱ����������");

        _Arg0_ = __REQ__["AppCtrl"][0][0];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["AppCtrl"][0][1];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_SysBatchEnqing_B_CheckBatchType(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE8;
        elif(_Result_[0] == 2): 
            return TD0204_STEP4_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���鵱ǰʱ����������");

        _Arg0_ = __REQ__["ABOP_OperationStrategy"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["BatchTypeDefaultValue"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_SysBatchEnqing_B_CheckBatchType(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE8;
        elif(_Result_[0] == 2): 
            return TD0204_STEP4_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���Ʋ���");

        _Arg0_ = "ABOP_OperationStrategy";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_Commom_Auto_B_GetSysParameterValue(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["ABOP_OperationStrategy"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["ABOP_OperationStrategy"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �Ƿ�����������ļ���С");

        _Arg0_ = __REQ__["HostCtrl"][0][0] == "1";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0204_STEP4_NODE14;
        elif(_Result_[0] == 1): 
            return TD0204_STEP4_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ȡ��ѭ�����¼���α�");

        _Arg0_ = "select LineNo from BPDM_OP_LZGasPayment where SysBatchID='"+__REQ__["__BODY__"]["SysBatchID"]+"' and RecordStatus='D' order by LineNo ASC";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_DB_B_ABOP_GetTheTableCircleCursor(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["DetailCurr"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["DetailCurr"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����ֵ");

        _Arg0_ = "BatchTypeDefaultValue";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_Commom_Auto_B_GetSysParameterValue(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["BatchTypeDefaultValue"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["BatchTypeDefaultValue"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� �Ƿ�Ҫ�����ļ���Ƭ");

        _Arg0_ = __REQ__["TotalRecord"][0][0] > int(__REQ__["HostCtrl"][0][1]);
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0204_STEP4_NODE14;
        elif(_Result_[0] == 1): 
            return TD0204_STEP4_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ����һ��ȡ�ö�����¼");

        _Arg0_ = __REQ__["DetailCurr"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = int(__REQ__["HostCtrl"][0][1]);
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_ABOP_FetchManyRecord(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["TmpList"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["TmpList"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE15;
        elif(_Result_[0] == 2): 
            return TD0204_STEP4_NODE22;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���кŲ���");

        _Arg0_ = "SEQ_HostBatchID";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 8;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["SEQ_HostBatchID"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["SEQ_HostBatchID"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���кŲ���");

        _Arg0_ = "SEQ_HostBatchID";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 8;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["SEQ_HostBatchID"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["SEQ_HostBatchID"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���кŲ���");

        _Arg0_ = "SEQ_HostBatchID";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 8;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["SEQ_HostBatchID"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["SEQ_HostBatchID"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE18;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE16(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������������");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [  ["AppType",__REQ__["__BODY__"]["AppType"]],  ["AppID",__REQ__["__BODY__"]["AppID"]],  ["BranchID",__REQ__["__BODY__"]["BranchID"]],  ["ChannelID",__REQ__["__BODY__"]["ChannelID"]],  ["SysBatchID",__REQ__["__BODY__"]["SysBatchID"]],  ["HostCfgID",__REQ__["__BODY__"]["HostCfgID"]],  ["HostExcuteType",__REQ__["__BODY__"]["HostExcuteType"]],  ["IsBatchClear",__REQ__["__BODY__"]["IsBatchClear"]],  ["RuleModeID",__REQ__["__BODY__"]["RuleModeID"]],  ["PropertyValue",__REQ__["__BODY__"]["PropertyValue"]],  ["HostBatchID",__REQ__["CurrentDate"]+__REQ__["SEQ_HostBatchID"]],  ["IsRealTimeDeal",__REQ__["__BODY__"]["IsRealTimeDeal"]],  ["IsUrgent",__REQ__["__BODY__"]["IsUrgent"]],  ["CurrentSeries","1"],  ["HostType",__REQ__["HostInfo"][0][0]],  ["HostID",__REQ__["HostInfo"][0][1]],  ["BatchType","1"],  ["ExcuteStatus","00"],  ["OnLineMsgStatus","00"],  ["HostFileDealStatus","00"],  ["HasChecedAcct","0"],  ["HostFilePath",""],  ["HostFileName",""],  ["HostRsltFilePath",""],  ["HostRsltFileName",""],  ["NearOperateDate",__REQ__["CurrentDate"]],  ["NearOperateTime",__REQ__["CurrentTime"]],  ["IsRecvFee",__REQ__["IsRecvFee"]],  ["FeeIsRecvFlg","0"],  ["LockOperateInfo","0"],  ["ErrorCode","000000"],  ["ErrorMsg",""],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = False;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLIns(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������������");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["AppType",__REQ__["__BODY__"]["AppType"]], ["AppID",__REQ__["__BODY__"]["AppID"]], ["BranchID",__REQ__["__BODY__"]["BranchID"]], ["ChannelID",__REQ__["__BODY__"]["ChannelID"]], ["SysBatchID",__REQ__["__BODY__"]["SysBatchID"]], ["HostCfgID",__REQ__["__BODY__"]["HostCfgID"]], ["HostExcuteType",__REQ__["__BODY__"]["HostExcuteType"]], ["IsBatchClear",__REQ__["__BODY__"]["IsBatchClear"]], ["RuleModeID",__REQ__["__BODY__"]["RuleModeID"]], ["PropertyValue",__REQ__["__BODY__"]["PropertyValue"]], ["HostBatchID",__REQ__["CurrentDate"]+__REQ__["SEQ_HostBatchID"]], ["IsRealTimeDeal",__REQ__["__BODY__"]["IsRealTimeDeal"]], ["IsUrgent",__REQ__["__BODY__"]["IsUrgent"]], ["CurrentSeries","1"], ["HostType",__REQ__["HostInfo"][0][0]], ["HostID",__REQ__["HostInfo"][0][1]], ["BatchType","0"], ["ExcuteStatus","00"], ["OnLineMsgStatus","00"], ["HostFileDealStatus","00"], ["HasChecedAcct","0"], ["HostFilePath",""], ["HostFileName",""], ["HostRsltFilePath",""], ["HostRsltFileName",""], ["NearOperateDate",__REQ__["CurrentDate"]], ["NearOperateTime",__REQ__["CurrentTime"]], ["IsRecvFee",__REQ__["IsRecvFee"]], ["FeeIsRecvFlg","0"], ["LockOperateInfo","0"], ["ErrorCode","000000"], ["ErrorMsg",""] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = False;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLIns(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������������");

        _Arg0_ = "ABOP_HostBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [  ["AppType",__REQ__["__BODY__"]["AppType"]],  ["AppID",__REQ__["__BODY__"]["AppID"]],  ["BranchID",__REQ__["__BODY__"]["BranchID"]],  ["ChannelID",__REQ__["__BODY__"]["ChannelID"]],  ["SysBatchID",__REQ__["__BODY__"]["SysBatchID"]],  ["HostCfgID",__REQ__["__BODY__"]["HostCfgID"]],  ["HostExcuteType",__REQ__["__BODY__"]["HostExcuteType"]],  ["IsBatchClear",__REQ__["__BODY__"]["IsBatchClear"]],  ["RuleModeID",__REQ__["__BODY__"]["RuleModeID"]],  ["PropertyValue",__REQ__["__BODY__"]["PropertyValue"]],  ["HostBatchID",__REQ__["CurrentDate"]+__REQ__["SEQ_HostBatchID"]],  ["IsRealTimeDeal",__REQ__["__BODY__"]["IsRealTimeDeal"]],  ["IsUrgent",__REQ__["__BODY__"]["IsUrgent"]],  ["CurrentSeries","1"],  ["HostType",__REQ__["HostInfo"][0][0]],  ["HostID",__REQ__["HostInfo"][0][1]],  ["BatchType","0"],  ["ExcuteStatus","00"],  ["OnLineMsgStatus","00"],  ["HostFileDealStatus","00"],  ["HasChecedAcct","0"],  ["HostFilePath",""],  ["HostFileName",""],  ["HostRsltFilePath",""],  ["HostRsltFileName",""],  ["NearOperateDate",__REQ__["CurrentDate"]],  ["NearOperateTime",__REQ__["CurrentTime"]],  ["IsRecvFee",__REQ__["IsRecvFee"]],  ["FeeIsRecvFlg","0"],  ["LockOperateInfo","0"],  ["ErrorCode","000000"],  ["ErrorMsg",""],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = False;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLIns(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP4_NODE21;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������ϸ��¼����������");

        _Arg0_ = "BPDM_OP_LZGasPayment";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostOperSearil",__REQ__["__BODY__"]["HostCfgID"]], ["HostBatchID",__REQ__["CurrentDate"]+__REQ__["SEQ_HostBatchID"]], ["CurrentSeries","1"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["SysBatchID","=",__REQ__["__BODY__"]["SysBatchID"],"and"], ["RecordStatus","=","D",None] ];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = False;
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
            return TD0204_STEP4_NODE22;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������ϸ��¼����������");

        _Arg0_ = "BPDM_OP_LZGasPayment";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostOperSearil",__REQ__["__BODY__"]["HostCfgID"]], ["HostBatchID",__REQ__["CurrentDate"]+__REQ__["SEQ_HostBatchID"]], ["CurrentSeries","1"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["SysBatchID","=",__REQ__["__BODY__"]["SysBatchID"],"and"], ["RecordStatus","=","D",None] ];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = False;
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
            return TD0204_STEP4_NODE23;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE21(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ������ϸ��¼����������");

        _Arg0_ = "BPDM_OP_LZGasPayment";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["HostOperSearil",__REQ__["__BODY__"]["HostCfgID"]], ["HostBatchID",__REQ__["CurrentDate"]+__REQ__["SEQ_HostBatchID"]], ["CurrentSeries","1"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["SysBatchID","=",__REQ__["__BODY__"]["SysBatchID"],"and"], ["RecordStatus","=","D","and"], ["LineNo",">=",__REQ__["TmpList"][0][0],"and"], ["LineNo","<=",__REQ__["TmpList"][-1][0],None] ];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = False;
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
            return TD0204_STEP4_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP4_NODE24);

def TD0204_STEP4_NODE22(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0204_STEP4_NODE23(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0204_STEP4_NODE24(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0204_STEP4_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 4 ���� ������������");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0204_STEP4_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0204_STEP5_IMPL;
        else:
            return TD0204_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0204_STEP5_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0204_STEP5_NODE2;

def TD0204_STEP5_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0204_STEP5_NODE4);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0204_STEP5_NODE4 �ڵ�");

    return TD0204_STEP5_NODE6;

def TD0204_STEP5_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0204_STEP5_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0204_STEP5_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������״̬");

        _Arg0_ = "ABOP_SysBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["ExcuteStatus","31"], ["Status","1"], ["NearOperateDate",__REQ__["TradeDay"]], ["NearOperateTime",__REQ__["TradeTime"]] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [ ["SysBatchID","=",__REQ__["__BODY__"]["SysBatchID"],None] ];
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
            return TD0204_STEP5_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP5_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP5_NODE4);

def TD0204_STEP5_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��ȡ����ʱ��");


        _Result_ = B_ABOP_Time_B_time_get();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TradeDay"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TradeDay"]);
            __REQ__["TradeTime"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["TradeTime"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP5_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP5_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP5_NODE4);

def TD0204_STEP5_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 5 ���� ��������״̬");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0204_STEP5_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0204_STEP6_IMPL;
        else:
            return TD0204_STEP7_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0204_STEP6_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0204_STEP6_NODE4;

def TD0204_STEP6_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0204_STEP6_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ý���ִ�гɹ�");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");

        _Result_ = B_ABOP_Trade_B_TradeSuccess(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0204_STEP6_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP6_NODE2);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP6_NODE2);

def TD0204_STEP6_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0204_STEP6_NODE2);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0204_STEP6_NODE2 �ڵ�");

    return TD0204_STEP6_NODE3;

def TD0204_STEP6_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0204_STEP6_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 6 ���� ��������");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0204_STEP6_NODE1;
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

def TD0204_STEP7_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��ʼ");
    return TD0204_STEP7_NODE2;

def TD0204_STEP7_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� Ĭ���߼�����ί��");
    ACMP_Builtin_SetDefaultExceptNode(TD0204_STEP7_NODE3);
    AFALoggerInfor("��Ĭ���쳣ί�е� TD0204_STEP7_NODE3 �ڵ�");

    return TD0204_STEP7_NODE8;

def TD0204_STEP7_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� �쳣����");
    return False;

def TD0204_STEP7_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0204_STEP7_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP7_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP7_NODE3);

def TD0204_STEP7_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ��������ֵ���ڽ���");

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
            return TD0204_STEP7_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP7_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP7_NODE3);

def TD0204_STEP7_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("���� ��������");
    return True;

def TD0204_STEP7_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� ���ʽ�����жϣ��ڽ���");

        _Arg0_ = len(__REQ__["ErrorMsg"])>127;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0204_STEP7_NODE4;
        elif(_Result_[0] == 1): 
            return TD0204_STEP7_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP7_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP7_NODE3);

def TD0204_STEP7_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0204_STEP7_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP7_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0204_STEP7_NODE3);

def TD0204_STEP7_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("���� 7 ���� �쳣����");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0204_STEP7_NODE1;
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
def MD0204_ENTRY(__REQ__,__RSP__):
    AFALoggerInfor("��ʼ���� D0204:ˮ�Ѵ����������δ���");

    __SND__ = {};
    __RCV__ = {};

    __REQ__["__TRADENAME__"] = "ˮ�Ѵ����������δ���";

    ACMP_Builtin_TradeInitialize(__REQ__,__RSP__,"KOP_SSK");

    _Result_ = None;
    _Method_ = TD0204_STEP1_IMPL;
    while(type(_Method_) is FunctionType):
        AFALoggerInfor(("Step "+getattr(_Method_,"__name__")));
        _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
        _Method_ = _Result_;

    __SND__.clear();
    __RCV__.clear();
    del __SND__;
    del __RCV__;

    ACMP_Builtin_CheckResponse(__REQ__,__RSP__);
    AFALoggerInfor("�������� D0204");

    return True;
