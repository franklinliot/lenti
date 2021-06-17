from bs4 import BeautifulSoup
import requests
import pandas as pd

npo_jobs = {}
jobs_no = 0
marque =""

html_text = requests.get("https://www.malentille.com/36-journaliere-36").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_ = "ajax_block_product")


for job in jobs:
    nomProduit = job.find("h3")
    nom_Produit = nomProduit.text.replace("</a>", "")

    prixProduit = job.find("font", class_ = "category_price")
    id = prixProduit.text.replace("</font>", "")
    
    if (nom_Produit.find('(30)') != -1):
        nom_Produit = str.replace(nom_Produit, " (30)", "")
    elif (nom_Produit.find('30') != -1):
        nom_Produit = str.replace(nom_Produit, " 30", "")
    
    if (nom_Produit.find('ACUVUE') != -1):
        nom_Produit = str.replace(nom_Produit, "ACUVUE", "Acuvue")
    elif (nom_Produit.find('DAILIES') != -1):
        nom_Produit = str.replace(nom_Produit, "DAILIES", "Dailies")
    
    if (nom_Produit.find('1 Day') != -1):
        nom_Produit = str.replace(nom_Produit, "1 Day", "1-Day")
    
    if (nom_Produit.find('Acuvue') != -1):
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
    '''
    nom_Produit = str(nom_Produit)
    if (nom_Produit.find('1-Day Acuvue Moist') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist for Astigmatism') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist Multifocal') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('Biomedics 1 Day Extra') != -1):
        marque = "Biomedics"
    elif (nom_Produit.find('Clariti 1 Day multifocal') != -1):
        marque = "Clariti"
    elif (nom_Produit.find('Dailies AquaComfort Plus') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies All Day Comfort') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Toric') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Multifocal') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies TOTAL 1 Multifocal') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Proclear 1 Day Multifocal') != -1):
        marque = "something else"
    elif (nom_Produit.find('Proclear 1 Day') != -1):
        marque = "Proclear"
    elif (nom_Produit.find('SofLens daily disposable pour Astigmates') != -1):
        marque = "something else"
    elif (nom_Produit.find('SofLens daily disposable') != -1):
        marque = "Soflens"
    else:
        marque = "something else"
    '''

    lienAchatMaLentille = "https://www.lentillesmoinscheres.com" + job.h3.a['href']
    jobs_no += 1
    npo_jobs[jobs_no] = [marque, nom_Produit,
                         id, lienAchatMaLentille]

#Définir les colonnes du dataframe
df3 = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
    'marque', 'nom_Produit', 'LMC30', 'lienAchatMaLentille'])

#Clean le LMC30
df3['LMC30'] = df3['LMC30'].str.replace("€", "")
df3['LMC30'] = df3['LMC30'].str.strip()
df3['LMC30'] = df3['LMC30'].str.slice(start=-5)

df3['nom_Produit'] = df3['nom_Produit'].str.replace('ACUVUE', 'Acuvue')

# Rendre les liens cliquables pour
def make_clickable(lienAchatMaLentille, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatMaLentille, id)


df3['LMC30'] = df3.apply(lambda x: make_clickable(
    x['lienAchatMaLentille'], x['LMC30']), axis=1)

# Cache la colonne lienAchatMaLentille
df3 = df3[['marque', 'nom_Produit', 'LMC30']]

df3 = df3.sort_values('nom_Produit')

#Cacher les something else
df3 = df3[~df3['marque'].str.contains("something else")]

df3 = df3[~df3['nom_Produit'].str.contains("90L")]


df3.set_index('nom_Produit', inplace=True)

df_products = pd.DataFrame.from_dict(df3)
df_products = df_products.to_html(table_id="sellers_table-id", render_links=True, escape=False)


text_file = open(
    "/home/franklin/coding/lenti/data/MaLentille/MaLentille.html", "w")
text_file.write(df_products)
text_file.close()

a_file = open(
    "/home/franklin/coding/lenti/data/MaLentille/MaLentille.html", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "<table id=\"myTable\">\n"

a_file = open(
    "/home/franklin/coding/lenti/data/MaLentille/MaLentille.html", "w")
a_file.writelines(list_of_lines)
a_file.close()

df3.to_csv(r'data/MaLentille/MaLentille.csv')
