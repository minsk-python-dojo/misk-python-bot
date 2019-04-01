import typing

import requests

from core.exceptions import (ConnectionError, APIConnectionError, IdentityError)


class Bot:

    __url: str = 'https://api.telegram.org/bot'
    
    def __init__(self, token: str) -> None:
        self.__token: typing.Union[str, None] = None
        self.token = token

    @property
    def token(self) -> typing.Union[str, None]:
        return self.__token

    @token.setter
    def token(self, value: str) -> None:
        response = self.get_me(value)
        if response.status_code != requests.codes.ok:
            raise ConnectionError
        response_json: dict = response.json()
        if not response_json.get('ok', False):
            raise APIConnectionError
        is_bot: bool = response_json.get('result', {}).get('is_bot', False)
        if not is_bot:
            raise IdentityError
        self.__token: typing.Union[str, None] = value
            
        

    def get_me(self, value: str) -> requests.Response:
        return requests.get(f'{self.__url}{value}/getMe')

    

