from bs4 import BeautifulSoup
import requests
import pandas as pd

npo_jobs = {}
jobs_no = 0
Colors = ["1-Day ACUVUE Moist (30)", "Miru"]

html_text = requests.get(
    "https://www.lentillesmoinscheres.com/lentilles-de-contact/journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_="type-LENS")

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

    lienAchatLMC = "https://www.lentillesmoinscheres.com" + job.h3.a['href']
    jobs_no += 1
    npo_jobs[jobs_no] = [marque, nom_Produit,
                         id, lienAchatLMC]

#Définir les colonnes du dataframe
df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
    'marque', 'nom_Produit', 'LMC30', 'lienAchatLMC'])

#Clean le LMC30
df['LMC30'] = df['LMC30'].str.replace("€", "")
df['LMC30'] = df['LMC30'].str.strip()
df['LMC30'] = df['LMC30'].str.slice(start=-5)

df['nom_Produit'] = df['nom_Produit'].str.replace('ACUVUE', 'Acuvue')

# Rendre les liens cliquables pour
def make_clickable(lienAchatLMC, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatLMC, id)


df['LMC30'] = df.apply(lambda x: make_clickable(
    x['lienAchatLMC'], x['LMC30']), axis=1)

# Cache la colonne lienAchatLMC
df = df[['marque', 'nom_Produit', 'LMC30']]

df = df.sort_values('nom_Produit')


df = df[~df['nom_Produit'].str.contains("something else")]



df_products = pd.DataFrame.from_dict(df)
df_products = df_products.to_html(
    index=False, table_id="sellers_table-id", render_links=True, escape=False)

text_file = open(
    "/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "w")
text_file.write(df_products)
text_file.close()

a_file = open(
    "/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "<table id=\"myTable\">\n"

a_file = open(
    "/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "w")
a_file.writelines(list_of_lines)
a_file.close()