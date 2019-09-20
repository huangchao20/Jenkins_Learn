import paramiko

def LoadServer(hostID, port, username, passwd):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(hostname=hostID, port=port, username=username, password=passwd)
	#stdin, stdout, stderr = ssh.exec_command('whoami')				#命令行
	#res, err = stdout.read(), stderr.read()
	#result = res if res else err

def sshClose(ssh):
	ssh.close()