class smallapp:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()

    def menu(self):
        user_input=input("""How are YOU!!
                         1.click 1 to sign up
                         2.click 2 to sign in
                         3.click 3 t0 write a post
                         4.click 4 to message a friend
                         5.clcik any key to exit""")
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.signin()
        elif user_input=="3":
            pass
        elif user_input=="4":
            pass
        else:
            exit()

    def signup(self):
        email=input("enter your email")
        pas=input("enter your password here")
        self.username=email
        self.password=pas
        self.menu()
    
    def signin(self):
        if self.username==''and self.password=='':
            print("please click 1 to sign up")
        else:
            ema=input("enter the username")
            ps=input("enter the password")
            if self.username==ema and self.password==ps:
                print("you have successfuly sign in")
                self.loggedin=True
            else:
                print("please input correct information")
        self.menu()

    # def postwriting(self):
    #     post=input("enter your post")

abhi=smallapp()