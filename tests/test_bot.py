import pytest

import conf
from core import exceptions
from core.bot import Bot


API_VALID_TOKEN: str = conf.BOT_API_KEY
API_INVALID_TOKEN: str = 'abc'

def test_bot_init_valid():
    bot = Bot(API_VALID_TOKEN)

    assert bot.token == API_VALID_TOKEN

def test_bot_init_raises_with_invalid_token():
    with pytest.raises(exceptions.ConnectionError):
        Bot(API_INVALID_TOKEN)