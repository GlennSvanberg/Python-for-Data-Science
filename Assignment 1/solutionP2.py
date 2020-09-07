
def WidthFromInput(str):
    try:
        value = int(input(str))
        if value <= 0:
            print("Come on, it must be more than zero?")
            return WidthFromInput(str)
        else:
            return value
    except:
        print("That's not a valid length!")
        return WidthFromInput(str)


a = WidthFromInput("Enter the width of the plinth at the highest level : ")
b = WidthFromInput("Enter the width of the plinth at ground level : ")

floors = a-b

volume = 0
height = 1
depth = 2

while b >= a:
    volume = volume + (height * depth * b)
    b = b - 1

if volume <= 0:
    print("The plinth must be thicker in the bottom than in the top!")
else:
    print("Volume of plinth: ", volume)
