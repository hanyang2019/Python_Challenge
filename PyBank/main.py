import os
import csv
csvpath=os.path.join('budget_data.csv')
max_increase = 0
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
     print(total_month)
     total_amount=sum(profit_loss_list)
     print(total_amount)
     average_change=(profit_loss_list[-1]-profit_loss_list[0])/total_month
     print(average_change)
     max_increase=max(profit_loss_list)
     max_decrease=min(profit_loss_list)
     print(max_increase)
     print(max_decrease)
     csvreader=csv.reader(csvfile, delimiter=',')
     for row in csvreader:
         if row[1]==str(max_increase):
            print(row[0])

with open(csvpath, newline='') as csvfile:
     csvreader=csv.reader(csvfile, delimiter=',')
     for row in csvreader:
         if row[1]==str(max_increase):
            print(row[0])
