
# get next target in page 
# return url and end_quote
def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link ==-1:             #if no link found,return None
        return None,0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)

#get all links in page to to links and return
def get_all_links(page):
    links = []                      #initial links as list
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)       #add url to links last
            page = page[endpos:]    #update page
        else:
            break                   #if no link found,break
    return links                    #return links


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            union(tocrawl, get_all_links(get_page(page)))
            crawled.append(page)
    return crawled