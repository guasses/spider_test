import requests
from bs4 import BeautifulSoup

class Login():

    def __init__(self):
        self.headers = {
            'Host': 'github.com',
            'Referer': 'https://github.com/login',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url,headers = self.headers).text
        html = BeautifulSoup(response,'lxml')
        token = html.input.next_sibling['value']
        return token

    def login(self,username,password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': username,
            'password': password,
        }
        response_post = self.session.post(self.post_url,data = post_data,headers=self.headers)
        #print(response_post.text)
        if response_post.status_code == 200:
            print("OK")
            #print(response_post.text)
        response_get = self.session.get(self.logined_url,headers=self.headers)
        #print(response_get.text)
        if response_get.status_code == 200:
            print("ok")

if __name__ == '__main__':
    login = Login()
    login.login('guasses','abc19970227.')