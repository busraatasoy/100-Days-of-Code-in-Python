print("Welcome to the tip calculator!")
bill = float(input("What was the total bill $?\n ")) #Total invoice information is requested.
tip = int(input("What percentage tip would you like to give? (10, 12, 15) \n")) #You will be asked to enter the tip amount.
people = int(input("How many people to split the bill?\n"))  #How many people will pay the bill?
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")  #The amount per person is printed.
