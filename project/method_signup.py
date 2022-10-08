import re
from validator_collection import validators, errors
from method_validation import Validation


class Project_New_User:

    # Initializing the parameters
    def __init__(self):
        self.name = ""
        self.email = "email@site.com"
        self.user_id = "12314516"
        self.password = "A123@"

    # Dictionary creating method
    def signup(self):
        mydict = {}
        valid = Validation()
        print()
        # SignUp Menu
        print("*"*5, "Signup", "*"*5)
        self.name = input("Full Name: ")
        self.email = input("Email_id: ")

        print("User Id format either Uppercase, lowercase and digit\nmuch be 8 character long")
        self.user_id = input("Set Username: ")
        # Username Validation Method
        while True:
            bool = valid.validation_username(self.user_id)
            if bool:
                print("\nUsername already Taken\nChoice again")
                self.user_id = input("Set Username:")
            else:
                break

        self.password = input("Set Password: ")
        # Storing to dictionary
        mydict["Name"] = self.name
        mydict["Email_Id"] = self.email
        mydict["User_Id"] = self.user_id
        mydict["Password"] = self.password
        # returning the value
        return mydict

    # Getter preventing overwriting
    @property
    def email(self):
        return self._email

    # Setting value of email after validating
    @email.setter
    def email(self, email):
        while True:
            try:
                if validators.email(email, allow_empty=False):
                    self._email = email
                    break

            except errors.InvalidEmailError:
                print("Invalid Email Format")
                self._email = input("Enter Again? ")
                try:
                    if validators.email(self._email, allow_empty=False):
                        break
                except errors.InvalidEmailError:
                    continue

    # Getter for Username
    @property
    def user_id(self):
        return self._user_id

    # Setting and validating username
    @user_id.setter
    def user_id(self, user_id):
        while True:
            if re.search(r"^[a-zA-Z0-9]{8,20}$", user_id):
                self._user_id = user_id
                break

            else:
                print("Try Again? ")
                self._user_id = input("Set Username: ")
                if re.search(r"^[a-zA-Z0-9]{8,20}$", self._user_id):
                    break

    # Getter for Password
    @property
    def password(self):
        return self._password

    # Setting and validating Password
    @password.setter
    def password(self, password):
        while True:
            if re.search(r"[a-z]|[A-Z]|[0-9]{8,20}", password):
                self._password = password
                break

            else:
                print("Password must have atleast 8 character long")
                print("Try Again? ")
                self._password = input("Set Password: ")
                if re.search(r"[a-z]|[A-Z]|[0-9]{8,20}", self._password):
                    break

