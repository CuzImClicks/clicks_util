import logging

lg = logging.getLogger("errors")


class InvalidPortError(Exception):

    pass


class PortAlreadyUsedError(Exception):

    pass
