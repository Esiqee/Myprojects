grocery = []
count = {}

while True:
    try:
        item = input("").upper()
        grocery.append(item)


    except EOFError:
        for item in grocery:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1

        for item in sorted(count):
            print(count[item], item)
        break