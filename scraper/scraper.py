"""
law scraper
"""

import asyncio

from utils.functions import fetch_laws, save_json


async def main():
    """main function"""
    url = 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'
    response = await fetch_laws(url)
    save_json(response, __file__)


...


if __name__ == '__main__':
    asyncio.run(main())
