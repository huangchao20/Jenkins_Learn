import paramiko

def connServer(host, port, username, password):
    try:
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(hostname=host, port=port, username=username, password=password)
        print('链接服务器【%s】成功!!!' % host)
        return conn
    except Exception as e:
        print(e)
        return False
    
def sendMassage(conn, cmd):
    print('要执行的命令[%s]' % cmd)
    stdin, stdout, stderr = conn.exec_command(cmd)
    print(stdout.read().decode('utf-8'))
    
if __name__ == '__main__':
    host = input('IP地址:')
    port = input('端口:')
    username = input('用户名:')
    password = input('密码:')
    conn = connServer(host, port, username, password)
    cmd = 'pwd'
    if conn != False:
        sendMassage(conn, cmd)