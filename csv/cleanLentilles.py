import csv

my_file_name = "/home/franklin/coding/projets_persos/lenti/csv/LentillesMoinsCheresDaily.csv"
cleaned_file = "/home/franklin/coding/projets_persos/lenti/csv/cleanLentilles.csv"
members = "something else"


lines = list()

with open("/home/franklin/coding/projets_persos/lenti/csv/LentillesMoinsCheresDaily.csv", 'r') as readFile:

    reader = csv.reader(readFile)

    for row in reader:

        lines.append(row)

        for field in row:

            if field == members:

                lines.remove(row)

with open("/home/franklin/coding/projets_persos/lenti/csv/cleanLentilles.csv", 'w') as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)




