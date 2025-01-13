# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
date_list = []
net_change_list = []

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    previous_revenue = int(first_row[1])
    total_months += 1
    total_net = previous_revenue


    # Process each row of data
    for row in reader:
        current_revenue = int(row[1])
        
        # Track the dates
        date_list.append(row[0])

        # Track the total
        total_net += int(row[1])

        # Track the net change
        net_change = current_revenue - previous_revenue
        net_change_list.append(net_change)
        previous_revenue = current_revenue

        # Increase the total number of months
        total_months += 1

        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(net_change_list)
        greatest_increase_index = net_change_list.index(greatest_increase)
        greatest_increase_date = date_list[greatest_increase_index]

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(net_change_list)
        greatest_idecrease_index = net_change_list.index(greatest_decrease)
        greatest_decrease_date = date_list[greatest_idecrease_index]
        

# Calculate the average net change across the months. 
# Round to the nearest 2 decimal places to match README.md
average_net = round((sum(net_change_list) / len(net_change_list)), 2)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
