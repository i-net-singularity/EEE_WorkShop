import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# セッションを開始
session = requests.session()
url_login = "https://thirdparty.aliexpress.com/login.htm?spm=a2g0o.home.0.0.572c5c72p9ZpOF&type=gg&return_url=https%3A%2F%2Fja.aliexpress.com%2F"
html = requests.get(url_login)
soup = BeautifulSoup(html.content, "html.parser")
print(soup)