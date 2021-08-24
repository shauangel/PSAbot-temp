import time, socket, sys
 
<<<<<<< HEAD
new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
#s_ip = '127.0.0.1'
=======
new_socket = socket.socket(socket.AF_INET, socket.SOCKET_STREAM)
host_name = socket.gethostname()
#s_ip = socket.gethostbyname(host_name)
s_ip = '8.8.8.8'
>>>>>>> bba6a35d21e83769ea8f811a2e9e987cabb55e1c
port = 55003

new_socket.bind((host_name, port))
print("Binding successful!")
print("This is your hostname: ", host_name)
print("This is your IP: ", s_ip)

name = input("Enter name: ")
new_socket.listen(1)

conn, add = new_socket.accept()
print("Received connection from", add[0])
print("Connection Established. Connected From", add[0])

client = (conn.recv(1024)).decode()
print(client + "has connected.")
conn.send(name.encode())

while True:
    message = input("Me: ")
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(client, ":", message)
