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


