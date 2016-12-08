import socket
bind_ip = input("Ip of your server? ")
bind_port = int(input("Port of your server? "))
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((bind_ip, bind_port))
print("[*] Listening on {}:{}".format(bind_ip, bind_port))
while True:
	data, addr = server.recvfrom(1024)
	print("[*] Accepted connection from: {}:{}".format(addr[0], addr[1]))
	print("Received message: {}".format(data))