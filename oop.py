class book: 
  def __init__(self, title, author, pages):
    self.title = title  
    self.autor = author 
    self.pages  = pages
    self.isAvailable = True


  def borrow(self):
    if self.isAvailable:
      self.isAvailable = False
      print(f"you have borrowed {self.title}")

    else:
      print(f"sorry {self.title} is not available")


  def returnBook(self):
    self.isAvailable = True
    print(f"you have returned {self.title}")

bookA = book("the alchemist", "paulo coelho", 192)
bookB = book("the prophet", "kahlil gibran", 160)

book.borrow(bookA) #this will borrow the book
book.borrow(bookA) #this will not borrow the book because it is already borrowed




#user class

class user:
  def __init__(self, username, password):
    self.username = username
    self.__password = password # the double underscore makes it private

  def authenticate(self, password): 
    return self.__password == password 
    
user = user("hassan", "12345") #
print (user.authenticate("12345"))




# Base class representing a general user
class User:
    # Constructor method to initialize a user with a username
    def __init__(self, username):
        self.username = username  # Store the username in the instance

    # Method to simulate the user logging in
    def logIn(self):
        print(f"user {self.username} has logged in")  # Output a login message

# Subclass representing an admin, which is a special type of user
class Admin(User):  # Admin inherits from User
    # Method specific to Admin: accessing logs
    def accessLog(self):
        print(f"admin {self.username} has accessed the log")  # Output access log message

# Create an instance of the Admin class
admin = Admin("hassan")  # Instantiate an Admin object with the username "hassan"

# Call the inherited method from the User class
admin.logIn()  # This uses the method defined in the User class

# Call the method defined in the Admin class
admin.accessLog()  # This uses the method defined in the Admin class















