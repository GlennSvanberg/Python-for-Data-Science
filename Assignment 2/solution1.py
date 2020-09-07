"""
Looking for a word in a dictionary is very easy since words are sorted alphabetically. But what if we are looking for all the words in the second letter is a, 
it's impossible unless you sort all the words by their second letter. In this case, you would need a different dictionary for each letter position. 
The objective of this exercise is to design a kind of dictionary that will allow you to find all the words with a given letter in a given position.

Example

words = ['class', 'case', 'course', 'dictionary', 'java', 'list', 'program', 'python', 'tuple', 'word']

w = words_letter_position(d, 'a', 1)

print ("result=",w)

output: result= ['case', 'java']

 w = words_letter_position(d, 't', 3)

print ("result=",w)

output: result=['dictionary', 'list']

1- Write the simplest solution that allow you to find all the words with a given letter in a given position.

2- Write a more efficient solution by using a different data structure? Explain your choice.

3- Compare the execution time between these two solutions. 
"""


def words_letter_position(words, char, pos):
    matches = []
    for word in words:
        if word[pos] == char:
            matches.append(word)
    return matches


words = ['class', 'case', 'course', 'dictionary',
         'java', 'list', 'program', 'python', 'tuple', 'word']

print("\n1. Simple solution -----------------------------")
print("result", words_letter_position(words, 'a', 1))

"""
dict letter : (key: pos, value: word_pos) requires to loop over all of the same letter

dict char_index: (key: letter, value:word_list_pos)

I'm using a dictionary nested inside another dictionary. 
The outer dictionary has the position in the word that the lerrer is searched for. 
The value of the outer dict is another dictionary with single letters as keys. 
The value for the letters is a list of positions in the original word list. 

This way nothing has to be looped over neither the words, the letters or the positions. Finding the values directly using a mapping is much more efficient

 chars{ key: char_index }
                   (name is the char_index key ){key: char, value: char_position_in_word }  
"""

print("\n2. More efficient solution ---------------------")

char_dict = {}


def init_dictionary(words):
    for word_index, word in enumerate(words):
        for char_index, char in enumerate(word):
            if not index_in_char_dict(char_index):
                add_index_to_char_dict(char_index)

            if not char_in_index(char, char_dict[char_index]):
                add_char_in_index(char, char_dict[char_index])

            add_word_index_to_char(char_dict[char_index][char], word_index)


def add_word_index_to_char(char, word_index):
    char.append(word_index)


def add_char_in_index(char, index_dict):
    index_dict[char] = []


def char_in_index(char, index_dict):
    if char in index_dict:
        return True
    return False


def add_index_to_char_dict(i):
    char_dict[i] = {}


def index_in_char_dict(i):
    if i in char_dict:
        return True
    return False


init_dictionary(words)
print(char_dict)