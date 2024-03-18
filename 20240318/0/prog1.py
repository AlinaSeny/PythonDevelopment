import sys
import socket
import shlex

host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
    ss.bind((host, port))
    ss.listen()
    conn, addr = ss.accept()
    while conn:
        print('Connested by', addr)
        while data := conn.recv(1024):
            print(data, type(data))
            s = shlex.split(data.decode(), False, False)
            if len(s) > 1 and  s[0] == 'print':
                conn.sendall(shlex.join(s[1:]))
            if len(s) > 1 and s[0] == 'info':
                address, port = transport.get_extra_info('peername')
                if s[1] == 'port':
                    conn.sendall(port.encode())
                else:
                    conn.sendall(address.encode())
