# **BMI Calculator with Interpretations**

# Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

#- If the bmi is under 18.5 (not including), print out "underweight"
#- If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
#- If the bmi is 25 (including) or over, print out "overweight" 

#BMI Calculator

weight = 85
height = 1.85

bmi = weight / (height ** 2)

# Write your code below 👇

if bmi >=25 :
    print("overweight")
elif bmi >=18.5:
    print("normal weight")
else:
    print("underweight")
