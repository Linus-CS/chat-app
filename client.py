import socket as s

ip = "https://chat-app-yi62.onrender.com"
port = 8000

client_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
client_socket.connect((ip, port))

print("Verbunden!")
name = input("Gib bitte deinen Namen ein:")
client_socket.sendall(name.encode())


nachricht = input()
while nachricht != 'stop':
    client_socket.sendall(nachricht.encode())
    nachricht = input()

client_socket.sendall(b"stop")
client_socket.close()
