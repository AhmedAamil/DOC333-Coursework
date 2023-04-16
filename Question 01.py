#START

#Initializing the variables
Patient_Temp = 0
Sum_Temp = 0
TempAvg = 0 #Average temperature for the day in Celsius.
TempAvg2 = 0 #Average temperature for the day in Fahrenheit.
Count_Read = 1 #Number of readings in particular day.

#Get 10 temperature reading inputs from the patient.
print ("\nEnter the Patient temperature readings for the Day")
while (Count_Read <= 10):
    Patient_Temp = float(input(f"Enter temperature reading {Count_Read} in Celsius: "))
    Sum_Temp += Patient_Temp #Adding the total temperature readings taken from the patient
    Count_Read += 1

#Calculate the average temperature and display the result.
TempAvg = Sum_Temp/10
print ("The average temperature for the day in Celsius is ", TempAvg,'°')

#Convert the average temperature to Fahrenheit display the result.
TempAvg2 = (TempAvg * 9/5) + 32
print ("The average temperature for the day in Fahrenheit is ", round(TempAvg2, 2), '°')

#If the average temperature value is between 97.0 Fahrenheit and 99.0 Fahrenheit then display "Your body temperature is normal…".
if TempAvg2 >= 97.00 and TempAvg2 <= 99.00 :
    print ("\nYour body temperature is normal…")

#If the average is more than 100.4 Fahrenheit then display "You have a fever caused by an infection or illness…".
elif TempAvg2 >= 100.4 :
    print ("\nYou have a fever caused by an infection or illness…")

else:
    print ("\nUnconvincing average body temperature.")
    
#STOP
    
    
   
    
    


    

    
    
