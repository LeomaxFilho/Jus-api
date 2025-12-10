"""
function utils
"""

import json

import aiohttp
from aiohttp.http import RESPONSES


async def fetch_laws(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as request:
            response = await request.text()

    return response


def save_json(data: str, path: str):
    with open(f'{path}/../data/law.json') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
