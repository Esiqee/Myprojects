x = str(input("Greeting: "))

if x.lower().strip().startswith("hello"):
    print("$0")
elif x.lower().strip().startswith("h"):
    print("$20")
else:
    print("$100")
