# spider_test

一些简单的爬虫练习和测试

### test_github_login
用python模拟登陆github<br>
本代码来自《Python3网络爬虫开发实战》,做了一点点改动，比如书上用的是lxml模块，而我用的是bs4<br>

----
### test_logitech
爬取了罗技商城https://store.logitech.com.cn/Product<br>
保存格式为标题,链接,价格的txt文档

----
### test_taobao_iphone
爬取了淘宝搜索iphone的商品信息<br>
保存格式为csv,编码为GB2312,为了方便打开csv文件查看<br>
主要用到了selenium模块<br>
不过由于淘宝翻页要登陆，目前只能爬取第一页<br>
