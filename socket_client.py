import socket
import sys
import time

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket_server.connect(("8.8.8.8", 80)) #80
#ip = socket_server.getsockname()[0]
ip = '127.0.0.1'
sport = 55003

print("This is your IP: ", ip)
server_host = input("Enter friend\'s IP address:")
name = input("Enter Friend\'s name:")

socket_server.connect((server_host, sport))

socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()

print(server_name, " has joined...")
while True:
    message = (socket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    socket_server.send(message.encode())
