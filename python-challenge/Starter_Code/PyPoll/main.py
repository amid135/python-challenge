import csv

# Path to collect data from the Resources folder
csvpath = ("C:\\Users\\amid1\\Desktop\\Python\\python-challenge\\Starter_Code\\PyPoll\\Resources\\election_data.csv")


total_votes = 0
candidates = []
votes_per_candidate = {}

# Read the csv file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through the data
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        
        # If the candidate is new, add them to the list of candidates
        if candidate not in candidates:
            candidates.append(candidate)
            votes_per_candidate[candidate] = 1
        # If the candidate already exists, increment their vote count
        else:
            votes_per_candidate[candidate] += 1

# Calculate the percentage of votes each candidate won
percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in votes_per_candidate.items()}

# Find the winner based on popular vote
winner = max(votes_per_candidate, key=votes_per_candidate.get)

# Print the analysis to the terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the analysis to a text file
with open("election_analysis.txt", 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {percentages[candidate]:.3f}% ({votes_per_candidate[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")