import csv
from html import escape
import io
import html
import sys
import pandas as pd


sys.stdout = open("data/ultime/uneditedTable.html", "w")


# to read csv file named "samplee"
a = pd.read_csv("data/ultime/Ultime.csv")
 
# to save as html file
# named as "Table"
a.to_html("data/ultime/uneditedTable.html", index=False)

html_file = a.to_html()

