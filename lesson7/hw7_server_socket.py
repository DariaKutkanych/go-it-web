"""The task was to make one answer OK. But I did really wanted them to communicate simultaniously 
and to have several users(not good implementation thaugh, needs lots of refactoring).
Please not that the keyword for breaking one connection is 'stop' on any side you like. 
Thanks in advance for comments and understanding.
"""


import threading
import socket


sock = None


def server_func():
    global sock
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("localhost", 5001))
    sock.listen(10)


def accept_conn(sock):
        client_socket, addr = sock.accept()
        print(f"Connected by {addr}")
        first_message(client_socket, addr)
        recv_msg = threading.Thread(target=receive_message, args=(client_socket, addr), daemon=True)
        send_msg = threading.Thread(target=send_message, args=(client_socket, addr), daemon=True)

        recv_msg.start()
        send_msg.start()

        recv_msg.join()
        send_msg.join()
        print(f"Connection {addr} closed")

       
def send_message(client_socket, addr):

    client_socket.send(f"Your IP: {addr}, OK".encode())
    while True:
        response = input('')
        if response.lower() == "stop":
            client_socket.send(response.encode())
            break
        try:
            client_socket.send(f"Server: {response}".encode())      
        except OSError:
            print(f"Sorry, your contact {addr} disconnected")
            break

def receive_message(client_socket, addr):
    
    while True:
        request = client_socket.recv(4096)
        if request.decode().lower() == "stop":
            client_socket.close()
            break
        if request:
            print(f"Msg from {addr}: {request.decode()}")


def first_message(client_socket, addr):
    request = client_socket.recv(4096)
    if request:
        print(f"Msg from {addr}: {request.decode()}")


def create_connections():
    while True:
        a = threading.Thread(target=accept_conn, args=(sock,), daemon=True)
        a.start()


if __name__=="__main__":

    server_func()
    create_connections()
