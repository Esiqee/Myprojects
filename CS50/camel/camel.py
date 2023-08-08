x = str(input("CamelCase: "))
y=""
for i in x:
    if(i.isupper()):
        y += "_" + i
    else:
        y += i
print(y.lower())
