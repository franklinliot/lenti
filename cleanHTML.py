import html
import sys

sys.stdout = open("/home/franklin/coding/lenti/data/ultime/semiCleanTable.html", "w")

with open('/home/franklin/coding/lenti/data/ultime/uneditedTable.html', 'r') as f:
    html_string = f.read()
    html_string = html.unescape(html_string)


print (html_string)
sys.stdout.close()

# Python program to demonstrate merging of two files
  
data = data2 = ""
  
# Reading data from file1
with open('/home/franklin/coding/lenti/data/ultime/PROPRE.html') as fp:
    data = fp.read()
  
# Reading data from file2
with open('/home/franklin/coding/lenti/data/ultime/semiCleanTable.html') as fp:
    data2 = fp.read()
  
# Merging 2 files
# To add the data of file2
# from next line
data += "\n"
data += data2

data = html.unescape(data)
  
with open ('/home/franklin/coding/lenti/data/ultime/CleanTable.txt', 'w') as fp:
    fp.write(data)


infile = open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)


infile = open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)


infile = open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)


infile = open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)

infile = open('/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt','r').readlines()
with open('/home/franklin/coding/lenti/data/ultime/CleanTable.txt','w') as outfile:
    for index,line in enumerate(infile):
        if index != 18:
            outfile.write(line)




import os
os.rename(r'/home/franklin/coding/lenti/data/ultime/CleanTable.txt',r'/home/franklin/coding/lenti/data/ultime/CleanTable.html')
'''
os.remove("/home/franklin/coding/lenti/data/ultime/CleanTableBis.txt")
'''




