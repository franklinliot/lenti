from bs4 import BeautifulSoup
import requests 
import pandas as pd

html_text = requests.get("https://www.malentille.com/36-journaliere-36").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_ = "ajax_block_product")

npo_jobs = {}
jobs_no = 0

for job in jobs:
    nomProduit = job.find("h3")
    nomProduitAdjusted = nomProduit.text.replace("</a>", "")

    prixProduit = job.find("font", class_ = "category_price")
    prixProduitAdjusted = prixProduit.text.replace("</font>", "")

    lienAchat = job.h3.a['href']

    revendeur = "MaLentille"

    jobs_no +=1
    npo_jobs[jobs_no]= [nomProduitAdjusted, prixProduitAdjusted, lienAchat, revendeur]
    
    print('nomProduitAdjusted', nomProduitAdjusted, '\nprixProduitAdjusted', prixProduitAdjusted, '\nlienAchat', lienAchat, '\nrevendeur', revendeur)


npo_jobs_df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['nomProduitAdjusted', 'prixProduitAdjusted', 'lienAchat', 'revendeur'])

npo_jobs_df.to_csv('csv/MalentilleDaily.csv')
