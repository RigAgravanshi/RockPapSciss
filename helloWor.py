from random import *

plr=input("Enter your choice:rock,paper or scissor?")
choices=["paper","rock","scissor"]
comp_choice=randint(0,2)
print("Computer choice= "+choices[comp_choice]+"\n")
print("Player's choice= "+plr+"\n")

                                                      #Edit it,while loop till the player wins
if(plr==choices[comp_choice]):
    print("Its a tie!")

elif(plr=="paper"):
    if(choices[comp_choice]=="scissor"):
        print("YOU LOSE")
    else:
        print("WIN")

elif(plr=="rock"):
    if(choices[comp_choice]=="paper"):
        print("YOU LOSE")
    else:
        print("YOU WIN")

else:
    if(choices[comp_choice]=="paper"):
        print("YOU WIN")
    else:
        print("YOU LOSE")
    
      

