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

# total number of votes each candidate received

          if row[2] =="Khan":
               khan_votes +=1
          elif row[2] == "Correy":
               correy_votes +=1
          elif row[2] == "Li":
               li_votes +=1
          elif row[2] == "O'Tooley":
               otooley_votes +=1


# percentage of votes each candidate received
     khan_percent = round((khan_votes)/(total_votes) * 100, 2)
     

     correy_percent = round((correy_votes)/(total_votes) * 100, 2)
     

     otooley_percent = round((otooley_votes)/(total_votes) * 100, 2)
     

     li_percent = round((li_votes)/(total_votes) * 100, 2)


#print statements

print("Election Results")
print("-------------------")
print("Total Votes: " + str(total_votes))
print("-------------------")
print("Khan: " + str(khan_percent) + "% " + "(" + str(khan_votes) + ")")
print("Correy: " + str(correy_percent) + "% " + "(" + str(correy_votes) + ")")
print("Li: " + str(li_percent) + "% " + "(" + str(li_votes) + ")")
print("O'Tooley: " + str(otooley_percent) + "% " + "(" + str(otooley_votes) + ")")
print("-------------------")
print("Winner: Khan")
          
#Output
output_file = Path("PyPoll", "analysis", "analysis.txt")

with open(output_file,"w") as file:


     file.write("Election Results")
     file.write("\n")
     file.write("-------------------")
     file.write("\n")
     file.write("Total Votes: " + str(total_votes))
     file.write("\n")
     file.write("-------------------")
     file.write("\n")
     file.write("Khan: " + str(khan_percent) + "% " + "(" + str(khan_votes) + ")")
     file.write("\n")
     file.write("Correy: " + str(correy_percent) + "% " + "(" + str(correy_votes) + ")")
     file.write("\n")
     file.write("Li: " + str(li_percent) + "% " + "(" + str(li_votes) + ")")
     file.write("\n")
     file.write("O'Tooley: " + str(otooley_percent) + "% " + "(" + str(otooley_votes) + ")")
     file.write("\n")
     file.write("-------------------")
     file.write("\n")
     file.write("Winner: Khan")

     

