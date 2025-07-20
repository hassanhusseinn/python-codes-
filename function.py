name = input("enter your name")



def greet(name):

  print ("hello "+name) 
  
greet(name)


passwords = ["bagzada2006", "bagzada2007", "bagzada2008"]

passwords.append("bagzada2009")

print (passwords)

#and when we have another set ofnames we can use the extend function

newpasswords = ["bagzada2010", "bagzada2011", "bagzada2012"]

passwords.extend(newpasswords) 

print (passwords)


