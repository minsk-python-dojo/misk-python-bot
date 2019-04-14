from collections import namedtuple

CommandsList = namedtuple(
    'CommandsList',
    [
        'GET_ME',
        'GET_UPDATES',
    ]
)

ALL_COMMANDS = CommandsList(
    GET_ME='getMe',
    GET_UPDATES='getUpdates'
)