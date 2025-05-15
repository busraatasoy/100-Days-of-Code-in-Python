'''**Scenario:**

You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

- Your program should print each number from 1 to 100 in turn and include number 100.
- But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
- When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
- And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"
    
    e.g. it might start off like this:
    `1. 1
    2. 2
    3. Fizz
    4. 4
    5. Buzz
    6. Fizz
    7. 7
    8. 8
    9. Fizz
    10. Buzz
    11. 11
    12. Fizz
    13. 13
    14. 14
    15. FizzBuzz`
    
    ...etc '''

#FizzBuzz Game:

for number in range(1, 101):                  # Loop from 1 to 100
    if number % 3 ==0 and number % 5 ==0:     #divisible by both 3 and 5 
        print("FizzBuzz")
    elif number % 3 == 0:                     #divisible by 3 
        print("Fizz")
    elif number % 5 == 0:                     #divisible by 5 
        print ("Buzz")
    else:
        print(number)                  # If none of the conditions are met, print it.
        
     















