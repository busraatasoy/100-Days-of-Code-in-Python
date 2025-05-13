if condition1:   # Check the condition1
   do A       # If condition1 is true, do A
elif condition2:   # Check the condition2
   do B    # If condition2 is true, do B
else:
   do this          # If all conditions are false, do this  

#**Scenario:**  

#- **The roller coaster company allows tickets to be sold to people who are 120 cm tall and above.**
#- **Additionally, tickets for people 12 and under are $5, between 12 and 18 are $7, and tickets for people over 18 are $12.**

#Sample 3:   
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  #Height information is obtained from the user.

if height >= 120:                                   # Check height for first condition.
   print("You can ride the rollercoaster")         #If the first condition query is true, it will print this.
   age = int(input("What is your age? "))           #Age information is obtained from the user.
   if age  <= 12 :                                  # Check age for condition1.
       print("Please pay $5 for the ticket.")       #If the condition1 query is true, it will print this.
  elif age  <= 18 :                                 # Check age for condition2.
       print("Please pay $7 for the ticket.")       #If the condition2 query is true, it will print this.
  else:
       print("Please pay $12 for the ticket.")     #If the condition2 query is false, it will print this.
else:
   print("Sorry you have to grow taller before you can ride.") #If the first condition query is false, it will print this.
   
