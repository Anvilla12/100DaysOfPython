from multiprocessing.connection import wait
import random
import time
print('''
β β π=============================================================================π  β β
                                 Rock, Paper & Scissors Game                                  
β β π=============================================================================π  β β
''')

player_1 = int(input('Choose "1" for rock β, "2" for Paper π or "3" for scissorsβ'    ))

choices = ["Rock β", "Paper π", "Scissors β"]

p1_choice = choices[player_1 - 1]

print(f"You choose {p1_choice}")
npc = random.choice(choices)

if npc ==  p1_choice:
    result = "TIE"
elif npc == "Rock β" and p1_choice == "Paper π":
    result = "You Won!"
elif npc == "Rock β" and p1_choice == "Scissors β":
    result = "You Loose D:"
elif npc == "Paper π" and p1_choice == "Scissors β":
    result = "You Won!"
elif npc == "Paper π" and p1_choice == "Rock β":
    result = "You Loose D:"
elif npc == "Scissors β" and p1_choice == "Rock β":
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









