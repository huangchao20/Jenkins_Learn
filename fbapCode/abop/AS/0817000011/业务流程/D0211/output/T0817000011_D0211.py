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
from B_ABOP_Socket import fileTrans as B_ABOP_Socket_fileTrans;
from B_ABOP_DB import B_db_sequence as B_ABOP_DB_B_db_sequence;
from B_ABOP_File import B_CheckFileExistAndIsFile as B_ABOP_File_B_CheckFileExistAndIsFile;
from B_ABOP_DB import B_DBDMLUpd as B_ABOP_DB_B_DBDMLUpd;
from B_ABOP_File import B_RenameFIle as B_ABOP_File_B_RenameFIle;
from B_ABOP_DB import B_SearchLinesIntoDelFileBySql as B_ABOP_DB_B_SearchLinesIntoDelFileBySql;
from B_ABOP_File import B_CreateSeparateStr as B_ABOP_File_B_CreateSeparateStr;
from B_ABOP_Commom_Auto import B_GetSysPath as B_ABOP_Commom_Auto_B_GetSysPath;
from B_ABOP_File import B_CloseTheFile as B_ABOP_File_B_CloseTheFile;
from B_ABOP_File import B_WriteOneLine as B_ABOP_File_B_WriteOneLine;
from B_ABOP_File import B_GetOneLineFromDelFile as B_ABOP_File_B_GetOneLineFromDelFile;
from B_ABOP_File import B_OpenTheFile as B_ABOP_File_B_OpenTheFile;
from B_ABOP_File import B_CreatePath as B_ABOP_File_B_CreatePath;
from B_ABOP_Time import B_date_fmt as B_ABOP_Time_B_date_fmt;
from B_SCNX_CFG import B_GetUOCPCfg as B_SCNX_CFG_B_GetUOCPCfg;
from B_ABOP_CustBatchEnqing import B_SysBatchWhereStrAssembly as B_ABOP_CustBatchEnqing_B_SysBatchWhereStrAssembly;
from B_ABOP_DB import B_DBDMLSelForPlaceholder as B_ABOP_DB_B_DBDMLSelForPlaceholder;
from B_ABOP_Dictionary import B_dict_setvalue as B_ABOP_Dictionary_B_dict_setvalue;
from B_ABOP_BatchCheck import B_CheckTheChoiceableField as B_ABOP_BatchCheck_B_CheckTheChoiceableField;
from B_ABOP_BatchCheck import B_IndispensableFieldCheck as B_ABOP_BatchCheck_B_IndispensableFieldCheck;
from B_ABOP_Time import B_time_get as B_ABOP_Time_B_time_get;



'''
--------------------------- 项目分期 ---------------------------
名    称：0817000011
描    述：南部一卡通批量代扣
----------------------------------------------------------------
'''


def TD0211_STEP1_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP1_NODE2;

def TD0211_STEP1_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP1_NODE7);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP1_NODE7 节点");

    return TD0211_STEP1_NODE3;

def TD0211_STEP1_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0211_STEP1_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP1_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP1_NODE7);

def TD0211_STEP1_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 必输字段合法性检查");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [ ["REQBODY","AppType","STRING",20], ["REQBODY","AppID","STRING",20], ["REQBODY","AgreementID","STRING",20], ["REQBODY","CustBatchID","CHAR",16], ["REQBODY","IsUrgent","CHAR",1], ["REQBODY","IsRealTimeDeal","CHAR",1], ["REQBODY","BankBranchID","STRING",10], ["REQBODY","ChannelID","STRING",10], ["REQBODY","ExcuteStatus","CHAR",2], ["REQBODY","Status","CHAR",1], ["REQBODY","IsBatchClear","CHAR",1], ["REQBODY","RuleModeID","STRING",10], ["REQBODY","BatchFilePath","STRING",128], ["REQBODY","BatchFileName","STRING",128], ["REQBODY","TotalRecord","STRING",10], ["REQBODY","TotalAmount","STRING",17], ["REQBODY","ScuRecord","STRING",10], ["REQBODY","ScuAmount","STRING",17], ["REQBODY","NearstDate","CHAR",8], ["REQBODY","NearstTime","CHAR",6] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_BatchCheck_B_IndispensableFieldCheck(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP1_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP1_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP1_NODE7);

