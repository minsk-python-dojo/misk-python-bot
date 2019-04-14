import pytest

import requests

import conf
from core import exceptions
from core.bot import Bot
from core.api_commands import ALL_COMMANDS


API_VALID_TOKEN: str = conf.BOT_API_KEY
API_INVALID_TOKEN: str = 'abc'


@pytest.fixture
def valid_bot() -> Bot:
    yield Bot(API_VALID_TOKEN)


def test_bot_init_valid():
    bot = Bot(API_VALID_TOKEN)

    assert bot.token == API_VALID_TOKEN


def test_bot_init_raises_with_invalid_token():
    with pytest.raises(exceptions.HTTPConnectionError):
        Bot(API_INVALID_TOKEN)


def test_bot_send_valid_command(valid_bot: Bot):
    response = valid_bot.invoke_command(ALL_COMMANDS.GET_ME)
    data = response.json()
    assert response.status_code == requests.codes.ok
    assert data['ok']
