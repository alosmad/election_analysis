import csv
import os


file_to_load = os.path.join('Resources','election_results.csv')
file_to_save = os.path.join('analysis','election_analysis.txt')

total_votes = 0

candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) *100
        #print(f'{candidate_name}: received{vote_percentage}% of the vote.')
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
        print(f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")
    
    winning_candidate_summary = (
        f' ---------------------\n'
        f"winner : {winning_candidate}\n"
        f'winning vote count: {winning_count:,}\n'
        f'winning percentage: {winning_percentage:.1f}%\n'
        f'----------------------\n')
    print(winning_candidate_summary)

#print(candidate_options)
#print(candidate_votes)
#print(total_votes)
#print(winning_candidate)
#print(winning_count)
#print(winning_percentage)



