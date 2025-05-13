#❗If we want the photo to be free, we can develop the codes as follows.
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))  # Height information is obtained from the user.
bill = 0  # A bill variable was created for payment.

if height >= 120:  # Check height for first condition.
    print("You can ride the rollercoaster")  # If the first condition query is true, it will print this.
    age = int(input("What is your age? "))  # Age information is obtained from the user.

    if age <= 12:  # Check age for condition1.
        bill = 5
        print("Child tickets are $5.")  # If the condition1 query is true, it will print this.
    elif age <= 18:
        bill = 7  # Check age for condition2.
        print("Youth tickets are $7.")  # If the condition2 query is true, it will print this.
    elif 45 <= age <= 55:  # Check age for midlife crisis
        print("Everything is going to be ok. Have a free ride on us!")  
        wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No. ")
        if wants_photo == "y":
            print("Photo is also free for you!")
        print("Your final bill is $0")  # No charge for ticket or photo
        exit()  # Programı burada bitiriyoruz çünkü fatura zaten 0.
    else:
        bill = 12
        print("Adult tickets are $12.")  # If the condition2 query is false, it will print this.

    wants_photo = input("Do you want to have a photo taken? Type y for Yes and n for No. ")
    if wants_photo == "y":
        bill += 3  # Add $3 to their bill. (bill = bill + 3)

    print(f"Your final bill is ${bill}")  # Final bill calculated
else:
    print("Sorry, you have to grow taller before you can ride.")  # If the first condition query is false, it will print this.
