# Imports
import os
import csv

# Declare file location
csvpath = os.path.join('..', 'Resources', 'election_data.csv')


# Set my variables

total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv
with open(csvpath,newline="", encoding="utf-8") as poll:

     # Store the contents of budget_data.csv in the variable csvreader

     csvreader = csv.reader(poll,delimiter=",")

       # Skip the header labels

     header = next(csvreader)

# Count the number of voter ids

     for row in csvreader: 

          total_votes +=1

          if row[2] =="Khan":
               khan_votes +=1
          elif row[2] == "Correy":
               correy_votes +=1
          elif row[2] == "Li":
               li_votes +=1
          elif row[2] == "O'Tooley":
               otooley_votes +=1



     khan_percent = round((khan_votes)/(total_votes) * 100, 2)
     print(khan_percent)

     correy_percent = round((correy_votes)/(total_votes) * 100, 2)
     print(correy_percent)

     otooley_percent = round((otooley_votes)/(total_votes) * 100, 2)
     print(otooley_percent)

          

     

