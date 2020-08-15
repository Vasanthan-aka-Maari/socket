import socket

client = socket.socket()
print("Connecting...")
print()
server_ip = '192.168.0.183'
client.connect((server_ip , 2154))
print("Connected to " , server_ip)
print()
name = input("Enter your name: ")
client.send(bytes(name ,'utf=8'))

msg = client.recv(1024)

print(msg.decode('utf-8'))

client.close()