import os
import re
starts = ['TR', 'BUG', 'XQ']

class Check:
    def __init__(self, dpath):
        self.dpath = dpath
    
    def checkTask(self):
        if os.path.isdir(self.dpath):
            for task in os.listdir(self.dpath):
                if task.startswith('BUG') or task.startswith('TR') or task.startswith('XQ'):
                    NewDir = os.path.join(self.dpath, task.strip())
                    if os.path.isdir(NewDir):
                        ret = self.__checkShName(NewDir)
                        if ret == False:
                            return ret
                
    def __checkShName(self, dpath):
        taseName = dpath.split('\\').pop()
        flag = False
        print('开始检查【%s】' % dpath)
        dp = False
        db = False
        dbak = False
        pbck = False
        datadpl = re.compile(r'TS_\d{5}_X_\d{8}.sh$')
        datarbk = re.compile(r'TS_\d{5}_X_\d{8}_rollback.sh$')
        #"TS_82529_AFA_20190808_databak.sh"
        databak = re.compile(r'TS_\d{5}_AFA_\d{8}_databak.sh$')
        #TS_82529_AFA_20190808_pybak.sh
        pybak = re.compile(r'TS_\d{5}_AFA_\d{8}_pybak.sh$')
        for chf in os.listdir(dpath):
            if chf.endswith('.sh'):
                if re.match(datadpl, chf) != None:
                    filename = os.path.join(dpath, chf)
                    #检查部署脚本是否包涵delete
                    if os.path.isfile(filename):
                        ret = self.__checkDelete(dpath, filename)
                    if ret == -1:
                        print('【%s】任务部署脚本包涵delete' % taseName)
                        return ret
                    else:
                        dp = True
                elif re.match(datarbk, chf) != None:
                    db = True
                elif re.match(databak, chf) != None:
                    dbak = True
                elif re.match(pybak, chf) != None:
                    pbck = True
        if dp == False:
            print("【%s】任务缺少数据部署脚本" % taseName)
            return False
        if db == False:
            print("【%s】任务缺少数据回退脚本" % taseName)
            return False
        if dbak == False:
            print("【%s】任务缺少数据备份脚本" % taseName)
            return False
        if pbck == False:
            print("【%s】任务缺少代码备份脚本" % taseName)
            return False
        return True
    
    """
    检查脚本调用的sql文件是否存在delete语句
    """
    def __checkDelete(self, dpath, filename):
        keyWords = 'delete'
        cmp = re.compile(r'db2.*?./(.*?.sql)|')
        with open(filename, encoding='utf-8') as fs:
            for fr in fs.readlines():
                rf = re.match(cmp, fr)
                if rf != None:
                    sqlname = rf[1].split('/').pop()
                    sql = os.path.join(dpath, sqlname)
                    with open(sql, encoding='utf-8') as sq:
                        for sqr in sq.readlines():
                            if sqr.startswith(keyWords) or sqr.startswith(keyWords.upper()):
                                return -1
        return 0
    
    def checkRead(self, filename):
        with open(filename, encoding='utf-8') as fs:
            pass
        
        