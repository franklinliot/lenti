from bs4 import BeautifulSoup
import requests
import pandas as pd

npo_jobs = {}
jobs_no = 0
marque =""

html_text = requests.get("https://www.visiondirect.fr/lentilles-de-contact/lentilles-journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_ = "layout__item +1/3 +1/2-tablet +1/2-smart")

for job in jobs:
    nomProduit = job.find("div", class_ ="products-list__name same-height__name")
    nom_Produit = nomProduit.text.replace("</a>", "").strip()

    prixProduit = job.find("span", class_ = "price")
    id = prixProduit.text.replace("</span>", "")
    
    if (nom_Produit.find('(30)') != -1):
        nom_Produit = str.replace(nom_Produit, " (30)", "")
    elif (nom_Produit.find('30') != -1):
        nom_Produit = str.replace(nom_Produit, " 30", "")
    
    if (nom_Produit.find('ACUVUE') != -1):
        nom_Produit = str.replace(nom_Produit, "ACUVUE", "Acuvue")
    elif (nom_Produit.find('DAILIES') != -1):
        nom_Produit = str.replace(nom_Produit, "DAILIES", "Dailies")
    elif (nom_Produit.find('clariti') != -1):
        nom_Produit = str.replace(nom_Produit, "clariti", "Clariti")

    if (nom_Produit.find('1 Day') != -1):
        nom_Produit = str.replace(nom_Produit, "1 Day", "1-Day")
    
    if (nom_Produit.find('1 day') != -1):
        nom_Produit = str.replace(nom_Produit, "1 day", "1-Day")

    if (nom_Produit.find('MoistL') != -1):
        nom_Produit = str.replace(nom_Produit, "MoistL", "Moist")
    
    if (nom_Produit.find('ComfortL') != -1):
        nom_Produit = str.replace(nom_Produit, "ComfortL", "Comfort")

    if (nom_Produit.find('  ') != -1):
        nom_Produit = str.replace(nom_Produit, "  ", " ")

    if (nom_Produit.find('plus') != -1):
        nom_Produit = str.replace(nom_Produit, "plus", "Plus")
        nom_Produit = str.replace(nom_Produit, "Aquacomfort", "AquaComfort")





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
        
    nom_Produit = str(nom_Produit)
    if (nom_Produit.find('1-Day Acuvue Moist') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist for Astigmatism') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist Multifocal') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('Biomedics') != -1 and id.find('12,99') != -1):
        marque = "Biomedics"
    elif (nom_Produit.find('Clariti 1-Day multifocal') != -1):
        marque = "Clariti"
    elif (nom_Produit.find('Dailies AquaComfort Plus') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies All Day Comfort') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Toric') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Multifocal') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies Total 1 Multifocal') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Proclear 1-Day Multifocal') != -1):
        marque = "something else"
    elif (nom_Produit.find('Proclear 1-Day') != -1):
        marque = "Proclear"
    elif (nom_Produit.find('SofLens Daily for Astigmatism') != -1):
        marque = "something else"
    elif (nom_Produit.find('SofLens Daily') != -1):
        marque = "Soflens"

    else:
        marque = "something else"
    

    lienAchatVisionDirect = job.a['href']

    jobs_no += 1
    npo_jobs[jobs_no] = [marque, nom_Produit,
                         id, lienAchatVisionDirect]

#Définir les colonnes du dataframe
df4 = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
     'nom_Produit', 'marque','VisionD30', 'lienAchatVisionDirect'])

#Clean le VisionD30
df4['VisionD30'] = df4['VisionD30'].str.replace("€", "")
df4['VisionD30'] = df4['VisionD30'].str.strip()
df4['VisionD30'] = df4['VisionD30'].str.slice(start=-5)

df4['nom_Produit'] = df4['nom_Produit'].str.replace('ACUVUE', 'Acuvue')

# Rendre les liens cliquables pour
def make_clickable(lienAchatVisionDirect, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatVisionDirect, id)


df4['VisionD30'] = df4.apply(lambda x: make_clickable(
    x['lienAchatVisionDirect'], x['VisionD30']), axis=1)

# Cache la colonne lienAchatVisionDirect
df4 = df4[['marque', 'nom_Produit', 'VisionD30']]

df4 = df4.sort_values('nom_Produit')

#Cacher les something else
df4 = df4[~df4['marque'].str.contains("something else")]

df4 = df4[~df4['nom_Produit'].str.contains("90L")]
df4 = df4[~df4['nom_Produit'].str.contains("180L")]
df4 = df4[~df4['nom_Produit'].str.contains("90")]

df_products = pd.DataFrame.from_dict(df4)
df_products = df_products.to_html(table_id="sellers_table-id", render_links=True, escape=False, index=False)

df4 = df4.sort_values('nom_Produit')


text_file = open(
    "/home/franklin/coding/lenti/data/VisionDirect/VisionDirect.html", "w")
text_file.write(df_products)
text_file.close()

a_file = open(
    "/home/franklin/coding/lenti/data/VisionDirect/VisionDirect.html", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "<table id=\"myTable\">\n"

a_file = open(
    "/home/franklin/coding/lenti/data/VisionDirect/VisionDirect.html", "w")
a_file.writelines(list_of_lines)
a_file.close()

df4.to_csv(r'data/VisionDirect/VisionDirect.csv', index=False)
