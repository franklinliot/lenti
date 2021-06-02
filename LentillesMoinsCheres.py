from bs4 import BeautifulSoup
import requests 
import pandas as pd

html_text = requests.get("https://www.lentillesmoinscheres.com/lentilles-de-contact/journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_ = "type-LENS")

npo_jobs = {}
jobs_no = 0

for job in jobs:
    nomProduit = job.find("h3", class_ = "product-title")
    nomProduitAdjusted = nomProduit.text.replace("</a>", "")

    prixProduit = job.find("div", class_ = "price")
    prixProduitAdjusted = prixProduit.text.replace("</a>", "")

    lienAchat = job.h3.a['href']

    revendeur = "LentillesMoinsCheres"

    jobs_no +=1
    npo_jobs[jobs_no]= [nomProduitAdjusted, prixProduitAdjusted, lienAchat, revendeur]
    
    print('nomProduitAdjusted', nomProduitAdjusted, '\nprixProduitAdjusted', prixProduitAdjusted, '\nlienAchat', lienAchat, '\nrevendeur', revendeur)


npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['nomProduitAdjusted', 'prixProduitAdjusted', 'lienAchat', 'revendeur'])

npo_jobs_df.to_csv('csv/LentillesMoinsCheresDaily.csv')
