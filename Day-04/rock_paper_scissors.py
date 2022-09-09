from multiprocessing.connection import wait
import random
import time
print('''
✌ ✊ 🖐=============================================================================🖐  ✊ ✌
                                 Rock, Paper & Scissors Game                                  
✌ ✊ 🖐=============================================================================🖐  ✊ ✌
''')

player_1 = int(input('Choose "1" for rock ✊, "2" for Paper 🖐 or "3" for scissors✌'    ))

choices = ["Rock ✊", "Paper 🖐", "Scissors ✌"]

p1_choice = choices[player_1 - 1]

print(f"You choose {p1_choice}")
npc = random.choice(choices)

if npc ==  p1_choice:
    result = "TIE"
elif npc == "Rock ✊" and p1_choice == "Paper 🖐":
    result = "You Won!"
elif npc == "Rock ✊" and p1_choice == "Scissors ✌":
    result = "You Loose D:"
elif npc == "Paper 🖐" and p1_choice == "Scissors ✌":
    result = "You Won!"
elif npc == "Paper 🖐" and p1_choice == "Rock ✊":
    result = "You Loose D:"
elif npc == "Scissors ✌" and p1_choice == "Rock ✊":
    result = "You Won!"
else:
    result = "You Loose D:"

print("Ready...?")
time.sleep(0.7)
print("3")
time.sleep(0.7)
print("2")
time.sleep(0.7)
print("1")
time.sleep(0.3)
print(f'''
         YOUR CHOICE     |       PC CHOICE

          {p1_choice}                 {npc}

                     {result}
''')









