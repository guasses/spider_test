'''Ajax爬取163music用户听歌排行'''
import requests
from bs4 import BeautifulSoup
import csv
import json

user_id = '406773448'
post_url = 'https://music.163.com/weapi/v1/play/record?csrf_token='
post_data = {
    'params': 'K+vDoKv6stJCKSTIzFmepA4qQB5AK8pGcRigQINFa4YzPJet1xfH1K3i1Le5zgmwJTnyoOa0KSYtH9OYJ7vBGuGAYyGYprfSWOoGSbdkJhbQ8DL3EzdigxI1eUPPitPMQaiDNbxjQTN01PNCu043C7j/FjrXS/hiXyeCkOqHDZXeQY0oMFGsQIgO+PfsJWRj',
    'encSecKey': '80176c17d6f4aa871b3beae552a68518db49c058fce6d28085339f88282ac6572d5970adbd85b6186ff8a671a38cd64cd71421c1e598a177ce84753a27d1c74b2d1bf508d03df799f95ea556c080fcb3cf310f4735aeaf1422512bb4957126620cbcab6e0e319bae4b41db957950437b22a149b16b6ffea3fa44c6084400c527' 
}
headers = {
    'Host': 'music.163.com',
    'Origin': 'https://music.163.com',
    'Referer': 'https://music.163.com/user/songs/rank?id=' + user_id,
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}
response = requests.post(post_url,data=post_data,headers=headers).json()
if response.get('allData'):
    for item in response.get('allData'):
        song_id = item['song']['al']['id']
        song_name = item['song']['name']
        for singer in item['song']['ar']:
            singer_id = singer['id']
            singer_name = singer['name']
        #存储为csv文件
        #with open('data.csv','a',encoding='utf-8') as f:
        #    fieldnames = ['song_id','song_name','singer_id','singer_name']
        #    writer = csv.DictWriter(f,fieldnames=fieldnames)
        #    writer.writeheader()
        #   writer.writerow({'song_id':song_id,'song_name':song_name,
        #                    'singer_id':singer_id,'singer_name':singer_name})
            #存储为json文件
            file_str = [{
                "song_id":song_id,
                "song_name":song_name,
                "singer_id":singer_id,
                "singer_name":singer_name
            }]
            
            with open('test_163music.json','a',encoding='utf-8') as f:
                f.write(json.dumps(file_str,indent=2,ensure_ascii=False))