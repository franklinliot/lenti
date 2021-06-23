from bs4 import BeautifulSoup
import requests
import pandas as pd

npo_jobs = {}
jobs_no = 0
MarqueLentiamo = ""

html_text = requests.get(
    "https://www.lentiamo.fr/lentilles-journalieres.html?loadPages=1/").text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all("li", class_="vc-product-item")

for job in jobs:
    nomProduit = job.find(
        "h2", class_="vc-product-item-heading")
    nom_Produit = nomProduit.text.replace("</a>", "").strip()
 

    prixProduit = job.find("strong", class_="vc-price-value")
    id = prixProduit.text.replace("</strong>", "").strip()
   
    
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

    if (nom_Produit.find('1-DAY') != -1):
        nom_Produit = str.replace(nom_Produit, "1-DAY", "1-Day")

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
        MarqueLentiamo = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist for Astigmatism') != -1):
        MarqueLentiamo = "Acuvue"
    elif (nom_Produit.find('1-Day Acuvue Moist Multifocal') != -1):
        MarqueLentiamo = "Acuvue"
    elif (nom_Produit.find('Biotrue ONEday for Astigmatism (30 lentilles)') != -1):
        MarqueLentiamo = "Biotrue"
    elif (nom_Produit.find('Clariti 1-Day Multifocal') != -1):
        MarqueLentiamo = "Clariti"
    elif (nom_Produit.find('Dailies AquaComfort Plus') != -1):
        MarqueLentiamo = "Dailies"
    elif (nom_Produit.find('Dailies All Day Comfort') != -1):
        MarqueLentiamo = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Toric') != -1):
        MarqueLentiamo = "Dailies"
    elif (nom_Produit.find('Dailies AquaComfort Plus Multifocal') != -1):
        MarqueLentiamo = "Dailies"
    elif (nom_Produit.find('Dailies Total 1 Multifocal') != -1):
        MarqueLentiamo = "Dailies"
    elif (nom_Produit.find('MyDay daily disposable CooperVision (30 lentilles)') != -1):
        MarqueLentiamo = "MyDay"
    elif (nom_Produit.find('Proclear 1-Day Multifocal') != -1):
        MarqueLentiamo = "something else"
    elif (nom_Produit.find('Proclear 1-Day') != -1):
        MarqueLentiamo = "Proclear"
    elif (nom_Produit.find('SofLens Daily Disposable for Astigmatism') != -1):
        MarqueLentiamo = "something else"
    elif (nom_Produit.find('SofLens Daily') != -1):
        MarqueLentiamo = "Soflens"
    elif (nom_Produit.find('Biomedics 1-Day Extra CooperVision') != -1):
        MarqueLentiamo = "Biomedics"
    else:
        MarqueLentiamo = "something else"
    
    if (MarqueLentiamo.find('Sof   lens') != -1):
        MarqueLentiamo = "Soflens"
    
    lienAchatLentiamo = "https://www.lentiamo.fr" + job.a['href']

    jobs_no += 1
    npo_jobs[jobs_no] = [nom_Produit, MarqueLentiamo,
                         id, lienAchatLentiamo]

# Définir les colonnes du dataframe
df5 = pd.DataFrame.from_dict(npo_jobs, orient='index', columns=[
    'nom_Produit', 'MarqueLentiamo', 'Lentiamo', 'lienAchatLentiamo'])

# Clean le Lentiamo
'''
df5['Lentiamo'] = df5['Lentiamo'].str.replace("€", "")
df5['Lentiamo'] = df5['Lentiamo'].str.strip()
df5['Lentiamo'] = df5['Lentiamo'].str.slice(start=-5)
'''

df5['nom_Produit'] = df5['nom_Produit'].str.replace('ACUVUE', 'Acuvue')
df5['nom_Produit'] = df5['nom_Produit'].str.replace(' \(30 lentilles\)', '', regex=True)
df5['nom_Produit'] = df5['nom_Produit'].str.replace('Focus Dailies All Day Comfort', 'Dailies All Day Comfort')



# Rendre les liens cliquables pour
def make_clickable(lienAchatLentiamo, id):
    return '<a href="{}" rel="noopener noreferrer" target="_blank">{}</a>'.format(lienAchatLentiamo, id)


df5['Lentiamo'] = df5.apply(lambda x: make_clickable(
    x['lienAchatLentiamo'], x['Lentiamo']), axis=1)

# Cache la colonne lienAchatLentiamo
df5 = df5[['nom_Produit', 'MarqueLentiamo', 'Lentiamo']]

df5 = df5.sort_values('nom_Produit')

# Cacher les something else
df5 = df5[~df5['MarqueLentiamo'].str.contains("something else")]

df5 = df5[~df5['nom_Produit'].str.contains("90L")]
df5 = df5[~df5['nom_Produit'].str.contains("180L")]
df5 = df5[~df5['nom_Produit'].str.contains("90")]
df5 = df5[~df5['nom_Produit'].str.contains("180")]

df5 = df5.sort_values('nom_Produit')
df5.rename(columns={'nom_Produit': 'NomProduitLentiamo'}, inplace=True)

df5 = df5.sort_values('NomProduitLentiamo')


df_products = pd.DataFrame.from_dict(df5)
df_products = df_products.to_html(
    table_id="sellers_table-id", render_links=True, escape=False, index=False)




text_file = open(
    "/home/franklin/coding/lenti/data/Lentiamo/Lentiamo.html", "w")
text_file.write(df_products)
text_file.close()

a_file = open(
    "/home/franklin/coding/lenti/data/Lentiamo/Lentiamo.html", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "<table id=\"myTable\">\n"

a_file = open(
    "/home/franklin/coding/lenti/data/Lentiamo/Lentiamo.html", "w")
a_file.writelines(list_of_lines)
a_file.close()

df5.to_csv(r'data/Lentiamo/Lentiamo.csv', index=False)


