from random import randrange


def game(number):
    return number


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


diff = input()
my_num = choose_difficulty(diff)
print(my_num)
#print(randrange(1,10))
