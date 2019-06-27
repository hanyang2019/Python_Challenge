import os
import csv
csvpath=os.path.join('election_data.csv')
total_vote=0
candidate_list=[]
count_list=[]
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        total_vote+=1
        if row[-1] not in candidate_list:
            candidate_list.append(row[-1])
    print('Election Results')
    print('------------------------')
    print(f'Total Votes: {total_vote}')
    print('------------------------')
    print('Election Results',file=open('PyPoll_Result.txt','a'))
    print('------------------------',file=open('PyPoll_Result.txt','a'))
    print(f'Total Votes: {total_vote}',file=open('PyPoll_Result.txt','a'))
    print('------------------------',file=open('PyPoll_Result.txt','a'))
    #print(candidate_list)
count_k=0
count_c=0
count_l=0
count_o=0
with open(csvpath, newline='') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        if row[-1]==candidate_list[0]:
            count_k+=1
        elif row[-1]==candidate_list[1]:
            count_c+=1
        elif row[-1]==candidate_list[2]:
            count_l+=1
        elif row[-1]==candidate_list[3]:
            count_o+=1
    count_list.append(count_k)
    count_list.append(count_c)
    count_list.append(count_l)
    count_list.append(count_o)
    percentage_k=round((count_k/total_vote)*100)
    percentage_c=round((count_c/total_vote)*100)
    percentage_l=round((count_l/total_vote)*100)
    percentage_o=round((count_o/total_vote)*100)
    print(f'{candidate_list[0]}: {percentage_k}.000% ({count_k})')
    print(f'{candidate_list[1]}: {percentage_c}.000% ({count_c})')
    print(f'{candidate_list[2]}: {percentage_l}.000% ({count_l})')
    print(f'{candidate_list[3]}: {percentage_o}.000% ({count_o})')
    print('------------------------')
    #print(count_list)
    print(f'Winner: {candidate_list[count_list.index(max(count_list))]}',file=open('PyPoll_Result.txt','a'))
    print('------------------------',file=open('PyPoll_Result.txt','a'))
    print(f'{candidate_list[0]}: {percentage_k}.000% ({count_k})',file=open('PyPoll_Result.txt','a'))
    print(f'{candidate_list[1]}: {percentage_c}.000% ({count_c})',file=open('PyPoll_Result.txt','a'))
    print(f'{candidate_list[2]}: {percentage_l}.000% ({count_l})',file=open('PyPoll_Result.txt','a'))
    print(f'{candidate_list[3]}: {percentage_o}.000% ({count_o})',file=open('PyPoll_Result.txt','a'))
    print('------------------------',file=open('PyPoll_Result.txt','a'))
    #print(count_list)
    print(f'Winner: {candidate_list[count_list.index(max(count_list))]}',file=open('PyPoll_Result.txt','a'))
    print('------------------------',file=open('PyPoll_Result.txt','a'))
     