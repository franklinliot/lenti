from bs4 import BeautifulSoup
import requests 


html_text = requests.get("https://www.lenstore.fr/c1/lentilles-journalieres").text
soup = BeautifulSoup(html_text, 'lxml')
models = soup.find("ul", { "id" : "ProductList" })


print(models)
