import wcrawler
import sys
arg_names = ['name', 'url', 'filename', 'counter']
args = dict(zip(arg_names, sys.argv))
if not "counter" in args:
    args["counter"] = None
if not "url" in args:
    args["url"] = "http://python.org"
if not "filename" in args:
    args["filename"] = "crawled.txt"

wcrawler.wcrawler(args["url"], args["filename"], args["counter"])
