from validator_collection import validators, errors


def main():
    print(email_address(input("Email Address:")))


def email_address(e_mail):

    try:
        if validators.email(e_mail, allow_empty = True):
            return "Valid"
        else:
            return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"


if __name__ == "__main__":
    main()