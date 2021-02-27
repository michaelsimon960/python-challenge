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

# Set my variables

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Count the number of voter ids

for row in csvreader: 

        total_votes +=1

