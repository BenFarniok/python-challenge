import os
import csv

winner = []
votenums= []
candidates = []
candidate_list  = []
total_votes = 0
total_vote = 0
vote_list =[]
votes = 0
votes_dict = {}
vote_values= []
percentage = 0
percentage_list = []
winner_score = 0
winner = []
value=0
j=0
percent = []
csvpath = os.path.join('Resources', 'election_data.csv')
with open(csvpath, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
    #get rid of header(already seen)
        
        csv_header = next(csvreader)
    #votes = [row[2]]
        for row in csvreader:
            total_votes += 1
            #make list of candidates/votes
            candidates.append(row[2])
            #make variable to hold candidate names from candidates list
            candidate_name = row[2]
            #create if statement to add name to new list
            if candidate_name not in candidate_list:
                candidate_list.append(candidate_name)
            #on dictionary, make an entry for the candidate, and set it to 0
                votes_dict[candidate_name] = 0
            #add a vote to the candidate in the slot
                votes_dict[candidate_name] = votes_dict[candidate_name] + 1
            #if candidate is already present, add 1 to their entry for each vote     
            elif candidate_name in candidate_list:
                votes_dict[candidate_name] = votes_dict[candidate_name] + 1

           #convert values of dict into a list 
        vote_values = list(votes_dict.values())
        votes = vote_values[j]
        for j in range(len(vote_values)):
            value=int(vote_values[j])
            #find who had the largest amount of votes
            if value > winner_score:
                winner_score=vote_values[j]
                winner = candidate_list[j]
            percentage = (vote_values[j]/total_votes)*100
            if percentage not in percentage_list:
                percentage ="{:.3}%".format(percentage)
                percentage_list.append(percentage)
            j=j+1  
        total_vote = sum(vote_values)

  #* The winner of the election based on popular vote.
#((/total_votes)*100)
print("Election Results")
print("--------------------")
print("Total votes: " + str(total_vote))
print("--------------------")
for j in range (len(candidate_list)):
    print(candidate_list[j] + ":   " + percentage_list[j] + "   " + str(vote_values[j]))
print("=======================")
print("Congratulations " + winner + "!" )
print("=======================")


#print all to txt doc
output_path = os.path.join("output", "results.txt")
f=open(output_path, 'w')
f.write("Election Results"+"\n")
f.write("--------------------"+"\n")
f.write("Total votes: " + str(total_vote)+"\n")
f.write("--------------------"+"\n")
for j in range (len(candidate_list)):
    f.write(candidate_list[j] + ":   " + percentage_list[j] + "   " + str(vote_values[j])+"\n")
f.write("=======================\n")
f.write("Congratulations " + winner + "!" +"\n" )
f.write("======================="+"\n")
