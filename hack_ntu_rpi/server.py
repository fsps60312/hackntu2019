#!/usr/bin/python
#coding=UTF-8
 
"""
TCP/IP Server sample
"""
 
import socket
import threading
import sys
 
bind_ip = "0.0.0.0"
bind_port = 60312
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
server.bind((bind_ip, bind_port))
            
server.listen(5)
 
#print "[*] Listening on %s:%d" % (bind_ip, bind_port)
 
def handle_client(client_socket):
    
    request = client_socket.recv(1024)
    #print "[*] Received: %s" % request
    print request
    sys.stdout.flush()
    
    client_socket.send("ACK!")
    client_socket.close()
    
while True:
    client, addr = server.accept()
    #print "[*] Acepted connection from: %s:%d" % (addr[0],addr[1])
    
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
