from socket_server.server import Server
from socket_server.client import Client
from asyncio import run
import logging

logging.getLogger("asyncio").disabled = True
Client("127.0.0.1", 5001)
Server("127.0.0.1", 5000)


