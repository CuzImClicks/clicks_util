import logging

lg_errors = logging.getLogger("errors")


class InvalidPortError(Exception):

    pass


class PortAlreadyUsedError(Exception):

    pass
