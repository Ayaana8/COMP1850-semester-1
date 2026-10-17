# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

averages = {}

with open("student_data.csv","r") as infile:

    data = infile.readlines()
    data = [ line.strip().split(",") for line in data[1:]]

for i in range(len(data)):
    averages[data[i][1]] = ((int(data[i][2])+int(data[i][3])+int(data[i][4])) / 3)

with open("report.txt","w") as outfile:
    for i in averages.keys():
        outfile.write(f"{i}: {averages[i]}\n")


# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
