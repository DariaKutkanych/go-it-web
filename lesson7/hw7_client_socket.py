import socket
import threading


stop_indicator = True


def send_message(sock):

    global stop_indicator

    while stop_indicator:
        command = input("")
        sock.send(command.encode())
        if command == "stop":
            stop_indicator = False


def receive_message(sock):

    global stop_indicator
    
    while stop_indicator:
        
            request = sock.recv(4000)
            print(request.decode())
            if request.decode().lower() == "stop":
                sock.send(request)
                stop_indicator = False


if __name__ == "__main__":

    with socket.socket() as sock:
        sock.connect(("localhost", 5001))

        send_msg = threading.Thread(target=send_message, args=(sock, ), daemon=True)
        recv_msg = threading.Thread(target=receive_message, args=(sock, ), daemon=True)

        recv_msg.start()
        send_msg.start()

        recv_msg.join()
        send_msg.join()
        