import socket
target_host = input("Which your target host? ")
target_port = int(input("Which your target port? "))
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto("ABC".encode('ascii'), (target_host, target_port))
data, addr = client.recvfrom(4096)
print(data.decode('ascii'))