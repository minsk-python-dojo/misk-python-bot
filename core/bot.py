import logging
import typing

import requests

from core.api_commands import ALL_COMMANDS
from core.exceptions import (
    HTTPConnectionError,
    APIConnectionError,
    IdentityError,
    InvalidCommand,
)


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class Bot:

    __url: str = 'https://api.telegram.org/bot'
    
    def __init__(self, token: str) -> None:
        self.__token: typing.Union[str, None] = token
        self.__check_token()

    @property
    def token(self) -> typing.Union[str, None]:
        return self.__token

    def __check_token(self) -> None:
        response = self.get_me()
        ret_status = response.status_code
        if ret_status != requests.codes.ok:
            logger.info(f'Got unexpected status code {ret_status}')
            raise HTTPConnectionError
        response_json: dict = response.json()
        if not response_json.get('ok', False):
            raise APIConnectionError
        is_bot: bool = response_json.get('result', {}).get('is_bot', False)
        if not is_bot:
            raise IdentityError

    def get_me(self) -> requests.Response:
        return self.invoke_command(ALL_COMMANDS.GET_ME)

    def get_update(self):
        return self.invoke_command(ALL_COMMANDS.GET_UPDATES)

    def invoke_command(self, command: str) -> requests.Response:
        if command not in ALL_COMMANDS:
            raise InvalidCommand(f'Try execute invalid command: {command}')

        command_endpoint = f'{self.__url}{self.__token}/{command}'
        logger.info(f'{command_endpoint}')
        return requests.get(command_endpoint)

    

