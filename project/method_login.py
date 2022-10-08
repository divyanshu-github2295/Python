import json
import sys


class Project_Login:

    # Initializing the parameters
    def __init__(self):
        self.user_id = ""
        self.password = ""

    # Validation of Username and Password
    def login_menu(self):

        # Open login_detail file
        with open("login_detail.json", "r") as detail:
            login_detail = json.load(detail)

        # Storing all Usernames
        user_ids = []
        for i in range(len(login_detail["user_detail"])):
            user_ids.append(login_detail["user_detail"][i]["User_Id"])

        # Login Menu
        print()
        print("*"*5, "LOGIN", "*"*5)

        # Validation of username
        self.user_id = input("Username: ")
        while True:
            if self.user_id not in user_ids:
                print("\nInvalid Username\nTry Again?")
                self.user_id = input("Username: ")
            else:
                break

        self.password = input("Password: ")
        self.logged_in()

    # Login into Account
    def logged_in(self):
        # open login_detail file
        with open("login_detail.json", "r") as detail:
            login_detail = json.load(detail)

        # Matching username and password
        for i in range(len(login_detail["user_detail"])):
            if login_detail["user_detail"][i]["User_Id"] == self.user_id:
                if login_detail["user_detail"][i]["Password"] == self.password:
                    print()
                    # To show details of user
                    self.personal_details(**login_detail["user_detail"][i])
                    # Menu for User
                    print("\n", "*"*5, "MENU", "*"*5)
                    print("\n1.Add Details\n2.Logout")
                    # Choice from Menu
                    choice = input("Enter Choice? ")
                    # Checking the choice
                    if choice == "1":
                        # Adding new detail of user
                        self.Add_detail(i)
                    elif choice == "2":
                        print()
                        # Logging out the user
                        sys.exit("Thanks for Using\nVisit Again")
                    break
                else:
                    # If user Input Wrong Password
                    print("\nInvalid Password\nTry Again?")
                    print("Username:", self.user_id)
                    self.password = input("Password: ")
                    continue

    # To show Details after login
    def personal_details(self, **details):
        print("*"*5, "PERSONAL DETAIL", "*"*5, "\n")
        for key, value in details.items():
            if key != "User_Id" and key != "Password":
                print(f" {key} : {value}")

    # Add new details
    def Add_detail(self, i):

        add_detail = {}
        print("Which detail you want to add?")
        print("1.Phone Number\n2.Address\n3.About\n4.Return to Account")
        choice = input("Enter Choice? ")

        with open("login_detail.json", "r+") as detail:
            # Load Existing data from json in Dict
            login_detail = json.load(detail)

            if choice == "1":
                # Adding Phone Number in user details
                phone = input("Enter Phone Number: ")
                add_detail["Phone Number"] = phone
                login_detail["user_detail"][i].update(add_detail)
                detail.seek(0)
                json.dump(login_detail, detail, indent=4)
                detail.close()
                self.logged_in()

            elif choice == "2":
                # Adding Address in user details
                address = input("Enter your Address: ")
                add_detail["Address"] = address
                login_detail["user_detail"][i].update(add_detail)
                detail.seek(0)
                json.dump(login_detail, detail, indent=4)
                detail.close()
                self.logged_in()

            elif choice == "3":
                # Adding about yourself in user details
                about = input("Write about yourself: ")
                add_detail["About"] = about
                login_detail["user_detail"][i].update(add_detail)
                detail.seek(0)
                json.dump(login_detail, detail, indent=4)
                detail.close()
                self.logged_in()
            else:
                detail.close()
                self.logged_in()

