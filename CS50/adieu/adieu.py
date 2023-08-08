kids = []

while True:
    try:
        name = input("Name: ")
        kids.append(name)

    except EOFError:
        if len(kids) == 1:
            print(f"Adieu, adieu, to {kids[0]}")
        elif len(kids) == 2:
            print(f"Adieu, adieu, to {kids[0]} and {kids[1]}")
        elif len(kids) > 2:
            print("Adieu, adieu, to ", end="")
            for i in range(len(kids) - 1):
                print(kids[i], end=", ")
            print(f"and {kids[-1]}")
        else:
            print("Error")
        break
        
