import time

# Simple slow solution


def words_letter_position(words, char, pos):
    """
    Matches words to certain positions in a word and returns them as a list

    Args:
    words: list of words
    char: one char that will be matched to a certain position in the word
    pos: int representing the position in the word the char should match to.

    Returns:
    list of words
    """
    matches = []
    for word in words:
        try:
            if word[pos] == char:
                matches.append(word)
        except IndexError:
            pass

    return matches

# More elaborate faster solution


def init_dictionary(words):
    """
    Takes a list of words and returns them as a nested dictionary.
    The outer dictionary stores the chars as keys.
    The value is another dictionary with positions of the chars in the words as keys.
    The values of the inner dictionary is a list of words matching the outer keys.

    Args:
    words: list of words

    Returns:
    dictionary of chars with dictionary of positions with words as values
    """
    char_dict = {}
    for word in words:
        for char_index, char in enumerate(word):
            if not char_index in char_dict:
                char_dict[char_index] = {}

            if not char in char_dict[char_index]:
                char_dict[char_index][char] = []

            char_dict[char_index][char].append(word)

    return char_dict


def dict_word_letter_pos(char_dict, char, pos):
    """
    Finds a char in a given position from a dictionary given these as elements

    Args:
    char_dict: Nested dictionary with all the words sorted under chars and positions
    char: the that is to match the given position
    pos: the position the char is to be found at

    Returns:
    list of words matching the given args
    """
    return char_dict[pos][char]


def evaluate_solution(data, implementation, iterations):
    start = time.time()
    for i in range(iterations):
        implementation(data, "a", 1)
    end = time.time()
    return end-start


def evaluate_dict_init(data):
    print("initializing char_dict")
    start = time.time()
    char_dict = init_dictionary(data)
    end = time.time()
    print("elapsed: ", end-start, " sec")
    return char_dict


# data structures
words = ['class', 'case', 'course', 'dictionary',
         'java', 'list', 'program', 'python', 'tuple', 'word']
char_dict = evaluate_dict_init(words)


# test the solutions
#print("\n1. Simple solution -----------------------------")
#print("result", words_letter_position(words, 'a', 1))
#print("\n2. More efficient solution ---------------------")
#print("result", mapped_word_letter_pos(char_dict, 'a', 1))


# Evaluate the performance of each solution by running both of them 10000000 times
char_dict = evaluate_dict_init(words)
iterations = 1000000
print("3. Evaluate with {} iterations ------------------------------------".format(iterations))
iterations = 1000000
print("Test 3.1: simple solution")
test_one = evaluate_solution(words, words_letter_position, iterations)
print("elapsed ", test_one, " sec")


print("Test 3.2: dict solution")
test_two = evaluate_solution(char_dict, dict_word_letter_pos, iterations)
print("elapsed ", test_two, " sec")

"""
The dict solution takes a bit more time to initialize but as long as it is ininilized it is a lot faster than the simple solution
This test was performed a lot of times on a small list. Below is the same test but with all the words from words.txt instead.
"""

# Evaluate the performance of each solution by running both of them at a larger dataset

iterations = 1000
print("4. Evaluate with big file and {} iterations -------------------------------".format(iterations))
words = []
f = open("words.txt", "r")
for row in f:
    words.append(row.strip().lower())
f.close()
char_dict = evaluate_dict_init(words)

print("Test 4.1: simple solution")
test_one = evaluate_solution(words, words_letter_position, iterations)
print("elapsed ", test_one, " sec")


print("Test 4.2: dict solution")
test_two = evaluate_solution(char_dict, dict_word_letter_pos, iterations)
print("elapsed ", test_two, " sec")
