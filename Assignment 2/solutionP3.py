from random import randrange


def random_word(words):

    random_index = randrange(len(words))
    return words[random_index]


def ask_for_letter():

    while True:
        guess = input("Please enter a letter:")
        if len(guess) == 1 and guess.isalpha():
            return guess
        print(guess, "is not a valid input, please enter a single letter")


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

    play(words)


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


def play(words):

    word = random_word(words)
    # print(word) # possible to chat by commenting this line out
    word_length = len(word)
    guesses = 5
    correct_guesses = 0
    total_guesses = 0
    answer = ["-" for x in range(word_length)]
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
            for p in positions:
                answer[p] = letter
        else:
            print("Wrong guess!")
        print("".join(answer))
        score = correct_guesses * total_guesses
        if not "-" in answer:
            end_game(True, score)

    final_guess = input("Please enter the corresponding word:")
    is_winner = final_guess == word
    end_game(is_winner, score, word)


# initalize the game
init_game()
