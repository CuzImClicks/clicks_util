import logging
import socket
from socket_server.util import *
from socket_server.errors import *
import asyncio

lg = logging.getLogger("Client")


class Client:

    def __init__(self, ip, port):

        self.ip = ip
        self.port = port
        lg.info(f"Socket Client by Clicks - v1 Alpha")

        if not asyncio.run(self.port_check()):

            raise InvalidPortError

        asyncio.run(self.create_socket())
        asyncio.run(self.connect("127.0.0.1", 5000))

    async def create_socket(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lg.info(f"Created socket client on {self.ip}:{self.port}")

    async def port_check(self) -> bool:
        try:
            int(self.port)
            return True
            lg.info(f"Port: {self.port} is a valid port")

        except ValueError:

            return False
            lg.info(f"Port {self.port} is not a valid port")

    async def connect(self, target_ip, target_port):

        self.target_ip = target_ip
        self.target_port = target_port

        while True:

            try:
                self.s.connect((target_ip, int(target_port)))
                lg.info(f"Connected to {target_ip}:{target_port}")
                break
            except ConnectionRefusedError as e:

                lg.error(f"Connection with {target_ip}:{target_port} was refused")

    async def send(self, data):

        msg = "Test"
        lg.info(f"Message being sent is {msg}")
        msg_encoded = msg.encode()

        self.s.sendall(msg_encoded)
        lg.info(f"Send data to target {self.target_ip}:{self.target_port}")
        self.s.close()







