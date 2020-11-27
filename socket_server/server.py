import socket
import logger
import logging
import asyncio
from socket_server.errors import *
import aiohttp
import aiofiles

lg = logging.getLogger("Server")
lg.info(f"Starting socket server")


class Server:

    def __init__(self, ip, port):

        self.ip = ip
        self.port = port
        if not asyncio.run(self.port_check()) == True:

            raise InvalidPortError
        asyncio.run(self.run())

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

            await f.write(data)
            await f.close()

        pass

    async def reply(self, reply: bytes):

        #Override this method here to change the reply
        pass

    async def create_socket(self):

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        lg.info(f"Created socket server on {self.ip}:{self.port}")
        await self.bind()

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
            global client
            client, addr = self.s.accept()

            lg.info(f"Accepted connection from {addr[0]}:{addr[1]}")

            while True:

                try:

                    data = client.recv(1024)
                    lg.info(f"Received data from {addr[0]}:{addr[1]} - {data.decode()}")

                    try:
                        if not await self.check_data(data):

                            break

                        lg.info(f"Message received from {addr[0]}:{addr[1]} is {len(data.decode())} characters long")
                        #await self.handle_data(data)

                        #await self.reply("Closed server".encode())

                        #client.close()
                        #lg.info(f"Closed connection with {addr[0]}:{addr[1]}")
                        self.s.close()

                    except Exception as e:

                        lg.error(e)
                        asyncio.sleep(1)

                except Exception as e:

                    lg.error(e)
                    asyncio.sleep(1)

    async def run(self):

        await self.port_check()
        await self.create_socket()
        await self.start()






