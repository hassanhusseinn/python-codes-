userInfo = {}#u could also add some existing users here so that the program will check if the user is already registered or not

# this function is for the registry part 
def register():

    username = input("Enter your username: ")

    if username in userInfo:
        print("Username already exists. Please choose a different one.")
    else:
        password = input("Enter your password: ")
        userInfo[username] = password
        print("Registration successful!")
       



# and this one is for the existing users its the login part
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in userInfo and userInfo[username] == password:
      print("log in succesful babyyyyyyyy")
    else:
      print("wrong username or password")







def authenticationSystem():
  while True:
  
    print("welcome to the authentication system") 
    print("choose one of the options below")
    print("1) register")
    print("2) login") 
    print("3) exit")
  
    option = input("enter your choice")  # ✅ Now this line is inside the function
  
    if option == "1":
      register()
    elif option == "2":
      login()
    elif option == "3": 
      print("you chose to exit the program so bye")
    else: 
      print("invalid option")

# to run the program
authenticationSystem()
