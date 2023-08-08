import random


def main():
    level = get_level()
    i = 0
    score = 0
    while i < 10:
        j = 0
        x, y = generate_integer(level)
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if x+y == answer:
                    score += 1
                    i += 1
                    break
                elif j == 2:
                    print(f"{x} + {y}= {x+y}")
                    i += 1
                    break
                else:
                    print("EEE")
                    j += 1
            except (ValueError):
                if j == 2:
                    print(f"{x} + {y}= {x+y}")
                    i += 1
                    break
                else:
                    print("EEE")
                    j += 1
    print("Score: ", score)

def get_level():
    # get valid lvl input
    while True:
        try:
            lvl = int(input("Level: "))
            if 0 < lvl <= 3:
                break
            else:
                print("Please enter valid input.")
        except (ValueError):
            print("Please enter valid input.")

    return lvl


def generate_integer(level):
    # generate random nubers in base of lvl
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x,y

if __name__ == "__main__":
    main()