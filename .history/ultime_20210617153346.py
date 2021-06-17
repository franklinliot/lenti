import pandas as pd

df = pd.concat(map(pd.read_csv, ['data/LenStore/LenStore.csv', 'data/LentMCheres/LentillesMoinsCheres.csv', 'data/MaLentille/MaLentille.csv', 'data/VisionDirect/VisionDirect.csv']))


df.to_csv(r'/home/franklin/coding/lenti/data/ultime/Ultime.csv', index=False)