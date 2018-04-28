import asyncio
from parsel import Selector

from .parser import get_all_valid_links
from .crawl import crawl


read = set()


def wcrawler(url, filename, counter):
    """ A function to  clean the file and initiate  the event loop"""

    # To clear everything inside file
    f = open(filename, 'w')
    f.write('')
    f.close()

    # getting the event loop
    loop = asyncio.get_event_loop()
    # setting up the main function in the loop
    loop.run_until_complete(
        main(url, url, counter, filename))
    # loop.close()


async def main(root, url, counter, filename):
    """ Main function to start the async request process"""
    # to prevent similar url to be inserted in the set
    if url in read or url+"/" in read:
        return
    # to check if we have a counter or we have to go indefinetly
    if counter != None:
        if len(read) >= int(counter):
            return
    # a block to  make a request to the url
    # the exception block takes care of all exceptions like timeout,connection error etc.we just need to ignore such urls
    try:
        print("fetching " + url)
        res = await crawl(url)
        f = open(filename, 'a')
        f.write(repr(url))
        f.write(" ")
        read.add(url)
        # get all the links from the content by scraping the response
        parsedLinks = get_all_valid_links(res, root)
        # a recursive call for all the links from the current url.until the counter threshold is reached or indefinetly till there are no urls to scrape.
        for link in parsedLinks[0:len(parsedLinks) - len(read)]:
            await main(root, link, counter, filename)
    except Exception as e:
        print(e)
        return
