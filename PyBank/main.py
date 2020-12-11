import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler)
    header = next(reader)

    month_year = []
    profit = [] 
    change_in_profit = []
    total_pl = 0
    num_of_months = 0

    for row in reader:
        num_of_months += 1
        total_pl += float(row[1])
        month_year.append(row[0]) 
        profit.append(int(row[1]))
    
    for a in range(len(profit)-1):
        change_in_profit.append(profit[a+1]-profit[a])

mpmonth = max(change_in_profit)
mipmonth = min(change_in_profit)

max = change_in_profit.index(mpmonth)+1
min = change_in_profit.index(mipmonth)+1



# print
print('Fiancial Analysis')
print('-------------------')
print(f'Total Months: {num_of_months}')
print(f"Total Revenue: ${(total_pl)}")
print(f'Average Change: {round(sum(change_in_profit)/len(change_in_profit),2)}')
print(f'Greatest Increase in Profits: {month_year[max]} (${(str(mpmonth))})')
print(f'Greatest Decrease in Profits: {month_year[min]} (${(str(mipmonth))})')


