#
# Webスクレイピングの練習
# 作詞掲示板：https://uta.pw/sakusibbs/ にログインし、お気に入りを列挙するスクレピング
#
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# メールアドレスとパスワードの指定
USER = "natosepia"
PASS = "willamette"

# セッションを開始
session = requests.session()

# ログイン
login_info = {
    "username_mmlbbs6":USER,
    "password_mmlbbs6":PASS,
    "back":"index.php",
    "mml_id":"0"
}

# action
url_login = "http://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる

# マイページのURLをピックアップする
soup = BeautifulSoup(res.text,"html.parser")
a = soup.select_one(".islogin a")# isloginクラス要素内のaタグ
if a is None:
    print("マイページが取得できませんでした")
    quit()

# 相対URLを絶対URLに変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("マイページ=", url_mypage)
res = session.get(url_mypage)
res.raise_for_status()

soup = BeautifulSoup(res.text,"html.parser")
links = soup.select("#favlist li > a")
for a in links:
    href = urljoin(url_mypage, a.attrs["href"])
    title = a.get_text()
    print("- {} > {}".format(title,href))
#print(res.text)

#print(res.text)