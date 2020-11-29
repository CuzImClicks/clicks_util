import socket
import asyncio
import logging
import aiofiles
from clicks_util import logger
import selectors

sel = selectors.DefaultSelector()

lg = logging.getLogger("Server")
lg.info(f"Starting socket server")

lg_errors = logging.getLogger("errors")
logging.getLogger("asyncio").disabled = True


class InvalidPortError(Exception):

    pass


class PortAlreadyUsedError(Exception):

    pass


class Server:

    def __init__(self, ip, port):

        self.ip = ip
        self.port = port
        lg.info(f"Async Socket Server - v1 Beta")
        if not asyncio.run(self.port_check()):

            raise InvalidPortError
        asyncio.run(self.start())

    async def port_check(self) -> bool:
        try:
            int(self.port)
            return True
            lg.info(f"Port: {self.port} is a valid port")

        except ValueError:

            return False
            lg.info(f"Port {self.port} is not a valid port")

    async def check_data(self, data) -> bool:

        if len(data.decode()) == 0:

            return False

        else:

            return True

    async def handle_data(self, data):

        #Override this method here to change input handling
        async with aiofiles.open("data.txt", "w+") as f:

            write_data = addr[0] + " - " + str(addr[1]) + " - " + data.decode()
            await f.write(data.decode())
            await f.close()

    async def create_socket(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lg.info(f"Created socket server on {self.ip}:{self.port}")
        await self.bind()
        #self.s.setblocking(False)
        sel.register(self.s, selectors.EVENT_READ, data=None)

    async def bind(self):

        try:
            self.s.bind((self.ip, self.port))
            self.s.listen(1)
            lg.info(f"Binded to {self.ip}:{self.port}")

        except OSError as e:

            if str(e).startswith("[WinError 10048]"):

                raise PortAlreadyUsedError

    async def start(self):

        while True:
            global client, addr
            await asyncio.sleep(1)
            await self.create_socket()
            client, addr = self.s.accept()

            lg.info(f"Accepted connection from {addr[0]}:{addr[1]}")

            while True:

                try:

                    data = client.recv(1024)
                    if not await self.check_data(data):
                        break
                    lg.info(f"Received data from {addr[0]}:{addr[1]} - {data.decode()}")

                    try:
                        lg.info(f"Message received from {addr[0]}:{addr[1]} is {len(data.decode())} characters long")
                        await self.handle_data(data)
                        client.sendall(data)
                        lg.info(f"Sent data back to client containing {data.decode()}")

                        lg.info(f"Closed connection with {addr[0]}:{addr[1]}")
                        self.s.close()

                    except OSError as e:

                        lg.error(e)
                        await asyncio.sleep(1)

                except Exception as e:

                    lg.error(e)
                    await asyncio.sleep(1)


Server("127.0.0.1", 5000)


