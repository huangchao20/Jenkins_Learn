import os
import re

from Func.checkSqlBysh import CheckSql

def listdir(ckdir):
    """
    TS_ID_AFA_Date_databak.sh
    TS_ID_AFA_Date_pybak.sh
    TS_ID_X_DATE.sh
    TS_ID_X_DATE_rollback.sh
    :param ckdir:
    :return:
    """
    #后期优化：DATE为上线日期
    databack = re.compile(r'^TS_\d{4,6}_AFA_\d{8}_databak.sh$')
    pyback = re.compile(r'^TS_\d{4,6}_AFA_\d{8}$')
    datarollback = re.compile(r'^TS_\d{4,6}_X_\d{8}.sh$')
    datadeply = re.compile(r'^TS_\d{4,6}_X_rollback.sh$')
    dbk = 0     #数据备份脚本是否规范标志
    pyb = 0     #代码备份脚本是否规范标志
    dbr = 0     #回退脚本是否规范标志
    dp = 0      #部署脚本是否规范标志
    li = [dbk, pyb, dbr, dp]
    lid = ['数据备份脚本', '代码备份脚本', '回退脚本', '部署脚本']
    if os.path.isdir(ckdir):
        for d in os.listdir(ckdir):
            if d.startswith('TR') or d.startswith('BUG') or d.startswith('XQ'):
                newdir = os.path.join(ckdir, d)
                for ld in os.listdir(newdir):
                    if ld.endswith('.sh'):
                        if databack.match(ld) != None:
                            dbk += 1
                        elif pyback.match(ld) != None:
                            pyb += 1
                        elif datarollback.match(ld) != None:
                            dbr += 1
                        elif datadeply.match(ld) != None:
                            dp += 1
                            ret = CheckSql(os.path.join(newdir, ld))
                errflag = 0
                for i in range(len(li)):
                    if li[i] == 0:
                        print('任务【%s】【%s】脚本不存在!!!!!!!!!!!!!!!!!!!!' % (d, lid[i]))
                        errflag += 1
                if errflag != 0:
                    return False
                    
                
    else:
        print('请输入正确的打包路径')
        return False