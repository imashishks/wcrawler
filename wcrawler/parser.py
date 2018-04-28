from parsel import Selector


""" A function to scrape the content returned from the request and get all valid links """


def get_all_valid_links(res, root):
    temp_list = []
    content = u""+res.text
    sel = Selector(text=content)
    links = sel.css('a::attr(href)').extract()
    for l in links:
        # ignore css and js
        # to remove ids
        if l.startswith("#") or l.endswith(".pdf"):
            continue
        # check realtive and absoulte paths
        if l.startswith("http") or l.startswith("www"):
            temp_list.append(l)
        else:
            temp_list.append(root +
                             l) if l.startswith("/") else temp_list.append(root + "/"+l)

    return temp_list
