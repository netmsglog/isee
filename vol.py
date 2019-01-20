import requests
from bs4 import BeautifulSoup
import time

cnt = 0
setno = 0
for group in range(35):
    r=requests.get('https://www.piqosity.com/isee-middle-level-vocabulary-list/group-' + str(group+1)+'/')
    soup=BeautifulSoup(r.text,'html.parser')
    cards=soup.find_all('div', class_='fusion-flip-box-wrapper col-lg-2 col-md-2 col-sm-2')

    for card in cards:
        word=card.find('h2')
        back=card.find('div',class_='flip-box-back-inner')
        cnt = cnt + 1
        if cnt % 100 == 1:
            print('\nTRI-ISEE Middle '+str(cnt)+'-'+str(cnt+99)+'\n')
        print(word.text.strip()+","+back.text.strip())
    time.sleep(5)
