# Importt os and csv
import os
import csv

# PyBank's variables
months = []
profit_loss_changes = []

count_months = 0
net_profit_loss = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
 
    # Read through each row of data after the header  
    for row in csv_reader:

        # Count of months
        count_months += 1

        # Net_total amount of "Profit/Losses" over the entire period
        current_month_profit_loss = int(row[1])
        net_profit_loss += current_month_profit_loss

        if (count_months == 1):
            previous_month_profit_loss = current_month_profit_loss
            continue

        else:

            # Insert change in profit loss 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Append each month to the months[] and ach profit_loss_change to the profit_loss_changes[]
            months.append(row[0])
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            previous_month_profit_loss = current_month_profit_loss

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Create  the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Find best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# Print the analysis to the terminal

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${net_profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# Export a text file with the results
with open('financial_analysis.txt', 'w') as text:

    text.write("Financial Analysis\n")
    text.write("----------------------------\n")
    text.write(f"Total Months:  {count_months}\n")
    text.write(f"Total:  ${net_profit_loss}\n")
    text.write(f"Average Change:  ${average_profit_loss}\n")
    text.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    text.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")