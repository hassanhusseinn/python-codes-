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
    return self.__password == password #this will return true if the password is correct and false if it is not
    
user = user("hassan", "12345") #this will create a new user
print (user.authenticate("12345")) #this will return true because the password is correct 















