

def brandFinder():
    if (nomProduitAdjusted.find('Acuvue') != -1 or nomProduitAdjusted.find('ACUVUE') != -1):
        marque = "Acuvue"
    elif (nomProduitAdjusted.find('Biomedics') != -1):
        marque = "Biomedics"
    elif (nomProduitAdjusted.find('Clariti') != -1):
        marque = "Clariti"
    elif (nomProduitAdjusted.find('Dailies') != -1):
        marque = "Dailies"
    elif (nomProduitAdjusted.find('Soflens') != -1):
        marque = "Soflens"
    elif (nomProduitAdjusted.find('everClear') != -1):
        marque = "everClear"
    elif (nomProduitAdjusted.find('Proclear') != -1):
        marque = "Proclear"
    else: 
        marque = "something else"

brandFinder()