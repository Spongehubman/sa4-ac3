number = 10
guess = None

print("I'm thinking of a number...")
while exit != True:
    guess = input("What number am I thinking of? Or press 'q' to quit.: ")

    if guess == 'q':
        print(f"The number is {number}.")
        exit = True
    else:
        if int(guess) == number:
            print("Congratulations! You guessed the right number.")
            exit = True
        else:
            print(f"Incorrect. Please try again!")
