def encoder(data):
    char_count = 1
    prev_char = ""
    if len(data) == 1:
        yield (data, 1)
    else:
        for char in data:
            if char.isnumeric():
                raise Exception(
                    "Sorry can't compress numbers, please provide a string without numbers")
            res = ()
            if prev_char == "":
                prev_char = char
                continue
            if char == prev_char:
                char_count += 1
            else:
                res = (prev_char, char_count)
                char_count = 1
                prev_char = char
                yield res
            res = (prev_char, char_count)
        yield res


def merge(char, nr_str):
    res = ""
    nr = int(nr_str)
    for letter in range(nr):
        res += char
    return res


def decoder(data):
    nr_str = ""
    prev_char = ""
    res = ""
    for index, char in enumerate(data):
        if char.isnumeric():
            res = ""
            nr_str = nr_str + char
        else:
            if nr_str != "":
                res = merge(prev_char, nr_str)
                nr_str = ""
            prev_char = char

        if index + 1 == len(data):
            res = merge(prev_char, nr_str)

        if res != "":
            yield res


data = "bbccccccdrrrffhhhh"
#data = "aa-s/)dsf!"
#data = "a"
print(data)
encoded = ""
for x in encoder(data):
    encoded = encoded + f"{x[0]}{x[1]}"
print(encoded)

decoded = ""
for x in decoder(encoded):
    decoded = decoded + x
print(decoded)
print(data == decoded)
