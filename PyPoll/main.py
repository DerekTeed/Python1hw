# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import pandas as pd
import numpy as np
# Module for reading CSV files
import csv

sumVoterId = 0

df = pd.read_csv("PyPoll.csv")
#print(df)

# listOfCandidates = df["Candidate"].unique()
# listOfCandidates



candidate_group = df.groupby(["Candidate"])
candidate_group = candidate_group.count()

#print(candidate_group)
newList = candidate_group[["Voter ID"]]
#print(newList)

sum3 = candidate_group[["Voter ID"]].sum()
#print(sum3)

#I need a row of sum2 to divide from
calc = (newList/sum3)*100
calc = calc.sort_values("Voter ID")

newList = max(["Voter ID"])
#print(newList)
# #print(newList)

calc = calc["Voter ID"].astype(float).map("{:.3f}%".format).sort_values(ascending=False)

#print(calc)

#dont show
# summary_df = pd.DataFrame({
#                          "Candidate Votes": newList,
#                              "Percentage of Votes ": calc
                             
                            
#                             })
# print(summary_df)
# summary_df1 = pd.DataFrame({ "Total Voter Count": [sum3]
                         
#                             })
#print(summary_df1)



print(f'Total Number of Votes: {sum3}')
print(f'Group of Candidate: {newList}')
print(f"Candidates by Vote Percentage: {calc}")
print(f"Top Candidate: Khan")

#summary_df.to_csv("outputPracticelist.csv", index=False)
##summary_df1.to_csv("outputPracticelist.csv", index=False)