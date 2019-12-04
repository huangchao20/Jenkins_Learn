import paramiko

class Server():
    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.passwd = password
    
    def connectSvr(self):
        try:
            conn = paramiko.SSHClient()
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            conn.connect(hostname=self.host, port=self.port, username=self.username, passeord=self.passwd)
            cmd = input('操作指令:')
            stdin, stdout, stderr = conn.exec_command(cmd)
            print(stdout.read().decode('utf-8'))
            
            # sf = paramiko.SSHClient()
            # # 允许连接不在know_hosts文件中的主机
            # sf.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # # 连接服务器
            # conn.connect(hostname=self.host, port=self.port, username=self.username, password=self.passwd)
            # remote = input('操作指令:')
            # stdin, stdout, stderr = sf.exec_command(remote)
            # result = stdout.read().decode('utf-8')
            # print(result)
        except:
            return False
        return True

    
    def ssh_connectionServer(self):
        try:
            # 创建SSH对象
            sf = paramiko.SSHClient()
            # 允许连接不在know_hosts文件中的主机
            sf.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # 连接服务器
            sf.connect(hostname=self.host, port=self.port, username=self.username, password=self.passwd)
            remote = input('操作指令:')
            if remote == 'exit' or remote == 'quit':
                return False
            stdin, stdout, stderr = sf.exec_command(remote)
            result = stdout.read().decode('utf-8')
            print(result)
            err = stderr.read().decode('utf-8')
            print(err)
        except Exception as e:
            # logger.error("SSHConnection" +self.serverIP+"failed!")
            return e
        return True
    

if __name__ == '__main__':
    host = input("服务器地址:")
    port = input("端口:")
    username = input('户名:')
    passwd = input('密码:')
    server = Server(host, port, username, passwd)
    while True:
        
        # conn = Server.connectSvr()
        # print("链接服务器成功!!")
        # cmd = input('执行的操作:')
        # readmsg = Server.sendCMD(cmd, conn)
        # print(readmsg)
    
        ret =server.ssh_connectionServer()
        #server.connectSvr()
        if ret == False:
            break