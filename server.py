import socket as s
import threading

ip = "0.0.0.0"
port = 8000

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((ip, port))
server_socket.listen()


def verbindung(conn):
    name = conn.recv(1024).decode()
    print(name + " hat sich verbunden!")

    text = conn.recv(1024).decode()
    while text != "stop":
        print(name + ": " + text)
        text = conn.recv(1024).decode()

    conn.close()


while True:
    print("Warten auf Verbindungen!")
    connection, address = server_socket.accept()
    new_thread = threading.Thread(target=verbindung, args=(connection,))
    new_thread.start()
