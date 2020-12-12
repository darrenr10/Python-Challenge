import os
import csv

total_vote = 0
candidates = {}
percentage = {}


csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, 'r') as file_handler:
    reader = csv.reader(file_handler)
    header = next(reader)

    for row in reader:
        total_vote += 1
        if row[2] in candidates:
            candidates[row[2]]["Votes"] += 1
        else: 
            candidates[row[2]] = {}
            candidates[row[2]]["Votes"] = 1

for key, value in candidates.items():
    vote_perc = round(((value["Votes"] / total_vote) * 100),2)
    candidates[key]["Percentage"] = vote_perc


print('Election Results')
print('-------------------')
print(f'Total Votes: ${total_vote}')
print('-------------------')

for key,value in candidates.items():
    print(f'{key}: %{value["Percentage"]} ({value["Votes"]}) ')

print('-------------------')
print('Winner: Khan')
print('-------------------')  

output = os.path.join('analysis.txt')
with open(output, 'w') as analysis:
    analysis.write('Election Results')
    analysis.write(f'Total Votes: ${total_vote}')
    analysis.write(f'{key}: %{value["Percentage"]} ({value["Votes"]}) ')
    analysis.write('Winner: Khan')
    