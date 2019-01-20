import sys
import time
sys.path.append('../')
from crawlkit import util

query = 'https://catalog.ocpl.org/client/en_US/default/search/results/?q=isee&ln=en_US&rw=0'
browser=util.MyChrome(False)

p=browser._driver.find_elements_by_tag_name('p')
for ea in p:
    if(ea.text=='Show More'):
        ea.click()

result=browser.smart_find('//*[@id="results_wrapper"]')

trs=result.find_elements_by_tag_name('tr')
for tr in trs:
    tds=tr.find_elements_by_tag_name('td')
    if(len(tds)>3):
        print(tds[0].text,"/" , tds[2].text, "/" , tds[3].text)