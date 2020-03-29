import os
import csv

# set variables
change = []
increase = []
decrease = []
months = []
change_total = 0
month_count = []
difference = []
change2= []
changediff = []
month1=[]
month2=[]
minimum= 999999999
maximum = 0
minimum_month= ""
maximum_month=""
csvpath = os.path.join('..' ,'Resources', 'budget_data.csv')
#create csv reader
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #get rid of header(already seen)
    csv_header = next(csvreader)
    j=0     
    for row in csvreader:
        #make a list of entries in position 1 for month count
        months.append(row[0])
        #add those entries
        #make a list of entries in position 2
        change.append(float(row[1]))
        change2
        #change2.append(row[1])
        #add them together
        if j>0:

            month1=change[j]
            month2=change[j-1]
        
        #create another list with the changes between datapoints each month
        #set variables for the months
        #create a second list that is the same, but without the first entry
        #change2=change[1:]
            changediff.append(month1-month2)
            if month1-month2 < minimum:
                minimum=month1-month2
                minimum_month = row[0]
            if month1-month2 > maximum:
                maximum=month1-month2
                maximum_month = row[0]
        j=j+1
change_total = sum(change)
average_change=sum(changediff)/(len(changediff))       
month_count = len(months)

print("Financial Analysis")
print("-------------------------")
print(f"Total Months: " + str(month_count))
print(f"Total: " + str(change_total))
print(f"Average Change: " + str(average_change))
print(f"Greatest Increase in Profits: " + str(maximum_month) + " "+ str(maximum))
print(f"Greatest Decrease in Profits: " + str(minimum_month) + " "+ str(minimum))

output_path = os.path.join("output", "results.txt")
f=open(output_path, 'w')
f.write("Financial Analysis\n")
f.write("-------------------------\n")
f.write(f"Total Months: " + str(month_count)+"\n")
f.write(f"Total: " + str(change_total)+"\n")
f.write(f"Average Change: " + str(average_change)+"\n")
f.write(f"Greatest Increase in Profits: " + str(maximum_month) + " "+ str(maximum)+"\n")
f.write(f"Greatest Decrease in Profits: " + str(minimum_month) + " "+ str(minimum)+ "\n")