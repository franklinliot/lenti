from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

npo_jobs = {}
jobs_no = 0

html_text = requests.get("https://www.lenstore.fr/c1/lentilles-journalieres").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_ = "o-unstyled-list c-product-list__item u-text-center js-impression-product")    

for job in jobs:
    nomProduit = job.find("h3", class_ ="c-product-list__title")
    nom_Produit = nomProduit.text.replace("</a>", "")
    nom_Produit = nomProduit.text.replace("1 Day", "1-Day").strip()


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

    LenStore30 = job.find("span", class_ = "u-price")
    LenStore30 = str(LenStore30)


    lienAchatLenStore = job.h3.a['href']
    jobs_no += 1
    npo_jobs[jobs_no] = [marque, nom_Produit,
                         LenStore30, lienAchatLenStore]

#Définir les colonnes du dataframe
df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
    'marque', 'nom_Produit', 'LenStore30', 'lienAchatLenStore'])

df['nom_Produit'] = df['nom_Produit'].str.replace('ACUVUE', 'Acuvue')

# Rendre les liens cliquables pour
def make_clickable(lienAchatLenStore, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatLenStore, id)

#Rendre LenStore30 cliquable
df['LenStore30'] = df.apply(lambda x: make_clickable(
    x['lienAchatLenStore'], x['LenStore30']), axis=1)

df['LenStore30'] = df['LenStore30'].str.replace("€", "")

# Cache la colonne lienAchatLenStore
df = df[['marque', 'nom_Produit', 'LenStore30']]

df = df.sort_values('nom_Produit')

df_products = pd.DataFrame.from_dict(df)
df_products = df_products.to_html(
    index=False, table_id="sellers_table-id", render_links=True, escape=False)

text_file = open(
    "/home/franklin/coding/lenti/data/LenStore/LenStore.html", "w")
text_file.write(df_products)
text_file.close()

a_file = open(
    "/home/franklin/coding/lenti/data/LenStore/LenStore.html", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "<table id=\"myTable\">\n"

a_file = open(
    "/home/franklin/coding/lenti/data/LenStore/LenStore.html", "w")
a_file.writelines(list_of_lines)
a_file.close()