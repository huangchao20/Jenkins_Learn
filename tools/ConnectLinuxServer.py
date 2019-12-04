import paramiko


HOST = "172.20.10.5"
USER = "root"
PWD = "pwd123"
PORT = 22

def connect_linux(HOST, PORT, USER, PWD):
    Client = paramiko.SSHClient()
    try:
        Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        Client.connect(HOST, PORT, USER, PWD)
    except Exception as e:
        print(e)
    return Client


def connectServer(Host, UserName, passwd, port):
    Client = paramiko.SSHClient()
    try:
        Client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        Client.connect(hostname=Host, username=UserName, password=passwd, port=port)
    #except Exception as e:
    except Exception as e:
        print(e)
    return Client

if __name__ == "__main__":
    Host = "172.20.10.5"
    UserName = "github"
    passwd = "cs123456"
    port = 22
    #print(connectServer(Host, UserName, passwd, port))
    cmd_linux = connectServer(Host, UserName, passwd, port)
    stdin, stdout, stderr = cmd_linux.exec_command("python3 /home/github/priv/TestPy/CountDirAndFiles.py")
    print(stdout.read().decode())