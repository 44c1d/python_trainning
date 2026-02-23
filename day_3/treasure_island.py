print("Welcome to the 'Treasure Island'.\nYour mission is to find the treasure")

start=input("Wich way you want to go? Left or Right?")

if start == "Left":
    stage2= input("Swim or Wait?")

    if stage2 == "Wait":
        stage3= input("Which door? (Red , Blue or Yellow)")
    
        if stage3 == "Yellow":
            print("You win!")
        elif stage3 == "Red":
            print("Burned by fire.\nGame Over!")
        elif stage3 == "Blue":
            print("Eaten by beasts.\nGame Over!")
        else:
            print("Game Over!!!!")
    else:
        print("Attacked by trout.\nGame Over")        
else:
    print("Fall into a hole.\nGame Over!")
                     


