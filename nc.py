import socket

SERVER_HOST = "0.0.0.0" #This is your localhost
SERVER_PORT = 5003
BUFFER_SIZE = 1024

def banner():
	print(f"              _   _        _\n")   
	print(f"             | \ | |      | |  \n")  
	print(f" _ __    ___ |  \| |  ___ | |_ \n")  
	print(f"| '_ \  / __|| . ` | / _ \| __|\n")  
	print(f"| | | || (__ | |\  ||  __/| |_ \n")  
	print(f"|_| |_| \___|\_| \_/ \___| \__|\n")  
                                          
banner()

creator = "				[---- creator: DevDeclann ----]	"
version = "					      ncNet: v1		"
print(creator)
print(version)

#create socket layer and bind shell
s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))

#listen for connection 
s.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} waiting for client connection")

#accept client connections
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} connection!")
message = "Hello, test".encode()
client_socket.send(message)

while True:
    command = input("Execute command:")
    client_socket.send(command.encode())
    if command.lower() == "exit":
        break
   
    reuslts = client_socket.recv(BUFFER_SIZE).decode()
    print(reuslts)

client_socket, client_address()

s.close()
