# Imports
import os
import csv

# Declare file location
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# Open csv
with open(csvpath,newline="", encoding="utf-8") as poll:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(poll,delimiter=",") 

    # Skip the header labels
    header = next(csvreader) 

