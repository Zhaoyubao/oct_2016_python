# Optional Assignment: CSV
import csv

with open('us-500.csv', 'rU') as f:
    reader = csv.reader(f)
    first_row = reader.next()
    for row in reader:
        print row[0], row[1]
        for idx in range(len(row)):
            print "{}: {}".format(first_row[idx], row[idx])
        print "-" * 40
