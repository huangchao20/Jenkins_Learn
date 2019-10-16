# -*- coding: gbk -*-
'''
----------------------------------------------------------------
内部名称：AS
说    明：批量代理教育类
作    者：
备    注：赞同科技AFA编译器V3.7.0.2_test 
编译器宏：
    1. __REQ__   ---> 交易请求数据上下文容器
    2. __RSP__   ---> 交易返回数据上下文容器
    3. __SND__   ---> 客户端发送数据上下文容器
    4. __RCV__   ---> 客户端接收数据上下文容器
    5. __TC__    ---> 交易代码
    6. __MC__    ---> 项目代码
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
from B_ABOP_Socket import natpbl_Comm as B_ABOP_Socket_natpbl_Comm;
from B_ABOP_DB import B_DBDMLSelForPlaceholder as B_ABOP_DB_B_DBDMLSelForPlaceholder;
from B_ABOP_File import B_HasFile as B_ABOP_File_B_HasFile;
from B_ABOP_Socket import fileTrans as B_ABOP_Socket_fileTrans;
from B_ABOP_Commom_Auto import B_GetTheOverallSituationCfg as B_ABOP_Commom_Auto_B_GetTheOverallSituationCfg;
from B_ABOP_DB import B_db_sequence as B_ABOP_DB_B_db_sequence;
from B_ABOP_DB import B_DBDMLUpd as B_ABOP_DB_B_DBDMLUpd;
from B_SCNX_CFG import B_GetUOCPCfg as B_SCNX_CFG_B_GetUOCPCfg;
from B_ABOP_Time import B_Tdateminu as B_ABOP_Time_B_Tdateminu;
from B_ABOP_DB import B_DBDMLSel as B_ABOP_DB_B_DBDMLSel;
from B_ABOP_BatchCheck import B_CheckTheChoiceableField as B_ABOP_BatchCheck_B_CheckTheChoiceableField;
from B_ABOP_BatchCheck import B_IndispensableFieldCheck as B_ABOP_BatchCheck_B_IndispensableFieldCheck;
from B_ABOP_Time import B_time_get as B_ABOP_Time_B_time_get;
from B_ABOP_Dictionary import B_dict_setvalue as B_ABOP_Dictionary_B_dict_setvalue;



'''
--------------------------- 项目分期 ---------------------------
名    称：0817000011
描    述：南部一卡通批量代扣
----------------------------------------------------------------
'''


def TD02011_STEP7_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD02011_STEP7_NODE2;

def TD02011_STEP7_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD02011_STEP7_NODE6);
    AFALoggerInfor("将默认异常委托到 TD02011_STEP7_NODE6 节点");

    return TD02011_STEP7_NODE8;

def TD02011_STEP7_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取交易时间");


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
            return TD02011_STEP7_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP7_NODE6);

    # except Exception,PyExcp:
    #     ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
    #     AFALoggerError(str(format_exc()));
    #     AFALoggerError(str(PyExcp));
    #     return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP7_NODE6);

def TD02011_STEP7_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 必输字段合法性检查");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [ ["REQBODY","AppType","STRING",20], ["REQBODY","AppID","STRING",20], ["REQBODY","AgreementID","STRING",20], ["REQBODY","CustBatchID","CHAR",16], ["REQBODY","IsUrgent","CHAR",1], ["REQBODY","IsRealTimeDeal","CHAR",1],["REQBODY","BankBranchID","STRING",10], ["REQBODY","ChannelID","STRING",10], ["REQBODY","ExcuteStatus","CHAR",2], ["REQBODY","Status","CHAR",1], ["REQBODY","IsBatchClear","CHAR",1], ["REQBODY","RuleModeID","STRING",10], ["REQBODY","BatchFilePath","STRING",128], ["REQBODY","BatchFileName","STRING",128], ["REQBODY","TotalRecord","STRING",10], ["REQBODY","TotalAmount","STRING",17], ["REQBODY","ScuRecord","STRING",10], ["REQBODY","ScuAmount","STRING",17], ["REQBODY","NearstDate","CHAR",8], ["REQBODY","NearstTime","CHAR",6] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_BatchCheck_B_IndispensableFieldCheck(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1):
            print(TD02011_STEP7_NODE5)
            return TD02011_STEP7_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP7_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP7_NODE6);

def TD02011_STEP7_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 选输字段校验");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_BatchCheck_B_CheckTheChoiceableField(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP7_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP7_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP7_NODE6);

def TD02011_STEP7_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD02011_STEP7_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD02011_STEP7_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 产品信息赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [	["AppType","AS"],	["AppID","0817000011"],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1):
            print(TD02011_STEP7_NODE3)
            return TD02011_STEP7_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP7_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP7_NODE6);

def TD02011_STEP7_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 7 功能 数据校验");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD02011_STEP7_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD02011_STEP8_IMPL;
        else:
            return TD02011_STEP11_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD02011_STEP8_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD02011_STEP8_NODE2;

def TD02011_STEP8_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD02011_STEP8_NODE3);
    AFALoggerInfor("将默认异常委托到 TD02011_STEP8_NODE3 节点");

    return TD02011_STEP8_NODE5;

def TD02011_STEP8_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD02011_STEP8_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD02011_STEP8_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 数据查询");

        _Arg0_ = "select CREATEDATE,CHANNELSERIALNO,NEARSTDATE,NEARSTTIME,TOTALRECORDS,BATCHFILENAME,AGREEMENTID   from ABOP_CUSTBATCHINFO  where CustBatchID = '"+__REQ__["__BODY__"]["CustBatchID"]+"'";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 0;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_DBDMLSel(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["CustBatchInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["CustBatchInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP8_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 计算两个时间差值");

        _Arg0_ = __REQ__["CustBatchInfo"][0][2]+__REQ__["CustBatchInfo"][0][3];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["CurrentDate"]+__REQ__["CurrentTime"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "seconds";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_Time_B_Tdateminu(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["seconds"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["seconds"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP8_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断时间差");

        _Arg0_ = __REQ__["seconds"] >= 60;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD02011_STEP8_NODE8;
        elif(_Result_[0] == 1): 
            return TD02011_STEP8_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 回退执行状态");

        _Arg0_ = "ABOP_CUSTBATCHINFO";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [	["EXCUTESTATUS","00"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [	["CUSTBATCHID","=",__REQ__["__BODY__"]["CustBatchID"],None]];
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
            return TD02011_STEP8_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 文件申请标识");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "GetFileFlag";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "1";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP8_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取平台流水信息");

        _Arg0_ = "SQ_PLATSEQNO";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 8;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["PlatformSerialno"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["PlatformSerialno"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP8_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取本机相关标识");


        _Result_ = B_ABOP_Commom_Auto_B_GetTheOverallSituationCfg();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["LocalHost_Cfg"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["LocalHost_Cfg"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP8_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取外联传输文件交互配置");


        _Result_ = B_SCNX_CFG_B_GetUOCPCfg();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["MsgSystemDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["MsgSystemDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP8_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 请求文件绝对路径");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "ReqFilePath";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["MsgSystemDict"]["ReqPath"]+"0817000011/";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP8_NODE14;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 请求文件名称赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "ReqFileName";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["CustBatchInfo"][0][5];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP8_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP8_NODE3);

def TD02011_STEP8_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 8 功能 数据准备");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD02011_STEP8_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD02011_STEP9_IMPL;
        else:
            return TD02011_STEP11_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD02011_STEP9_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD02011_STEP9_NODE2;

def TD02011_STEP9_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD02011_STEP9_NODE7);
    AFALoggerInfor("将默认异常委托到 TD02011_STEP9_NODE7 节点");

    return TD02011_STEP9_NODE19;

def TD02011_STEP9_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断AFE错误码");

        _Arg0_ = __REQ__["RspResult"].has_key("afecode") and __REQ__["RspResult"]["afecode"] == "AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD02011_STEP9_NODE4;
        elif(_Result_[0] == 1): 
            return TD02011_STEP9_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断失败次数");

        _Arg0_ = int(__REQ__["CustBatchInfo"][0][4]) < 3;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD02011_STEP9_NODE11;
        elif(_Result_[0] == 1): 
            return TD02011_STEP9_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 数据查询");

        _Arg0_ = "select CustBatchID from ABOP_CustBatchInfo where BatchFileName='"+__REQ__["ReqFileName"]+"' and appid='0817000011' and Status='1'";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = 0;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_DBDMLSel(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["Num"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["Num"]);
            __REQ__["TMP"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["TMP"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE6;
        elif(_Result_[0] == 2): 
            return TD02011_STEP9_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断是否重复处理");

        _Arg0_ = __REQ__["Num"] == 1;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD02011_STEP9_NODE18;
        elif(_Result_[0] == 1): 
            return TD02011_STEP9_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD02011_STEP9_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 从AFE获取文件到AFA");

        _Arg0_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["__MC__"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["__TC__"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "CustBatchReq/0817000011/";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = "0817000011/recv/";
        ACMP_Builtin_LoggerVar(4,"A4",_Arg4_);
        _Arg5_ = __REQ__["ReqFileName"];
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);
        _Arg6_ = "GET";
        ACMP_Builtin_LoggerVar(4,"A6",_Arg6_);

        _Result_ = B_ABOP_Socket_fileTrans(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE14;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 处理失败");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FBAP02";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "三方代扣文件未生成!";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 回退执行状态");

        _Arg0_ = "ABOP_CUSTBATCHINFO";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [	["TOTALRECORDS",str(int(__REQ__["CustBatchInfo"][0][4])+1)],	["EXCUTESTATUS","00"],	["NEARSTDATE",__REQ__["CurrentDate"]],	["NEARSTTIME",__REQ__["CurrentTime"]]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [	["CUSTBATCHID","=",__REQ__["__BODY__"]["CustBatchID"],None]];
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
            return TD02011_STEP9_NODE17;
        elif(_Result_[0] == 2): 
            return TD02011_STEP9_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新客户批次信息表");

        _Arg0_ = "abop_custbatchinfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["ExcuteStatus","11"], ["Status","9"], ["ErroCode","FBAP"], ["ErroMsg","获取批扣文件失败！"],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [["custbatchid","=",__REQ__["__BODY__"]["CustBatchID"],None]];
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
            return TD02011_STEP9_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 natp负载均衡通信代理");

        _Arg0_ = __REQ__["__SEND__"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "0817000011_PUB";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = __REQ__["__MC__"];
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = __REQ__["__TC__"];
        ACMP_Builtin_LoggerVar(4,"A4",_Arg4_);

        _Result_ = B_ABOP_Socket_natpbl_Comm(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["RspResult"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["RspResult"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD02011_STEP9_NODE23;
        elif(_Result_[0] == 1): 
            return TD02011_STEP9_NODE3;
        elif(_Result_[0] == 2): 
            return TD02011_STEP9_NODE23;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 是否有正在处理或处理完成的批");

        _Arg0_ = "select CustBatchID from ABOP_CustBatchInfo where BatchFileName=? and appid=? and Status='0'";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [__REQ__["ReqFileName"],__REQ__["__BODY__"]["AppID"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["Record"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["Record"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE22;
        elif(_Result_[0] == 2): 
            return TD02011_STEP9_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 检查文件是否存在");

        _Arg0_ = __REQ__["ReqFilePath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["ReqFileName"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_HasFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD02011_STEP9_NODE16;
        elif(_Result_[0] == 1): 
            return TD02011_STEP9_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新客户批次信息表");

        _Arg0_ = "abop_custbatchinfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [    ["EXCUTESTATUS","11"],	["NEARSTDATE",__REQ__["CurrentDate"]],	["NEARSTTIME",__REQ__["CurrentTime"]],    ["BATCHFILEPATH",__REQ__["ReqFilePath"]],    ["ErroMsg",__REQ__["CustBatchInfo"][0][5]+"获取批扣文件成功！"],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [["custbatchid","=",__REQ__["__BODY__"]["CustBatchID"],None]];
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
            return TD02011_STEP9_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE16(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 文件不存在");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FBAP02";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "未获取到代扣文件!";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD02011_STEP9_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 文件处理中");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FBAP02";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "代扣文件正在处理中或已处理结束!";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断申请文件标识");

        _Arg0_ = __REQ__.get("GetFileFlag","0") == "1";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD02011_STEP9_NODE20;
        elif(_Result_[0] == 1): 
            return TD02011_STEP9_NODE21;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD02011_STEP9_NODE21(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 对象初始化");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "__SEND__";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = {  "reqSendDate":__REQ__["CurrentDate"],  "reqSendTime":__REQ__["CurrentTime"],  "reqProdArea":"511300",  "reqProdCate":__REQ__["AppType"],  "reqProdCode":__REQ__["AppID"],  "reqProdSubCate":__REQ__["AppID"],  "reqReceiverSID":"",  "reqTransID":"FBAP"+__REQ__["PlatformSerialno"],  "reqReserve":"",  "AFAServiceFunCode":"P00001",  "MC":__REQ__["__MC__"],  "TC":"D02011",   "FilePath":__REQ__["ReqFilePath"],  "BatchFileName":__REQ__["CustBatchInfo"][0][5],};
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE22(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 已有处理成功文件");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FBAP02";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "代扣已有处理成功文件!";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE23(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 AFE通讯异常");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FBAP00";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "请求AFE失败!";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP9_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP9_NODE24);

def TD02011_STEP9_NODE24(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD02011_STEP9_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 9 功能 文件获取请求");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD02011_STEP9_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD02011_STEP10_IMPL;
        else:
            return TD02011_STEP11_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD02011_STEP10_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD02011_STEP10_NODE3;

def TD02011_STEP10_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD02011_STEP10_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD02011_STEP10_NODE2);
    AFALoggerInfor("将默认异常委托到 TD02011_STEP10_NODE2 节点");

    return TD02011_STEP10_NODE6;

def TD02011_STEP10_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD02011_STEP10_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 设置交易执行成功");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");

        _Result_ = B_ABOP_Trade_B_TradeSuccess(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD02011_STEP10_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP10_NODE2);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP10_NODE2);

def TD02011_STEP10_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 10 功能 正常结束");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD02011_STEP10_NODE1;
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

def TD02011_STEP11_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD02011_STEP11_NODE2;

def TD02011_STEP11_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD02011_STEP11_NODE4);
    AFALoggerInfor("将默认异常委托到 TD02011_STEP11_NODE4 节点");

    return TD02011_STEP11_NODE3;

def TD02011_STEP11_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

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
            return TD02011_STEP11_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP11_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP11_NODE4);

def TD02011_STEP11_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD02011_STEP11_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 设置交易执行失败");

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
            return TD02011_STEP11_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP11_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD02011_STEP11_NODE4);

def TD02011_STEP11_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD02011_STEP11_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 11 功能 异常结束");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD02011_STEP11_NODE1;
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
------------------------- 交易入口函数 -------------------------
'''
def MD02011_ENTRY(__REQ__,__RSP__):
    AFALoggerInfor("开始交易 D02011:代扣文件获取");

    __SND__ = {};
    __RCV__ = {};

    __REQ__["__TRADENAME__"] = "代扣文件获取";

    ACMP_Builtin_TradeInitialize(__REQ__,__RSP__,"KAS_SSK");

    _Result_ = None;
    _Method_ = TD02011_STEP7_IMPL;
    while(type(_Method_) is FunctionType):
        AFALoggerInfor(("Step "+getattr(_Method_,"__name__")));
        _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
        _Method_ = _Result_;

    __SND__.clear();
    __RCV__.clear();
    del __SND__;
    del __RCV__;

    ACMP_Builtin_CheckResponse(__REQ__,__RSP__);
    AFALoggerInfor("结束交易 D02011");

    return True;
