from bs4 import BeautifulSoup
import requests 
import pandas as pd
import numpy as np


nomProduitAdjusted = ""
marque = ""
prix90 = ""
originalName = "" 

html_text = requests.get("https://www.lentillesmoinscheres.com/lentilles-de-contact/journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_ = "type-LENS")

npo_jobs = {}
jobs_no = 0
arr = np.array(["(90)", "(30)", "(180)", "6", "(6)", "90", "30", "60"])


for job in jobs:
    nomProduit = job.find("h3", class_ = "product-title")
    nomProduitAdjusted = nomProduit.text.replace("</a>", "")

    if (nomProduitAdjusted.find('Acuvue') != -1 or nomProduitAdjusted.find('ACUVUE') != -1):
        marque = "Acuvue"
    elif (nomProduitAdjusted.find('Biomedics') != -1):
        marque = "Biomedics"
    elif (nomProduitAdjusted.find('Clariti') != -1):
        marque = "Clariti"
    elif (nomProduitAdjusted.find('Dailies') != -1):
        marque = "Dailies"
    elif (nomProduitAdjusted.find('Soflens') != -1):
        marque = "Soflens"
    elif (nomProduitAdjusted.find('everClear') != -1):
        marque = "everClear"
    elif (nomProduitAdjusted.find('Proclear') != -1):
        marque = "Proclear"
    else: 
        marque = "something else"

    prixProduit = job.find("div", class_ = "price")
    prix30 = prixProduit.text.replace("</a>", "")

    lienAchat = "lentillesmoinscheres.com" + job.h3.a['href']

    revendeur = "LentillesMoinsCheres"

    jobs_no +=1
    npo_jobs[jobs_no]= [nomProduitAdjusted, marque, prix30, lienAchat, revendeur, prix90, originalName]
    
    # While loop to shorten originalNamelec
    if (nomProduitAdjusted.find('(90)') != -1 or nomProduitAdjusted.find('90') != -1):
        prix90 = "seulement 30"
        originalName = nomProduitAdjusted
    else : 
        prix90 = "bien 90"
        originalName = nomProduitAdjusted
    
df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=['nomProduitAdjusted', 'marque', 'prix30', 'lienAchat', 'revendeur', 'prix90', "originalName"])

df['prix30'] = df['prix30'].str.replace("€","")

df['prix30'] = df['prix30'].str.strip()

df['prix30'] = df['prix30'].str.slice(start=-5)





print(df.iloc[5]['originalName'])

df.to_csv('/home/franklin/coding/lenti/csv/LentillesMoinsCheresDaily.csv', index=False)

