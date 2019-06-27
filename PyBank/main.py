import os
import csv
csvpath=os.path.join('budget_data.csv')
max_increase = 0
max_decrease = 0
with open(csvpath, newline='') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=',')
     print(csvreader)
     csvheader=next(csvreader)
     #print(f'{csvheader}')
     total_month=0
     profit_loss_list=[]
     for row in csvreader:
        total_month+=1
        profit_loss_list.append(int(row[1]))
     #print(profit_loss_list)
     print('Financial Analysis')
     print('-----------------------------')
     print(f'Total Months: {total_month}')
     print('Financial Analysis',file=open('PyBank_Result.txt','a'))
     print('-----------------------------',file=open('PyBank_Result.txt','a'))
     print(f'Total Months: {total_month}',file=open('PyBank_Result.txt','a'))
     total_amount=sum(profit_loss_list)
     print(f'Total: ${total_amount}')
     print(f'Total: ${total_amount}',file=open('PyBank_Result.txt','a'))
     average_change=round(total_amount/total_month,2)
     print(f'Average Change: ${average_change}')
     print(f'Average Change: ${average_change}',file=open('PyBank_Result.txt','a'))
     max_increase=max(profit_loss_list)
     max_decrease=min(profit_loss_list)
     #print(max_increase)
     #print(max_decrease)
with open(csvpath, newline='') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=',')
     for row in csvreader:
         if row[1]==str(max_increase):
            print(f'Greatest Increase in Profit: {row[0]} (${max_increase})')
            print(f'Greatest Increase in Profit: {row[0]} (${max_increase})',file=open('PyBank_Result.txt','a'))
         elif row[1]==str(max_decrease):
            print(f'Greatest Decrease in Profit: {row[0]} (${max_decrease})')
            print(f'Greatest Decrease in Profit: {row[0]} (${max_decrease})',file=open('PyBank_Result.txt','a'))

