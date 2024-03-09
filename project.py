from random import randrange


def choose_difficulty(difficulty):
    num = 0
    difficulties = {
        "e": "easy",
        "m": "medium",
        "h": "hard",
        "i": "impossible"
    }
    if difficulty in difficulties.keys():
        mode = difficulties[difficulty]
        if mode == "easy":
            num = randrange(1, 10)
        elif mode == "medium":
            num = randrange(1, 50)
        elif mode == "hard":
            num = randrange(1, 100)
        elif mode == "impossible":
            num = randrange(1, 1000)
        return num
    else:
        print("Unrecognised command")
        return


num_of_guesses = 0
diff = input()
number = choose_difficulty(diff)
guess = int(input("Enter your guess: "))
while number != guess:
    if guess < number:
        print("The number you are trying to guess is higher.")
        guess = int(input("Try again: "))
        num_of_guesses += 1
    elif guess > number:
        print("The number you are trying to guess is lower.")
        guess = int(input("Try again: "))
        num_of_guesses += 1
    else:
        break
print(f"Guessed! {num_of_guesses} guesses")
