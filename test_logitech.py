import requests
from bs4 import BeautifulSoup

base_url = 'https://store.logitech.com.cn/Product'
def get_item(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    response = requests.get(url,headers = headers).text
    html = BeautifulSoup(response,'lxml')
    items = html.find(class_='productList-list-ul clearfix').find_all(name='li')
    for item in items:
        title = item.find(class_='p-name').a['title']
        item_url ='https://store.logitech.com.cn' + item.find(class_='p-name').a['href']
        price = item.find(class_='p-price-comment').strong.text
        with open('item.txt','a',encoding='utf-8') as f:
            f.write('{0} {1} {2}\n'.format(title.strip(),item_url.strip(),price.strip()))

PAGE = 24
for page in range(PAGE):
    if page==1:
        url = base_url
    else:
        url = base_url +'?pageid='+str(page)
    get_item(url)
