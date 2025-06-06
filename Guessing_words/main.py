from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too High!")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it! The answer is {actual_answer}")


def set_difficulty():
    level = input("Choose a dificulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number gussing game!")
    print("I'm thinking of a nuber beetween 1 and 100.")
    answer = randint(1, 100)
    print(f"The correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose!")
            break


game()

