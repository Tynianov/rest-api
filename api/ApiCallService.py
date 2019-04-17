from requests import get, exceptions
import json
from datetime import datetime,timedelta
from cachetools import cached, TTLCache

func_cache = TTLCache(maxsize=1, ttl=60)

@cached(func_cache)
def make_api_call():
    blocks = []

    today = datetime.today().replace(microsecond=0)
    day_ago = (today - timedelta(days=1))

    try:
        response = get(
            'https://api.blockchair.com/bitcoin/blocks?q=time({}..{})&limit=100'.format(day_ago, today))
        data = response.json()
        last_block = data['context']['state']

        for i in data['data']:
            blocks.append(i)

        response = get(
            'https://api.blockchair.com/bitcoin/blocks?q=time({}..{}),id(..{})&limit=100&offset=100'.format(day_ago,
                                                                                                            today,
                                                                                                            last_block))
        data = response.json()
        for i in data['data']:
            blocks.append(i)

        return blocks
    except ConnectionError as e:
        return e.args