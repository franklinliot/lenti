import pandas as pd
import glob

path = r'/home/franklin/coding/lenti/data/LenStore' # use your path
all_files = glob.glob(path + "/*.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0)

df.to_csv(r'/home/franklin/coding/lenti/data/ultime/Ultime.csv')
