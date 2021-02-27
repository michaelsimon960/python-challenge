# Imports
import os
import csv

# Declare file location
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Empty List
total_months = []
total_profit = []
monthly_profit_change = []
 
# Open csv
with open(csvpath,newline="", encoding="utf-8") as budget:

     # Store the contents of budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header labels
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total months and total profit
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    # For loop to go through profits...start from the bottom of the list
    for i in range(len(total_profit)-1):
        
        # Profit monthly change
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        
# Max and min of profit change list
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# correlate month with profit change
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Output files
output_file = Path("PyBank", "analysis", "analysis.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")




