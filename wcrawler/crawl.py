import asyncio
import requests


""" A function to get the response of a given url"""


async def crawl(url):
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, requests.get, url)
    response = await asyncio.ensure_future(future)
    return response
