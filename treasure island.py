print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the treasure island Your mission is to find the treasure !")
way = input("There is two way which one you choose - Right or Left ?---> ").lower()
if way == "left":
    river = input("There is a river which one you choose - Wait or Swim ?--->").lower()
    river.lower()
    if river == "wait":
        gate = input("There is three colors of doors which one you want to choose - blue,red or yellow ?---> ").lower()
        if gate == "red":
            print("Burned by fire game over !")
        elif gate == "blue":
            print("Eaten by beasts game over !")
        elif gate == "yellow":
            print("You win \n You find the treasure")
        else:
            print("Game over")
    elif river == "swim":
        print("Attack by crocodile game over !")
    else:
        print("Game over !")
elif way == "right":
    print("Fall into a hole game over")
else:
    print("game over !")



