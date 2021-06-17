import pandas as pd
import glob

df = pd.concat(map(pd.read_csv, ['data/LenStore/LenStore.csv', 'data/LenStore/LentillesMoinsCheres.csv']))


df.to_csv(r'/home/franklin/coding/lenti/data/ultime/Ultime.csv')


text_file = open(
    "/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "w")
text_file.write(df)
text_file.close()

a_file = open(
    "/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "r")
list_of_lines = a_file.readlines()
list_of_lines[0] = "<table id=\"myTable\">\n"

a_file = open(
    "/home/franklin/coding/lenti/data/LentMCheres/LentMCheres.html", "w")
a_file.writelines(list_of_lines)
a_file.close()