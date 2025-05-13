if condition:   # Check the first condition
   if another condition: # Check the second condition
       do this       # Execute this if both conditions are true
   else:
       do this      # Execute this if the second condition is false
else:
   do this          # Execute this if the first condition is false      

#**Scenario:** 

#- **The roller coaster company allows tickets to be sold to people who are 120 cm tall and above.**
#- **Additionally, tickets for people 18 and under are $7, and tickets for people over 18 are $12.**

#Sample 2:

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  #Height information is obtained from the user.

if height >= 120:                                   # Check height for first condition.
   print("You can ride the rollercoaster")         #If the first condition query is true, it will print this.
   age = int(input("What is your age? "))           #Age information is obtained from the user.
   if age  <= 18 :                                  # Check age for second condition.
       print("Please pay $7 for the ticket.")       #If the second condition query is true, it will print this.
   else:
       print("Please pay $12 for the ticket.")     #If the second condition query is false, it will print this.
else:
   print("Sorry you have to grow taller before you can ride.") #If the first condition query is false, it will print this.
   
