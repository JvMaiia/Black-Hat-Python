import socket
target_host = input("Which your target host? ")
target_port = int(input("Which your target port? "))
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
data = client.recv(1024)
print(data.decode('ascii'))