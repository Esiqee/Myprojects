months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        x = input("Date: ").strip()
        m, d, y = x.replace("/", " ").replace(",", "").split(' ')
        if m in months and "," in x:
            m = months[m]
        if (0 < int(d) < 31) and (0 < int(m) < 12):
            break
    except ValueError:
        print("Please enter valid input.")

# i have here strange issue with formatting of leading 0 it yields 80 instead oof 08 so i need to fix it in str way adding leading zero if d<10
#print(d)
#d = f"{d:02}"
#print(d)

if int(d) < 10:
    d = "0" + str(d)
if int(m) < 10:
    m = "0" + str(m)

print(f"{y}-{m}-{d}")