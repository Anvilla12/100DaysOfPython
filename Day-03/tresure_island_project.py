print('''
===========================================================================
                   🏝️ Tresure Island Game 👑
===========================================================================

    Welcome to tresure island!

    Your goal is to find the tresure without dying

''')

print('📕 1. bla,bla,bla... ')


step_1 = input("Where we go? right or left?\n ")
if step_1 != "left":
    print("💀 You died, GAME OVER... ")
else:
    print('📕 2.  bla,bla,bla... ')
    step_2 = input("What we do? swim or wait?\n ")
    if step_2 != "wait":
        print("💀 You died, GAME OVER... ")
    else:
        print('📕 3.  bla,bla,bla... ')
        step_3 = input("Which door should be opened? red, yellow or blue?\n ")
        if step_3 == "yellow":
            print('📕 4.  bla,bla,bla... ')
            print('🤴 You have found the tresure... YOU WON!!!')
        else:
            if step_3 == "red":
                print('📕 5.  bla,bla,bla... ')
                print("💀 You died, GAME OVER... ")
            else:
                print('📕 6.  bla,bla,bla... ')
                print("💀 You died, GAME OVER... ")




