# Instructions
# =======================================================================
# Write a program that calculates the Body Mass Index (BMI)
# from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height.
# e.g. If a tall person and a short person both weigh the same amount,
# the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the
# square of their height (in m):

# BMI = weight(Kg)/ height^2(M)
# ========================================================================

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight / (height * height))

if bmi < 18.5:
    info = "are underweight"
elif bmi < 25:
    info = "have a normal weight"
elif bmi < 30:
    info = "are slightly overweight"
elif bmi < 35:
    info = "are obese"
else:
    info = "are clinical obese"

print(f"Your BMI is {bmi}, you {info}.")