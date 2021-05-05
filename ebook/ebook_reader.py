# -*- coding: utf-8 -*
from bs4 import BeautifulSoup
import requests
import re
import sys

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
rooturl = r'http://www.biquge.com.cn'

def get_html(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.content.decode('utf-8')
    else:
        print("Connect failed with code: " + str(r.status_code))

def show_chapter():
    url = ''
    with open('.\\cache.txt', 'r') as f:
        ebook_cache = f.readlines()[0].strip()
        url = rooturl + ebook_cache
    page_content = get_html(url)
    if page_content == None:
        print("Unknown url: "+ url)
        exit(0)
    soup = BeautifulSoup(page_content, 'html.parser')
    title = soup.find_all(name='div', attrs={'class': 'con_top'})[0].contents[-2].string
    chapter = soup.find_all(name='div', attrs={'class': 'bookname'})[0].h1.string
    print('\n\n\n' + title + ' ' + chapter + '\n')
    content = soup.find_all('div', attrs={'id': 'content'})[0].get_text()
    content = re.sub(r'\s+',  '\n\n    ', content)
    print(content + '\n\n')
    chapter_content = soup.find_all(name='div', attrs={'class': 'bottem1'})[0].contents
    for con in chapter_content:
        if '上一章' in con.string:
            next_chapter = con['href']
            with open('.\\cache_prev.txt', 'w') as f:
                f.write(next_chapter)
        if '下一章' in con.string:
            next_chapter = con['href']
            with open('.\\cache_next.txt', 'w') as f:
                f.write(next_chapter)
    return

def goto_next():
    next_cache = ''
    with open('.\\cache_next.txt', 'r') as f:
        next_cache = f.readlines()[0].strip()
    with open('.\\cache.txt', 'w') as f:
        f.write(next_cache)
    return

def goto_prev():
    next_cache = ''
    with open('.\\cache_prev.txt', 'r') as f:
        next_cache = f.readlines()[0].strip()
    with open('.\\cache.txt', 'w') as f:
        f.write(next_cache)
    return

if __name__ == "__main__":
    chapter = 0
    if len(sys.argv) == 1:
        show_chapter()
    else:
        print("Unknown Input")