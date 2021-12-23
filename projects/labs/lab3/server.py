import socket
import threading
from cezar import decezar
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "192.168.88.59"
print(ip)
port = 1240
server.bind((ip, port))
server.listen()
users = []

def dataaccept(user):
    choice = user.recv(2048).decode("utf-8")
    print(f"User choose: {choice}")
    while True:
        data = user.recv(2048).decode("utf-8")
        if choice == "y":
            dmsg = decezar(data)
            print(f"Accepted {data}")
            print(f"{data} entcrypted to {dmsg}")
        else:
            print(f"Accepted {data}")
def server_start():
    print("Starting...")
    while True:
        user_socket, address = server.accept()
        users.append(user_socket)
        da = threading.Thread(target=dataaccept, args=(user_socket,))
        da.start()
if  __name__ == "__main__":
    server_start()
    
