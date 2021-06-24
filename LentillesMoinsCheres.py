from bs4 import BeautifulSoup
import requests
import pandas as pd
from PIL import Image

npo_jobs = {}
jobs_no = 0

html_text = requests.get(
    "https://www.lentillesmoinscheres.com/lentilles-de-contact/journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_="type-LENS")

for job in jobs:
    nomProduit = job.find("h3", class_="product-title")
    nom_Produit = nomProduit.text.replace("</a>", "")

    prixProduit = job.find("div", class_="price")
    id = prixProduit.text.replace("</a>", "")
    
    if (nom_Produit.find('(30)') != -1):
        nom_Produit = str.replace(nom_Produit, " (30)", "")
    elif (nom_Produit.find('30') != -1):
        nom_Produit = str.replace(nom_Produit, " 30", "")
    

    if (nom_Produit.find('ACUVUE') != -1):
        nom_Produit = str.replace(nom_Produit, "ACUVUE", "Acuvue")
    elif (nom_Produit.find('DAILIES') != -1):
        nom_Produit = str.replace(nom_Produit, "DAILIES", "Dailies")


    nom_Produit = str(nom_Produit)
    if (nom_Produit.find('1-Day Acuvue Moist') != -1):
        MarqueLMC = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist for Astigmatism') != -1):
        MarqueLMC = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist Multifocal') != -1):
        MarqueLMC = "Acuvue"
    elif (nom_Produit.find('Biomedics 1 Day Extra') != -1):
        MarqueLMC = "Biomedics"
    elif (nom_Produit.find('Biotrue One Day pour Astigmates') != -1):
        MarqueLenStore = "Biotrue"
    elif (nom_Produit.find('Clariti 1 Day multifocal') != -1):
        MarqueLMC = "Clariti"
    elif (nom_Produit.find('Dailies AquaComfort Plus') != -1):
        MarqueLMC = "Dailies"
    elif (nom_Produit.find('Dailies All Day Comfort') != -1):
        MarqueLMC = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Toric') != -1):
        MarqueLMC = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Multifocal') != -1):
        MarqueLMC = "Dailies"
    elif (nom_Produit.find('Dailies TOTAL 1 Multifocal') != -1):
        MarqueLMC = "Dailies"
    elif (nom_Produit.find('MyDay') != -1 and id.find("19") != -1):
        MarqueLMC = "MyDay"
    elif (nom_Produit.find('Proclear 1 Day Multifocal') != -1):
        MarqueLMC = "something else"
    elif (nom_Produit.find('Proclear 1 Day') != -1):
        MarqueLMC = "Proclear"
    elif (nom_Produit.find('SofLens daily disposable pour Astigmates') != -1):
        MarqueLMC = "something else"
    elif (nom_Produit.find('SofLens daily disposable') != -1):
        MarqueLMC = "Soflens"
    else:
        MarqueLMC = "something else"
    

    lienAchatLMC = "https://www.lentillesmoinscheres.com" + job.h3.a['href']
    

    jobs_no += 1
    npo_jobs[jobs_no] = [nom_Produit,MarqueLMC, 
                         id, lienAchatLMC]

#Définir les colonnes du dataframe
df = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
     'nom_Produit', 'MarqueLMC', 'Lentilles Moins Cheres', 'lienAchatLMC'])

#Clean le Lentilles Moins Cheres
df['Lentilles Moins Cheres'] = df['Lentilles Moins Cheres'].str.replace("€", "")
df['Lentilles Moins Cheres'] = df['Lentilles Moins Cheres'].str.strip()
df['Lentilles Moins Cheres'] = df['Lentilles Moins Cheres'].str.slice(start=-5)

df['nom_Produit'] = df['nom_Produit'].str.replace('ACUVUE', 'Acuvue')

df['Lentilles Moins Cheres'] = df['Lentilles Moins Cheres'].apply(lambda x: f"{x} €")

# Rendre les liens cliquables pour
def make_clickable(lienAchatLMC, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatLMC, id)



df['Lentilles Moins Cheres'] = df.apply(lambda x: make_clickable(
    x['lienAchatLMC'], x['Lentilles Moins Cheres']), axis=1)

# Cache la colonne lienAchatLMC
df = df[['nom_Produit', 'MarqueLMC', 'Lentilles Moins Cheres']]


#Cacher les something else
df = df[~df['MarqueLMC'].str.contains("something else")]
df = df[~df['nom_Produit'].str.contains("90")]
df = df[~df['nom_Produit'].str.contains("8")]

df.rename(columns={'nom_Produit': 'Nom Produit LMC'}, inplace=True)

df['Nom Produit LMC'] = df['Nom Produit LMC'].str.replace(" ", "")

new_rowBiotrueAstig = {'Nom Produit LMC': 'Biotrue ONEday for Astigmatism', 'MarqueLMC': 'Biotrue', 'Lentilles Moins Cheres': '/'}
df = df.append(new_rowBiotrueAstig, ignore_index=True)

# new_rowBiotrueMyDay = {'Nom Produit LMC': 'MyDay', 'MarqueLMC': 'MyDay', 'Lentilles Moins Cheres': '/'}
# df = df.append(new_rowBiotrueMyDay, ignore_index=True)


df = df.sort_values('Nom Produit LMC')


df_products = pd.DataFrame.from_dict(df)
df_products = df_products.to_html(table_id="sellers_table-id", render_links=True, escape=False, index=False)


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

df.to_csv(r'/home/franklin/coding/lenti/data/LentMCheres/LentillesMoinsCheres.csv', index=False)

