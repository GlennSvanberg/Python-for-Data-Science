"""
In this problem, we will implement a small game where the computer will select a random word from a list of words and the player will try
to guess the selected word. Here are the different steps for this game:

The computer will select a random word from a list of words (words.txt) and let the player know how many letters in the selected word
At the beginning, the user is given 5 chances to guess the letters of the selected word
For each guess, the computer should tell the player if the letter is in the selected word and print the position of these letter in the word
(example: --a--a-, with "-" is an unknown letter)
After 5 guesses, the player should enter the entire word: if it is correct he will get a score of 100+ (number of correct guessed letter * number of guesses),
otherwise, he will get a score of (number of correct guessed letter * number of guesses).

Example:

I am thinking of a word that is 8  letters long! Try to guess this word!
you have  5 guesses left!
Please enter a letter: a
wrong guess!
--------
you have  4 guesses left!
Please enter a letter: e
good guess!
e----e-e
you have  3 guesses left!
Please enter a letter: d
good guess!
e-d--e-e
you have  2 guesses left!
Please enter a letter: t
wrong guess!
e-d--e-e
you have  1 guesses left!
Please enter a letter: p
good guess!
e-dp-e-e
Please enter the corresponding word: endpiece
You win! Your score is :  115
"""
from random import randrange


def random_word(words):
    random_index = randrange(len(words))
    return words[0]
    return words[random_index]


def ask_for_letter():
    while True:
        guess = input("Please enter a letter:")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print(guess, "is not a valid input, please enter a single letter")


def add_letter_to_answer(letter, positions, answer):
    for p in positions:
        answer[p] = letter
    return answer


def letter_in_word(letter, word):
    positions = []
    for i, p in enumerate(word):
        if letter == p:
            positions.append(i)
    return positions


def init_game():
    f = open("words.txt", "r")
    words = []
    for row in f:
        words.append(row.strip().lower())
    f.close()

    word = random_word(words)
    print(word)
    play(word)


def answer_is_correct(answer):
    return not "-" in answer


def end_game(is_winner, score, word=""):
    if is_winner:
        score += 100
        print("You win! Score: {}".format(score))
    else:
        print("Sorry you lost, the word was: {}".format(word))
        print("Score: {}".format(score))

    res = input("Play again y/n : ")
    if res == "y":
        init_game()
    else:
        exit()


def play(word):
    word_length = len(word)
    guesses = 5
    correct_guesses = 0
    total_guesses = 0
    # list comprehension
    answer = []
    for x in range(word_length):
        answer.append("-")
    print("I am thinking of a word that is {} letters long! Try to guess this word!".format(
        word_length))

    while guesses > 0:
        print("you have {} guesses left!".format(guesses))
        letter = ask_for_letter()
        guesses = guesses - 1
        total_guesses += 1
        positions = letter_in_word(letter, word)
        if len(positions) > 0:
            print("Good guess!")
            correct_guesses += 1
            add_letter_to_answer(letter, positions, answer)
        else:
            print("Wrong guess!")
        print("".join(answer))
        score = correct_guesses * total_guesses
        if answer_is_correct(answer):
            end_game(True, score)

    final_guess = input("Please enter the corresponding word:")
    is_winner = final_guess == word
    end_game(is_winner, score, word)


init_game()
