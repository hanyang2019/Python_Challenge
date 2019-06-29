import os
import csv
import datetime
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
input_csvpath=os.path.join('employee_data.csv')
output_csvpath=os.path.join('new_employee_data.csv')
with open(input_csvpath, newline='') as in_csv, open(output_csvpath, 'w', newline='') as out_csv:
    csvreader=csv.reader(in_csv, delimiter=',')
    csvwriter=csv.writer(out_csv, delimiter=',')
    csvwriter.writerow(['Emp ID','First Name','Last Name','DOB','SSN','State'])
    csv_header=next(csvreader)
    for row in csvreader:
        row[1]=row[1].split(' ')
        row.append(row[1][0])
        row.append(row[1][1])
        row[2]=datetime.datetime.strptime(row[2],'%Y-%m-%d').strftime('%m-%d-%Y')
        row.append(row[2])
        row[3]=row[3].split('-')
        row.append(row[3][2])
        row[8]='***-**-'+row[8]
        row[4]=us_state_abbrev[row[4]]
        row.append(row[4])
        row.remove(row[1])
        row.remove(row[1])
        row.remove(row[1])
        row.remove(row[1])

        csvwriter.writerow(row)