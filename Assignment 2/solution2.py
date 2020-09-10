def get_words():
    """
    Reads a file, 'words.txt' and returns a list of all the lines in that file stipped and lowercased.

    Returns:
    list of words
    """
    word_list = []
    f = open("words.txt", "r")
    for row in f:
        word_list.append(row.strip().lower())
    f.close()
    return word_list


def map_anagrams(words):
    """
    Takes a list of words and puts all the words in a dictionary sorted by anagrams. 

    Args:
    words: list of words

    Returns: 
    dictionary of anagrams, sorted anagram as key and lists of anagrams as values
    """
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
    """
    Iterates through a list of words and put all the words in a dictionary, one dictionary for each anagram. 
    Keyname in the dictionary is the words in a sorted order and values is all the anagrams matching the sorted word

    Args:
    words: a dictionary containing words grouped together as lists of anagrams.

    Returns:
    Dictionary containing lists of anagrams grouped together based on list length. Keyname is the length of the lists. 
    """
    anagrams = {}
    for key in words:
        if len(words[key]) > 1:
            list_length = len(words[key])
            if not list_length in anagrams:
                anagrams[list_length] = []
            anagrams[list_length].append(words[key])
    return anagrams


def anagram_key_list(anagrams):
    """
    create a list with the sorted keys of the anagrams dict

    Args:
    anagrams: dictionary containing lists of words

    Returns:
    List of keys from the dictionary sorted biggest to smallest
    """
    key_list = []
    for key in anagrams:
        key_list.append(key)
    key_list.sort(reverse=True)
    return key_list


def print_anagrams(anagrams, key_list, word_length=0):
    """
    Prints anagrams as lists in descending order,
    if word_length is other than 0 print only the specified word length

    Args:
    anagrams: dictionary of lists containing anagrams.
    key_list: list containing the keys to the dictionary of anagrams
    """
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
