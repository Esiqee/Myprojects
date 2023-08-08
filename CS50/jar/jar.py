class Jar:
    def __init__(self, capacity=12):
        if capacity < 1:
            raise ValueError("Must be a non-negative integer")
        self._capacity = capacity
        self._n = 0


    def __str__(self):
        return f"🍪"*self._n

    def deposit(self, n):
        if self._n + n > self._capacity:
            raise ValueError("Oops.... Jar will be so full, that it explodes")
        self._n += n

    def withdraw(self, n):
        if self._n - n < 0:
            raise ValueError("Not enough cookies :(")
        self._n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n


def main():
    try:
        x = int(input("Size of jar: "))
        jar = Jar(x)
        while True:
            y = int(input("""
---------------------------------------
Please choose one of following actions:
---------------------------------------
For deposit type '1'
For withdraw type '2'
If you want to end application type '3'
---------------------------------------\n"""))
            if y == 1:
                d = int(input("How much cookies do you want to deposit?\n"))
                jar.deposit(d)
                print(f"Jar contains {jar} cookies")
            elif y == 2:
                d = int(input("How much cookies do you want to withdraw?\n"))
                jar.withdraw(d)
                print(f"Jar contains {jar} cookies")
            elif y == 3:
                print(f"Jar is closed with {jar} cookies")
                break
            else:
                raise ValueError("Incorrect Value")


    except ValueError:
        print("Incorrect Value")


if __name__ == "__main__":
    main()