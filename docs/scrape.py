from bs4 import BeautifulSoup
import requests 


html_text = requests.get("https://www.lenstore.fr/c1/lentilles-journalieres").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("h3", class_ ="c-product-list__title")
for job in jobs:
    company_name = job.text.replace("</a>", "" )
    company_name = company_name.text.replace("\n", "")
    print(f'''
    Nom du modèle: {company_name}
    ''')
