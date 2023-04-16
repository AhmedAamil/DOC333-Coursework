#START

#Initializing the variables.
Year = 0
Month = 0
Day = 0
Total_Days = 0

#Get Year input
Year = int(input("Insert the year: "))
#Get Month input
Month = int(input("Insert the Month: "))
#Get Date input
Day = int(input("Insert the Date: "))

#Assigning the Total days in a month.

#If Month contains 31 days,
if Month == 1 or Month == 3 or Month == 5 or Month == 7 or Month == 8 or Month == 10 or Month == 12 :
    Total_Days = 31

#If Month contains 30 days,
elif Month == 4 or Month == 6 or Month == 9 or Month == 11 :
    Total_Days = 30

#If the Year is a leap year,
#A leap year is divisible by four and the century year is completely divisible by 400 would that be a leap year.
elif Year % 4 == 0 and Year % 100!= 0 or Year % 400 == 0 :
    Total_Days = 29

else:
    Total_Days = 28

#Conditions for Valid or Invalid date output and printing the next Incremented date if the user input date is Valid.
if Year<1 or Year>9999 :
    print ("\nDate is invalid")
    print ("Check the input range")
    
elif Month<1 or Month>12 :
    print ("\nDate is invalid")
    print ("Check the input range")

elif Day<1 or Day> Total_Days :
    print ("\nDate is invalid")
    print ("Check the input range")

#Display the Next date (Incrementing the date),
elif Day == 31 and Month==12 :
    Day = 1
    Month = 1
    Year += 1
    print ("\nDate is Valid")
    print ("The next (Incremented) date is (dd / mm / yy) : ", Day,"/",Month,"/",Year)

elif Month !=12 and Day == Total_Days :
    Day = 1
    Month += 1
    print ("\nDate is Valid")
    print ("The next (Incremented) date is (dd / mm / yy) : ", Day,"/",Month,"/",Year)

else:
    Day +=1
    print ("\nDate is Valid")
    print ("The next (Incremented) date is (dd / mm / yy) : ", Day,"/",Month,"/",Year)

#END








