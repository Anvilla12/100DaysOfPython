# Instructions
# ===================================================
# Write a program that works out whether
# if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# ===================================================
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆
#Write your code below this line 👇

if number % 2 == 0:
    even_or_odd = "even"
else:
    even_or_odd = "odd"

print(f'This is an {even_or_odd} number.')
