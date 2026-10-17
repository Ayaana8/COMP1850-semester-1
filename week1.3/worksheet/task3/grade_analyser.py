# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file

fileName = input("What is the name of the student file?  ")

# open the file

# read in the data, and for each student calculate their average grade and classification

averages = []
classifications =[]

with open(fileName,"r") as infile:

    data = infile.readlines()
    data = [ line.strip().split(",") for line in data[1:]]

currTotal =0
currClassification =""

currMean=0

for i in range(len(data)):
    for j in range(1,len(data[i])):
        if data[i][j] != "":
            currTotal += int(data[i][j])
    currMean = (currTotal/len(data[i]))

    if currMean >= 70:
        currClassification = "1"
    elif currMean >= 60:
        currClassification= "2:1"
    elif currMean >=50:
        currClassification = "2:2"
    elif currMean >=40:
        currClassification = "3"
    else:
        currClassification= "F"

    averages.append(currMean)
    classifications.append(currClassification)

with open(f"{fileName}_out.csv","w") as outfile:
    for i in range(len(data)):
        outfile.write(f"{data[i][0]}, {averages[i]:.2f}, {classifications[i]} \n")



# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder