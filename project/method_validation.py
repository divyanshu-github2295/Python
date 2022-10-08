import json


class Validation:
    # Initializing the username
    def __init__(self):
        self.username = ""

    # Username validation for while signing up
    def validation_username(self, username):
        with open("login_detail.json", "r") as detail:
            login_detail = json.load(detail)

        for i in range(len(login_detail["user_detail"])):
            if login_detail["user_detail"][i]["User_Id"] == username:
                return True

