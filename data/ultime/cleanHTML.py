import html
import sys

sys.stdout = open("data/ultime/semiCleanTable.html", "w")

with open('data/ultime/uneditedTable.html', 'r') as f:
    html_string = f.read()
    html_string = html.unescape(html_string)


print (html_string)
sys.stdout.close()

# Python program to demonstrate merging of two files
  
data = data2 = ""
  
# Reading data from file1
with open('data/ultime/PROPRE.html') as fp:
    data = fp.read()
  
# Reading data from file2
with open('data/ultime/semiCleanTable.html') as fp:
    data2 = fp.read()
  
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

data = html.unescape(data)
  
with open ('data/ultime/CleanTable.txt', 'w') as fp:
    fp.write(data)


infile = open('data/ultime/CleanTable.txt','r').readlines()
with open('data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('data/ultime/CleanTableBis.txt','r').readlines()
with open('data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('data/ultime/CleanTableBis.txt','r').readlines()
with open('data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('data/ultime/CleanTable.txt','r').readlines()
with open('data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)


infile = open('data/ultime/CleanTableBis.txt','r').readlines()
with open('data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('data/ultime/CleanTable.txt','r').readlines()
with open('data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)


infile = open('data/ultime/CleanTableBis.txt','r').readlines()
with open('data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('data/ultime/CleanTable.txt','r').readlines()
with open('data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)


infile = open('data/ultime/CleanTableBis.txt','r').readlines()
with open('data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('data/ultime/CleanTable.txt','r').readlines()
with open('data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)


infile = open('data/ultime/CleanTableBis.txt','r').readlines()
with open('data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('data/ultime/CleanTable.txt','r').readlines()
with open('data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)





import os
os.rename(r'data/ultime/CleanTable.txt',r'data/ultime/CleanTable.html')







