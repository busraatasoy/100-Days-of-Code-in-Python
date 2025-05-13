#**Scenario:** 

#- **Determines whether the number is odd or even.**

print("Welcome to the numbercontroller!")
number_to_check = int(input("What is the number you want to check? "))   #Numberinformation is obtained from the user.

if number_to_check % 2 == 0:       #When the number entered by the user is divided by 2, is the remainder 0?
   print("This number is Even!")    #If the query is true, it will print this.
else:
   print("This number is Odd!")     #If the query is false, it will print this.
