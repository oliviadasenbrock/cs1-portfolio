#Paycheck.py

"""This program informs the employee what their paycheck will be."""


hours = float(input("How many hours did you work this week?"))

hourly_rate = float(input("What is your hour rate?"))

product1 = hours * hourly_rate



if hours < 0:
    print("Error: You cannot enter a negative number.")
    
if hourly_rate < 0:
    print("Error: You cannot enter a negative number.")
    
if hours > 0:
    if hourly_rate > 0:


        if hours <= 40:
            print("Your paycheck before deductions will be: $", product1)


        if hours > 40:
            subtraction1 = hours - 40
        

            product2 = hourly_rate * 1.5
        
         
            addition1 = subtraction1 * product2 + 40 * hourly_rate
            
            print("Your paycheck before deductions will be: $", addition1)
    