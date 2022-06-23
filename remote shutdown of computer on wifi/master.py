import time
import sys
import socket
import os

s = socket.socket()
host = socket.gethostname()
print(host)
port = 8080
s.bind((host,port))
print("")
print("waiting for any incoming connections ...")
s.listen(1)
conn, addr = s.accept()
print("")
print(addr, " - Has connect to the server")
print("")

command = input(str("Command : "))
conn.send(command.encode())
print("Command has been sent success. Waiting for confirmation")
print("")
data = conn.recv(1024)
if data:
    print("shutdown command has been recived and excuted")
    print("")
    
