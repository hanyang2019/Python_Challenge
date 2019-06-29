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
     cur_profit_loss_list=[]
     pre_profit_loss_list=[]
     date_list=[]
     monthly_change_list=[]
     for row in csvreader:
        total_month+=1
        profit_loss_list.append(int(row[1]))
# change=current month - previous month create two lists representing each respectively
        cur_profit_loss_list.append(int(row[1]))
        pre_profit_loss_list.append(int(row[1]))
        date_list.append(row[0])
     cur_profit_loss_list.remove(cur_profit_loss_list[0]) # remove the first month due to no previous month
     pre_profit_loss_list.remove(pre_profit_loss_list[-1]) # remove the last month cuz the sencond last month is the last one
     date_list.remove(date_list[0]) # remove the first month since change starts from the 2nd month
     for i in range(total_month-1): # change occurs 85 times since it's the differnece between 2 months
        monthly_change_list.append(cur_profit_loss_list[i]-pre_profit_loss_list[i])
   
     print('Financial Analysis')
     print('-----------------------------')
     print(f'Total Months: {total_month}')
     print('Financial Analysis',file=open('PyBank_Result.txt','a'))
     print('-----------------------------',file=open('PyBank_Result.txt','a'))
     print(f'Total Months: {total_month}',file=open('PyBank_Result.txt','a'))
     total_amount=sum(profit_loss_list)
     print(f'Total: ${total_amount}')
     print(f'Total: ${total_amount}',file=open('PyBank_Result.txt','a'))
     average_change=round((sum(monthly_change_list)/(total_month-1)),2)
     print(f'Average Change: ${average_change}')
     print(f'Average Change: ${average_change}',file=open('PyBank_Result.txt','a'))
    
     max_increase=max(monthly_change_list)
     max_decrease=min(monthly_change_list)

     print(f'Greatest Increase in Profit: {date_list[monthly_change_list.index(max_increase)]} (${max_increase})')
     print(f'Greatest Increase in Profit: {date_list[monthly_change_list.index(max_increase)]} (${max_increase})',file=open('PyBank_Result.txt','a'))
     print(f'Greatest Decrease in Profit: {date_list[monthly_change_list.index(max_decrease)]} (${max_decrease})')
     print(f'Greatest Decrease in Profit: {date_list[monthly_change_list.index(max_decrease)]} (${max_decrease})',file=open('PyBank_Result.txt','a'))

