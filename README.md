# wcrawler
A web crawler made in python to scrap all links from a seed link.A crawler is a program that fetches the web-page corresponding to an url, and parses all
the links on that page into a repository of links.It fetches the contents of any of the url from
the repository just created, parses the links from this new content into the repository and
continues this process for all links in the repository until stopped or after a given number
of links are fetched.

## Steps

* Go to the root folder
* Install the dependencies :
	
    ```pip3 install -r requirements.txt ```
* Run the command in the root folder to install the application :

	```pip3 install . ```
* The command to run the Crawler

	```python3 runcrawler.py https://example.com list.txt 10```


## Output
A file list.txt with all the links.

* **/wcrawler** - root folder
* **/wcrawler** - the folder with the crawler code . the __init__ file contains the
initialization and main logic,supported by crawler and parser files.
* **requirements.txt** - contains all the dependencies needed
* **runcrawler.py** - the file to run the crawler
* **setup.py** - the file to install the application
