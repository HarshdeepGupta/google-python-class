# -*- coding: utf-8 -*-

import time
import urllib
import bs4
import requests


start_url = "https://en.wikipedia.org/wiki/Ankylosaurus"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
    response = requests.get(url)
    html = response.text
    soup = bs4.BeautifulSoup(html, "html.parser")

    first_link = ""
    content_div = soup.find(id="mw-content-text").find(class_ = "mw-parser-output")
    for element in content_div.find_all("p", recursive = "False"):
        if element.find("a", recursive = False):
            first_link = element.find("a", recursive = False).get('href')
            break

    if not first_link:
        return None

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', first_link)

    return first_link

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        print("We've found the target article!")
        return False
    elif len(search_history) > max_steps:
        print("The search has gone on too long, aborting search!")
        return False
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    else:
        return True

article_chain = [start_url]


# The main loop
while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    time.sleep(2)
