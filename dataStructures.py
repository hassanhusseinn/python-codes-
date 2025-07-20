someNames = ["hassan", "ali", "ahmed", "hussain"]

#this will add the name at the end of the list(array)
someNames.append("bagzada")

#this will take another list of names and add it to the list that we want
someNames.extend(["bagzada2006", "bagzada2007", "bagzada2008"])

print (someNames)


#if u wannna remove something u will use this function

someNames.remove("ali")

print (someNames)

#also to clear u will use this function

someNames.clear()

print (someNames)

#to use loops in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22,33,45,24]


highActivity = [attempt for attempt in numbers if attempt > 5]

print (highActivity)

#city name lastName and age they are called keys they each have a value 
dictionaries = {
  "city": "erbil",
  "name": "hassan",
  "last name": "bagzada",
  "age": int("19")
}

dictionaries["email"] = "bagzada@gmil.com"

print (dictionaries)




#also if u wanna change some of the existing ones u can just rewrite it like that

dictionaries["last name"] = "mahmmood"

print (dictionaries)

print (dictionaries.get("name"))

for key, value in dictionaries.items():
 print (f"{key}: {value}")


#nested dictionaries 
nestedDic = {
  "person1": {"name ": "hassan", "age": 19},
  "person2": {"name ": "ali", "age": 20},
  "person3": {"name ": "ahmed", "age": 21}
}

print(nestedDic.get("person1"))



#sets

newSet = {1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 22,33,45,24}#it will only show the 8 value once 

newList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22,33,45,24]
#the difference between them is that sets dont allow duplicate values and also they dont have an order but lists do and they allow duplicate values

print (newSet, newList)