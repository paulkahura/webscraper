import requests
from bs4 import BeautifulSoup
URL = 'https://www.amazon.com/Acer-Predator-i7-9750H-Keyboard-PH315-52-78VL/dp/B07QXLFLXT/ref=sr_1_8?fst=as%3Aoff&pf_rd_i=16225007011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=74069509-93ef-4a3c-8dca-a9e3fa773a64&pf_rd_r=X0ZT45ECF7AJWZ1YQ7GG&pf_rd_s=merchandised-search-4&pf_rd_t=101&qid=1564486449&rnid=16225007011&s=computers-intl-ship&sr=1-8'



headers = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content,'html.parser')

title = soup.find(id="ad")

print(title)
