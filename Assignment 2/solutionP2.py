def get_words():

    word_list = []
    f = open("words.txt", "r")
    for row in f:
        word_list.append(row.strip().lower())
    f.close()
    return word_list


def map_anagrams(words):

    word_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))

        # add key to dict if it doesn't exist already
        if not word_dict.get(sorted_word):
            word_dict[sorted_word] = []

        # add the word to the list in the anagram_list
        word_dict[sorted_word].append(word)
    return word_dict


def sort_by_list_length(words):

    anagrams = {}
    for key in words:
        if len(words[key]) > 1:
            list_length = len(words[key])
            if not list_length in anagrams:
                anagrams[list_length] = []
            anagrams[list_length].append(words[key])
    return anagrams


def anagram_key_list(anagrams):

    key_list = []
    for key in anagrams:
        key_list.append(key)
    key_list.sort(reverse=True)
    return key_list


def print_anagrams(anagrams, key_list, word_length=0):

    for key in key_list:
        for anagram in anagrams[key]:
            if word_length == 0:
                print(anagram)
            elif word_length == len(anagram[0]):
                print(anagram)


# Control flow
words = map_anagrams(get_words())

anagrams = sort_by_list_length(words)

anagram_key_list = anagram_key_list(anagrams)

while True:
    try:
        word_length = int(
            input("How long words do you want to see anagrams for? type zero to see all anagrams: "))
        print_anagrams(anagrams, anagram_key_list, word_length)
    except:
        print("That is not a valid number")