def TD0211_STEP1_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0211_STEP1_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP1_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP1_NODE7);

def TD0211_STEP1_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP1_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP1_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0211_STEP1_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP1_NODE7);

    # except Exception,PyExcp:
    #     ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
    #     AFALoggerError(str(format_exc()));
    #     AFALoggerError(str(PyExcp));
    #     return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP1_NODE7);

def TD0211_STEP1_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 1 功能 客户批数据校验");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP1_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0211_STEP2_IMPL;
        else:
            return None;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0211_STEP2_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP2_NODE2;

def TD0211_STEP2_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP2_NODE5);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP2_NODE5 节点");

    return TD0211_STEP2_NODE3;

def TD0211_STEP2_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 查询回盘标识");

        _Arg0_ = "select  IsCrtRspFile,createdate  from ABOP_CustBatchInfo where CustBatchID= ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["CustBatchID"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["IsCrtRspFileInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["IsCrtRspFileInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP2_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP2_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP2_NODE5);

def TD0211_STEP2_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断是否生成回盘文件");

        _Arg0_ = __REQ__["IsCrtRspFileInfo"][0][0]=="1";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP2_NODE7;
        elif(_Result_[0] == 1): 
            return TD0211_STEP2_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP2_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP2_NODE5);

def TD0211_STEP2_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP2_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP2_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 2 功能 判断是否生成文件");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP2_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0211_STEP3_IMPL;
        else:
            return TD0211_STEP6_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0211_STEP3_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP3_NODE2;

def TD0211_STEP3_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP3_NODE9);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP3_NODE9 节点");

    return TD0211_STEP3_NODE3;

