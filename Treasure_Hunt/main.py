print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

mimartuleba1 = input('You are at a cross road. Where do you want to go?\nType "left" or "right": ')

if mimartuleba1 == "left":
    mimartuleba2 = input("You have come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across: ")

    if mimartuleba2 == "wait":
        mimartuleba3 = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose? ")

        if mimartuleba3.lower() == "yellow":
            print("You found the treasure! You Win!")
        elif mimartuleba3.lower() == "red":
            print("Burned by fire.\n Game Over.")
        elif mimartuleba3.lower() == "blue":
            print("Eaten by beasts.\n Game over")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("Attacked by trout.\n Game Over.")
else:
    print("You fall into a hole. Game Over.")
