import time
import os

import random
import arcade

import sys


startSound = arcade.load_sound(":resources:sounds/upgrade3.wav")


arcade.play_sound(startSound)

print("Music and sound resources from python arcade library: https://api.arcade.academy/en/stable/api_docs/resources.html")
print("Under CC0 by kenney.nl : https:kenney.nl")

soundPlAtt= arcade.load_sound(":resources:sounds/hit3.wav")
soundPlDef= arcade.load_sound(":resources:sounds/hurt5.wav")
soundGOBAtt= arcade.load_sound(":resources:sounds/hit5.wav")
soundGOBDef= arcade.load_sound(":resources:sounds/hurt1.wav")
soundPlDeath= arcade.load_sound(":resources:sounds/fall3.wav")
soundGOBDeath = arcade.load_sound(":resources:sounds/explosion2.wav")
soundGOver= arcade.load_sound(":resources:sounds/gameover2.wav")
soundStartEffect= arcade.load_sound(":resources:sounds/upgrade5.wav")
soundStartEffect2= arcade.load_sound(":resources:sounds/secret2.wav")
soundPlNothing = arcade.load_sound(":resources:sounds/jump5.wav")
soundGOBNothing = arcade.load_sound(":resources:sounds/jump4.wav")
soundPlRun = arcade.load_sound(":resources:sounds/lose3.wav")
bmusic = arcade.load_sound(":resources:music/funkyrobot.mp3",streaming=True)

choiceChoose1 = arcade.load_sound(":resources:sounds/coin1.wav") 
choiceChoose2 = arcade.load_sound(":resources:sounds/coin2.wav") 
choiceChoose3 = arcade.load_sound(":resources:sounds/coin3.wav") 
choiceChoose4 = arcade.load_sound(":resources:sounds/coin4.wav") 




# ask if want to begin adventure
loadBegin = 'L O A D I N G......'
for i in range(20):
    print('{}'.format(loadBegin[:i]),end="\r")
    time.sleep(0.2)

arcade.play_sound(soundStartEffect)

print('\n')
message = "~~~ Popeyes Terminal Adventure --> A Codedex Project By Saad Shahid ~~~"
for i in range(len(message)):
    print(message[i:]+message[:i],end="\r")
    time.sleep(0.2)

popeye1="""
      
Art by Joan Stark
          .-'-.
       __|     `\\
      `-,-`--._  `\\
 []  .->'  a   `|-'
  `=/ (__/_     /
    \\_,    `  _)
jgs   `----; |
      
      """

for i in popeye1.splitlines():
    print (i)
    time.sleep(0.5)

print("Stark, J. Popeye ASCII art [ASCII art]. ASCII Art Archive. Injosoft. Retrieved August 17, 2025, from https://www.asciiart.eu/cartoons/popeye\n")

arcade.play_sound(soundStartEffect2)


time.sleep(2)

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
confirm = 0


print('\n')


while confirm ==0:
    introm = "~~~ The Game Begins ~~~"
    for i in range(len(introm)):
        print(introm[i:]+introm[:i],end="\r")
        time.sleep(0.2)
    print()
    arcade.play_sound(choiceChoose1)
    begin = input("~ Do you want to begin? \nAnswer with Yes or No: \n-------------\n~ Your Answer: ")
    arcade.play_sound(choiceChoose2)
    if begin.lower() == 'yes':
        # first name of character
        chFN = input("\n~ Alright... \n Lets Begin... \nEnter Your FIRST NAME: \n-------------\n~ Your Answer: ")
        arcade.play_sound(choiceChoose3)
        #neeed to implement last name (wip rn)
        chLN = input("\n~ Enter Your LAST NAME: \n-------------\n~ Your Answer: ")
        arcade.play_sound(choiceChoose4)
        print("Hello {} {}".format(chFN[:1].upper()+chFN[1:].lower(),chLN[:1].upper()+chLN[1:].lower()))
        confirm+=1
    elif begin.lower() == 'no':
        print('\n ~~ Exiting ~~ -')
        arcade.play_sound(soundGOver)
        time.sleep(2)
        sys.exit()

    else:
        print("Invalid Input")
    



message = "~~~ The Game Begins ~~~"
arcade.play_sound(choiceChoose1)
for i in range(len(message)):
    print(message[i:]+message[:i],end="\r")
    time.sleep(0.2)


if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
confirm = 0

mPlayer= arcade.play_sound(bmusic,loop=True)


print("\nYou have arrived at a crossroad!")
print("What CHOICE SHALL YOU MAKE???")

print("Will you go to 1. TOWN or 2. Face the MEGA goblin???!!!")


ultChoice = input("Enter 1 or 2\n:")


if ultChoice == "1":
    print("You decide to visit town.\n What's this? You FOUND A POTION!!!")
    playerHealth=220
    maxphealth= 220
    print(f"Your health has increased 20 points. Your health is {playerHealth}")
    isChoice1= True
elif ultChoice == "2":
    print("You decide to fight the goblin. ")
    isChoice1= False
else:
    print("You failed to make a choice and fell down a hole. Now you have no choice but to fight the goblin")
    isChoice1= False


print("You walk into a dungeon")