def TD0211_STEP3_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取批量业务名称");

        _Arg0_ = "select AppID,AppName from ABOP_AppInfo where AppType = ? and AppID = ?";
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
            __REQ__["AppNameInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["AppNameInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP3_NODE4;
        elif(_Result_[0] == 2): 
            return TD0211_STEP3_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取所有的系统批次号");

        _Arg0_ = "select SysBatchID from ABOP_SysBatchInfo where CustBatchID= ? ";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["CustBatchID"] ];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["SysBatchIDList"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["SysBatchIDList"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP3_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 设置全局错误");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "系统批[%s]所属批量业务的批量业务记录不存在"%(__REQ__["__BODY__"]["SysBatchID"]);
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP3_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 系统批where条件拼装");

        _Arg0_ = __REQ__["SysBatchIDList"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_CustBatchEnqing_B_SysBatchWhereStrAssembly(_Arg0_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["SysBatchIDList"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["SysBatchIDList"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP3_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0211_STEP3_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取得系统批回盘文件路径");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");
        _Arg1_ = "CustBatchRspPath";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["MsgSystemDict"]["RspThirdPath"]+"0817000011/";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP3_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP3_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 创建路径");

        _Arg0_ = __RSP__["CustBatchRspPath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = B_ABOP_File_B_CreatePath(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP3_NODE12;
        elif(_Result_[0] == 1): 
            return TD0211_STEP3_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 日期格式化");

        _Arg0_ = __REQ__["CurrentDate"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "yyyy-mm-dd";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Time_B_date_fmt(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["reqdate"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["reqdate"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP3_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP3_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 文件名称赋值");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");
        _Arg1_ = [["CustBatchRspFile","0817000011"+__REQ__["CurrentDate"]+"_"+__REQ__["CurrentTime"]+".txt.fbaptmp"],["ReadyCustBatchRspFile","NB_SCH_OP_HP_"+__REQ__["__BODY__"]["AgreementID"]+"_"+__REQ__["reqdate"]+".txt"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP3_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP3_NODE9);

def TD0211_STEP3_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 3 功能 生成文件数据准备");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP3_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0211_STEP4_IMPL;
        else:
            return TD0211_STEP10_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0211_STEP4_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP4_NODE2;

def TD0211_STEP4_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP4_NODE13);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP4_NODE13 节点");

    return TD0211_STEP4_NODE4;

def TD0211_STEP4_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 初始信息赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [["SuccessRecord",0],["SuccessAmount",0.0],["TotalRecord",0],["TotalAmount",0.0]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 打开回盘文件");

        _Arg0_ = __RSP__["CustBatchRspPath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __RSP__["CustBatchRspFile"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "w";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_OpenTheFile(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["RSPFileDesc"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["RSPFileDesc"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取数据库Load操作路径");

        _Arg0_ = "DBLoaderTmpPath";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["__BODY__"]["AppType"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["__BODY__"]["AppID"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = __REQ__["__BODY__"]["BankBranchID"];
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);

        _Result_ = B_ABOP_Commom_Auto_B_GetSysPath(_Arg0_,_Arg1_,_Arg2_,_Arg3_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["DBTmpPath"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["DBTmpPath"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 组装一个分隔符字符串");

        _Arg0_ = [__REQ__["__BODY__"]["AgreementID"],__REQ__["OneInfo"][5],__REQ__["OneInfo"][2],__REQ__["OneInfo"][4],__REQ__["OneInfo"][9],__REQ__["CurrentTime"],];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "|";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CreateSeparateStr(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["StrData"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["StrData"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE15;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 预留回盘文件头空间");

        _Result_ = [1, None, None, []];

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 关闭打开的文件");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "RSPFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE22;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 数据库Loader临时文件名");

        _Arg0_ = [ "CustBatchRsp", __REQ__["__BODY__"]["CustBatchID"],"DBLoad.txt" ];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "_";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CreateSeparateStr(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["DBTmpFile"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["DBTmpFile"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE14;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 从数据库文件读取一条记录");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "DBTmpDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_GetOneLineFromDelFile(_Arg0_,_Arg1_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["OneInfo"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["OneInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE16;
        elif(_Result_[0] == 2): 
            return TD0211_STEP4_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 关闭打开的文件");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "DBTmpDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP4_NODE17;
        elif(_Result_[0] == 1): 
            return TD0211_STEP4_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE14(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 导出批量明细记录");

        _Arg0_ = "select  PRIVATEACCOUNT,  PRIVATEACCOUNTNAME,  ARREARAGEMONEY,  RECORDSTATUS, CHANNELSERIALNO, USERID, CHANNELSERIALNO, ARREARAGESERIALNO, ARREARAGEMONEY, NEAROPERATEDATE from  BPDM_OP_LZGasPayment where "+__REQ__["SysBatchIDList"]+" and RecordStatus = 'S' order by LineNo ASC";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["DBTmpPath"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["DBTmpFile"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_SearchLinesIntoDelFileBySql(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE18;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE15(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 往文件中写入一行数据");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "RSPFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["StrData"]+"\r\n";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_WriteOneLine(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE16(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断成功标识");

        _Arg0_ = __REQ__["OneInfo"][3] == "S";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP4_NODE20;
        elif(_Result_[0] == 1): 
            return TD0211_STEP4_NODE21;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 关闭打开的文件");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "RSPFileDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP4_NODE23;
        elif(_Result_[0] == 1): 
            return TD0211_STEP4_NODE23;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE18(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 打开指定文件");

        _Arg0_ = __REQ__["DBTmpPath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["DBTmpFile"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "r";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_OpenTheFile(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["DBTmpDesc"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["DBTmpDesc"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 关闭打开的文件");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "DBTmpDesc";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CloseTheFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE20(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 失败汇总");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [["TotalRecord",int(__REQ__["TotalRecord"])+1],["TotalAmount",float(__REQ__["TotalAmount"])+float(__REQ__["OneInfo"][2])],["ErrInfo","失败"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE21(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 成功汇总");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = [["SuccessRecord",int(__REQ__["SuccessRecord"])+1],["SuccessAmount",float(__REQ__["SuccessAmount"])+float(__REQ__["OneInfo"][2])],["TotalRecord",int(__REQ__["TotalRecord"])+1],["TotalAmount",float(__REQ__["TotalAmount"])+float(__REQ__["OneInfo"][2])],["ErrInfo","成功"]];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_Dictionary_B_dict_setvalue(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP4_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP4_NODE23);

def TD0211_STEP4_NODE22(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP4_NODE23(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP4_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 4 功能 系统导表回盘");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP4_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0211_STEP5_IMPL;
        else:
            return TD0211_STEP10_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0211_STEP5_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP5_NODE7;

def TD0211_STEP5_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP5_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新批次状态信息与成功统计金额信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [["IsCrtRspFile","1"],["BatchRspPath",__RSP__["CustBatchRspPath"]],["BatchRspName",__RSP__["ReadyCustBatchRspFile"]],["SucRecords",str(__REQ__["SuccessRecord"])],["SucAmount",str(__REQ__["SuccessAmount"])],["ErroCode","0000"],["ErroMsg","回盘文件生成成功"]];
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
            return TD0211_STEP5_NODE5;
        elif(_Result_[0] == 2): 
            return TD0211_STEP5_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP5_NODE2);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP5_NODE2);

def TD0211_STEP5_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 设置全局错误");

        _Arg0_ = "E";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = "FFFF";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = "更新批次状态时出现意外的错误!影响的批次记录数为0";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetErrorToGlobal(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP5_NODE2;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP5_NODE2);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP5_NODE2);

def TD0211_STEP5_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP5_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 修改指定文件名称");

        _Arg0_ = __RSP__["CustBatchRspPath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __RSP__["CustBatchRspFile"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __RSP__["ReadyCustBatchRspFile"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_File_B_RenameFIle(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP5_NODE3;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP5_NODE2);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP5_NODE2);

def TD0211_STEP5_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP5_NODE2);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP5_NODE2 节点");

    return TD0211_STEP5_NODE6;

def TD0211_STEP5_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 5 功能 更新批次状态");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP5_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0211_STEP6_IMPL;
        else:
            return TD0211_STEP10_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0211_STEP6_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP6_NODE2;

def TD0211_STEP6_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP6_NODE7);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP6_NODE7 节点");

    return TD0211_STEP6_NODE3;

def TD0211_STEP6_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取回盘文件名称");

        _Arg0_ = "select  BatchRspName from ABOP_CustBatchInfo where CustBatchID= ? and IsCrtRspFile=?";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [ __REQ__["__BODY__"]["CustBatchID"] ,"1"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = 0;
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = B_ABOP_DB_B_DBDMLSelForPlaceholder(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["TMP"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["TMP"]);
            __REQ__["BatchRspNameInfo"] = _RTVAL_[1];
            ACMP_Builtin_LoggerVar(4,"O1",__REQ__["BatchRspNameInfo"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP6_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

def TD0211_STEP6_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取外联交互配置");


        _Result_ = B_SCNX_CFG_B_GetUOCPCfg();

        if((_Result_[1] == None) and (_Result_[2] == None)):
            _RTVAL_ = _Result_[3];

            __REQ__["MsgSystemDict"] = _RTVAL_[0];
            ACMP_Builtin_LoggerVar(4,"O0",__REQ__["MsgSystemDict"]);
        else:
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP6_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

def TD0211_STEP6_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 客户批上送文件路径");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "CustRsltFilePath";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["MsgSystemDict"]["RspThirdPath"]+"0817000011/";
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP6_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

def TD0211_STEP6_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 客户批上送文件名称");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "CustRsltFileName";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["BatchRspNameInfo"][0][0];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP6_NODE9;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

def TD0211_STEP6_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP6_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP6_NODE9(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断文件是否存在");

        _Arg0_ = __REQ__["CustRsltFilePath"];
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["CustRsltFileName"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);

        _Result_ = B_ABOP_File_B_CheckFileExistAndIsFile(_Arg0_,_Arg1_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP6_NODE10;
        elif(_Result_[0] == 1): 
            return TD0211_STEP6_NODE10;
        elif(_Result_[0] == 2): 
            return TD0211_STEP6_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

def TD0211_STEP6_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 不执行通知外联");

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
            return TD0211_STEP6_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

def TD0211_STEP6_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 执行通知外联");

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
            return TD0211_STEP6_NODE12;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

def TD0211_STEP6_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新批次信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [["BatchRspPath",__REQ__["CustRsltFilePath"]]];
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
            return TD0211_STEP6_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP6_NODE7);

def TD0211_STEP6_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 6 功能 通知准备");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP6_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0211_STEP7_IMPL;
        else:
            return TD0211_STEP10_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0211_STEP7_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP7_NODE2;

def TD0211_STEP7_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP7_NODE7);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP7_NODE7 节点");

    return TD0211_STEP7_NODE3;

def TD0211_STEP7_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 通知外联文件已上传(0N/1Y)");

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
            return TD0211_STEP7_NODE4;
        elif(_Result_[0] == 2): 
            return TD0211_STEP7_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

def TD0211_STEP7_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 无文件");

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
            return TD0211_STEP7_NODE11;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

def TD0211_STEP7_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 AFE负载均衡文件传输客户端");

        _Arg0_ = "fbap_afa_afe_comm.conf";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = __REQ__["__MC__"];
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = __REQ__["__TC__"];
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);
        _Arg3_ = "CustBatchThirdRsp/0817000011/";
        ACMP_Builtin_LoggerVar(4,"A3",_Arg3_);
        _Arg4_ = "0817000011/send/";
        ACMP_Builtin_LoggerVar(4,"A4",_Arg4_);
        _Arg5_ = __REQ__["CustRsltFileName"];
        ACMP_Builtin_LoggerVar(4,"A5",_Arg5_);
        _Arg6_ = "PUT";
        ACMP_Builtin_LoggerVar(4,"A6",_Arg6_);

        _Result_ = B_ABOP_Socket_fileTrans(_Arg0_,_Arg1_,_Arg2_,_Arg3_,_Arg4_,_Arg5_,_Arg6_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP7_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

def TD0211_STEP7_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 获取平台流水信息");

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
            return TD0211_STEP7_NODE10;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

def TD0211_STEP7_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP7_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0211_STEP7_NODE23;
        elif(_Result_[0] == 1): 
            return TD0211_STEP7_NODE22;
        elif(_Result_[0] == 2): 
            return TD0211_STEP7_NODE23;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

def TD0211_STEP7_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 请求容器赋值");

        _Arg0_ = __REQ__;
        ACMP_Builtin_LoggerVar(4,"A0","__REQ__");
        _Arg1_ = "__SEND__";
        ACMP_Builtin_LoggerVar(4,"A1",_Arg1_);
        _Arg2_ = {"reqSendDate":__REQ__["CurrentDate"],"reqSendTime":__REQ__["CurrentTime"],"reqProdArea":"511300","reqProdCate":__REQ__["__BODY__"]["AppType"],"reqProdCode":__REQ__["__BODY__"]["AppID"],"reqProdSubCate":__REQ__["__BODY__"]["AppID"],"reqReceiverSID":"","reqTransID":"FBAP"+__REQ__["PlatformSeq"],"reqReserve":"","reqThdTrsCode":"B4","FilePath":__REQ__["CustRsltFilePath"],"FileName":__REQ__["CustRsltFileName"],"MC":__REQ__["__MC__"],"TC":__REQ__["__TC__"],"AFAServiceFunCode":"D00003","SchoolCode":__REQ__["__BODY__"]["AgreementID"],};
        ACMP_Builtin_LoggerVar(4,"A2",_Arg2_);

        _Result_ = ACMP_Builtin_SetValueToContext(_Arg0_,_Arg1_,_Arg2_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP7_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

def TD0211_STEP7_NODE11(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP7_NODE22(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 通讯正常");

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
            return TD0211_STEP7_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

def TD0211_STEP7_NODE23(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 通讯异常");

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
            return TD0211_STEP7_NODE24;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP7_NODE7);

def TD0211_STEP7_NODE24(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP7_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 7 功能 通知三方文件上传");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP7_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0211_STEP8_IMPL;
        else:
            return TD0211_STEP10_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0211_STEP8_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP8_NODE3;

def TD0211_STEP8_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 执行结果判断");

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
            return TD0211_STEP8_NODE5;
        elif(_Result_[0] == 2): 
            return TD0211_STEP8_NODE8;
        elif(_Result_[0] == 3): 
            return TD0211_STEP8_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

def TD0211_STEP8_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP8_NODE6);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP8_NODE6 节点");

    return TD0211_STEP8_NODE2;

def TD0211_STEP8_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断AFE处理结果");

        _Arg0_ = __REQ__["RspResult"]["afecode"]=="AFE_000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP8_NODE10;
        elif(_Result_[0] == 1): 
            return TD0211_STEP8_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

def TD0211_STEP8_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新批次状态信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [["ExcuteStatus","51"],["Status","1"],["NearstDate",__REQ__["CurrentDate"]], ["NearstTime",__REQ__["CurrentTime"]],["ErroCode",""],["ErroMsg","回盘文件上送未完成"]];
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
            return TD0211_STEP8_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

def TD0211_STEP8_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP8_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 判断三方处理结果");

        _Arg0_ = __REQ__["RspResult"]["ThirdRetCode"]=="000000";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP8_NODE12;
        elif(_Result_[0] == 1): 
            return TD0211_STEP8_NODE17;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

def TD0211_STEP8_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新批次状态信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [["ExcuteStatus","51"],["Status","1"],["NearstDate",__REQ__["CurrentDate"]], ["NearstTime",__REQ__["CurrentTime"]],["ErroCode","FFFF"],["ErroMsg","与AFE通信失败"]];
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
            return TD0211_STEP8_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

def TD0211_STEP8_NODE10(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新批次状态信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [["ExcuteStatus","51"],["Status","1"],["NearstDate",__REQ__["CurrentDate"]], ["NearstTime",__REQ__["CurrentTime"]],["ErroCode",__REQ__["RspResule"]["rspErrCode"][-6:]],["ErroMsg",__REQ__["RspResule"].get("rspErrMsg","AFE处理失败!")]];
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
            return TD0211_STEP8_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

def TD0211_STEP8_NODE12(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新批次状态信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [["ExcuteStatus","51"],["Status","1"],["NearstDate",__REQ__["CurrentDate"]], ["NearstTime",__REQ__["CurrentTime"]],["ErroCode","FFFF"],["ErroMsg","三方处理失败!"]];
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
            return TD0211_STEP8_NODE13;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

def TD0211_STEP8_NODE13(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP8_NODE17(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 更新批次状态信息");

        _Arg0_ = "ABOP_CustBatchInfo";
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);
        _Arg1_ = [["ExcuteStatus","61"],["Status","0"],["NearstDate",__REQ__["CurrentDate"]], ["NearstTime",__REQ__["CurrentTime"]],["ErroCode","0000"],["ErroMsg","交易执行成功"]];
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
            return TD0211_STEP8_NODE19;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP8_NODE6);

def TD0211_STEP8_NODE19(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP8_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 8 功能 通知应答结果处理");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP8_NODE1;
        while(type(_Method_) is FunctionType):
            AFALoggerInfor(("Node "+getattr(_Method_,"__name__")));
            _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
            _Method_ = _Result_;

        if(_Method_ is True):
            return TD0211_STEP9_IMPL;
        else:
            return TD0211_STEP10_IMPL;
    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return None;

def TD0211_STEP9_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP9_NODE2;

def TD0211_STEP9_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP9_NODE4);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP9_NODE4 节点");

    return TD0211_STEP9_NODE3;

def TD0211_STEP9_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 设置交易执行成功");

        _Arg0_ = __RSP__;
        ACMP_Builtin_LoggerVar(4,"A0","__RSP__");

        _Result_ = B_ABOP_Trade_B_TradeSuccess(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 1): 
            return TD0211_STEP9_NODE5;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP9_NODE4);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP9_NODE4);

def TD0211_STEP9_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP9_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP9_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 9 功能 批次执行成功");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP9_NODE1;
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

def TD0211_STEP10_NODE1(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 开始");
    return TD0211_STEP10_NODE2;

def TD0211_STEP10_NODE2(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 默认逻辑错误委托");
    ACMP_Builtin_SetDefaultExceptNode(TD0211_STEP10_NODE5);
    AFALoggerInfor("将默认异常委托到 TD0211_STEP10_NODE5 节点");

    return TD0211_STEP10_NODE3;

def TD0211_STEP10_NODE3(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 取全局错误到容器（内建）");

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
            return TD0211_STEP10_NODE7;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP10_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP10_NODE5);

def TD0211_STEP10_NODE4(__REQ__,__RSP__,__SND__,__RCV__):
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
            return TD0211_STEP10_NODE6;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP10_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP10_NODE5);

def TD0211_STEP10_NODE5(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 异常结束");
    return False;

def TD0211_STEP10_NODE6(__REQ__,__RSP__,__SND__,__RCV__):
    AFALoggerInfor("功能 正常结束");
    return True;

def TD0211_STEP10_NODE7(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 表达式布尔判断（内建）");

        _Arg0_ = len(__REQ__["ErrorMsg"])>127;
        ACMP_Builtin_LoggerVar(4,"A0",_Arg0_);

        _Result_ = ACMP_Builtin_BoolFrame(_Arg0_);

        if((_Result_[1] != None) and (_Result_[2] != None)):
            ACMP_Builtin_SetGlobalError("D",str(_Result_[1]),str(_Result_[2]));

        AFALoggerInfor("RET="+str(_Result_[0]));

        if(_Result_[0] == 0): 
            return TD0211_STEP10_NODE4;
        elif(_Result_[0] == 1): 
            return TD0211_STEP10_NODE8;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP10_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP10_NODE5);

def TD0211_STEP10_NODE8(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("功能 给容器赋值（内建）");

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
            return TD0211_STEP10_NODE4;
        else:
            ACMP_Builtin_SetGlobalError("E",_Result_[1],_Result_[2]);
            return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP10_NODE5);

    except Exception,PyExcp:
        ACMP_Builtin_SetGlobalError("E","ACMP0E001",str(PyExcp));
        AFALoggerError(str(format_exc()));
        AFALoggerError(str(PyExcp));
        return ACMP_Builtin_GetDefaultExceptNode(TD0211_STEP10_NODE5);

def TD0211_STEP10_IMPL(__REQ__,__RSP__,__SND__,__RCV__):
    try:
        AFALoggerInfor("步骤 10 功能 批次执行失败");

        ACMP_Builtin_SetDefaultExceptNode(None);

        _Result_ = None;
        _Method_ = TD0211_STEP10_NODE1;
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
def MD0211_ENTRY(__REQ__,__RSP__):
    AFALoggerInfor("开始交易 D0211:代扣整合回盘");

    __SND__ = {};
    __RCV__ = {};

    __REQ__["__TRADENAME__"] = "代扣整合回盘";

    ACMP_Builtin_TradeInitialize(__REQ__,__RSP__,"KAS_SSK");

    _Result_ = None;
    _Method_ = TD0211_STEP1_IMPL;
    while(type(_Method_) is FunctionType):
        AFALoggerInfor(("Step "+getattr(_Method_,"__name__")));
        _Result_ = _Method_(__REQ__,__RSP__,__SND__,__RCV__);
        _Method_ = _Result_;

    __SND__.clear();
    __RCV__.clear();
    del __SND__;
    del __RCV__;

    ACMP_Builtin_CheckResponse(__REQ__,__RSP__);
    AFALoggerInfor("结束交易 D0211");

    return True;
