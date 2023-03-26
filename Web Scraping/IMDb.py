from urllib.request import urlopen, Request
from urllib.request import Request
from bs4 import BeautifulSoup
import pandas

def tratar_html(html):
    # html = html.decode("utf-8")
    return " ".join(html.split()).replace("> <", "><")

#region - G1

# url_g1 = "https://g1.globo.com/"

# response = urlopen(url_g1)
# html = response.read()

# # G1
# soup = BeautifulSoup(html, 'html.parser')
# var = soup.find('h2', id="").get_text()
# print(var)

#endregion


abrir_html = open("C:\Users\luan2\Desktop\Histórico.html", "r")

arquivo_html = abrir_html.read()

abrir_html.close()



# url_imdb_pre_tratamento = "chrome://history/"

# req_imdb = Request(url_imdb_pre_tratamento)
# response_imdb = urlopen(req_imdb)
# html_imdb = response_imdb.read()
html_imdb = tratar_html(arquivo_html)

soup = BeautifulSoup(html_imdb, "html.parser")

links = soup.find("a", class_="website-link")

print(links)



