import csv
from html import escape
import io
import html
import sys
import pandas as pd


sys.stdout = open("/home/franklin/coding/lenti/data/ultime/uneditedTable.html", "w")


# to read csv file named "samplee"
a = pd.read_csv("/home/franklin/coding/lenti/data/ultime/Ultime.csv")
 
# to save as html file
# named as "Table"
a.to_html("/home/franklin/coding/lenti/data/ultime/uneditedTable.html", index=False)

html_file = a.to_html()

