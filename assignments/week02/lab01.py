"""
BMI Calculator (20 points)

Write a program that:

Asks for weight in kilograms
Asks for height in meters
Calculates BMI using formula: BMI = weight / (height²)
Displays BMI with 1 decimal place
Shows BMI category based on the ranges below

BMI Categories:

Below 18.5: Underweight
18.5 - 24.9: Normal weight
25.0 - 29.9: Overweight
30.0 and above: Obese

"""

weight = float(input("Enter your weight(KG) : "))
height = float(input("Enter yout height(M) : "))
BMI = weight / height ** 2

if BMI < 18.5:
    print("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Normal Weight")
elif BMI >= 25.0 and BMI <= 29.9:
    print("Overweigth")
else:
    print("Obese")

print("Your BMI = ",BMI)