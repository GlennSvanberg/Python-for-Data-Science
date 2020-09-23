"""
frog
jump over river 11 feet long with 10 stones, either jump 1 or 2 feet and not jump back
how many ways is there for the frog to jump over the river?
"""


def frog(feet):
    if feet == 0:
        return 1
    elif feet < 0:
        return 0
    return frog(feet-1) + frog(feet-2)


print(frog(10))
