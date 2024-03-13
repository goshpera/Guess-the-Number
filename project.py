from random import randrange


def impossible(guess_count):  #counts the guesses and made already and checks them
    is_game_over = False
    if guess_count >= 7:
        is_game_over = True
    return is_game_over


def choose_difficulty(difficulty):
    num = 0
    is_impossible = False
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
            is_impossible = True
        return num, is_impossible  #packs the 2 variables into a tuple and returns it
    else:
        print("Unrecognised command")
        return


num_of_guesses = 0
diff = input()
number, impossible_mode = choose_difficulty(diff)
guess = int(input("Enter your guess: "))
while number != guess:
    if guess < number:
        print("The number you are trying to guess is higher.")
        guess = int(input("Try again: "))
        num_of_guesses += 1
        if impossible_mode:
            if impossible(num_of_guesses):
                print("Lost game")
                break
    elif guess > number:
        print("The number you are trying to guess is lower.")
        guess = int(input("Try again: "))
        num_of_guesses += 1
        if impossible_mode:
            if impossible(num_of_guesses):
                print("Lost game")
                break
    else:
        break
print(f"Guessed! {num_of_guesses} guesses")
