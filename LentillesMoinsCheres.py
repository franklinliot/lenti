from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np


nom_Produit = ""
marque = ""
LMC90 = ""
originalName = ""

html_text = requests.get(
    "https://www.lentillesmoinscheres.com/lentilles-de-contact/journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_="type-LENS")

npo_jobs = {}
jobs_no = 0
arr = np.array(["(90)", "(30)", "(180)", "6", "(6)", "90", "30", "60"])


for job in jobs:
    nomProduit = job.find("h3", class_="product-title")
    nom_Produit = nomProduit.text.replace("</a>", "")

    if (nom_Produit.find('Acuvue') != -1 or nom_Produit.find('ACUVUE') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('Biomedics') != -1):
        marque = "Biomedics"
    elif (nom_Produit.find('Clariti') != -1):
        marque = "Clariti"
    elif (nom_Produit.find('Dailies') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Soflens') != -1):
        marque = "Soflens"
    elif (nom_Produit.find('everClear') != -1):
        marque = "everClear"
    elif (nom_Produit.find('Proclear') != -1):
        marque = "Proclear"
    else:
        marque = "something else"

    prixProduit = job.find("div", class_="price")
    LMC30 = prixProduit.text.replace("</a>", "")

    # lienAchat = "https://lentillesmoinscheres.com" + job.h3.a['href']
    lienAchat = "https://lentillesmoinscheres.com" + job.h3.a['href']
    jobs_no += 1
    npo_jobs[jobs_no] = [marque, nom_Produit,
                         LMC30, lienAchat, LMC90]

    # While loop to shorten originalNamelec
    if (nom_Produit.find('(90)') != -1 or nom_Produit.find('90') != -1):
        LMC90 = "seulement 30"
        originalName = nom_Produit
    else:
        LMC90 = "bien 90"
        originalName = nom_Produit

df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
    'marque', 'nom_Produit', 'LMC30', 'lienAchat', 'LMC90'])

df['LMC30'] = df['LMC30'].str.replace("€", "")

df['LMC30'] = df['LMC30'].str.strip()

df['LMC30'] = df['LMC30'].str.slice(start=-5)

df = df[~df['marque'].isin(['something else'])]

def make_clickable(val):
    # target _blank to open new window
    return '<a target="_blank" href="{}">{}</a>'.format(val, val)
df.style.format({'lienAchat': make_clickable})

html = df.to_html(index=False, render_links=True)

text_file = open("/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "w")
text_file.write(html)
text_file.close()


a_file = open("/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "<table id=\"myTable\">\n"

a_file = open("/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "w")
a_file.writelines(list_of_lines)
a_file.close()

df.to_csv(r'/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.csv', index=False)

print(df)