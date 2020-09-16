import pdb


def encode_generator(data):
    char_count = 1
    prev_char = ""
    for char in data:
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


def encoder(data):
    res = ""
    for x in encode_generator(data):
        res = res + f"{x[0]}{x[1]}"
    return res


def seq(char, nr):
    seq = ""
    for n in range(nr):
        seq = seq + char
    return seq


def decoder_generator2(data):
    is_letter = True
    current_char = ""
    nr = 0
    seq = ""
    for index, char in enumerate(data):
        pdb.set_trace()
        if char.isnumeric():
            nr = nr + int(char)
            print("nr:", nr)

        if nr == 0:
            current_char = char
            seq = ""
            for n in range(nr):
                seq = seq + current_char
            nr = 0
            yield seq

        if index == len(data) - 1:
            print("last")
            seq = ""
            for n in range(nr):
                seq = seq + current_char
        yield seq


def decoder_generator(data):
    prev_char = ""
    nr = 0
    new_pair = False
    seq = ""

    for index, char in enumerate(data):

        if char.isnumeric():
            print("numberic", char)
            new_pair = False
            nr += int(char)
        else:
            if new_pair:
                for i in range(int(nr)):
                    print("Adding letter to seq", prev_char)
                    seq = seq + prev_char
                print("new _pair: ", seq, nr)
                nr = 0
                prev_char = char
                new_pair = True
                yield seq

            else:
                prev_char = char
                new_pair = True

        if index + 1 == len(data):
            seq = ""
            for i in range(int(nr)):
                seq = seq + prev_char
                yield seq
        print("char", char)
        print("-----------")


def decoder(data):
    res = ""
    for x in decoder_generator(data):
        res = res + x
    return res


data = "bbccccccdrrrffhhhh"
data = "aa"
print(data)

encoded = encoder(data)
print(encoded)

decoded = decoder(encoded)
print(decoded)
