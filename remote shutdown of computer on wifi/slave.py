import time
import sys
import socket
import os

s = socket.socket()
host = "DESKTOP-8ORIJOR"
port = 8080
s.connect((host,port))
print("")
print(" Connected to server ")

command = s.recv(1024)
command = command.decode()
if command == "shutdown":
    print("")
    print("shutdown command")
    s.send("command recived".encode())
    os.system("shutdown.bat")
    
