class BotException(Exception):
    pass


class HTTPConnectionError(BotException):
    pass


class APIConnectionError(BotException):
    pass


class IdentityError(BotException):
    pass


class InvalidCommand(BotException):
    pass
