from bs4 import BeautifulSoup
import requests 
import pandas as pd

html_text = requests.get("https://www.lenstore.fr/c1/lentilles-journalieres").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_ = "o-unstyled-list c-product-list__item u-text-center js-impression-product")    

npo_jobs = {}
jobs_no = 0

for job in jobs:
    nomProduit = job.find("h3", class_ ="c-product-list__title")
    nomProduitAdjusted = nomProduit.text.replace("</a>", "").strip()

    prixProduit = job.find("span", class_ = "u-price")
    prixProduitAdjusted = prixProduit.text.replace("</a>", "").strip()

    lienAchat = job.a['href']
    revendeur = "LenStore"

    jobs_no +=1
    npo_jobs[jobs_no]= [nomProduitAdjusted, prixProduitAdjusted, lienAchat, revendeur]
    
    print('nomProduitAdjusted', nomProduitAdjusted, '\nprixProduitAdjusted', prixProduitAdjusted, '\nlienAchat', lienAchat, '\nrevendeur', revendeur)

npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['nomProduitAdjusted', 'prixProduitAdjusted', 'lienAchat', 'revendeur'])

npo_jobs_df.to_csv('csv/LenStoreDaily.csv')