import socket
import threading
from cezar import cezar

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print(ip)
port = 1240
client.connect((ip, port))
print("Connected!")
def dataaccept1():
    while True:
        data = client.recv(2048).decode("utf-8")    
        print(data)
def sendserver():
    data = threading.Thread(target=dataaccept1)
    data.start()
    choice = input("Do you want to encrypt your massages? (y/n)")
    client.send(choice.encode("utf-8"))  
    while True:
        if choice == "y": 
            while True:        
                massage = cezar(input("msg for encryption:"))
                client.send(massage.encode("utf-8"))
        else:
            massage = input("Normal msg: ")
            client.send(massage.encode("utf-8"))       
sendserver()


    
    
 
    