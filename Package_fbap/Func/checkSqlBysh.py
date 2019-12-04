import os
import re

"""
部署脚本：TS_80441_X_20190711.sh
回退脚本：TS_80441_X_20190711_rollback.sh
代码备份：TS_80441_AFA_20190711_pybak.sh
数据备份：TS_80441_AFA_20190711_databak.sh
"""

class CheckSql():
    def __init__(self, dpath):
        self.dpath = dpath
    
    def checksql(self):
        with open(self.dpath) as fs:
            pass