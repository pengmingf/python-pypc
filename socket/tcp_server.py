import socket
import threading
import logging

class ChatServer:
    def __init__(self,ip='127.0.0.1',port=9877):
        self.addr = (ip, port)
        self.sock = socket.socket()
        self.clients = {}
        # self.event = threading.Event()
    
    def start(self):
        self.sock.bind(self.addr)
        self.sock.listen()
        
        threading.Thread(target=self.accept, name="accept").start()

    def accept(self):
        while True:
            s,raddr = self.sock.accept()
            self.clients[raddr] = s
            logging.info(raddr)
            logging.info(s)
            threading.Thread(target=self.recv, name="recv", args=(s,raddr)).start()

    def recv(self, sock, raddr):
        while True:
            data = sock.recv(1024)
            if data == b'quit':
                self.clients.pop(sock.getpeername())
                sock.close()
                break
            # msg = raddr[0]+":"+(data.decode())
            # msg = data.decode().encode
            msg = "ack{} . {}".format(sock.getpeername(),data.decode()).encode()
            # print(msg)
            for s in self.clients.values():
                s.send(msg)

    def stop(self):
        for s in self.clients.values():
            s.close()
        self.sock.close()
        print("退出成功")

cs = ChatServer()
cs.start()

while True:
    cmd = input(">>>")
    if cmd.strip() == 'quit':
        cs.stop()
        threading.Event.wait(3)
        break
    print(threading.enumerate())
# server = socket.socket()
# server.bind(('0.0.0.0',9877))
# server.listen()

# s1,ip = server.accept()

# while True:
#     data = s1.recv(1024)
#     print(data)
#     s1.send('ack '.format(data.decode()).encode())

# s1.close()
# server.close()