# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import pandas as pd
import numpy as np
# Module for reading CSV files
import csv

df = pd.read_csv("excelBank.csv")

print(df)
something1 = df.sum(axis = 1)

print(df['Profit/Losses'])
profitChange = df['Profit/Losses']
profitChange1 = profitChange.diff().values
print("new Hope")

gtIncrease = max(profitChange1[1:])
gtDecrease = min(profitChange1[1:])

print(max(profitChange1))
newhope1 = max(profitChange1)
print(type(newhope1))

totalProfit = sum(something1)
csvpath = os.path.join('excelBank.csv')
    

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    data = list(csvreader)
    
    row_count = len(data)
    rowcount = row_count - 1
    for line in csvreader:
        print("printing line 1")
        print(line[1])
    


    print(f"Number of Months: {rowcount} months")
    print(f"Total Profits over time: ${totalProfit}")
    avgProfit = round(totalProfit/rowcount, 2)
    print(f"Average Profits: ${avgProfit}")
    print(f"Greatest Increase in Profits: ${gtIncrease}")
    print(f"Greatest Decrease in Profits: ${gtDecrease}")

# with open(csvpath, 'w') as wf:
#     for line in wf:
#         wf.write(line)
#         print("printing line 1")



summary_df = pd.DataFrame({ "Total Months": [rowcount],
                            "Total Profits": [totalProfit],
                              "Average profit": avgProfit,
                              "Greatest Increase": gtIncrease,
                              "Greatest Decrease": gtDecrease})
print(summary_df)

summary_df.to_csv("outputPracticelist.csv", index=False)
#print(summary_df,file=open("something.txt","w"))
