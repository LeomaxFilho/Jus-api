"""
function utils
"""

import os
from pickletools import string1

import aiohttp
from bs4 import BeautifulSoup


async def fetch_laws(url: str) -> str:
    """fetch data from url"""
    header = {
        'User-Agent': '"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"'
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=header) as request:
            response = await request.text(encoding='ISO-8859-1')

    return response


def save_json(data: str, path: str) -> None:
    """save file to json"""

    with open(
        f'{os.path.dirname(os.path.abspath(path))}/data/law.txt', 'w', encoding='utf-8'
    ) as file:
        _ = file.write(data)


async def soup_laws(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')

    content = soup.find_all('p')
    real_content = '\n\n'.join([c.getText(strip=True) for c in content])

    return real_content
