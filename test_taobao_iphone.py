from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from bs4 import BeautifulSoup
import csv
import codecs

def request_html(page):
    '''根据页数获取html'''
    url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
    browser.get(url)
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.form > input')))
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.form > span.btn.J_Submit')))
    input.clear()
    input.send_keys(page)
    button.click()
    try:
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
    except TimeoutException:
        username = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_Static div.field.username-field > input')))
        password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_StandardPwd > input')))
        commit = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,'#J_Static > div.submit'))
        username.clear()
        username.send_keys('')
        password.clear()
        password.send_keys('')
        commit.click()

    html = browser.page_source   
    return html

def get_data(html):
    """根据网页源代码爬取相应的内容"""
    soup = BeautifulSoup(html,'lxml')
    for item in soup.find(class_='m-itemlist').find_all(class_='item'):
        price = item.find(class_='row row-1 g-clearfix').strong.text
        num_payment = item.find(class_='row row-1 g-clearfix').find(class_='deal-cnt').text
        href = 'https:' + item.find(class_='row row-2 title').a['href']
        title = item.find(class_='row row-2 title').a.text.strip()
        shop_name = item.find(class_='row row-3 g-clearfix').a.text.strip()
        shop_location = item.find(class_='row row-3 g-clearfix').find(class_='location').text
        with open('test_taobao_iphone.csv','a',encoding='GB2312',newline='') as f:
            #f.write(codecs.BOM_UTF8)
            writer = csv.writer(f)
            writer.writerow([price,num_payment,href,title,shop_name,shop_location])


browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
KEYWORD = 'iphone'
page = 1

for i in range(1,101):
    page = i
    html = request_html(page)
    get_data(html)


