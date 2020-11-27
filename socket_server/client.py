import socket
from socket_server.errors import *
import logging

lg = logging.getLogger("Client")


class Client:

    def __init__(self, ip, port):

        self.ip = ip
        self.port = port





