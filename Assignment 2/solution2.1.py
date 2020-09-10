f = open("words.txt", "r")
words = []

for row in f:
    words.append(row.strip().lower())
words = words[0:2000]
# print(words[411859])


def map_anagrams():
    for word in words:
        # mappings is the outmost holder key: length , value: list of anagrams[sets]
        mappings = {}

        # make the word comparable
        s_word = "".join(sorted(word))

        word_length = len(s_word)

        # add the outer mapping if it doesn't exist already
        if not mappings.get(word_length):
            mappings[word_length] = []
        mapping_values = mappings[word_length]

        # add the word
        if not mapping_values

f.close()