    # MINI ACCOUNT INTERFACE
    #### Video Demo:  https://youtu.be/gUMlIxaYnCw
    #### Description: Project is based on How the SignUp and Login Process work for a Website. Account interface about the how a website work in background and MINI ACCOUNT INTERFACE just a overview with my perception, how a website work in background.

    #### The choice function asks User to choice what task they want to perform as user provided with Menu 1. SignUp for new user and 2. Login for existing user.If user choice Signup then it will call the new_user function or if user choice Existing User then it will call the exist_user function.

    #### Now in new_user function a instance of class method_signup is created to call a signup method in method_signup class to create a dictionary which stores the user details and return dictionary back to new_user function. The dictionary is written to json format file using dump method from json module.

    ####class method_signup is inside the method_signup.py program. Class name method_signup contain a constructor and signup method. Getting user input for email and a check method runs in background to check the validity of email using validation_collection module if user inputed wrong format of email, it prompt the user again and again until user input valid email id. Getting user input for username and a check method runs in background to check the format of username with the help of regular expression, if user inputed wrong format of username, it prompt the user again and again until user input right format of username. Getting user input for password and a check method runs in background to check the format of password with the help of regular expression, if user inputed wrong format of password, it prompt the user again and again until user input right format of password.

    ####If user is already existed then it can choice the 2nd option Existed User it will call the exist_user function. class method_login inside method_login.py program.
    ####Now in exist_user function a instance of class method_login is created to call a login_menu method in method_login class open json file which stores the user details in read only mode and ask user to input its Username and Password.
    ####Method also check for username whether user input valid username or not, if not prompt the user again and again. After asking for username and password, login_menu method call another method name logged_in from the same class to logged into account and show details given by user at the time of creating the account other than username and password. User can add addition details to its account such as Phone Number, Address, About. This can be done using the menu prompt for the user while login.
    ####If User chooses to Add Addition Detail, it call another method of class login_menu Add_detail which prompt user for what detail to add, user can choose according. User can add detail one by one, if user try to input multiple detail at a time it will cause an error which may lead to break down of code. Addition detail automatically added to json file into the user space.

    ####User can safely logout by choosing another option available other than ADD Detail.

    ####Method_validation.py contains Validation Class inside the class a method validation_username which check the username choose by user while creating the account. If username selected by user is already taken then it prompt the user to try another username.

    ####In short, New user can create account and login into the account using username and password and details such as Name and Email id are showed at first login and User can also add new details into the account simply by choosing Add Details from given menu. Also user can safely Logout from account. Logout option is also provided. Add single detail at a time for more efficient working of program.

    ## THIS FINAL PROJECT MINI ACCOUNT INTERFACE