scene = """
================================================================================
|  \\|/                                                                \\|/     |
|  / \\                      D U N G E O N   C H A M B E R             / \\     |
|----------------------------------------------------------------------------|
|                                                                            |
|  [ G O B L I N ]                                                           |
|           ,_                                                               |
|        ,'/ \\_.-\"\"\"-._                                                     |
|       /  \\_/  _   _  \\                                                    |
|      |  (o ) (o )  ) |          (snarl)  >:E                               |
|      |     .-`-'.   /                                                     |
|       \\   /  _  \\  /                                                      |
|        '._\\ (_) /_.'                                                      |
|           /`-^-`\\                                                         |
|          /  \\_/  \\                                                        |
|         /___/ \\___\\                                                       |
|                                                                            |
|                                    <<  V S  >>                             |
|                                                                            |
|                                                     [ P O P E Y E ]        |
|                                                       ____                  |
|                                                       \\__/         # ##     |
|                                                      `(  `^=_ p _###_       |
|                                                       c   /  )  |   /       |
|                                                _____- //^---~  _c  3        |
|                                              /  ----^\\ /^_\\   / --,-        |
|                                             (   |  |  O_| \\_/  ,/           |
|                                             |   |  | / \\|  `-- /            |
|                                            (((G   |-----|                     |
|                                                  //-----\\\\                   |
|                                                 //       \\\\                  |
|                                               /   |     |  ^|                |
|                                               |   |     |   |                |
|                                               |____|    |____|               |
|                                              /______)   (_____\\              |
|                                                                            |
|----------------------------------------------------------------------------|
|  cobblestones:  ~^..^~..~^..^~..~^..^~..~^..^~..~^..^~..~^..^~..~^..^~      |
================================================================================
"""

for i in scene.splitlines():
    print (i)
    time.sleep(0.5)

print("A GOBLIN APPEARS. WHAT WILL YOU DO?")
goblinHealth = 150
goblinAttack = 20
goblinDefend = 15
goblinEXP = 50

if isChoice1 ==False:
    playerHealth = 200
    maxphealth =200
elif isChoice1 == True:
    playerHealth =220
    maxphealth =220


playerAttack = 25
playerDefend = 20
playerEXP = 0
playerNextLevel = 100
battle =0
playerCurrentLevel = 1

goblinIsDefend=False


lastAction = ""

lastAction2=""
while battle ==0:
    
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



    print("~~~~~~~~~~~~~~~~")
    print(f"Your HP: {playerHealth}/{maxphealth}\n Goblin HP: {goblinHealth}")
    print("~~~~~~~~~~~~~~~~")
    print(scene)

        
    

    if lastAction:
        print(lastAction)
    if lastAction2:
        print(lastAction2)

    print("\nMake your action")
    print("\n1: Attack")
    print("\n2: Defend")
    print("\n3: Nothing")
    print("\n4: Run away")

    lastAction2 = ""

    isDefend =False

    choice = input("Enter a number from 1 to 4 to determine the choice:\n")

    if choice =="1":
        dmg= playerAttack
        if goblinIsDefend:
            dmg= max(0,playerAttack-goblinDefend)
            lastAction= "You attack was reduced by the goblin."
            goblinIsDefend=False
            arcade.play_sound(soundGOBDef)
        goblinHealth-=dmg
        lastAction= f"You attacked the goblin with {dmg} damage! Goblin Health: {goblinHealth}"
        arcade.play_sound(soundPlAtt)
    elif choice =="2":
        isDefend=True
        lastAction= "You defend"
        arcade.play_sound(soundPlDef)
    elif choice =="3":
        lastAction= "You chose to do nothing"
        arcade.play_sound(soundPlNothing)
    elif choice == "4":
        mPlayer.pause()
        arcade.play_sound(soundPlRun)
        lastAction= "You ran away."
        battle =1
        break
    else:
        lastAction= "Wrong choice. Turn lost."


    if goblinHealth >0:
        detFTurn = random.randint(1,15)
        if detFTurn <5:
            dmg=goblinAttack
            if isDefend:
                dmg = max(0,dmg-playerDefend//2)
                lastAction2= "The goblins attack was reduced by your defense!"
                isDefend=False
            playerHealth-=dmg
            lastAction2= f"The goblin attacks. You lost {goblinAttack} HP! Remaining HP: {playerHealth}"
            arcade.play_sound(soundGOBAtt)
        elif detFTurn<=10:
            goblinIsDefend=True
            lastAction2= "The goblin defends"
            arcade.play_sound(soundGOBDef)
        else:
            lastAction2= "The goblin does nothing"
            arcade.play_sound(soundGOBNothing)
       
    if goblinHealth <=0:
        lastAction2="\nThe goblin is dead"
        mPlayer.pause()
        arcade.play_sound(soundPlAtt)
        arcade.play_sound(soundGOBDeath)
        battle=1

        playerEXP+=goblinEXP
        lastAction=f"You gained {goblinEXP} EXP.  Total = {playerEXP/playerNextLevel}"
        if playerEXP >=playerNextLevel:
            playerCurrentLevel+=1
            playerEXP-=playerNextLevel
            playerNextLevel= int(playerCurrentLevel*3.3)

            maxphealth+=2
            playerHealth=maxphealth
            playerDefend+=2
            lastAction2=f"LEVEL UP. increased health: {maxphealth} and defense: {playerDefend}. Exp gained: {playerEXP}/{playerNextLevel}"
    elif playerHealth <=0:
        lastAction2="You lost"
        mPlayer.pause()
        battle=1
    

if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")
confirm = 0



print("~~~~~~~~~~~~~~~~")
print(f"Your HP: {playerHealth}/{maxphealth}\n Goblin HP: {goblinHealth}")
print("~~~~~~~~~~~~~~~~")
print(scene)
    

if lastAction:
    print(lastAction)
if lastAction2:
    print(lastAction2)



print()
mPlayer.pause()
arcade.play_sound(soundGOver)

print("\nTHE GAME HAS ENDED!!!!!!!!!!!!!!!!")
time.sleep(3)
