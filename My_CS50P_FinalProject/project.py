from cs50 import SQL
from tabulate import tabulate


print("""
+---------------------------------------------------------------------------+
|                          Welcome in CS50 Company                          |
|                                                                           |
|          This program is designed to keep evidence of your team.          |
|    You can add, manage, view, or delete personal data in this program.    |
|            This program stores all of your data in a database.            |
+---------------------------------------------------------------------------+
""")


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///database.db")


def main():
    while True:


        print("""
+---------------------------------------------------------------------------+
|      Please select your action by writing one of following commands:      |
|                                                                           |
| To add a new person in DB:  Type "A"                                      |
| To manage person data:      Type "M"                                      |
| To view table of employees: Type "V"                                      |
| To delete person:           Type "D"                                      |
| To end this program:        Type "E"                                      |
+---------------------------------------------------------------------------+
""")


        action = input("Action: ")

        if action.upper() == "A":
            add(*getdata_add())


        elif action.upper() == "M":
            manage(getdata_manage())

        elif action.upper() == "V":
            view(*getdata_view())

        elif action.upper() == "D":
            delete(getdata_del())


        elif action.upper() == "E":
            break

        else:
            print("""
+---------------------------------------------------------------------------+
|                           ERROR: INVALID ACTION!                          |
+---------------------------------------------------------------------------+
""")


    print("""
+---------------------------------------------------------------------------+
|                              Program ended...                             |
+---------------------------------------------------------------------------+
""")



""" _______________ Functions under this line _______________ """




def add(n, d, p, t, j):
    # Add person to DB (arguments: name, dob, position, team, joined)

    # Query database for username
    rows = db.execute("SELECT * FROM people WHERE name = ?", n)
    # If person already exists, return error
    if len(rows) == 1:
        print("""
+---------------------------------------------------------------------------+
|                     ERROR : THIS PERSON ALREADY EXISTS                    |
+---------------------------------------------------------------------------+
""")
        return 1

    db.execute("INSERT INTO people (name, dob, position, team, joined) VALUES (?, ?, ?, ?, ?)", n, d, p, t, j)
    print("""
+---------------------------------------------------------------------------+
|                        Person succesfully added :)                        |
+---------------------------------------------------------------------------+
""")
    return 0



def getdata_add():
    # Get user data for add function
    try:
        name  = input("Name: ")
        dob = int(input("Date of birth: "))
        position = input("Position: ")
        team = input("Team: ")
        joined = int(input("Joined: "))
        return name, dob, position, team, joined
    except ValueError("ValueError"):
        return 1



def manage(name):
    # Manage person data
    # Query database for username
    rows = db.execute("SELECT * FROM people WHERE name = ?", name)
    # If person exists, ask what to change
    if len(rows) == 1:
        print(f"""
+---------------------------------------------------------------------------+
|      You are editing data of {name:<8}, what would you like to change?     |
+---------------------------------------------------------------------------+
| To change date of birth:    Type "1"                                      |
| To change position:         Type "2"                                      |
| To change team:             Type "3"                                      |
| To change year joined:      Type "4"                                      |
+---------------------------------------------------------------------------+
""")

        change = input("Action: ")
        if change == "1":
            new = input("Updated date of birth: ")
            db.execute("UPDATE people SET dob = ? WHERE name = ?", new, name)
        elif change == "2":
            new = input("Updated position: ")
            db.execute("UPDATE people SET position = ? WHERE name = ?", new, name)
        elif change == "3":
            new = input("Updated team: ")
            db.execute("UPDATE people SET team = ? WHERE name = ?", new, name)
        elif change == "4":
            new = input("Updated year joined: ")
            db.execute("UPDATE people SET joined = ? WHERE name = ?", new, name)
        else:
            print("""
+---------------------------------------------------------------------------+
|                           ERROR: INVALID ACTION!                          |
+---------------------------------------------------------------------------+
""")
        return 0


    else:
        raise ValueError("""
+---------------------------------------------------------------------------+
|                     ERROR : THIS PERSON DOESN'T EXIST                     |
+---------------------------------------------------------------------------+
""")



def getdata_manage():
    # Get data for manage function
    name  = input("Who you want to edit?: ")
    return name



def getdata_view():
    # Get input for view action
    dbfile = db.execute("SELECT name, dob, position, team, joined FROM people")
    return dbfile



def view(*dbfile):
    # Print table of employees
    headers = dbfile[0].keys()
    rows = [list(row.values()) for row in dbfile]
    print()
    print(tabulate(rows, headers=headers, tablefmt="grid"))



def getdata_del():
    # Get user data for del function
    name  = input("Who you want to delete from DB?: ")
    return name



def delete(name):
    # Delete person from DB

    # Query database for username
    rows = db.execute("SELECT * FROM people WHERE name = ?", name)
    # If person doesnt exists, return error
    if len(rows) != 1:
        print("""
+---------------------------------------------------------------------------+
|               ERROR : YOU CANNOT DELETE NON-EXISTING PERSON               |
+---------------------------------------------------------------------------+
""")
        return 1

    # If person  exists, delete person
    if len(rows) == 1:
        db.execute("DELETE FROM people WHERE name = ?", name)
        print("""
+---------------------------------------------------------------------------+
|                       Person succesfully deleted :)                       |
+---------------------------------------------------------------------------+
""")
        return 0








if __name__ == "__main__":
    main()