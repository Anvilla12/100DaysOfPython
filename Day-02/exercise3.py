# Instructions
# =======================================================================
# Create a program using maths and f-Strings that tells us 
# how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our
# time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.
# =======================================================================
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_years = 90
total_months = total_years * 12
total_weeks = total_years * 52
total_days = total_years * 365

years_left = total_years - int(age)
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365


print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")