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
    id = prixProduit.text.replace("</a>", "")

    # lienAchat = "https://lentillesmoinscheres.com" + job.h3.a['href']
    lienAchat = "https://lentillesmoinscheres.com" + job.h3.a['href']
    lienAchat = lienAchat
    jobs_no += 1
    npo_jobs[jobs_no] = [marque, nom_Produit,
                         id, lienAchat, LMC90]

    # While loop to shorten originalNamelec
    if (nom_Produit.find('(90)') != -1 or nom_Produit.find('90') != -1):
        LMC90 = "seulement 30"
        originalName = nom_Produit
    else:
        LMC90 = "bien 90"
        originalName = nom_Produit

df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
    'marque', 'nom_Produit', 'id', 'lienAchat', 'LMC90'])

df['id'] = df['id'].str.replace("€", "")

df['id'] = df['id'].str.strip()

df['id'] = df['id'].str.slice(start=-5)

df = df[~df['marque'].isin(['something else'])]


df_products = pd.DataFrame.from_dict(df)
list_ids = df_products.id.tolist()
df_products = df_products.to_html(index=False, table_id="sellers_table-id", render_links=True,escape=False)
for id in list_ids:
    df_products = df_products.replace(
        '<td>{0}</td>'.format(id),
        '''<td><a href="../../link/to/{id}" target="_blank">{id}</a></td>'''.format(id=id)
    )


text_file = open("/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "w")
text_file.write(df_products)
text_file.close()


a_file = open("/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "<table id=\"myTable\">\n"

a_file = open("/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "w")
a_file.writelines(list_of_lines)
a_file.close()

#df.to_csv(r'/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.csv', index=False)
