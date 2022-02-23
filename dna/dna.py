import csv
import sys

# Ensure correct usage
if len(sys.argv) != 3:
    print("Usage: missing files")
    sys.exit(1)

    # 1. Open files
    # open a CSV file and read its contents into a dictionary (used "open" module to keep the reader open)
csvfile = open(sys.argv[1], "r")
reader = csv.DictReader(csvfile)

# 2. Create an empty list with max numbers of repeats
STRcounts = []
# open a text file, read its content - a sequence of DNA - as a string
with open(sys.argv[2]) as txtfile:
    DNA = txtfile.read()
    # iterating over each STR
    for s in range(1, len(reader.fieldnames)):
        STR = reader.fieldnames[s]
        j = 0
        repeats = 0
        maxrepeats = 0
        # iterating over DNA sequence
        while j < len(DNA):
            if DNA[j:j+len(STR)] == STR:
                j += len(STR)
                repeats += 1
                maxrepeats = max(maxrepeats, repeats)
            else:
                repeats = 0
                j += 1
        # populating STRcounts with maxrepeats - max number of times each STR repeats consequetively in the DNA sequence
        STRcounts.append(maxrepeats)

# 3. For each STRcount compare max numbers of repeats in STRcounts against data in csv file
rowint = []
match = 0
# used scvfile to read it as a string
for row in csvfile:
    # separating words in the string and converting them into integers to get a list of integers
    row = row.split(',')
    for x in range(1, len(row)):
        row[x] = int(row[x])
        rowint.append(row[x])
    # comparing integers in two lists
    if STRcounts == rowint:
        match += 1
    # clearing the values to go over the next row
    rowint = []    
    if match > 0:
        # if match is found, printing the name
        print(row[0])
        exit(0)
        
print("No match")

csvfile.close()
