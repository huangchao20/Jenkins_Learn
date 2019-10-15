# -*- coding: gbk -*-
'''
----------------------------------------------------------------
内部名称：AS_0817000010
说    明：南部校园一卡通
备    注：赞同科技AFA编译器V3.7.0.2 业务组件编译模式
----------------------------------------------------------------
'''


'''
import sys function:
'''
from copy  import deepcopy;
from types import FunctionType;
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
from AFABuiltIn import ACMP_Builtin_GetDefaultExceptNode;
from AFABuiltIn import ACMP_Builtin_SetDefaultExceptNode;
from AFABuiltIn import ACMP_Builtin_BoolFrame;
from AFABuiltIn import ACMP_Builtin_DefaultErrorHolder;
from AFABuiltIn import ACMP_Builtin_SwitchCaseFrame;
from AFABuiltIn import ACMP_Builtin_SetValueToContext;
from AFABuiltIn import ACMP_Builtin_SetErrorToGlobal;
from AFABuiltIn import ACMP_Builtin_GetGlobalErrorToDict;
from AFABuiltIn import ACMP_Builtin_SwitchToAsyncMode;

#import dependent components
from P_Dict import P_Dict_Copy as P_Dict_P_Dict_Copy;
from B_Message import B_Mesg_UnPack as B_Message_B_Mesg_UnPack;
from B_Communicate import B_Comm_CommClient as B_Communicate_B_Comm_CommClient;
from P_Dict import P_Dict_SetValue as P_Dict_P_Dict_SetValue;
from P_Object import P_Obj_Crt as P_Object_P_Obj_Crt;

def COMP_C00005_NODE1(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__={}):
    AFALoggerInfor("功能 开始");
    return COMP_C00005_NODE2;

