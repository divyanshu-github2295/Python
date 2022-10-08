import json
from method_signup import Project_New_User
from method_login import Project_Login


def main():

    while True:
        choose = choice()
        # Matching User Choice
        match choose:
            case "1":
                new_user()
                break
            case "2":
                exist_user()
                break
            case _:
                print("Try Again!")
                print("1. New User: Signup\n2. Existed User: Login")


# User Choice
def choice():

    print("1. New User: Signup\n2. Existed User: Login")
    return input("Enter Choice? ")


# Signup New user
def new_user():

    # Instance of class
    create = Project_New_User()
    # Calling Class Method
    mydict = create.signup()
    with open("login_detail.json", "r+") as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside user_details
        file_data["user_detail"].append(mydict)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)
        file.close()


# Login User
def exist_user():
    signin = Project_Login()
    signin.login_menu()


if __name__ == "__main__":
    main()
