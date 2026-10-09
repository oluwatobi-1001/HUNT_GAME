# ==========================================
#           TREASURE QUEST GAME
# ==========================================

print("""
╔══════════════════════════════════════════╗
║                                          ║
║           🏝️  TREASURE QUEST  🏝️         ║
║                                          ║
╚══════════════════════════════════════════╝
""")

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
print("You're at a crossroad. Where do you want to go?")
print()

choice1 = input("Type 'left' or 'right': ").lower()


# FIRST CHOICE
if choice1 == "left":

    print()
    print("You come to a lake.")
    print("There is an island in the middle of the lake.")
    print("You wait for a boat.")
    print()

    choice2 = input("Type 'wait' to wait for a boat or 'swim' to swim: ").lower()


    # SECOND CHOICE
    if choice2 == "wait":

        print()
        print("A boat arrives and takes you to the island.")
        print("You arrive at the island unharmed.")
        print()
        print("There is a house with 3 doors.")
        print("One red, one yellow and one blue.")
        print()

        choice3 = input(
            "Which colour do you choose? "
        ).lower()


        # THIRD CHOICE
        if choice3 == "yellow":

            print()
            print("🎉 You found the treasure!")
            print("🏆 YOU WIN! CONGRATULATIONS!")

        elif choice3 == "red":

            print()
            print("🔥 You entered a dangerous room.")
            print("GAME OVER!")

        elif choice3 == "blue":

            print()
            print("🌊 You entered a room filled with water.")
            print("GAME OVER!")

        else:

            print()
            print("That is not one of the available doors.")
            print("GAME OVER!")


    else:

        print()
        print("You tried to swim across the lake.")
        print("GAME OVER!")


# RIGHT PATH
else:

    print()
    print("You chose the wrong path.")
    print("You fell into a trap.")
    print("GAME OVER!")