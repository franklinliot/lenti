import pandas as pd
import LenStore
import Lentiamo
import LentillesMoinsCheres
import MaLentille
import VisionDirect
import os.path
import os
import pandas
from os import path

if (path.exists("data/ultime/uneditedTable.html")) :
    os.remove("data/ultime/uneditedTable.html")
    
if (path.exists("data/ultime/semiCleanTable.html")) :
    os.remove("data/ultime/semiCleanTable.html")

from LenStore import *
from Lentiamo import *
from LentillesMoinsCheres import *
from MaLentille import *
from VisionDirect import *










df = df.reset_index(drop=True)
df2 = df2.reset_index(drop=True)
df3 = df3.reset_index(drop=True)
df4 = df4.reset_index(drop=True)
df5 = df5.reset_index(drop=True)




dfBis = pandas.concat([df, df2], axis=1)
dfBis = pandas.concat([dfBis, df3], axis=1)
dfBis = pandas.concat([dfBis, df4], axis=1)
dfBis = pandas.concat([dfBis, df5], axis=1)


dfBis = dfBis.drop('Nom Produit LMC', 1)
dfBis = dfBis.drop('NomProduitLentiamo', 1)
dfBis = dfBis.drop('NomProduitMaLentille', 1)
dfBis = dfBis.drop('NomProduitVisionDirect', 1)

dfBis = dfBis.drop('MarqueLenStore', 1)
dfBis = dfBis.drop('MarqueVisionDirect', 1)
dfBis = dfBis.drop('MarqueLentiamo', 1)
dfBis = dfBis.drop('MarqueLMC', 1)


dfBis = dfBis[['NomProduitLenStore', 'MarqueMaLentille', 'LenStore', 'Lentiamo', 'Lentilles Moins Cheres', 'Ma Lentille', 'Vision Direct']]


dfBis.to_csv(r'/home/franklin/coding/lenti/data/ultime/Ultime.csv', index = False)

import CSVToHTML
import cleanHTML
