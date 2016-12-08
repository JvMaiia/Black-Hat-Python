import socket
bind_ip = input("Ip of your server? ")
bind_port = int(input("Port of your server? "))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(1)
print("[*] Listening on {}:{}".format(bind_ip, bind_port))
#Thread for client handling
def handle_client(client_socket):
	#send one package back
	msg = "YEAH"
	client_socket.send(msg.encode('ascii'))
	client_socket.close()
while True:
	client, addr = server.accept()
	print("[*] Accepted connection from: {}:{}".format(addr[0], addr[1]))
	handle_client(client)