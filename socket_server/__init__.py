from socket_server.server import Server
import asyncio
import logging

logging.getLogger("asyncio").disabled = True

server = Server("127.0.0.1", 5000)

