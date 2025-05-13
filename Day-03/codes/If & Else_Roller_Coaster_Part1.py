if condition:   #The query condition is written here.
   do this      #If the condition is true, this action is executed.
else:
   do this      #If the condition is false, this action is executed.

#**Scenario:** 
#- **The roller coaster company allows tickets to be sold to people who are 120 cm tall and above.**

#Sample 1:    
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  #Height information is obtained from the user.

if height >= 120:                                   #Is the user's height greater than or equal to 120?
   print("You can ride the rollercoaster")          #If the query is true, it will print this.
else:
   print("Sorry you have to grow taller before you can ride.") #If the query is false, it will print this.
