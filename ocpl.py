
# %%

from collections import defaultdict
from operator import itemgetter
import urllib.parse

import sys
import time

if len(sys.argv) < 2:
    print('Usage:', sys.argv[0], 'search_words')
    sys.exit()

sys.path.append('../')
from crawlkit import util

# %%
print('Initing browser...')
browser = util.MyChrome(True, '/Users/yu/Chrome')  # False)


# %%
term = sys.argv[1]
#term = 'python'
query = 'https://catalog.ocpl.org/client/en_US/default/search/results/?q=' + \
    urllib.parse.quote_plus(term)+'&ln=en_US&rw=0'
# print(query)


# %%
print('Start query, waiting browser...')
browser.goto(query)
print('Wait page loading...')
browser.smart_wait('#results_wrapper')

# %%
time.sleep(3)
print('Expand all results...')
allps = browser._driver.find_elements_by_tag_name('p')
for p in allps:
    if p.text == 'Show More':
        p.click()
        time.sleep(1)


# %%
time.sleep(3)
books = []
result = browser.smart_find('//*[@id="results_wrapper"]')
cells = result.find_elements_by_class_name('cell_wrapper')
for cell in cells:
    book_title = cell.find_elements_by_class_name('displayDetailLink')[0].text
    # print(book_title)
    trs = cell.find_elements_by_tag_name('tr')
    for tr in trs:
        tds = tr.find_elements_by_tag_name('td')
        if(len(tds) > 3):
            if tds[3].text == 'Check Shelf':
                books.append(
                    {"library": tds[0].text, "title": book_title, "shelf": tds[2].text})
sortlibs = sorted(books, key=itemgetter('library'))
# debug only
# for book in books:
#        print(book['library'], "/", book['title'], "/", book['shelf'])


# %%
libcnts = defaultdict(int)
for book in sortlibs:
    libcnts[book['library']] += 1
# print(libcnts)
for w in sorted(libcnts, key=libcnts.get, reverse=True):
    print(w, '(', libcnts[w], ')')
    for book in sortlibs:
        if book['library'] == w:
            print("        ", book['library'], "/",
                  book['title'], "/", book['shelf'])

# %%
browser.close()
