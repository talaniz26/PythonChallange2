# Crate a Python script that analyzes the PyBank records for the following
# --> Calculate the total number of months in the dataset
# --> Calcuate the net total "Profit/Loss" over the dataset record
# --> Calculate the average change in "Profit/Loss" over the dataset
# --> Calcualte the largest increase in profit by date and amount
# --> Calculate the largest decrease in losses by date and amount


# Dependencies
import os
import csv

# Define Variables


months = []
monthly_change =[]

count_months = 0
net_profit_loss = 0
previous_month = 0
current_month = 0

# make sure the directory is the current python script
os.chdir(os.path.dirname(__file__))

# Collect the data from the path of the Resources folder
budget_data_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_data_csv, newline="") as csvfile: # notes: newline argument empty string as flag to start new line

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first with the next method
    csv_header = next(csvfile)

   # print(f"Header: {csv_header}")
   #Testing the directory is located and printed the header

    for row in csv_reader:

        #Count the months
        count_months += 1

        #Net total amount of Profit/Loss over the entire dataset
        current_month = int(row[1])
        net_profit_loss += current_month

        if (count_months == 1):
            # Set the previous month value equal to current month value
            previous_month = current_month
            continue
        else:
            # Formula - for the change in profit
            profit_loss_change = current_month - previous_month

            months.append(row[0])
            monthly_change.append(profit_loss_change)
            previous_month = current_month
    total_profit_loss = sum(monthly_change)
    average_profit_loss = round(total_profit_loss/(count_months-1),2)

    max_change = max(monthly_change)
    min_change = min(monthly_change)

    hmi = monthly_change.index(max_change)
    lmi = monthly_change.index(min_change)
    
    best_month = months[hmi]
    worst_month = months[lmi]
# -->>  Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${max_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${min_change})")

# -->>  Export a text file with the results
budget_file = os.path.join("Output", "budget_data.txt")
with open(budget_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${max_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${min_change})\n")