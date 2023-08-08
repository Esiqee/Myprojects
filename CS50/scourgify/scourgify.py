import sys
import csv


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


table = []


try:
    with open (sys.argv[1]) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            table.append(line)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")


new_table = []
header = ["first", "last", "house"]
new_table.append(header)
for element in table:
    e1, e2 = element[0].split(', ')
    e3 = element[1]
    values = [e2, e1, e3]
    new_table.append(values)



with open (sys.argv[2], "w") as file:
    writer = csv.writer(file)
    for line in new_table:
        writer.writerow(line)


#print(table[1])
#print(new_table)




