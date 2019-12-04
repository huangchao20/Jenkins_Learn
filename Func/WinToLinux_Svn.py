import paramiko

def connectServer(host, port, username, password):
    print('----------------Step 01------------------')
    try:
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(hostname=host, port=port, username=username, password=password)
        # stdin, stdout, stderr = conn.exec_command(cmd)
        # print(stdout.read().decode('utf-8'))
    except Exception as e:
        print('链接错误:', e)
        return False
    return conn

def main(filename, conn):
    with open(filename, encoding='utf-8') as fs:
        i = 1
        for cmd in fs.readlines():
            print(cmd)
            stdin, stdout, stderr = conn.exec_command(cmd)
            print('--------------print [%d]-----------------' % i)
            i += 1
            print(stdout.read().decode('utf-8'))
            print(stderr.read().decode('utf-8'))
        
        # cmd = 'svn export svn://172.20.10.6/提版文件jar包/WEEK/fbap.20190711r.t15 /home/github/TestDirs/TestWinPython/20190829rw --username 17524 --password hc123456'
        # stdin, stdout, stderr = conn.exec_command(cmd)
        # print(stdout.read().decode('utf-8'))
        # print(stderr.read().decode('utf-8'))
    
if __name__ == '__main__':
    endFlag = 'exit'
    host = input('服务器IP:')
    port = input('端口:')
    username = input('username:')
    password = input('password:')
    accNoFile = 'G:\\黄大宝python\\测试目录\\accNo.txt'
    conn = connectServer(host, port, username, password)
    # while True:
    #     if conn != False:
    #         cmd = input('执行的指令:')
    #         stdin, stdout, stderr = conn.exec_command(cmd)
    #         # print(stdin.read().decode('utf-8'))
    #         if stdout != None:
    #             print(stdout.read().decode('utf-8'))
    #         print(stderr.read().decode('utf-8'))
    #         if endFlag == cmd or endFlag.upper() == cmd:
    #             break
    if conn != False:
        filename = 'G:\\黄大宝python\\测试目录\\cmds.txt'
        main(filename, conn)