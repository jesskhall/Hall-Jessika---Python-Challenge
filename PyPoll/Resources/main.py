
import os
import csv

election_data = os.path.join("election_data.csv")

# Count total number of votes 
totalnumber_votes = 0

# A list to hold the names of candidates
candidate_name = []

# A complete list of candidates who received votes
numberof_votes = []

# The percentage of votes each candidate won 
percentof_votes = []


with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # vote counter +1 to loop through data 
        totalnumber_votes += 1 

    
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
            index = candidate_name.index(row[2])
            numberof_votes.append(1)
        else:
            index = candidate_name.index(row[2])
            numberof_votes[index] += 1
    
    # Add to percentof_votes list 
    for votes in numberof_votes:
        percentage = (votes/totalnumber_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percentof_votes.append(percentage)
    
    # Find the winner (candidate_name)
    winner = max(numberof_votes)
    index = numberof_votes.index(winner)
    winning_candidatename = candidate_name[index]

# Print Results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(totalnumber_votes)}")
print("--------------------------")
for i in range(len(candidate_name)):
    print(f"{candidate_name[i]}: {str(percentof_votes[i])} ({str(numberof_votes[i])})")
print("--------------------------")
print(f"Winner: {winning_candidatename}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(totalnumber_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate_name)):
    line = str(f"{candidate_name[i]}: {str(percentof_votes[i])} ({str(numberof_votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidatename}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))