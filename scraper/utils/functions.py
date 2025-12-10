"""
function utils
"""

import os

import aiohttp


async def fetch_laws(url: str) -> str:
    header = {
        'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as request:
            response = await request.text(encoding='ISO-8859-1')

    return response


def save_json(data: str, path: str):
    with open(
        f'{os.path.dirname(os.path.abspath(path))}/data/law.html', 'w', encoding='ISO-8859-1'
    ) as file:
        _ = file.write(data)
