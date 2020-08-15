import socket 

server = socket.socket()
print("Socket created.")
server.bind(('192.168.0.183' , 2154))

server.listen(6)
print("Listening...")

client = ""
addr = ""

while True :
    client , addr = server.accept()

    name = client.recv(1024).decode()

    print("Connected with " , name)
    

    client.send(bytes( "Congrats! you are connected with Maari." , 'utf-8'))

server.close()