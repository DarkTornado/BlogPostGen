import requests
from bs4 import BeautifulSoup

url = 'https://m.blog.naver.com/dt3141592/222564558533'
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
title = html.select_one("div.se-module.se-module-text.se-title-text").get_text().strip()
print(title)
