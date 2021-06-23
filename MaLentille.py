from bs4 import BeautifulSoup
import requests
import pandas as pd

npo_jobs = {}
jobs_no = 0
MarqueMaLentille =""

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


    print (nom_Produit)    
    nom_Produit = str(nom_Produit)
    if (nom_Produit.find('1-Day Acuvue Moist') != -1):
        MarqueMaLentille = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist for Astigmatism') != -1):
        MarqueMaLentille = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist Multifocal') != -1):
        MarqueMaLentille = "Acuvue"
    elif (nom_Produit.find('Biomedics 1 Day Extra') != -1):
        MarqueMaLentille = "Biomedics"
    elif (nom_Produit.find('Biotrue') != -1):
        MarqueLenStore = "Biotrue"
    elif (nom_Produit.find('Clariti 1 Day multifocal') != -1):
        MarqueMaLentille = "Clariti"
    elif (nom_Produit.find('Dailies AquaComfort Plus') != -1):
        MarqueMaLentille = "Dailies"
    elif (nom_Produit.find('Dailies All Day Comfort') != -1):
        MarqueMaLentille = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Toric') != -1):
        MarqueMaLentille = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Multifocal') != -1):
        MarqueMaLentille = "Dailies"
    elif (nom_Produit.find('Dailies Total 1 Multifocal') != -1):
        MarqueMaLentille = "Dailies"
    elif (nom_Produit.find('MyDayL') != -1):
        MarqueMaLentille = "MyDay"
    elif (nom_Produit.find('Proclear 1-Day Multifocal') != -1):
        MarqueMaLentille = "something else"
    elif (nom_Produit.find('Proclear 1-Day') != -1):
        MarqueMaLentille = "Proclear"
    elif (nom_Produit.find('SofLens daily disposable pour Astigmates') != -1):
        MarqueMaLentille = "something else"
    elif (nom_Produit.find('Soflens Daily DisposableL') != -1):
        MarqueMaLentille = "Soflens"
    else:
        MarqueMaLentille = "something else"
    

    lienAchatMaLentille = job.h3.a['href']
    jobs_no += 1
    npo_jobs[jobs_no] = [nom_Produit, MarqueMaLentille, 
                         id, lienAchatMaLentille]

#Définir les colonnes du dataframe
df3 = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
     'nom_Produit', 'MarqueMaLentille','Ma Lentille', 'lienAchatMaLentille'])

#Clean le Ma Lentille
'''
df3['Ma Lentille'] = df3['Ma Lentille'].str.replace("€", "")
df3['Ma Lentille'] = df3['Ma Lentille'].str.strip()
df3['Ma Lentille'] = df3['Ma Lentille'].str.slice(start=-5)
'''
df3['nom_Produit'] = df3['nom_Produit'].str.replace('ACUVUE', 'Acuvue')

# Rendre les liens cliquables pour
def make_clickable(lienAchatMaLentille, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatMaLentille, id)


df3['Ma Lentille'] = df3.apply(lambda x: make_clickable(
    x['lienAchatMaLentille'], x['Ma Lentille']), axis=1)

# Cache la colonne lienAchatMaLentille
df3 = df3[['nom_Produit', 'MarqueMaLentille',  'Ma Lentille']]

new_rowBiotrueAstig = {'nom_Produit': 'Biotrue ONEday for Astigmatism', 'MarqueMaLentille': 'Biotrue', 'Ma Lentille': '/'}
df3 = df3.append(new_rowBiotrueAstig, ignore_index=True)
# new_rowBiotrueAstig = {'nom_Produit': 'Myday', 'MarqueMaLentille': 'Myday', 'Ma Lentille': '/'}
# df3 = df3.append(new_rowBiotrueAstig, ignore_index=True)

df3 = df3.sort_values('nom_Produit')

#Cacher les something else
df3 = df3[~df3['MarqueMaLentille'].str.contains("something else")]

df3 = df3[~df3['nom_Produit'].str.contains("90L")]
df3 = df3[~df3['nom_Produit'].str.contains("180L")]
df3 = df3[~df3['nom_Produit'].str.contains("90")]


df3.rename(columns={'nom_Produit': 'NomProduitMaLentille'}, inplace=True)

new_rowBiomedics = {'NomProduitMaLentille': 'Biomedics 1-Day Extra', 'MarqueMaLentille': 'Biomedics', 'Ma Lentille': '/'}
new_rowClariti = {'NomProduitMaLentille': 'Clariti 1-Day multifocal', 'MarqueMaLentille': 'Clariti', 'Ma Lentille': '/'}
df3 = df3.append(new_rowBiomedics, ignore_index=True)
df3 = df3.append(new_rowClariti, ignore_index=True)

df3 = df3.sort_values('NomProduitMaLentille')

df_products = pd.DataFrame.from_dict(df3)
df_products = df_products.to_html(table_id="sellers_table-id", render_links=True, escape=False, index=False)


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

df3.to_csv(r'/home/franklin/coding/lenti/data/MaLentille/MaLentille.csv', index=False)


