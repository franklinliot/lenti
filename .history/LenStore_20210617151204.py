from bs4 import BeautifulSoup
import requests
import pandas as pd

npo_jobs = {}
jobs_no = 0
ProductList = ["1-Day Acuvue Moist"]

html_text = requests.get(
    "https://www.lenstore.fr/c1/lentilles-journalieres").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all(
    "li", class_="o-unstyled-list c-product-list__item u-text-center js-impression-product")

for job in jobs:
    nomProduit = job.find("h3", class_="c-product-list__title")
    nom_Produit = nomProduit.text.replace("</a>", "")
    nom_Produit = nomProduit.text.replace(
        "1 Day", "1-Day").replace("MOIST", "Moist").replace("OASYS", "Oasys").strip()

    if (nom_Produit.find('ACUVUE') != -1):
        nom_Produit = str.replace(nom_Produit, "ACUVUE", "Acuvue")
    elif (nom_Produit.find('DAILIES') != -1):
        nom_Produit = str.replace(nom_Produit, "DAILIES", "Dailies")
    elif (nom_Produit.find('1 Day') != -1):
        nom_Produit = str.replace(nom_Produit, "1 Day", "1-Day")

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

    LenStore30 = job.find("span", class_="u-price")
    LenStore30 = str(LenStore30)

    if (nom_Produit.find('1-Day Acuvue Moist') != -1 and LenStore30.find('16,49') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist for Astigmatism') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist Multifocal') != -1):
        marque = "Acuvue"
    elif (nom_Produit.find('Biomedics 1-Day Extra') != -1 and LenStore30.find('12,19€') != -1):
        marque = "Biomedics"
    elif (nom_Produit.find('Clariti 1-Day Multifocal') != -1):
        marque = "Clariti"
    elif (nom_Produit.find('Dailies AquaComfort Plus Toric') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus') != -1 and LenStore30.find('16,19€') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Multifocal') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Dailies Total 1 Multifocal') != -1):
        marque = "Dailies"
    elif (nom_Produit.find('Focus Dailies All Day Comfort') != -1 and LenStore30.find('15,59€') != -1):
        marque = "Dailies"
        nom_Produit = 'Dailies All Day Comfort'
    elif (nom_Produit.find('Proclear 1-Day') != -1 and LenStore30.find('13,29€') != -1):
        marque = "Proclear"
    elif (nom_Produit.find('Soflens Daily Disposable') != -1 and LenStore30.find('11,09€') != -1):
        marque = "Soflens"
    else:
        marque = "something else"

    lienAchatLenStore = job.h3.a['href']
    jobs_no += 1
    npo_jobs[jobs_no] = [nom_Produit, marque, 
                         LenStore30, lienAchatLenStore]


# Définir les colonnes du dataframe
df2 = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
     'nom_Produit', 'marque', 'LenStore30', 'lienAchatLenStore'])

df2['nom_Produit'] = df2['nom_Produit'].str.replace('ACUVUE', 'Acuvue')

# Rendre les liens cliquables pour


def make_clickable(lienAchatLenStore, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatLenStore, id)


# Rendre LenStore30 cliquable
df2['LenStore30'] = df2.apply(lambda x: make_clickable(
    x['lienAchatLenStore'], x['LenStore30']), axis=1)

df2['LenStore30'] = df2['LenStore30'].str.replace("€", "")

# Cache la colonne lienAchatLenStore
df2 = df2[['marque', 'nom_Produit', 'LenStore30']]

df2 = df2.sort_values('nom_Produit')

# Drop les something else
df2 = df2[~df2['marque'].str.contains("something else")]

df_products = pd.DataFrame.from_dict(df2)


df_products = df_products.to_html(
    table_id="sellers_table-id", render_links=True, escape=False, index=False)

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

df2.to_csv(r'data/LenStore/LenStore.csv', index=False)