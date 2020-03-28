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




# Remove unecessary columns from the DataFrame and save the new DataFrame
# Only keep: "isbn", "original_publication_year", "original_title", "authors",
# "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5"
# reduced_df = books_df[["isbn", "original_publication_year", "original_title", "authors",
#                        "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5"]]
# reduced_df.head()            
# #Need to create a new columns  
# renamed_df = reduced_df.rename(columns={"isbn": "ISBN",
#                                         "original_title": "Original Title",
#                                         "original_publication_year": "Publication Year",
#                                         "authors": "Authors",
#                                         "ratings_1": "One Star Reviews",
#                                         "ratings_2": "Two Star Reviews",
#                                         "ratings_3": "Three Star Reviews",
#                                         "ratings_4": "Four Star Reviews",
#                                         "ratings_5": "Five Star Reviews", })
#  # Push the remade DataFrame to a new CSV file
# renamed_df.to_csv("Output/books_clean.csv",
#                   encoding="utf-8", index=False, header=True)
#     wins = int(csvreader[1])
#     # losses = int(csvreader[2])
#     # draws = int(csvreader[3])
#     print(wins)
#     print(f"WIN PERCENT: {str(wins)}")
#     # Total matches can be found by adding wins, losses, and draws together
#     # total_matches = wins + losses + draws
#
    # # Win percent can be found by dividing the the total wins by the total matches and multiplying by 100
    # win_percent = (wins / total_matches) * 100

    # # Loss percent can be found by dividing the total losses by the total matches and multiplying by 100
    # loss_percent = (losses / total_matches) * 100

    # # Draw percent can be found by dividing the total draws by the total matches and multiplying by 100
    # draw_percent = (draws / total_matches) * 100

    # If the loss percentage is over 50, type_of_wrestler is "Jobber". Otherwise it is "Superstar".
    # if loss_percent > 50:
    #     type_of_wrestler = "Jobber"
    # else:
    #     type_of_wrestler = "Superstar"

    # Print out the wrestler's name and their percentage stats
    # print(f"Stats for {name1}")
    # print(f"WIN PERCENT: {str(win_percent)}")
    # print(f"LOSS PERCENT: {str(loss_percent)}")
    # print(f"DRAW PERCENT: {str(draw_percent)}")
    # print(f"{name} is a {type_of_wrestler}")
   
    
   
   
    


        
        
    #     if row[0].upper() == video.upper():
    #         print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

    #         # BONUS: Set variable to confirm we have found the video
    #         found = True

    #         # BONUS: Stop at first results to avoid duplicates
    #         break
    #    # else:
       #     found = false

    # If the video is nethe hunter
    # ver found, alert the user
    # if found is False:
    #     print("Sorry about this, we don't seem to have what you are looking for!")

    # print(csvreader)

    # # Read the header row first (skip this step if there is now header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    # for row in csvreader:
    #     print(row)





#   import csv
# import os

# # Three Lists
# indexes = [1, 2, 3, 4]
# employees = ["Michael", "Dwight", "Meredith", "Kelly"]
# department = ["Boss", "Sales", "Sales", "HR"]

# # Zip all three lists together into tuples
# roster = zip(indexes, employees, department)

# # save the output file path
# output_file = os.path.join("output.csv")

# # open the output file, create a header row, and then write the zipped object to the csv
# with open(output_file, "w", newline="") as datafile:
#     writer = csv.writer(datafile)

#     writer.writerow(["Index", "Employee", "Department"])

#     writer.writerows(roster)