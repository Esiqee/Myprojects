price = 50

while True :
    print(f"Amount Due: {price}")
    x = int(input("Insert Coin: "))
    if x == 25 or x == 10 or x == 5:
        price = price - x
        if price <= 0:
            break
print("Change Owed:", price * -1)

