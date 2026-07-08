print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." / ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Invalid inputs will lead to the termination of the game, be careful")
first_step = input("Left or right\n")
if first_step == "Left":
    print("Are you ready for the adventure? It isn't easy.")
    wait_go = input("Do you wish to wait or take the next step? Wait or go")
    if wait_go == "go":
        print("Nice, You advance to the next stage")
        monster = input("A monster is feeding in front of you. Do you wish to kill it or leave it? Y for kill and N for leave it.")
        if monster == "Y":
            print("You kill the monster and obtain a magical chest")
            print("You have reached the final stage. Very well, brave warrior. Are you ready to defeat the final boss and claim the treasure?")
            open_chest = input("Would you like to open chest? Y for yes and N for no")
            if open_chest == "Y":
                print("You obtain a magical sword and magical armor.\nYour battle with boss goes on for three days and nights and finally you emerge victorious.\nYou have obtained the ultimate treasure.\nGame completed!")
            else:
                print("You fought bravely, but the final boss proved too powerful. You have been defeated.\nGAME OVER")
        else:
            print("The monster catches your scent, sneaks up behind you, and kills you.\nGAME OVER")

    else:
        print("Oops, the floor became lava, You die\nGAME OVER")

elif first_step == "Right":
    print("You chose right, You have entered the dragons lair")
    print("As you walk deep into the dungeon you find a mighty dragon deep in its sleep.\nThe very sight of the dragon sends chills down your spine.")
    print("As you come closer you realize that this i5fgs the ancient dragon that destroyed the earth once upon a time 'The Chaos Dragon'")
    sneak_train = input("Do you want to sneak past the dragon or train it?Press Y to train and N to sneak.")
    if sneak_train == "Y":
        print("As you try to approach the dragon it wakes up from its deep sleep and gets angry.\nIt looks at you and wants to devour you and then you suddenly remember you have food, So you feed the dragon and it calms down.")
        print("Once it calms down, you go near it and keep offering food, It slowly starts to trust and becomes your partner.")
        print("Now the dragon and you have a bond and the rapport between you two is the best.")
        print("Now you get on the dragon and fly out of the dungeon and as you come out you see that the entire sky is black feels ominous.")
        print("You have reached the final stage, The final boss")
        dragon = input("Do you want the dragon's help or want to fight the final boss alone?Y for help, N for no help.")
        if dragon == "Y":
            print("The dragon and you easily overpower the Final boss who ruled over the world.\nAfter a single blast from the dragons breath the demon is already on his knees.")
            print("You use your sword to deal the final blow and kill the demon\nCongratulations!You obtained the treasure.\nTHE END")
        else:
            print("You fight the demon on your own, He is very powerful for you to fight alone.\nHe overpowers you, You fight bravely but you die\nGAME OVER")
    else:
        print("You try to sneak past the dragon.")
        print("The dragon who hasn't eaten since a century smells the scent of food and wakes up.")
        print("It wakes up and devours you. You couldn't even fight back.\nGAME OVER")

else:
    print("Invalid inputs will lead to the termination of the game\nGAME OVER")