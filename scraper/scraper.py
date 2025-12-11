"""
law scraper
"""

import asyncio

from utils.functions import fetch_laws, save_json, soup_laws


async def main():
    """main function"""
    url = 'https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm'
    response: str = await fetch_laws(url)
    laws: str = await soup_laws(response)

    save_json(laws, __file__)


if __name__ == '__main__':
    asyncio.run(main())
