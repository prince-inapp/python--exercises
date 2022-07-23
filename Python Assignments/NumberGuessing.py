import random

def print_menu():
    print("1. Start the Game")
    print("2. Exit")

def compare_guess(guess, number):
    heatMap = {
        9: "very cold",
        8: "very cold",
        7: "cold",
        6: "cold",
        5: "neutral",
        4: "neutral",
        3: "warm",
        2: "hot"
    }
    if guess == number:
        print("Its a match! Congrats")
        return True
    else:
        difference = guess - number
        print(difference)
        
        
        
compare_guess(guess= 1,number = 10)

'''
while(True):
    print_menu()
    choice = int(input("Enter your choice: "))
    if choice == 1:
        computer_guess = random.randint(1, 10)
        print("I've already guessed a number between 1 and 10. Can you guess it?")
        user_guess = int(input("Enter your guess: "))
        compare_guess(user_guess, computer_guess)
    elif choice == 2:
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice")
        continue
'''