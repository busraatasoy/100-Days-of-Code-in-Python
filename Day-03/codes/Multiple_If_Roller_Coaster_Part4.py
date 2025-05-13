if condition1:   # Check the condition1
   do A          # If condition1 is true, do A
if condition2:   # Check the condition2
   do B          # If condition2 is true, do B
if condition3:   # Check the condition3
   do C          # If condition3 is true, do B    

# **Scenario:**  

# - **The roller coaster company allows tickets to be sold to people who are 120 cm tall and above.**
# - **Additionally, tickets for people 12 and under are $5, between 12 and 18 are $7, and tickets for people over 18 are $12.**
# - **An additional $3 fee is charged for those who want to take photos.**

#Sample 4:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  #Height information is obtained from the user.
bill = 0                            #A bill variable was created for payment.

if height >= 120:                                   # Check height for first condition.
   print("You can ride the rollercoaster")         #If the first condition query is true, it will print this.
   age = int(input("What is your age? "))           #Age information is obtained from the user.
   if age  <= 12 :                                  # Check age for condition1.
       bill = 5
       print("Child tickets are $5.")       #If the condition1 query is true, it will print this.
   elif age  <= 18 :
       bill = 7                                 # Check age for condition2.
       print("Youth tickets are $7.")       #If the condition2 query is true, it will print this.
   else:
       bill = 12
       print("Adult tickets are $12.")     #If the condition2 query is false, it will print this.
   wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No. ")
   if wants_photo == "y":
       bill +=3            #Add $3 to their bill. (bill = bill + 3)
   
   print(f"Your final bill is {bill}")     #Final bill calculated
else:
   print("Sorry you have to grow taller before you can ride.") #If the first condition query is false, it will print this.
   
