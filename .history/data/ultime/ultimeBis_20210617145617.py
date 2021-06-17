#input file
fin = open("/home/franklin/coding/lenti/data/ultime/ultime.html", "rt")
#output file to write the result to
fout = open("/home/franklin/coding/lenti/data/ultime/ultimeBis.html", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('t', 'papa'))
#close input and output files
fin.close()
fout.close()