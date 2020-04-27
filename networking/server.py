import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
s.bind(("127.0.0.1", 5000))
s.listen(5)

conn, addr = s.accept()
print("Got connected", addr)

while True:
    data = "Manoj" + input(r"")
    conn.send(bytes(data, encoding='uyf-8'))
    print(conn.recv(1024))