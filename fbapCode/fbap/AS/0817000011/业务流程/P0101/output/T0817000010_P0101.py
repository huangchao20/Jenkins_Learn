# -*- coding: gbk -*-
'''
----------------------------------------------------------------
内部名称：AS
说    明：代理教育类
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
from B_Message import B_Mesg_Pack as B_Message_B_Mesg_Pack;
from B_Interface import B_API_MapMsg as B_Interface_B_API_MapMsg;
from P_DataBase import P_DB_ExecGrpSQL as P_DataBase_P_DB_ExecGrpSQL;
from AS_0817000010 import COMP_B0000101_ENTRY as AS_0817000010_B0000101;
from P_Time import P_Date_Fmt as P_Time_P_Date_Fmt;
from P_Dict import P_Dict_SetValue as P_Dict_P_Dict_SetValue;
from P_Object import P_Obj_Crt as P_Object_P_Obj_Crt;
from B_RiskCtrl import B_RiskCtrl_SelTimeOutTrade as B_RiskCtrl_B_RiskCtrl_SelTimeOutTrade;
from P_Cmd import P_GetTradeLogPath as P_Cmd_P_GetTradeLogPath;
from P_Cmd import P_GetIp as P_Cmd_P_GetIp;
from B_Interface import B_API_InitMsg as B_Interface_B_API_InitMsg;
from B_Message import B_Mesg_UnPack as B_Message_B_Mesg_UnPack;



'''
--------------------------- 项目分期 ---------------------------
名    称：0817000010
描    述：南部校园一卡通
----------------------------------------------------------------
'''


def TP0101_STEP7_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TP0101_STEP7_NODE2;

def TP0101_STEP7_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TP0101_STEP7_NODE11);
    AFALoggerInfor("将默认异常委托到 TP0101_STEP7_NODE11 节点");

    return TP0101_STEP7_NODE3;

def TP0101_STEP7_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 报文拆包");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "natp";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = B_Message_B_Mesg_UnPack(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP7_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

def TP0101_STEP7_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 交易初始化");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = __REQ__["__MC__"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["__TC__"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "N";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = B_Interface_B_API_InitMsg(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));
        print("RET="+str(_Result_[0]))

        if(_Result_[0] == 1): 
            return TP0101_STEP7_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        print(str(PyExcp))
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

def TP0101_STEP7_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取系统IP");

        _Arg0_ = __REQ__["_NETNAME_"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = None;
        ACMP_Builtin_LoggerVar(4, "A1", None);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);

        _Result_ = P_Cmd_P_GetIp(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["serverip"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["serverip"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP7_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

def TP0101_STEP7_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取交易日志路径");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = None;
        ACMP_Builtin_LoggerVar(4, "A1", None);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);

        _Result_ = P_Cmd_P_GetTradeLogPath(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP7_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

def TP0101_STEP7_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 超时交易友好拒绝");

        _Arg0_ = __REQ__["__MC__"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["__TC__"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["workdate"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);

        _Result_ = B_RiskCtrl_B_RiskCtrl_SelTimeOutTrade(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP7_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

def TP0101_STEP7_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 创建信息数据字典");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(3,"A0","__REQ__");
        _Arg1_ = [ ["AGENT",dict] ];
        ACMP_Builtin_LoggerVar(3,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Object_P_Obj_Crt(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP7_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

def TP0101_STEP7_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 查询sqlkey条件赋值");

        _Arg0_ = __REQ__["AGENT"];
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["productcode" , __REQ__["productcode"]], ["templatecode" , __REQ__["templatecode"]], ["transcode" , __REQ__["transcode"]], ["busitype" , __REQ__.get("busitype","0")], ];
        ACMP_Builtin_LoggerVar(3,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Dict_P_Dict_SetValue(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP7_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

def TP0101_STEP7_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TP0101_STEP7_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取全局错误到容器（内建）");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "status";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "dealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "dealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP7_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP7_NODE12);

def TP0101_STEP7_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TP0101_STEP7_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 7 功能 拆渠道请求报文");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TP0101_STEP7_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TP0101_STEP8_IMPL;
        else:
            return TP0101_STEP9_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TP0101_STEP8_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TP0101_STEP8_NODE2;

def TP0101_STEP8_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TP0101_STEP8_NODE10);
    AFALoggerInfor("将默认异常委托到 TP0101_STEP8_NODE10 节点");

    return TP0101_STEP8_NODE3;

def TP0101_STEP8_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [ ['retInfo', {}] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Dict_P_Dict_SetValue(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP8_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 送三方字段处理");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [  ["BankAccountName",__REQ__.get("BankAccountName","")],  ["SignBegDate",__REQ__["newdate"]],  ["SignBegDate","2099-12-30"],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Dict_P_Dict_SetValue(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP8_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 日期格式化");

        _Arg0_ = __REQ__["workdate"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "yyyy-mm-dd";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Time_P_Date_Fmt(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["newdate"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["newdate"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP8_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断用户编号长度");

        _Arg0_ = len(__REQ__["CustomerNo"]) == 18;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TP0101_STEP8_NODE12;
        elif(_Result_[0] == 1): 
            return TP0101_STEP8_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 缴费签约");

        __DeFaultExcp__ = ACMP_Builtin_GetDefaultExceptNode(None);

        AFALoggerTrace(">>>>>>开始业务组件调用<<<<<<");
        __BUILTIN__ = {};
        __BUILTIN__["reqseq"] = deepcopy(__REQ__["agentserialno"]);
        ACMP_Builtin_LoggerVar(4,'A0:__BUILTIN__["reqseq"]',__BUILTIN__["reqseq"]);
        __BUILTIN__["reqdate"] = deepcopy(__REQ__["newdate"]+" "+__REQ__["newtime"]);
        ACMP_Builtin_LoggerVar(4,'A1:__BUILTIN__["reqdate"]',__BUILTIN__["reqdate"]);
        __BUILTIN__["SchoolCode"] = deepcopy(__REQ__["SchoolCode"]);
        ACMP_Builtin_LoggerVar(4,'A2:__BUILTIN__["SchoolCode"]',__BUILTIN__["SchoolCode"]);
        __BUILTIN__["No"] = deepcopy(__REQ__["CustomerNo"]);
        ACMP_Builtin_LoggerVar(4,'A3:__BUILTIN__["No"]',__BUILTIN__["No"]);
        __BUILTIN__["CustomerNo"] = deepcopy(__REQ__["CustomerName"]);
        ACMP_Builtin_LoggerVar(4,'A4:__BUILTIN__["CustomerNo"]',__BUILTIN__["CustomerNo"]);
        __BUILTIN__["CustomerName"] = deepcopy(__REQ__["BankAccountNo"]);
        ACMP_Builtin_LoggerVar(4,'A5:__BUILTIN__["CustomerName"]',__BUILTIN__["CustomerName"]);
        __BUILTIN__["BankAccountNo"] = deepcopy(__REQ__["BankAccountName"]);
        ACMP_Builtin_LoggerVar(4,'A6:__BUILTIN__["BankAccountNo"]',__BUILTIN__["BankAccountNo"]);
        __BUILTIN__["BankAccountName"] = deepcopy(__REQ__["SignBegDate"]);
        ACMP_Builtin_LoggerVar(4,'A7:__BUILTIN__["BankAccountName"]',__BUILTIN__["BankAccountName"]);
        __BUILTIN__["SignBegDate"] = deepcopy(__REQ__["SignEndDate"]);
        ACMP_Builtin_LoggerVar(4,'A8:__BUILTIN__["SignBegDate"]',__BUILTIN__["SignBegDate"]);
        __BUILTIN__["SignEndDate"] = deepcopy(__REQ__["SignEndDate"]);
        ACMP_Builtin_LoggerVar(4,'A9:__BUILTIN__["SignEndDate"]',__BUILTIN__["SignEndDate"]);

        _Result_ = AS_0817000010_B0000101(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__);
        ACMP_Builtin_SetDefaultExceptNode(__DeFaultExcp__);

        if __BUILTIN__.has_key("thirdstatus"):
            __REQ__["thirdstatus"] = __BUILTIN__.get("thirdstatus");
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["thirdstatus"]);
        if __BUILTIN__.has_key("thirddealcode"):
            __REQ__["thirddealcode"] = __BUILTIN__.get("thirddealcode");
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["thirddealcode"]);
        if __BUILTIN__.has_key("thirddealmsg"):
            __REQ__["thirddealmsg"] = __BUILTIN__.get("thirddealmsg");
            ACMP_Builtin_LoggerVar(4,"O2",__REQ__["thirddealmsg"]);
        AFALoggerInfor("RET="+str(_Result_));

        AFALoggerTrace(">>>>>>结束业务组件调用<<<<<<");
        if(_Result_ == True): 
            return TP0101_STEP8_NODE16;
        elif(_Result_ == False): 
            return TP0101_STEP8_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E","ACMP0010","业务组件返回值不正确");
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetDefaultExceptNode(__DeFaultExcp__);
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        AFALoggerTrace(">>>>>>结束业务组件调用<<<<<<");
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新步骤状态为成功");

        _Arg0_ = { "agentserialno" : __REQ__["agentserialno"], "workdate" : __REQ__["workdate"], "tradestep" : __REQ__["tradestep"], "tradebusistep" : __REQ__["_BusiStep_Receipt"], "tradestatus" : __REQ__["_BusiStatus_Succ"], "status" : __REQ__.get("status",""), "dealcode" : __REQ__.get("dealcode",""), "dealmsg" : __REQ__.get("dealmsg",""), "thirdstatus" : __REQ__.get("thirdstatus",""), "thirddealcode" : __REQ__.get("thirddealcode",""), "thirddealmsg" : __REQ__.get("thirddealmsg",""), };
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = "ALT_THIRD_FLOWSTATUS";
        ACMP_Builtin_LoggerVar(3,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(3,"A2",_Arg2_);
        _Arg3_ = True;
        ACMP_Builtin_LoggerVar(3,"A3",_Arg3_);
        _Arg4_ = __REQ__["AGENT"];
        ACMP_Builtin_LoggerVar(3,"A4",_Arg4_);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);

        _Result_ = P_DataBase_P_DB_ExecGrpSQL(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP8_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TP0101_STEP8_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "status";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "dealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "dealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP8_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 请求ESB失败设置");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(3,"A0","__REQ__");
        _Arg1_ = [ ["status" ,"F"], ["_Send_Status_" ,"F"], ];
        ACMP_Builtin_LoggerVar(3,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Dict_P_Dict_SetValue(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TP0101_STEP8_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [  ["dealcode","FBAP01"],  ["dealmsg","用户编号长度错误，请输入18为身份证号码！"],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Dict_P_Dict_SetValue(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP8_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新步骤状态为失败");

        _Arg0_ = { "agentserialno" : __REQ__["agentserialno"], "workdate" : __REQ__["workdate"], "tradestep" : __REQ__["tradestep"], "tradebusistep" : __REQ__["_BusiStep_Receipt"], "tradestatus" : __REQ__["_BusiStatus_Fail"], "status" : __REQ__.get("status",""), "dealcode" : __REQ__.get("dealcode",""), "dealmsg" : __REQ__.get("dealmsg",""), "thirdstatus" : __REQ__.get("thirdstatus",""), "thirddealcode" : __REQ__.get("thirddealcode",""), "thirddealmsg" : __REQ__.get("thirddealmsg",""), };
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = "ALT_THIRD_FLOWSTATUS";
        ACMP_Builtin_LoggerVar(3,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(3,"A2",_Arg2_);
        _Arg3_ = True;
        ACMP_Builtin_LoggerVar(3,"A3",_Arg3_);
        _Arg4_ = __REQ__["AGENT"];
        ACMP_Builtin_LoggerVar(3,"A4",_Arg4_);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);

        _Result_ = P_DataBase_P_DB_ExecGrpSQL(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP8_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [  ["dealcode",__REQ__.get("thirddealcode","FBAP21")],  ["dealmsg",__REQ__.get("thirddealmsg","申请失败")],];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Dict_P_Dict_SetValue(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP8_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TP0101_STEP8_NODE16(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 查询是否成功");

        _Arg0_ = __REQ__["thirdstatus"] == "S";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TP0101_STEP8_NODE14;
        elif(_Result_[0] == 1): 
            return TP0101_STEP8_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP8_NODE15);

def TP0101_STEP8_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 8 功能 组单笔发送报文");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TP0101_STEP8_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TP0101_STEP9_IMPL;
        else:
            return TP0101_STEP9_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TP0101_STEP9_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TP0101_STEP9_NODE2;

def TP0101_STEP9_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TP0101_STEP9_NODE11);
    AFALoggerInfor("将默认异常委托到 TP0101_STEP9_NODE11 节点");

    return TP0101_STEP9_NODE3;

def TP0101_STEP9_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 交易初始化是否正常");

        _Arg0_ = __REQ__.has_key("_Plat_RetCode_Success_");
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TP0101_STEP9_NODE10;
        elif(_Result_[0] == 1): 
            return TP0101_STEP9_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

def TP0101_STEP9_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 交易是否异常");

        _Arg0_ = __REQ__.has_key("dealcode") and __REQ__["dealcode"] != __REQ__["_Plat_RetCode_Success_"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TP0101_STEP9_NODE6;
        elif(_Result_[0] == 1): 
            return TP0101_STEP9_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

def TP0101_STEP9_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 交易状态赋值");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(3,"A0","__RSP__");
        _Arg1_ = [["status", "F"]];
        ACMP_Builtin_LoggerVar(3,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Dict_P_Dict_SetValue(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP9_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

def TP0101_STEP9_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 通讯参数赋值");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(3,"A0","__RSP__");
        _Arg1_ = [ ["MC",__REQ__["__MC__"]], ["TC",__REQ__["__TC__"]] ];
        ACMP_Builtin_LoggerVar(3,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Dict_P_Dict_SetValue(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP9_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

def TP0101_STEP9_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 接口字典映射");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(3,"A0","__REQ__");
        _Arg1_ = "chl->afa";
        ACMP_Builtin_LoggerVar(3,"A1",_Arg1_);
        _Arg2_ = __REQ__["_MSGTYPELIST_RSP_"];
        ACMP_Builtin_LoggerVar(3,"A2",_Arg2_);
        _Arg3_ = __RSP__;
        ACMP_Builtin_LoggerVar(3,"A3","__RSP__");
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = B_Interface_B_API_MapMsg(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP9_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

def TP0101_STEP9_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 报文拼包");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");
        _Arg1_ = "natp";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);

        _Result_ = B_Message_B_Mesg_Pack(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP9_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

def TP0101_STEP9_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TP0101_STEP9_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 交易是否异常");

        _Arg0_ = __REQ__.has_key("dealcode") and __REQ__["dealcode"] != "000000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TP0101_STEP9_NODE6;
        elif(_Result_[0] == 1): 
            return TP0101_STEP9_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

def TP0101_STEP9_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "status";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "dealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "dealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TP0101_STEP9_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TP0101_STEP9_NODE12);

def TP0101_STEP9_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TP0101_STEP9_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 9 功能 同步响应渠道");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TP0101_STEP9_NODE1;
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
def MP0101_ENTRY(__REQ__,__RSP__):
    AFALoggerInfor("开始交易 P0101:校园卡签约");

    __SND__ = {};
    __RCV__ = {};

    __REQ__["__TRADENAME__"] = "校园卡签约";

    ACMP_Builtin_TradeInitialize(__REQ__,__RSP__,"KAS_SSK");

    _Result_ = None;
    _Method_ = TP0101_STEP7_IMPL;
    while(type(_Method_) is FunctionType):
        AFALoggerInfor(("Step "+getattr(_Method_,"__name__")));
        _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
        _Method_ = _Result_;

    __SND__.clear();
    __RCV__.clear();
    del __SND__;
    del __RCV__;

    ACMP_Builtin_CheckResponse(__REQ__,__RSP__);
    AFALoggerInfor("结束交易 P0101");

    return True;
