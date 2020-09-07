from math import sqrt


def LengthFromInput(side):
    try:
        value = input("Enter the length of side {}: ".format(side))
        if float(value) <= 0:
            print("Come on, the side must be longer than that?")
            return LengthFromInput(side)
        else:
            return float(value)
    except:
        print("That's not a valid length!")
        return LengthFromInput(side)


def PrintNotATriangle():
    print("That is impossible! \nNo triangle can have sides with the length of {}, {}, & {}".format(a, b, c))


a = LengthFromInput("a")
b = LengthFromInput("b")
c = LengthFromInput("c")

perimeter = a + b + c
p = perimeter / 2.0

try:
    area = sqrt(p * (p - a) * (p - b) * (p - c))
    if area > 0:
        print("Perimeter: ", perimeter)
        print("Area: ", area)
    else:
        PrintNotATriangle()

except:
    PrintNotATriangle()
