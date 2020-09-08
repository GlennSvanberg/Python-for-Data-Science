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
words = words[0:2000]
# print(words[411859])


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


def anagrams_by_length(anagrams):
    anagrams_length = {}
    for anagram in anagrams:
        if anagrams_length.get(len(anagram)):
            anagrams_length[len(anagram)].append(anagram)
        else:
            anagrams_length[len(anagram)] = [anagram]
    return anagrams_length


anagrams = map_anagrams()

al = anagrams_by_length(anagrams)

print(al[7])


def print_sorted_anagrams():
    pass


print_sorted_anagrams()
