from bs4 import BeautifulSoup
import requests
import pandas as pd

npo_jobs = {}
jobs_no = 0
MarqueVisionDirect = ""

html_text = requests.get(
    "https://www.visiondirect.fr/lentilles-de-contact/lentilles-journalieres/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_="layout__item +1/3 +1/2-tablet +1/2-smart")

for job in jobs:
    nomProduit = job.find(
        "div", class_="products-list__name same-height__name")
    nom_Produit = nomProduit.text.replace("</a>", "").strip()

    prixProduit = job.find("span", class_="price")
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

    print (nom_Produit)
    nom_Produit = str(nom_Produit)
    if (nom_Produit.find('1-Day Acuvue Moist') != -1):
        MarqueVisionDirect = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist for Astigmatism') != -1):
        MarqueVisionDirect = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist Multifocal') != -1):
        MarqueVisionDirect = "Acuvue"
    elif (nom_Produit.find('Biomedics') != -1 and id.find('12,99') != -1):
        MarqueVisionDirect = "Biomedics"
    elif (nom_Produit.find('Biotrue One Day for Astigmatism') != -1):
        MarqueVisionDirect = "Biotrue"
    elif (nom_Produit.find('Clariti 1-Day multifocal') != -1):
        MarqueVisionDirect = "Clariti"
    elif (nom_Produit.find('Dailies AquaComfort Plus') != -1):
        MarqueVisionDirect = "Dailies"
    elif (nom_Produit.find('Dailies All Day Comfort') != -1):
        MarqueVisionDirect = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Toric') != -1):
        MarqueVisionDirect = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Multifocal') != -1):
        MarqueVisionDirect = "Dailies"
    elif (nom_Produit.find('Dailies Total 1 Multifocal') != -1):
        MarqueVisionDirect = "Dailies"
    elif (nom_Produit.find('MyDay') != -1 and id.find("19,49") != -1):
        MarqueVisionDirect = "MyDay"
    elif (nom_Produit.find('Proclear 1-Day Multifocal') != -1):
        MarqueVisionDirect = "something else"
    elif (nom_Produit.find('Proclear 1-Day') != -1):
        MarqueVisionDirect = "Proclear"
    elif (nom_Produit.find('SofLens Daily for Astigmatism') != -1):
        MarqueVisionDirect = "something else"
    elif (nom_Produit.find('SofLens Daily') != -1):
        MarqueVisionDirect = "Soflens"
    else:
        MarqueVisionDirect = "something else"

    lienAchatVisionDirect = job.a['href']

    jobs_no += 1
    npo_jobs[jobs_no] = [nom_Produit, MarqueVisionDirect,
                         id, lienAchatVisionDirect]

# D??finir les colonnes du dataframe
df4 = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
    'nom_Produit', 'MarqueVisionDirect', 'Vision Direct', 'lienAchatVisionDirect'])

# Clean le Vision Direct
'''
df4['Vision Direct'] = df4['Vision Direct'].str.replace("???", "")
df4['Vision Direct'] = df4['Vision Direct'].str.strip()
df4['Vision Direct'] = df4['Vision Direct'].str.slice(start=-5)
'''

df4['nom_Produit'] = df4['nom_Produit'].str.replace('ACUVUE', 'Acuvue')

# Rendre les liens cliquables pour
def make_clickable(lienAchatVisionDirect, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatVisionDirect, id)



df4['Vision Direct'] = df4.apply(lambda x: make_clickable(
    x['lienAchatVisionDirect'], x['Vision Direct']), axis=1)

# Cache la colonne lienAchatVisionDirect
df4 = df4[['nom_Produit', 'MarqueVisionDirect', 'Vision Direct']]

# new_rowBiotrueMyday = {'nom_Produit': 'Myday', 'MarqueVisionDirect': 'Myday', 'Vision Direct': '/'}
# df4 = df4.append(new_rowBiotrueMyday, ignore_index=True)

# Cacher les something else
df4 = df4[~df4['MarqueVisionDirect'].str.contains("something else")]

df4 = df4[~df4['nom_Produit'].str.contains("90L")]
df4 = df4[~df4['nom_Produit'].str.contains("180L")]
df4 = df4[~df4['nom_Produit'].str.contains("90")]





df4 = df4.sort_values('nom_Produit')
df4.rename(columns={'nom_Produit': 'NomProduitVisionDirect'}, inplace=True)

df_products = pd.DataFrame.from_dict(df4)
df_products = df_products.to_html(
    table_id="sellers_table-id", render_links=True, escape=False, index=False)




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


