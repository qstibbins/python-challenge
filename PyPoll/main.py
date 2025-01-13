# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
# Track the total number of votes cast
total_votes = 0  

# Define lists and dictionaries to track candidate names and vote counts
# Track the total number of votes each candidate receives
vote_counts = {} 

# Track the names of the candidates who received votes 
candidates = []  


# Winning Candidate and Winning Count Tracker
# Track the winning candidate
winning_candidate = "" 
winning_percentage = 0 


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1


        # Get the candidate's name from the row
        candidate_name = row[2]


        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            vote_counts[candidate_name] = 0

        # Add a vote to the candidate's count
        vote_counts[candidate_name] = vote_counts.get(candidate_name, 0) + 1

# winning_candidate = max(vote_counts, key=vote_counts.get)

# Print the results and export the data to a text file
print(f"\ncandidates: {candidates}")
print(f"\ntotal_votes: {total_votes}")
print(f"\nwinning_candidate: {winning_candidate}")

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"\nvote_counts: {vote_counts}\n")

    # Add header to text file
    output = (
        f"Election Results\n"
        f"-------------------------\n"
    )
    txt_file.write(output)

    # Write the total vote count to the text file
    txt_file.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidates:


        # Get the vote count and calculate the percentage
        votes = vote_counts[candidate]
        percent = float(votes) / float(total_votes) * 100

        # Update the winning candidate if this one has more votes
        if percent > winning_percentage:
            winning_percentage = percent
            winning_candidate = candidate   

        # Print and save each candidate's vote count and percentage
        output = f"{candidate}: {percent:.3f}% ({votes})\n"
        print(output, end="")
        txt_file.write(output)

    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)
