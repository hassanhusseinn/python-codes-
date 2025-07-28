with open("hehe file.txt", "w") as file:
  file.write("hello world")

with open ("hehe file.txt", "r") as file:
  content = file.read()  
  print (content)



#if u wanna take the usernamefrom the user and write it inside a file u will do it like so

username = input("enter your username: ")

with open ("username.txt", "a") as file: 
 file.write(username + "\n") 
 print("username has been saved to the file")


with open ("username.txt", "r") as file:
  for names in file:
    print ("username: " + names.strip())



#if u wanna write long strings u will use this function or this method 

namess = ["hassan\n", "ali\n", "ahmed\n", "hussain\n"]

with open ("username.txt", "a") as file:
  file.writelines(namess)

#and another method will be this one 



with open ("username.txt", "r") as file:
   line = file.readline()
   while line:
    print(line.strip())
    line = file.readline()

    

#to handle file errors u will use the try and except method

try:
  with open ("username.txt", "r") as file:
    content = file.read()
    print (content)

except: 
  print("file not found") #what this will do it will search for the file if it doesnt find it it will print the error message









