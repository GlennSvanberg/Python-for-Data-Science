"""
An anagram is a word formed by rearranging the letters of a different word by using all the original letters exactly once.
For example, the word bawl can be rearranged into 'blaw' or the word 'alerts' into 'salter'.

1- Write a program that reads a word list from the file words.txt

Preview the document and as an output, it prints all the lists of words that are anagrams ordered by the length of lists.
all the lists of words that are anagrams and contains n letters which is given as an input.
Example:

For 6 letters, we will have for example:

(2, ['append', 'napped'])

(12, ['enters', 'ernest', 'estren', 'nester', 'renest', 'rentes',
 'resent', 'sterne', 'streen', 'tenser', 'ternes', 'treens'])

2- Which data structure did you use and why?
"""
f = open("words.txt", "r")
words = []

for row in f:
    words.append(row.strip().lower())
#words = words[0:50000]
# print(words[411859])
f.close()


def map_anagrams():
    mappings = {}
    for word in words:
        s_word = "".join(sorted(word))
        if mappings.get(s_word):
            mappings[s_word].append(word)
        else:
            mappings[s_word] = [word]
    anagrams = {}
    for m in mappings:
        if len(mappings[m]) > 1:
            anagrams[m] = mappings[m]
    return anagrams


def add_to_dict(list_length_dict, word_list):
    list_length = len(word_list)
    if not list_length_dict.get(list_length):
        list_length_dict[list_length] = {}

    word_length_dict = list_length_dict[list_length]
    word_length = len(word_list[0])

    if not word_length_dict.get(word_length):
        word_length_dict[word_length] = []

    word_length_dict[word_length].append(word_list)


def convert_to_nested_list(anagrams):
    """
    anagrams is a dict
    word, is a str each word
    """
    list_length_dict = {}
    for key in anagrams:
        word_list = anagrams[key]
        if len(word_list) > 1:
            add_to_dict(list_length_dict, word_list)
    return list_length_dict


anagrams = map_anagrams()


def print_sorted_anagrams():
    pass


print_sorted_anagrams()


word_dict = convert_to_nested_list(anagrams)

for key in word_dict:
    nested_dict = word_dict[key]
    print("List_length: ", key)
    if key == 6:
        for nested_key in nested_dict:
            print("Word_length: ", key)
            print(nested_dict[nested_key])
