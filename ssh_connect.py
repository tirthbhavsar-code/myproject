import paramiko

print("Connecting to server...")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname="192.168.137.1",   # server IP
    username="ubuntu",         
    password="1234"            
)

stdin, stdout, stderr = ssh.exec_command("ls")

print("Output:\n")
print(stdout.read().decode())

ssh.close()
print("Connection closed")
