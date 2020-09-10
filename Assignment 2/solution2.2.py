# word_list = ["car", "arc", "pizza", "art", "rat",
# "poolo", "flamingo", "fish", "scar", "cars", "shif", "ifhs"]
word_list = []
f = open("words.txt", "r")
for row in f:
    word_list.append(row.strip().lower())
f.close()
# 1. put anagrams in dict key:sorted word value: list of anagrams
# word_dict key: sorted word value: word_list


def map_anagrams(words):
    word_dict = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        word_length = len(sorted_word)

        # add key to dict if it doesn't exist already
        if not word_dict.get(sorted_word):
            word_dict[sorted_word] = []

        # add the word to the list in the anagram_list
        word_dict[sorted_word].append(word)
    return word_dict


# 2. loop over the anagrams dict and put all the words
# anagram_dict key: list_length value: anagram_list[wordlist[]]
def sort_by_list_length(words):
    anagrams = {}
    for key in words:
        # add the words to anagram if there is more than one value under the corresponding key
        if len(words[key]) > 1:
            # print("anagram: ", words[key])
            list_length = len(words[key])
            if not list_length in anagrams:
                anagrams[list_length] = []
            anagrams[list_length].append(words[key])
    return anagrams

# create a list with the sorted keys of the anagrams dict


def anagram_key_list(anagrams):
    key_list = []
    for key in anagrams:
        key_list.append(key)
    # sort the list with biggest number first
    key_list.sort(reverse=True)
    return key_list

# print anagrams as lists in descending order, if word_length is other than 0 print only the specified word length


def print_anagrams(anagrams, key_list, word_length=0):
    for key in key_list:
        for anagram in anagrams[key]:
            if word_length == 0:
                print(anagram)
            elif word_length == len(anagram[0]):
                print(anagram)


words = map_anagrams(word_list)

anagrams = sort_by_list_length(words)

anagram_key_list = anagram_key_list(anagrams)


#print_anagrams(anagrams, anagram_key_list)


word_length = int(input("How long words do you wnat to see anagrams for? "))
print_anagrams(anagrams, anagram_key_list, word_length)
