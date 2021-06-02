from bs4 import BeautifulSoup
import requests 
import pandas as pd

html_text = requests.get("https://www.visiondirect.fr/lentilles-de-contact/lentilles-journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_ = "layout__item +1/3 +1/2-tablet +1/2-smart")

npo_jobs = {}
jobs_no = 0

for job in jobs:
    nomProduit = job.find("div", class_ ="products-list__name same-height__name")
    nomProduitAdjusted = nomProduit.text.replace("</div>", "").strip()

    prixProduit = job.find("span", class_ = "price")
    prixProduitAdjusted = prixProduit.text.replace("</span>", "")

    lienAchat = job.a['href']

    revendeur = "VisionDirect"

    jobs_no +=1
    npo_jobs[jobs_no]= [nomProduitAdjusted, prixProduitAdjusted, lienAchat, revendeur]
    
    print('nomProduitAdjusted', nomProduitAdjusted, '\nprixProduitAdjusted', prixProduitAdjusted, '\nlienAchat', lienAchat, '\nrevendeur', revendeur)


npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['nomProduitAdjusted', 'prixProduitAdjusted', 'lienAchat', 'revendeur'])

npo_jobs_df.to_csv('csv/VisionDirectDaily.csv')