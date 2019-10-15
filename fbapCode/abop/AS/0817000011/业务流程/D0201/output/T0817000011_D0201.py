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
from B_ABOP_DB import B_DBDMLIns as B_ABOP_DB_B_DBDMLIns;
from B_ABOP_Socket import natpbl_Comm as B_ABOP_Socket_natpbl_Comm;
from B_ABOP_DB import B_db_sequence as B_ABOP_DB_B_db_sequence;
from B_ABOP_DB import B_DBDMLSelForPlaceholder as B_ABOP_DB_B_DBDMLSelForPlaceholder;
from B_SCNX_CFG import B_GetUOCPCfg as B_SCNX_CFG_B_GetUOCPCfg;
from B_ABOP_Commom_Auto import B_GetTheOverallSituationCfg as B_ABOP_Commom_Auto_B_GetTheOverallSituationCfg;
from B_ABOP_Dictionary import B_dict_setvalue as B_ABOP_Dictionary_B_dict_setvalue;
from B_ABOP_Time import B_time_get as B_ABOP_Time_B_time_get;



'''
--------------------------- 项目分期 ---------------------------
名    称：0817000011
描    述：南部一卡通批量代扣
----------------------------------------------------------------
'''


def TD0201_STEP1_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0201_STEP1_NODE2;

def TD0201_STEP1_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0201_STEP1_NODE3);
    AFALoggerInfor("将默认异常委托到 TD0201_STEP1_NODE3 节点");

    return TD0201_STEP1_NODE4;

def TD0201_STEP1_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0201_STEP1_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP1_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP1_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP1_NODE3);

def TD0201_STEP1_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0201_STEP1_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 1 功能 数据校验");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0201_STEP1_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0201_STEP2_IMPL;
        else:
            return TD0201_STEP6_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0201_STEP2_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0201_STEP2_NODE3;

def TD0201_STEP2_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0201_STEP2_NODE8);
    AFALoggerInfor("将默认异常委托到 TD0201_STEP2_NODE8 节点");

    return TD0201_STEP2_NODE14;

def TD0201_STEP2_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP2_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP2_NODE8);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP2_NODE8);

def TD0201_STEP2_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0201_STEP2_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP2_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP2_NODE8);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP2_NODE8);

def TD0201_STEP2_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP2_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP2_NODE8);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP2_NODE8);

def TD0201_STEP2_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0201_STEP2_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP2_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP2_NODE8);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP2_NODE8);

def TD0201_STEP2_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 2 功能 数据准备");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0201_STEP2_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0201_STEP3_IMPL;
        else:
            return TD0201_STEP6_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0201_STEP3_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0201_STEP3_NODE2;

def TD0201_STEP3_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0201_STEP3_NODE20);
    AFALoggerInfor("将默认异常委托到 TD0201_STEP3_NODE20 节点");

    return TD0201_STEP3_NODE13;

