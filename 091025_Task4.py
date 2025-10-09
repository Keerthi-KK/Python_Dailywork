user_name_stored="Keerthi"
mail_id_stored="kkeerthikanagaraj@gmail.com"
password_stored="Keerthi_123"

username =input("Enter user name : ")
if username==user_name_stored:
    print("Valid username")
    mailid=input("Enter your mail id : ")
    if mailid==mail_id_stored:
        print("valid mail id ")
        password=input("Enter your password")
        if password==password_stored:
            print("Login Successful !!")
        else:print("invalid password,Try again ")
    else:print ("Not a valid mail id")
else:
    print ("Not a valid username")
