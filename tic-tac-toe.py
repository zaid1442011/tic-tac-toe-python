import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

paper = "{0} | {1} | {2}"

values = [" ", " ", " " ," ", " ", " ", " ", " ", " "]

def print_paper():
    print(paper.format(values[0], values[1], values[2]))
    print(paper.format(values[3], values[4], values[5]))
    print(paper.format(values[6], values[7], values[8]))

print_paper()

while not((" " != values[0] == values[1] == values[2] or " " != values[0] == values[3] == values[6] or " " != values[0] == values[4] == values[8] or " " != values[1] == values[4] == values[7] or " " != values[2] == values[5] == values[8] or " " != values[3] == values[4] == values[5] or " " != values[6] == values[7] == values[8] or " " != values[0] == values[1] == values[2] or " " != values[3] == values[4] == values[5] or " " != values[6] == values[7] == values[8] or " " != values[0] == values[4] == values[8] or " " != values[2] == values[4] == values[6]) or (values[0] and values[1] and values[2] and values[3] and values[4] and values[5] and values[6] and values[7] and values[8] != " ")):

    user = input("Choose where do you want to place X: ")
    data = int(user) - 1
    user = None
    cls()
    if values[data] == " ":
        values[data] = "X"
        cls()
    else:
        data = None
        user = input("Try another move X")
        data = int(user) - 1
        user = None
        cls()
        if values[data] == " ":
            values[data] = "X"
            cls()
        else:
            raise TypeError("Only numbers are allowed")
    
    print_paper()


    if (" " != values[0] ==  values[1] == values[2] or " " != values[0] ==  values[3] == values[6] or " " != values[0] ==  values[4] == values[8] or " " != values[1] ==  values[4] == values[7] or " " != values[2] ==  values[5] == values[8] or " " != values[3] ==  values[4] == values[5] or " " != values[6] ==  values[7] == values[8] or " " != values[2] ==  values[4] == values[6]) or (values[0] and values[1] and values[2] and values[3] and values[4] and values[5] and values[6] and values[7] and values [8] != " "):
        break


    user = input("Choose where do you want to place O: ")
    data = int(user) - 1
    user = None
    cls()
    if values[data] == " ":
        values[data] = "O"
        cls()
        
    else:
        data = None
        user = input("Try another move O")
        data = int(user) - 1
        user = None
        cls()
        if values[data] == " ":
            values[data] = "O"
            cls()
        else:
            raise TypeError("Only numbers are allowed")

    print_paper()
