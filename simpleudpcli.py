import socket
UDP_IP_ADDRESS="10.1.24.128"
UDP_PORT_NO=6789
message=("aravind")
bytesToSend=str.encode(message)
clientSock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
clientSock.sendto(bytesToSend ,(UDP_IP_ADDRESS,UDP_PORT_NO))
