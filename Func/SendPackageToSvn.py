import sys
import os
import paramiko


"""
WEEK/2019/20191114, ENC/2019u/20191114/,2019常规/20191114
svn提交可以新增目录
svn command:svn import -m "new Package" /home/hc1604/TestDirs/DocDirs/REL_WEEK_20191030 svn://172.20.10.5/SVN_Dir/DocBranch/ --username huangchao --password huangchao
"""
class SendSvn():
    def __init__(self, cls, svnd, dirs, username, password):
        self.cls = cls
        self.svnd = svnd
        self.dirs = dirs
        self.username = username
        self.password = password
    
    def Send(self):
        print('---------Step Send--------')
        print('上传目录:[%s]' % self.cls)
        os.sys('svn import -m "new Package" %s %s --username %s --password %s' % (self.dirs, self.svnd, self.username, self.password))
        

svndir = 'svn://172.20.10.5/SVN_Dir/DocBranch'
def main():
    print('-------------------------------------------------------')
    print('WEEK/2019/20191114')
    print('ENC/2019u/20191114')
    print('2019常规/20191114')
    print('-------------------------------------------------------')
    cls = input('请输入：')
    while True:
        if cls.startswith('WEEK'):
            date = cls.split('/').pop()[4:]
            Newsvndir = svndir + '/待发布区' + '/常规版本' + '/一周一次' + '/' + date + '/特色业务产品'
            dirs = '/home/hc1604/TestDirs/DocDirs/REL_WEEK_{0}'.format(cls.strip().split('/').pop())
        elif cls.startswith('ENC'):
            date = cls.split('/').pop()[4:]
            Newsvndir = svndir + '/待发布区' + '/紧急版本' + '/特色业务产品' + '/' + date
            dirs = '/home/hc1604/TestDirs/DocDirs/ENC_{0}'.format(cls.strip().split('/').pop())
        elif cls.startswith('2019常规'):
            date = cls.split('/').pop()[4:]
            Newsvndir = svndir + '/待发布区' + '/常规版本' + '/' + date + '/特色业务产品'
            dirs = '/home/hc1604/TestDirs/DocDirs/REL_{0}'.format(cls.strip().split('/').pop())
        else:
            print('输入格式有误，请重新输入！！~~~')
            
if __name__ == '__main__':
    main()