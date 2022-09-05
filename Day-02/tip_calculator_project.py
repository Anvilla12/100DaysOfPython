print('''
========================================================================
                      TIP CALCULATOR 🧮
========================================================================
''')

total = float(input("🧾 What's the total bill? $"))
percentage = int(input("What's the percentage you would like to give?\n(5, 10, 12, 15)\n"))
people = int(input('How many people to split the bill? '))

tip = (total * (percentage / 100))

pay_for_person = round((total + tip) / people, 2)

pay_format = "{:.2f}".format(pay_for_person)

print(f'Each person should pay ${pay_format}')