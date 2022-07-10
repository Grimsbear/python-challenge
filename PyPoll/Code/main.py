#import dependendenices 
import os
import csv

# route to resources
polldata = os.path.join("..","Resources","election_data.csv")

# open csv file
with open(polldata) as csv_file:
    
    csvreader = csv.reader(csv_file)
    #print(csvreader)
    csv_header = next(csv_file)

    count = 0
    Candidate = []
    CandidateVote1 = 0
    CandidateVote2 = 0
    CandidateVote3 = 0

    for row in csvreader:

        count = count + 1

        if row[2] not in Candidate:
            Candidate.append(row[2])

        if row[2] == Candidate[0]:
            CandidateVote1 = CandidateVote1 + 1
        elif row[2] == Candidate[1]:
            CandidateVote2 = CandidateVote2 + 1
        else:
            CandidateVote3 = CandidateVote3 + 1
        
    P1 = "{:.2%}".format(CandidateVote1/count)
    P2 = "{:.2%}".format(CandidateVote2/count)
    P3 = "{:.2%}".format(CandidateVote3/count)
        
    print("Election Results")
    print("----------------------")
    print(f"Total Votes : {count}")
    print("----------------------")
    print(f"{Candidate[0]} : {P1} ({CandidateVote1})")
    print(f"{Candidate[1]} : {P2} ({CandidateVote2})")
    print(f"{Candidate[2]} : {P3} ({CandidateVote3})")
    print("----------------------")

    if (CandidateVote1/count) >= .5:

        print(f"{Candidate[0]} is the Winner")
    
    elif (CandidateVote2/count) >= .5:

        print(f"{Candidate[1]} is the Winner")

    else:

        print(f"{Candidate[2]} is the Winner")
    