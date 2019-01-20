import sys
import time
sys.path.append('../')
from crawlkit import util

#browser=util.MyChrome(False,'/Users/yu/Library/Application Support/Google/Chrome')
browser=util.MyChrome(False,'/Users/yu/Chrome')

browser.goto('https://quizlet.com/tri-isee/folders/middle-100/sets')
xpath_add = '/html/body/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div[3]/span[1]/span/button'
btn_add = browser.smart_wait(xpath_add, "btn_add")
if btn_add is None:
    print('Cannot find btn_add')
    browser.close()
    sys.exit()
time.sleep(2)
btn_add.click()
xpath_create = '/html/body/div[8]/div[2]/div/div[2]/div/div[1]/a'
btn_create = browser.smart_wait(xpath_create, 'btn_create')
time.sleep(2)
btn_create.click()
xpath_title = '/html/body/div[2]/main/div/div/div[1]/div[2]/div/div/label/div/div/div[2]/textarea'
input_title = browser.smart_wait(xpath_title, 'input_title')
input_title.send_keys('测试集')
