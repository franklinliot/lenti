import pandas as pd
import glob

df = pd.concat(map(pd.read_csv, ['data/LenStore/LenStore.csv', 'data/LenStore/LentillesMoinsCheres.csv']))


df.to_csv(r'/home/franklin/coding/lenti/data/ultime/Ultime.csv')
