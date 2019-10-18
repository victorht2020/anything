import paramiko

hostname = '172.16.103.103'
port = 22

# trans = paramiko.Transport((hostname, port))
# trans.window_size = 2147483647

ssh = paramiko.SSHClient()
#Yes ou No do ssh
ssh.load_system_host_keys()
# add policy
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# server, username, password
ssh.connect(hostname, username='', password='')

#stdin,stdout,stderr =ssh.exec_command('touch apagar')
stdin,stdout,stderr = ssh.exec_command('cat apagar')

stdin.close()
print((stdout.read()).decode())
