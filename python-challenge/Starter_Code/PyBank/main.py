import csv

# Function to read data from a CSV file
def read_csv():
    with open("C:\\Users\\amid1\\Desktop\\Python\\python-challenge\\Starter_Code\\PyBank\\Resources\\budget_data.csv", 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        data = [row for row in reader]
    return data

# Function to calculate financial analysis
def calculate_analysis(data):
    # Initialize variables
    total_months = 0
    net_total = 0
    monthly_changes = []
    previous_month_profit = 0
    greatest_increase = 0
    greatest_increase_date = ""
    greatest_decrease = 0
    greatest_decrease_date = ""

    # Iterate through each row of data
    for row in data:
        # Calculate total months and net total
        total_months += 1
        net_total += int(row[1])

        # Calculate monthly change and append to list
        current_month_profit = int(row[1])
        if previous_month_profit != 0:
            monthly_change = current_month_profit - previous_month_profit
            monthly_changes.append(monthly_change)

            # Find greatest increase and decrease
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_date = row[0]
            elif monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_date = row[0]

        # Update previous month profit for next iteration
        previous_month_profit = current_month_profit

    # Calculate average change
    average_change = sum(monthly_changes) / len(monthly_changes)

    # Output results to terminal
    print("Financial Analysis")
    print("------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    # Write results to a text file
    with open("financial_analysis.txt", "w") as file:
        file.write("Financial Analysis\n")
        file.write("------------------\n")
        file.write(f"Total Months: {total_months}\n")
        file.write(f"Total: ${net_total}\n")
        file.write(f"Average Change: ${average_change:.2f}\n")
        file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
        file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")

# Example usage
data = read_csv()
calculate_analysis(data)