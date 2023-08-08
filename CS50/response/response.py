from validator_collection import checkers


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    is_email_address = checkers.is_email(s)
    if is_email_address == True:
        return "Valid"
    if is_email_address == False:
        return "Invalid"



if __name__ == "__main__":
    main()