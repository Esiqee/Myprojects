#CS50 Company

##Video Demo: https://youtu.be/LtOkGUR5Txc

###Description:

    Welcome to the CS50 Company!

    This program is designed to help you keep track of data for your employees. It utilizes two libraries: SQL from cs50 and tabulate.

    With this program, you can perform various tasks such as adding new employees, updating existing records, deleting entries, and retrieving employees details.
    It aims to streamline the process of managing and organizing your workforce data efficiently.

    Thanks to user friendly CLI is this program really easy to use.

    After we start the program following message will greet you to introduce program shortly:
    +---------------------------------------------------------------------------+
    |                          Welcome in CS50 Company                          |
    |                                                                           |
    |          This program is designed to keep evidence of your team.          |
    |    You can add, manage, view, or delete personal data in this program.    |
    |            This program stores all of your data in a database.            |
    +---------------------------------------------------------------------------+


    After you can follow the on-screen instructions to navigate through the program:
    +---------------------------------------------------------------------------+
    |      Please select your action by writing one of following commands:      |
    |                                                                           |
    | To add a new person in DB:  Type "A"                                      |
    | To manage person data:      Type "M"                                      |
    | To view table of employees: Type "V"                                      |
    | To delete person:           Type "D"                                      |
    | To end this program:        Type "E"                                      |
    +---------------------------------------------------------------------------+

    After typing in your instruction program will execute following tasks:

    1 Add person to the database, wich is made of 2 functions wich will get input from user, validate it and save person data in database.

    2 Manage person data will execute following:

        +---------------------------------------------------------------------------+
        |      You are editing data of {name:<8}, what would you like to change?     |
        +---------------------------------------------------------------------------+
        | To change date of birth:    Type "1"                                      |
        | To change position:         Type "2"                                      |
        | To change team:             Type "3"                                      |
        | To change year joined:      Type "4"                                      |
        +---------------------------------------------------------------------------+

        This user interface will friendly guide you trough the changing of data of your employees.

    3 Will output table of all current people in database for example:

        +--------+-------+-------------------+------------+----------+
        | name   |   dob | position          | team       |   joined |
        +========+=======+===================+============+==========+
        | John   |  1987 | Programmer        | Coding 1   |     2022 |
        +--------+-------+-------------------+------------+----------+
        | Peter  |  1992 | Senior Programmer | Coding 1   |     2016 |
        +--------+-------+-------------------+------------+----------+
        | Evelyn |  1979 | HR Manager        | Management |     2007 |
        +--------+-------+-------------------+------------+----------+
        | Thomas |  1987 | Data Sciencist    | Data 1     |     2019 |
        +--------+-------+-------------------+------------+----------+

    4 Is simple function wich will check current DB, and delete person we prompted.

    5 Will end our program


    After exitting the program all data will be saved in our DB so we can safely store all the data without missing them,
    and it will be accessible everytime we run the program.


    Test_project.py was designed to proof that our functions in Project are fully working and tested

    Have a nice user experience while working with CS50 Company!