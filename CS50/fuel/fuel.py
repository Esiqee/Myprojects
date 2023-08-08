def main():
    y, z = fuel()
    pct = y / z
    if pct <= 0.01:
        print("E")
    elif pct >= 0.99:
        print("F")
    else:
        print(f"{round(pct*100)}%")


def fuel():
    while True:
        try:
            x = input("Fraction: ")
            y, z = x.split('/')
            if (int(y) <= int(z)):
                return int(y), int(z)
        except (ValueError, ZeroDivisionError):
            print("Please enter valid input.")



main()