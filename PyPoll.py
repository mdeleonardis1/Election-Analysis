# Data to register_archive_format
# 1. Total number of votes cast
# 2. A list of candiates
# 3. % of votes each candidate won 
# 4. Total number of votes each candidate won 
# 5. Winner of the election base on popular 

import os 
import csv


# assign a variable to load a file from a path

file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to save the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# with open(file_to_load) as election_data:
#     print(election_data)

 #with open(file_to_load) as election_data
#     print(election_data)
   
   # Read and print csv file 
    
# with open(file_to_load, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(types(lines))
# Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")
# 1 Start count of total votes Intialize count variable
total_votes = 0

#2 list of canidate names 
candidate_options = []

#3 Candidate Votes
candidate_votes = {}

# Winner determination

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the Election results and read the file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
# read header row
    headers = next(file_reader)
    #Count votes 
    for row in file_reader:
        total_votes += 1
            # Print the candidate name from each row.
        candidate_name = row[2]
        if candidate_name not in candidate_options:
        # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
              # Begin Tracking canidates vote count
            candidate_votes[candidate_name] = 0 

        # Count canidate votes
        candidate_votes[candidate_name] += 1 


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # # Print total votes
    # print(total_votes)

    # # Print Candidate Names
    # print(candidate_options)

    # # Print Canidate Votes 
    # print(candidate_votes)


    # 3 Determine the percentage of votes for each candidate by looping through the counts.
    #  Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage}% of the vote.")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        # Print the final vote count to the terminal.
    
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # winning_candidate_summary = (
    #     f"-------------------------\n"
    #     f"Winner: {winning_candidate}\n"
    #     f"Winning Vote Count: {winning_count:,}\n"
    #     f"Winning Percentage: {winning_percentage:.1f}%\n"
    #     f"-------------------------\n")
    #print(winning_candidate_summary)

        # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)