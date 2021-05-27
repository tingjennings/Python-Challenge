# Import the pathlib and csv library
from pathlib import Path
import csv
import os

# Set the file path
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize lists
voterIDs = []
counties = []
candidate = []

# Open the csv file as an object
with open(csvpath, "r") as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
    # Read months and profits as seperate lists    
        voterIDs.append(row[0])
        counties.append(row[1])
        candidate.append(row[2])

# Initialize variables for analysis        
candidateresults = dict()
winner = ""
winnervotes = 0
#create unique list of candidates
unique = set(candidate)
# # Open the output path as a file object
# Set output file name
output_path = 'output.txt'
with open(output_path, 'w') as file:
   #Interate candidates
    file.write("Election Results\n")
    file.write("----------------------------\n")
    file.write(f"Total Votes:  {len(candidate)}\n")
    file.write("----------------------------\n")
    for can in unique:

        counter = 1
        candidatevotes = 0

        # Count votes
        while counter < (len(voterIDs)):      
            # If this candidate
           if candidate[counter] == can:
              candidatevotes += 1
 # Increment counter to get next element in the list
           counter +=1 
        if candidatevotes > winnervotes:
            winnervotes = candidatevotes
            winner = can 
        percentage = candidatevotes/len(candidate) * 100
        candidateresults[can] = candidatevotes
        file.write(f"{can}: {percentage:.3f}% ({candidatevotes})\n") 
    file.write("----------------------------\n")
    file.write(f"Winner:{winner}\n")
    file.write("----------------------------\n")

