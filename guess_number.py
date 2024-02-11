number = 10
guess = None
guesses_left = 3

print("I'm thinking of a number...")
while exit != True:
    if guesses_left > 0:
        guess = input("What number am I thinking of? Or press 'q' to quit.: ")

    if guess == 'q' or guesses_left < 1:
        print(f"The number is {number}.")
        exit = True
    else:
        if int(guess) == number:
            print("Congratulations! You guessed the right number.")
            exit = True
        else:
            print(f"Sorry! Incorrect.")
            guesses_left = guesses_left - 1
            if guesses_left > 0 and guesses_left > 1:
                print(f"Please try again! You have {guesses_left} guesses left!")
            elif guesses_left > 0 and guesses_left == 1:
                print(f"Please try again! You have {guesses_left} guess left!")

            if guesses_left > 0:
                if int(guess) > number:
                    print("Your guess is too high!")
                elif int(guess) < number:
                    print("Your guess is too low.")