def TD0201_STEP3_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断AFE错误码");

        _Arg0_ = __REQ__["RspResult"].has_key("rspErrCode") and __REQ__["RspResult"]["rspErrCode"] == "AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0201_STEP3_NODE5;
        elif(_Result_[0] == 1): 
            return TD0201_STEP3_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP3_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 AFE处理失败");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["RspResult"].get("rspErrCode","");
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["RspResult"].get("rspErrMsg","");
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE20;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 三方处理状态映射");

        _Arg0_ = __REQ__["RspResult"]["rescode"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "N";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "Y";
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

        if(_Result_[0] == 0): 
            return TD0201_STEP3_NODE18;
        elif(_Result_[0] == 1): 
            return TD0201_STEP3_NODE18;
        elif(_Result_[0] == 2): 
            return TD0201_STEP3_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断今日是否有批扣数据");

        _Arg0_ = __REQ__["RspResult"].has_key("FileName") and __REQ__["RspResult"]["FileName"] != "";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0201_STEP3_NODE8;
        elif(_Result_[0] == 1): 
            return TD0201_STEP3_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取客户批次号");

        _Arg0_ = "SEQ_CUSTOMBATCHID";
        ACMP_Builtin_LoggerVar(0,"A0",_Arg0_);
        _Arg1_ = 8;
        ACMP_Builtin_LoggerVar(0,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["FeeIDSeq"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(0,"O0",__REQ__["FeeIDSeq"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 对象初始化");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "__SEND__";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = {  "reqSendDate":__REQ__["CurrentDate"],  "reqSendTime":__REQ__["CurrentTime"],  "reqProdArea":"511300",  "reqProdCate":__REQ__["AppType"],  "reqProdCode":__REQ__["AppID"],  "reqProdSubCate":__REQ__["AppID"],  "reqReceiverSID":"",  "reqTransID":"FBAP"+__REQ__["PlatformSerialno"],  "reqReserve":"",  "AFAServiceFunCode":"D00001",  "MC":__REQ__["__MC__"],  "TC":"D0201",   "FilePath":__REQ__["ReqFilePath"],  "SchoolCode":__REQ__["AgreeMentInfo"][int(__REQ__["i"])][3],};
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE14;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取客户批次号");

        _Arg0_ = "SEQ_CUSTOMBATCHID";
        ACMP_Builtin_LoggerVar(0,"A0",_Arg0_);
        _Arg1_ = 8;
        ACMP_Builtin_LoggerVar(0,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["FeeIDSeq"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(0,"O0",__REQ__["FeeIDSeq"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 登记客户批次信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [  ["CustomerID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][4]],  ["AppType",__REQ__["AppType"]],  ["AppID",__REQ__["AppID"]],  ["AgreementID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][3]],  ["CustBatchID",__REQ__["CurrentDate"]+__REQ__["FeeIDSeq"]],  ["IsUrgent","0"],  ["BankBranchID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][1]],  ["ChannelID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][0]],  ["Teller",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][2]],  ["Channelserialno",""],  ["CreateDate",__REQ__["CurrentDate"]],  ["ExcuteStatus","00"],  ["Status","1"],  ["IsBatchClear","0"],  ["RuleModeID",""],  ["IsSubscribe","0"],  ["IsRealTimeDeal","1"],  ["IsNeedMoneyCtrl","0"],  ["MoneyCtrlDirection","0"],  ["MoneyCtrlAmount","0"],  ["IsCrtRspFile","0"],  ["BatchFilePath",__REQ__["ReqFilePath"]],  ["BatchFileName",__REQ__["RspResult"]["FileName"]],  ["DecodeBatchFileName",""],  ["BatchRspPath",""],  ["BatchRspName",""],  ["TotalRecords","0"],  ["TotalAmount","0"],  ["SucRecords","0"],  ["SucAmount","0"],  ["ErroCode","000000"],  ["ErroMsg","客户批次创建成功！"],  ["IsRecvFee","0"],  ["FeeIsRecvFlg","0"],  ["OperateInfo","0"],  ["NearstDate",__REQ__["CurrentDate"]],  ["NearstTime",__REQ__["INCurrentTime"]],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = True;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLIns(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE27;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0201_STEP3_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取签约信息");

        _Arg0_ = "select  A.VMCHANNELID, A.BRANCHID, A.VMTELLETER, B.PROTOCOLNO, B.ENTERPLATCLIENTNO from ABOP_APPBATCHINDOORACCTINFO A   join AFA_MEMY_PROTOCOLINFO B on A.AGREEMENTID=B.PROTOCOLNO  where  A.APPTYPE=? and  A.APPID=? and A.BankAccType=? and B.PROTOCOLSTATUS=? and B.PRODUCTCODE=?";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [__REQ__["AppType"],__REQ__["AppID"],'1','A2',__REQ__["AppID"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["Temp"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["Temp"]);
            __REQ__["AgreeMentInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["AgreeMentInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE17;
        elif(_Result_[0] == 2): 
            return TD0201_STEP3_NODE23;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP3_NODE4;
        elif(_Result_[0] == 1): 
            return TD0201_STEP3_NODE3;
        elif(_Result_[0] == 2): 
            return TD0201_STEP3_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP3_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE16(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 登记客户批次信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [  ["CustomerID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][4]],  ["AppType",__REQ__["AppType"]],  ["AppID",__REQ__["AppID"]],  ["AgreementID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][3]],  ["CustBatchID",__REQ__["CurrentDate"]+__REQ__["FeeIDSeq"]],  ["IsUrgent","0"],  ["BankBranchID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][1]],  ["ChannelID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][0]],  ["Teller",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][2]],  ["Channelserialno",""],  ["CreateDate",__REQ__["CurrentDate"]],  ["ExcuteStatus","61"],  ["Status","2"],  ["IsBatchClear","0"],  ["RuleModeID",""],  ["IsSubscribe","0"],  ["IsRealTimeDeal","1"],  ["IsNeedMoneyCtrl","0"],  ["MoneyCtrlDirection","0"],  ["MoneyCtrlAmount","0"],  ["IsCrtRspFile","0"],  ["BatchFilePath",__REQ__["ReqFilePath"]],  ["BatchFileName",__REQ__["RspResult"]["FileName"]],  ["DecodeBatchFileName",""],  ["BatchRspPath",""],  ["BatchRspName",""],  ["TotalRecords","0"],  ["TotalAmount","0"],  ["SucRecords","0"],  ["SucAmount","0"],  ["ErroCode","000000"],  ["ErroMsg","该批次今日没有代扣数据！"],  ["IsRecvFee","0"],  ["FeeIsRecvFlg","0"],  ["OperateInfo","0"],  ["NearstDate",__REQ__["CurrentDate"]],  ["NearstTime",__REQ__["INCurrentTime"]],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = True;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLIns(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE27;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 时间赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "INCurrentTime";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["CurrentTime"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE26;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取客户批次号");

        _Arg0_ = "SEQ_CUSTOMBATCHID";
        ACMP_Builtin_LoggerVar(0,"A0",_Arg0_);
        _Arg1_ = 8;
        ACMP_Builtin_LoggerVar(0,"A1",_Arg1_);

        _Result_ = B_ABOP_DB_B_db_sequence(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["FeeIDSeq"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(0,"O0",__REQ__["FeeIDSeq"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 登记客户批次信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [  ["CustomerID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][4]],  ["AppType",__REQ__["AppType"]],  ["AppID",__REQ__["AppID"]],  ["AgreementID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][3]],  ["CustBatchID",__REQ__["CurrentDate"]+__REQ__["FeeIDSeq"]],  ["IsUrgent","0"],  ["BankBranchID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][1]],  ["ChannelID",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][0]],  ["Teller",__REQ__["AgreeMentInfo"][int(__REQ__["i"])][2]],  ["Channelserialno",""],  ["CreateDate",__REQ__["CurrentDate"]],  ["ExcuteStatus","00"],  ["Status","9"],  ["IsBatchClear","0"],  ["RuleModeID",""],  ["IsSubscribe","0"],  ["IsRealTimeDeal","1"],  ["IsNeedMoneyCtrl","0"],  ["MoneyCtrlDirection","0"],  ["MoneyCtrlAmount","0"],  ["IsCrtRspFile","0"],  ["BatchFilePath",__REQ__["ReqFilePath"]],  ["BatchFileName",__REQ__["RspResult"]["FileName"]],  ["DecodeBatchFileName",""],  ["BatchRspPath",""],  ["BatchRspName",""],  ["TotalRecords","0"],  ["TotalAmount","0"],  ["SucRecords","0"],  ["SucAmount","0"],  ["ErroCode","000001"],  ["ErroMsg","三方报错，客户批次创建失败！"],  ["IsRecvFee","0"],  ["FeeIsRecvFlg","0"],  ["OperateInfo","0"],  ["NearstDate",__REQ__["CurrentDate"]],  ["NearstTime",__REQ__["INCurrentTime"]],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = True;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLIns(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE27;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0201_STEP3_NODE23(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 设置全局错误");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "OP10";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "南部校园一卡通对公协议不存在！";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE24(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0201_STEP3_NODE25(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断文件是否获取完成");

        _Arg0_ = int(__REQ__["i"]) < int(__REQ__["Temp"]);
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0201_STEP3_NODE12;
        elif(_Result_[0] == 1): 
            return TD0201_STEP3_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE26(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 初始化字段赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "i";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE25;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_NODE27(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 给容器赋值（内建）");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "i";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = int(__REQ__["i"])+1;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP3_NODE25;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP3_NODE24);

def TD0201_STEP3_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 3 功能 代扣数据申请");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0201_STEP3_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0201_STEP5_IMPL;
        else:
            return TD0201_STEP6_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0201_STEP5_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0201_STEP5_NODE2;

def TD0201_STEP5_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0201_STEP5_NODE3);
    AFALoggerInfor("将默认异常委托到 TD0201_STEP5_NODE3 节点");

    return TD0201_STEP5_NODE6;

def TD0201_STEP5_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0201_STEP5_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 设置交易执行成功");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");

        _Result_ = B_ABOP_Trade_B_TradeSuccess(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP5_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP5_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP5_NODE3);

def TD0201_STEP5_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0201_STEP5_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 容器变量赋值");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");
        _Arg1_ = [["dealcode","000000"],["dealmsg","代扣文件申请交易成功！"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP5_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP5_NODE3);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP5_NODE3);

def TD0201_STEP5_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 5 功能 正确返回");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0201_STEP5_NODE1;
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

def TD0201_STEP6_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0201_STEP6_NODE2;

def TD0201_STEP6_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0201_STEP6_NODE5);
    AFALoggerInfor("将默认异常委托到 TD0201_STEP6_NODE5 节点");

    return TD0201_STEP6_NODE3;

def TD0201_STEP6_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP6_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP6_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP6_NODE5);

def TD0201_STEP6_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 容器变量赋值");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");
        _Arg1_ = [["dealcode",__REQ__["ErrorCode"]],["dealmsg",__REQ__["ErrorMsg"]]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0201_STEP6_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP6_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP6_NODE5);

def TD0201_STEP6_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0201_STEP6_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0201_STEP6_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP6_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0201_STEP6_NODE5);

def TD0201_STEP6_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0201_STEP6_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 6 功能 异常返回");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0201_STEP6_NODE1;
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
def MD0201_ENTRY(__REQ__,__RSP__):
    AFALoggerInfor("开始交易 D0201:代扣文件申请");

    __SND__ = {};
    __RCV__ = {};

    __REQ__["__TRADENAME__"] = "代扣文件申请";

    ACMP_Builtin_TradeInitialize(__REQ__,__RSP__,"KAS_SSK");

    _Result_ = None;
    _Method_ = TD0201_STEP1_IMPL;
    while(type(_Method_) is FunctionType):
        AFALoggerInfor(("Step "+getattr(_Method_,"__name__")));
        _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
        _Method_ = _Result_;

    __SND__.clear();
    __RCV__.clear();
    del __SND__;
    del __RCV__;

    ACMP_Builtin_CheckResponse(__REQ__,__RSP__);
    AFALoggerInfor("结束交易 D0201");

    return True;