def COMP_C00005_NODE2(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(COMP_C00005_NODE6);
    AFALoggerInfor("将默认异常委托到 COMP_C00005_NODE6 节点");

    return COMP_C00005_NODE3;

def COMP_C00005_NODE3(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 创建映射列表");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["_ReqList_", list],["_RspList_", list],["ReqDict" , dict],["RspDict" , dict]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Object_P_Obj_Crt(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00005_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE4(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [   ["MC" ,"0817000010"],   ["AFAServiceFunCode" ,"C00005"],];
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
            return COMP_C00005_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE5(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 通讯客户端");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "natpbl";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "0817000010_PUB";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = B_Communicate_B_Comm_CommClient(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __BUILTIN__["RspDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__BUILTIN__["RspDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00005_NODE9;
        elif(_Result_[0] == 1): 
            return COMP_C00005_NODE7;
        elif(_Result_[0] == 2): 
            return COMP_C00005_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE6(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "thirdstatus";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "thirddealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "thirddealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00005_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE7(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 报文拆包");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "NATP";
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
            return COMP_C00005_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE8(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE超时设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "E"], ["thirddealcode"   , "FBAPEOUT"], ["thirddealmsg"    , "通信超时/异常!"],];
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
            return COMP_C00005_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE9(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "F"], ["thirddealcode"   , "FBAP00"], ["thirddealmsg"    , "请求AFE失败！"],];
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
            return COMP_C00005_NODE12;
        elif(_Result_[0] == 1): 
            return COMP_C00005_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE10(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量拷贝");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [["AccountID","AccountID"],["Sno","Sno"],["Name","Name"],["DeptName","DeptName"],["TranNo","TranNo"],["TranMoney","TranMoney"],];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = P_Dict_P_Dict_Copy(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00005_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE11(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 判断AFE错误码");

        _Arg0_ = __BUILTIN__["RspDict"].has_key("afecode") and __BUILTIN__["RspDict"]["afecode"] == "AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00005_NODE14;
        elif(_Result_[0] == 1): 
            return COMP_C00005_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE12(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 异常结束");
    return False;

def COMP_C00005_NODE13(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00005_NODE14(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode",__BUILTIN__.get("errCode","")], ["thirddealmsg",__BUILTIN__.get("errMsg","")], ];
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
            return COMP_C00005_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE15(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 SWITCH实现框架（内建）");

        _Arg0_ = __BUILTIN__["RspDict"]["ThirdRetCode"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = None;
        ACMP_Builtin_LoggerVar(4, "A1", None);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = "000000";
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00005_NODE18;
        elif(_Result_[0] == 5): 
            return COMP_C00005_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE16(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00005_NODE17(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 成功赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "S"], ["thirddealcode"   , "1"], ["thirddealmsg"    , "查询成功"],];
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
            return COMP_C00005_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE18(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 失败赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [["thirdstatus" , "F"],["thirddealcode" , __BUILTIN__["RspDict"]["ThirdRetCode"]],["thirddealmsg" ,__BUILTIN__["RspDict"]["ThirdRetMsg"]],];
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
            return COMP_C00005_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00005_NODE12);

def COMP_C00005_NODE19(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00005_ENTRY(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("开始运行组件 钱包冲正");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = False;
        _Method_ = COMP_C00005_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__);
            _Method_ = _Result_;

        return (_Method_ == True);
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def COMP_DZ_NODE1(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__={}):
    AFALoggerInfor("功能 开始");
    return COMP_DZ_NODE2;

def COMP_DZ_NODE2(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(COMP_DZ_NODE6);
    AFALoggerInfor("将默认异常委托到 COMP_DZ_NODE6 节点");

    return COMP_DZ_NODE3;

def COMP_DZ_NODE3(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 创建映射列表");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["_ReqList_", list],["_RspList_", list],["ReqDict" , dict],["RspDict" , dict]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Object_P_Obj_Crt(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_DZ_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE4(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [   ["MC" ,"0817000010"],   ["AFAServiceFunCode" ,"Z00001"],];
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
            return COMP_DZ_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE5(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 通讯客户端");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "natpbl";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "0817000010_PUB";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = B_Communicate_B_Comm_CommClient(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __BUILTIN__["RspDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__BUILTIN__["RspDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_DZ_NODE9;
        elif(_Result_[0] == 1): 
            return COMP_DZ_NODE7;
        elif(_Result_[0] == 2): 
            return COMP_DZ_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE6(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "thirdstatus";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "thirddealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "thirddealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_DZ_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE7(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 报文拆包");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "NATP";
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
            return COMP_DZ_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE8(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE超时设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"E"], ["thirddealcode" ,"FBAPEOUT"], ["thirddealmsg" ,"通信超时/异常!"], ];
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
            return COMP_DZ_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE9(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode","FBAP00"], ["thirddealmsg","请求AFE失败！"], ];
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
            return COMP_DZ_NODE12;
        elif(_Result_[0] == 1): 
            return COMP_DZ_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE10(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量拷贝");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [["Name","Name"],["Sex","Sex"],["DeptName","DeptName"],["AccountID","AccountID"],["Sno","Sno"],["CardNo","CardNo"],["IDType","IDType"],["IDCard","IDCard"],["BankNo","BankNo"],["Status","Status"],["EbagBalance","EbagBalance"],["Photo","Photo"],];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = P_Dict_P_Dict_Copy(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_DZ_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE11(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 判断AFE错误码");

        _Arg0_ = __BUILTIN__["RspDict"].has_key("afecode") and __BUILTIN__["RspDict"]["afecode"] == "AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_DZ_NODE14;
        elif(_Result_[0] == 1): 
            return COMP_DZ_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE12(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 异常结束");
    return False;

def COMP_DZ_NODE13(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_DZ_NODE14(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode",__BUILTIN__.get("errCode","")], ["thirddealmsg",__BUILTIN__.get("errMsg","")], ];
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
            return COMP_DZ_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE15(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 SWITCH实现框架（内建）");

        _Arg0_ = __BUILTIN__["RspDict"]["ThirdRetCode"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = None;
        ACMP_Builtin_LoggerVar(4, "A1", None);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = "000000";
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_DZ_NODE18;
        elif(_Result_[0] == 5): 
            return COMP_DZ_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE16(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_DZ_NODE17(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 成功赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "S"], ["thirddealcode"   , "000000"], ["thirddealmsg"    , "成功"],];
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
            return COMP_DZ_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE18(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 失败赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [["thirdstatus" , "S"],["thirddealcode" , __BUILTIN__["RspDict"]["ThirdRetCode"]],["thirddealmsg" ,__BUILTIN__["RspDict"]["ThirdRetMsg"]],];
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
            return COMP_DZ_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_DZ_NODE12);

def COMP_DZ_NODE19(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_DZ_ENTRY(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("开始运行组件 发送对账通知");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = False;
        _Method_ = COMP_DZ_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__);
            _Method_ = _Result_;

        return (_Method_ == True);
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def COMP_C00003_NODE1(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__={}):
    AFALoggerInfor("功能 开始");
    return COMP_C00003_NODE2;

def COMP_C00003_NODE2(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(COMP_C00003_NODE6);
    AFALoggerInfor("将默认异常委托到 COMP_C00003_NODE6 节点");

    return COMP_C00003_NODE3;

def COMP_C00003_NODE3(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 创建映射列表");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["_ReqList_", list],["_RspList_", list],["ReqDict" , dict],["RspDict" , dict]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Object_P_Obj_Crt(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00003_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE4(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [   ["MC" ,"0817000010"],   ["AFAServiceFunCode" ,"C00003"],];
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
            return COMP_C00003_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE5(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 通讯客户端");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "natpbl";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "0817000010_PUB";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = B_Communicate_B_Comm_CommClient(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __BUILTIN__["RspDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__BUILTIN__["RspDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00003_NODE9;
        elif(_Result_[0] == 1): 
            return COMP_C00003_NODE7;
        elif(_Result_[0] == 2): 
            return COMP_C00003_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE6(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "thirdstatus";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "thirddealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "thirddealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00003_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE7(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 报文拆包");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "NATP";
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
            return COMP_C00003_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE8(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE超时设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "E"], ["thirddealcode"   , "FBAPEOUT"], ["thirddealmsg"    , "通信超时/异常!"],];
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
            return COMP_C00003_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE9(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "F"], ["thirddealcode"   , "FBAP00"], ["thirddealmsg"    , "请求AFE失败！"],];
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
            return COMP_C00003_NODE12;
        elif(_Result_[0] == 1): 
            return COMP_C00003_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE10(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量拷贝");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [["AccountID","AccountID"],["Sno","Sno"],["Name","Name"],["DeptName","DeptName"],["TranNo","TranNo"],["TranMoney","TranMoney"],];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = P_Dict_P_Dict_Copy(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00003_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE11(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 判断AFE错误码");

        _Arg0_ = __BUILTIN__["RspDict"].has_key("afecode") and __BUILTIN__["RspDict"]["afecode"] == "AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00003_NODE14;
        elif(_Result_[0] == 1): 
            return COMP_C00003_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE12(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 异常结束");
    return False;

def COMP_C00003_NODE13(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00003_NODE14(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode",__BUILTIN__.get("errCode","")], ["thirddealmsg",__BUILTIN__.get("errMsg","")], ];
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
            return COMP_C00003_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE15(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 SWITCH实现框架（内建）");

        _Arg0_ = __BUILTIN__["RspDict"]["ThirdRetCode"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = None;
        ACMP_Builtin_LoggerVar(4, "A1", None);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = "000000";
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00003_NODE18;
        elif(_Result_[0] == 5): 
            return COMP_C00003_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE16(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00003_NODE17(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 成功赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "S"], ["thirddealcode"   , "1"], ["thirddealmsg"    , "查询成功"],];
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
            return COMP_C00003_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE18(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 失败赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [["thirdstatus" , "F"],["thirddealcode" , __BUILTIN__["RspDict"]["ThirdRetCode"]],["thirddealmsg" ,__BUILTIN__["RspDict"]["ThirdRetMsg"]],];
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
            return COMP_C00003_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00003_NODE12);

def COMP_C00003_NODE19(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00003_ENTRY(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("开始运行组件 钱包充值");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = False;
        _Method_ = COMP_C00003_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__);
            _Method_ = _Result_;

        return (_Method_ == True);
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def COMP_B0000102_NODE1(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__={}):
    AFALoggerInfor("功能 开始");
    return COMP_B0000102_NODE2;

def COMP_B0000102_NODE2(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(COMP_B0000102_NODE6);
    AFALoggerInfor("将默认异常委托到 COMP_B0000102_NODE6 节点");

    return COMP_B0000102_NODE3;

def COMP_B0000102_NODE3(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 创建映射列表");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["_ReqList_", list],["_RspList_", list],["ReqDict" , dict],["RspDict" , dict]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Object_P_Obj_Crt(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_B0000102_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE4(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [   ["MC" ,"0817000011"],      ["TC" ,"B00001"],   ["AFAServiceFunCode" ,"B00001"],];
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
            return COMP_B0000102_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE5(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 通讯客户端");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "natpbl";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "0817000011_PUB";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = B_Communicate_B_Comm_CommClient(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __BUILTIN__["RspDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__BUILTIN__["RspDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_B0000102_NODE9;
        elif(_Result_[0] == 1): 
            return COMP_B0000102_NODE7;
        elif(_Result_[0] == 2): 
            return COMP_B0000102_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE6(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "thirdstatus";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "thirddealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "thirddealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_B0000102_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE7(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 报文拆包");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "NATP";
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
            return COMP_B0000102_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE8(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE超时设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"E"], ["thirddealcode" ,"FBAPEOUT"], ["thirddealmsg" ,"通信超时/异常!"], ];
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
            return COMP_B0000102_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE9(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode","FBAP00"], ["thirddealmsg","请求AFE失败！"], ];
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
            return COMP_B0000102_NODE12;
        elif(_Result_[0] == 1): 
            return COMP_B0000102_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE10(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量拷贝");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [["Name","Name"],["Sex","Sex"],["DeptName","DeptName"],["AccountID","AccountID"],["Sno","Sno"],["CardNo","CardNo"],["IDType","IDType"],["IDCard","IDCard"],["BankNo","BankNo"],["Status","Status"],["EbagBalance","EbagBalance"],["Photo","Photo"],];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = P_Dict_P_Dict_Copy(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_B0000102_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE11(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 判断AFE错误码");

        _Arg0_ = __BUILTIN__["RspDict"].has_key("afecode") and __BUILTIN__["RspDict"]["afecode"] == "AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_B0000102_NODE14;
        elif(_Result_[0] == 1): 
            return COMP_B0000102_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE12(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 异常结束");
    return False;

def COMP_B0000102_NODE13(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_B0000102_NODE14(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode",__BUILTIN__.get("errCode","")], ["thirddealmsg",__BUILTIN__.get("errMsg","")], ];
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
            return COMP_B0000102_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE15(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 SWITCH实现框架（内建）");

        _Arg0_ = __BUILTIN__["RspDict"]["ThirdRetCode"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = None;
        ACMP_Builtin_LoggerVar(4, "A1", None);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = "000000";
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_B0000102_NODE18;
        elif(_Result_[0] == 5): 
            return COMP_B0000102_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE16(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_B0000102_NODE17(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 成功赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [["thirdstatus" , "S"],["thirddealcode" , "000000"],["thirddealmsg" ,"成功"],];
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
            return COMP_B0000102_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE18(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 失败赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [["thirdstatus" , "F"],["thirddealcode" , __BUILTIN__["RspDict"]["ThirdRetCode"]],["thirddealmsg" ,__BUILTIN__["RspDict"]["ThirdRetMsg"]],];
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
            return COMP_B0000102_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000102_NODE12);

def COMP_B0000102_NODE19(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_B0000102_ENTRY(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("开始运行组件 缴费解约");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = False;
        _Method_ = COMP_B0000102_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__);
            _Method_ = _Result_;

        return (_Method_ == True);
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def COMP_B0000101_NODE1(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__={}):
    AFALoggerInfor("功能 开始");
    return COMP_B0000101_NODE2;

def COMP_B0000101_NODE2(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(COMP_B0000101_NODE6);
    AFALoggerInfor("将默认异常委托到 COMP_B0000101_NODE6 节点");

    return COMP_B0000101_NODE3;

def COMP_B0000101_NODE3(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 创建映射列表");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["_ReqList_", list],["_RspList_", list],["ReqDict" , dict],["RspDict" , dict]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Object_P_Obj_Crt(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_B0000101_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE4(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [   ["MC" ,"0817000011"],      ["TC" ,"B00001"],   ["AFAServiceFunCode" ,"B00001"],];
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
            return COMP_B0000101_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE5(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 通讯客户端");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "natpbl";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "0817000011_PUB";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = B_Communicate_B_Comm_CommClient(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __BUILTIN__["RspDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__BUILTIN__["RspDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_B0000101_NODE9;
        elif(_Result_[0] == 1): 
            return COMP_B0000101_NODE7;
        elif(_Result_[0] == 2): 
            return COMP_B0000101_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE6(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "thirdstatus";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "thirddealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "thirddealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_B0000101_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE7(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 报文拆包");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "NATP";
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
            return COMP_B0000101_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE8(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE超时设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"E"], ["thirddealcode" ,"FBAPEOUT"], ["thirddealmsg" ,"通信超时/异常!"], ];
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
            return COMP_B0000101_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE9(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode","FBAP00"], ["thirddealmsg","请求AFE失败！"], ];
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
            return COMP_B0000101_NODE12;
        elif(_Result_[0] == 1): 
            return COMP_B0000101_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE11(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 判断AFE错误码");

        _Arg0_ = __BUILTIN__["RspDict"].has_key("afecode") and __BUILTIN__["RspDict"]["afecode"] == "AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_B0000101_NODE14;
        elif(_Result_[0] == 1): 
            return COMP_B0000101_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE12(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 异常结束");
    return False;

def COMP_B0000101_NODE13(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_B0000101_NODE14(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode",__BUILTIN__.get("errCode","")], ["thirddealmsg",__BUILTIN__.get("errMsg","")], ];
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
            return COMP_B0000101_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE15(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 SWITCH实现框架（内建）");

        _Arg0_ = __BUILTIN__["RspDict"]["ThirdRetCode"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = None;
        ACMP_Builtin_LoggerVar(4, "A1", None);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = "000000";
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_B0000101_NODE18;
        elif(_Result_[0] == 5): 
            return COMP_B0000101_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE16(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_B0000101_NODE17(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 成功赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "S"], ["thirddealcode"   , "000000"], ["thirddealmsg"    , "成功"],];
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
            return COMP_B0000101_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE18(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 失败赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [["thirdstatus" , "F"],["thirddealcode" , __BUILTIN__["RspDict"]["ThirdRetCode"]],["thirddealmsg" ,__BUILTIN__["RspDict"]["ThirdRetMsg"]],];
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
            return COMP_B0000101_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_B0000101_NODE12);

def COMP_B0000101_NODE19(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_B0000101_ENTRY(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("开始运行组件 缴费签约");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = False;
        _Method_ = COMP_B0000101_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__);
            _Method_ = _Result_;

        return (_Method_ == True);
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def COMP_C00001_NODE1(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__={}):
    AFALoggerInfor("功能 开始");
    return COMP_C00001_NODE2;

def COMP_C00001_NODE2(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(COMP_C00001_NODE6);
    AFALoggerInfor("将默认异常委托到 COMP_C00001_NODE6 节点");

    return COMP_C00001_NODE3;

def COMP_C00001_NODE3(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 创建映射列表");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ ["_ReqList_", list],["_RspList_", list],["ReqDict" , dict],["RspDict" , dict]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);

        _Result_ = P_Object_P_Obj_Crt(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00001_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE4(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [   ["MC" ,"0817000010"],   ["AFAServiceFunCode" ,"C00001"],];
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
            return COMP_C00001_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE5(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 通讯客户端");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "natpbl";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "0817000010_PUB";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = B_Communicate_B_Comm_CommClient(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __BUILTIN__["RspDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__BUILTIN__["RspDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00001_NODE9;
        elif(_Result_[0] == 1): 
            return COMP_C00001_NODE7;
        elif(_Result_[0] == 2): 
            return COMP_C00001_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE6(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 取全局错误到容器");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "thirdstatus";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "thirddealcode";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "thirddealmsg";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = ACMP_Builtin_GetGlobalErrorToDict(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00001_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE7(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 报文拆包");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "NATP";
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
            return COMP_C00001_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE8(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE超时设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"E"], ["thirddealcode" ,"FBAPEOUT"], ["thirddealmsg" ,"通信超时/异常!"], ];
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
            return COMP_C00001_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE9(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode","FBAP00"], ["thirddealmsg","请求AFE失败！"], ];
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
            return COMP_C00001_NODE12;
        elif(_Result_[0] == 1): 
            return COMP_C00001_NODE16;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE10(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 字典变量拷贝");

        _Arg0_ = __BUILTIN__["RspDict"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = [["Name","Name"],["Sex","Sex"],["DeptName","DeptName"],["AccountID","AccountID"],["Sno","Sno"],["CardNo","CardNo"],["IDType","IDType"],["IDCard","IDCard"],["BankNo","BankNo"],["Status","Status"],["EbagBalance","EbagBalance"],];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = None;
        ACMP_Builtin_LoggerVar(4, "A5", None);

        _Result_ = P_Dict_P_Dict_Copy(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return COMP_C00001_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE11(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 判断AFE错误码");

        _Arg0_ = __BUILTIN__["RspDict"].has_key("afecode") and __BUILTIN__["RspDict"]["afecode"] == "AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00001_NODE14;
        elif(_Result_[0] == 1): 
            return COMP_C00001_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE12(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 异常结束");
    return False;

def COMP_C00001_NODE13(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00001_NODE14(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 AFE失败设置");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus" ,"F"], ["thirddealcode",__BUILTIN__.get("errCode","")], ["thirddealmsg",__BUILTIN__.get("errMsg","")], ];
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
            return COMP_C00001_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE15(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 SWITCH实现框架（内建）");

        _Arg0_ = __BUILTIN__["RspDict"]["ThirdRetCode"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = None;
        ACMP_Builtin_LoggerVar(4, "A1", None);
        _Arg2_ = None;
        ACMP_Builtin_LoggerVar(4, "A2", None);
        _Arg3_ = None;
        ACMP_Builtin_LoggerVar(4, "A3", None);
        _Arg4_ = None;
        ACMP_Builtin_LoggerVar(4, "A4", None);
        _Arg5_ = "000000";
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);
        _Arg6_ = None;
        ACMP_Builtin_LoggerVar(4, "A6", None);
        _Arg7_ = None;
        ACMP_Builtin_LoggerVar(4, "A7", None);

        _Result_ = ACMP_Builtin_SwitchCaseFrame(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_,_Arg7_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return COMP_C00001_NODE18;
        elif(_Result_[0] == 5): 
            return COMP_C00001_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE16(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00001_NODE17(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 成功赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [ ["thirdstatus"     , "S"], ["thirddealcode"   , "1"], ["thirddealmsg"    , "审核成功"],];
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
            return COMP_C00001_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE18(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("功能 失败赋值");

        _Arg0_ = __BUILTIN__;
        ACMP_Builtin_LoggerVar(3,"A0",_Arg0_);
        _Arg1_ = [["thirdstatus" , "F"],["thirddealcode" , __BUILTIN__["RspDict"]["ThirdRetCode"]],["thirddealmsg" ,__BUILTIN__["RspDict"]["ThirdRetMsg"]],];
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
            return COMP_C00001_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(COMP_C00001_NODE12);

def COMP_C00001_NODE19(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    AFALoggerInfor("功能 正常结束");
    return True;

def COMP_C00001_ENTRY(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__ = {}):
    try:
        AFALoggerInfor("开始运行组件 个人信息查询");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = False;
        _Method_ = COMP_C00001_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__,__BUILTIN__);
            _Method_ = _Result_;

        return (_Method_ == True);
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;
