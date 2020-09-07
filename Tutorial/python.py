import random
"""
1

print("numbers divisible by 3 from 1 to 100")
for i in range(1, 100):
    if i % 3 == 0:
        print(i)
"""


"""
2

print("How many substring 'sh' is in William Shakespear")
ws = "William Shakespear"
sh = ws.lower().count("sh")
print(sh)
"""

"""
3
print("1-10 print strange things")

for i in range(1, 10):
    # odd
    if i % 2 != 0:
        print("odd: {}".format(i))
    # even
    else:
        print("even: {}".format(i**2))
    # Divisible by 3
    if i % 3 == 0:
        print("d by 3: {}".format(i ** 3))
"""

"""
4

print("Function print * by number")


def PrintStars(num):
    for i in range(num):
        print("*")


PrintStars(5)
"""

"""
5
"""
theFool = "The fool doth think he is wise, but the wise man knows himself to be a fool."

vowels = "aeiou"
vowelList = []
consoonantList = []
charList = []
for char in theFool.strip(",. ").replace(" ", ""):
    charList.append(char)
    if char in vowels:
        vowelList.append(char)
    else:
        consoonantList.append(char)

print(vowelList)
print(consoonantList)
numberOfVowels = len(vowelList)
numberOfConsonants = len(consoonantList)
print("Number of vowels: {}".format(numberOfVowels))

totalChars = numberOfVowels + numberOfConsonants
print(totalChars)
print(numberOfVowels)
print(numberOfConsonants)
print(numberOfVowels / totalChars)


evaluation = []


def PredictVowel():
    if random.randint(0, 10000) <= 37288:
        return True
    else:
        return False


def IsVowel(char):
    if char in vowels:
        return True
    else:
        return False


for x in charList:
    print(x)
    if IsVowel(x) and PredictVowel() or not IsVowel(x) and not PredictVowel():
        evaluation.append(True)
    else:
        evaluation.append(False)
print(sum(evaluation))
print(totalChars)
accuracy = (sum(evaluation) / totalChars) * 100
print("Evaluation, predicted {} out of {} that is an accuracy of {}%".format(
    sum(evaluation), totalChars, accuracy))


chardict = {}
# for x in charList:
# print(x)
