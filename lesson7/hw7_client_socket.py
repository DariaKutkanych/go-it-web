import socket
import threading


def send_message(sock):

    while True:
        command = input("")
        try:
            sock.send(command.encode())
        except OSError:
            print(f"Sorry, your contact disconnected")
            break
        if command in ["stop", "break"]:
            break


def receive_message(sock):
    
    while True:
            request = sock.recv(4000)
            print(request.decode())
            if request.decode().lower() == "stop":
                sock.send(request)
                break


if __name__ == "__main__":

    with socket.socket() as sock:
        sock.connect(("localhost", 5001))

        send_msg = threading.Thread(target=send_message, args=(sock, ), daemon=True)
        recv_msg = threading.Thread(target=receive_message, args=(sock, ), daemon=True)

        recv_msg.start()
        send_msg.start()

        recv_msg.join()
        send_msg.join()
        