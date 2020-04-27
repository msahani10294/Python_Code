import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.connect(("127.0.0.1", 5000))

while True:
    print(s.recv(1024))
    data = "Rohit" + input("")
    s.send(bytes(data, encoding='utf-8'))