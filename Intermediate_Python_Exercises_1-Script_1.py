# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

# Links used for this exercise 
# https://www.geeksforgeeks.org/python-get-a-list-as-input-from-user/
# https://www.w3resource.com/python-exercises/python-functions-exercise-8.php

def uniquelist(y):
    # creates an empty list
    emptylist = []
    # iterates through the list
    for x in y:
        # appends unique values on to a new list
        if x not in emptylist:
            emptylist.append(x)
    return emptylist

# creates an empty list
mylist = []
inputs = int(input("Enter number of elements for the list: "))
 
# iterates through the range in the list
for i in range(0, inputs):
    # enter in elements for the list
    element = int(input("Enter element: " ))
    mylist.append(element)

print(uniquelist(mylist))

