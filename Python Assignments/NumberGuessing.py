import random

def take_guess():
    try:
        print()
        guess = int(input("Enter your guess: "))
        if(guess < 1 or guess > 10):
            print("Please enter a number between 1 and 10")
            take_guess()
        else:
            return guess
    except(ValueError or TypeError):
        print("Unsupported Character.\nPlease enter a valid number between 1 and 10")
        return take_guess()

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
        2: "hot",
        1: "hot"
    }

    if guess == number:
        print()
        print("Its a match! Congrats")
        print()
        return True
    else:
        difference = guess - number
        print("Your guess is {}".format(heatMap[abs(difference)]))
        return False    


while(True):
    count = 5
    print_menu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            computer_guess = random.randint(1, 10)
            print("I've already guessed a number between 1 and 10. Can you guess it?")
            #user_guess = take_guess()
            while(count > 0):
                user_guess = take_guess()
                if(compare_guess(user_guess, computer_guess)):
                    break
                else:
                    count -= 1
                    print("You have {} guesses left.".format(count))
                    print()
                    if(count == 0):
                        print()
                        print("The number was {}".format(computer_guess))
                        print()
        elif choice == 2:
            print()
            print("Thanks for playing!")
            print()
            break
        else:
            print("Invalid choice")
            print()
            continue
    except(ValueError or TypeError):
        print()
        print("Enter a valid choice")
        print()
        continue
