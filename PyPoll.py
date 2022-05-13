# Data we need to retrieve:
## 1 - Total number of votes cast
## 2 - Complete list of candidates who recieved votes
## 3 - The percentage of votes each candidate won
## 4 - The total number of votes each candidate won
## 5 - The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "Election_analysis.txt")

#initializing total votes to zero
total_votes = 0

#initializing candidate list
candidate_options = []

#initializing dictionary of candidate votes
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #creates a file reader variable
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    for row in file_reader:
        #Increments total votes and initializes candidate names var as the candidate names column
        total_votes += 1
        candidate_name = row[2]
        
        #Checks if it's a new candidate, adds to candidate list and makes new key in votes dict
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        #increases the number of vote per candidate
        candidate_votes[candidate_name]+=1

    #defining our output file
    with open(file_to_save, 'w') as txt_file:
        
        #Creating a formatted header for our output file
        election_results = (
            f"\nElection Results:\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n")

        #printing the header to the console
        print(election_results, end="")

        #saving the header to a text file
        txt_file.write(election_results)
        
        #Win conditions and win tracker
        winning_candidate = ""
        winning_votes = 0
        winning_votes_percent = 0

        #Eye-candy layout for my own personal formatting practice
        #header_display = (
        #    f"=====[ALL CANDIDATES]=====\n"
        #    f" NAME:  PERCENT%  (VOTES)\n"
        #    f"--------------------------\n"
        #)

        #printing the neat header I made to make sure it works
        #print(header_display)

            #calculating the percent of votes by candidate
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]
            vote_percentage = float(votes) / float(total_votes) * 100

            #winner logic
            if votes > winning_votes and vote_percentage > winning_votes_percent:
                winning_candidate = candidate_name
                winning_votes = votes
                winning_votes_percent = vote_percentage
        
            #creating a variable to store candidate results
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            #printing the results to the console
            print(candidate_results)

            #saving the results to a text file
            txt_file.write(candidate_results)

        #Defining the display of the winner's data
        winner_display = (
            f"-------------------------\n"
            f"Winning Candidate: {winning_candidate}\n"
            f"Winning Vote Count: {winning_votes:,.0f}\n"
            f"Winning Percent of Vote: {winning_votes_percent:.1f}%\n"
            f"-------------------------\n"
        )

        #Printing the winning candidate:
        print(winner_display)

        #writing the winning display to our output
        txt_file.write(winner_display)

###### -- LEGACY CODE BELOW -- ######

            #Printing all candidate info
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        