

name = input("Enter your name: ")
name2 = name

print ("welcome to the real world",name2) 


length = len(name2)
print("length of name is",length)


password = (input("enter your password"))
masked = ("*") * len(password)

print(masked)
print ("the length of your password is" , len(password))
firstChar = password[0]
secondChar = password[1]
thirdChar= password[2]
print("the three letters of your password are")
      
output = print(firstChar,secondChar,thirdChar, sep="*")



print(password [0:5])
print (password [5:])


lowerr = name2.lower()
upperr = name2.upper ()

print (lowerr, upperr)



## shti zyada ladada spaces for example
zyada = "     hassann  "
print (zyada.strip())


message = "the password is: bagzada2006$"
print (message.replace("bagzada2006$", "[hv854fxy]"))

## if u wanna split a string into two parts u can use this functio (split)
email = "hassan@gmail.com"
if email.find("@") !=1:
  print ("valid email")


hehe =email.split("g")[-1]
print (hehe)


emaoil = "hassan@gmail.com"

username = email.split("@")[0]
domain = email.split("@") [-1]

print ("username is", username)
print ("domain is", domain)


number = input("enter a number between 1-9")
print (number)

if int(number) < 5:
  print ("the number is less than 5")
  
elif int(number) == 5:
      print ("the number is 5")
  
else: 
  print ("the number you entered is greater than 5")

  

storedPassword = "bagzada2006"

enteredPassword = input("enter your password") 

if storedPassword == enteredPassword: 
  print ("welcome to the real world")

elif storedPassword != enteredPassword:
  print ("wrong password")















