# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

# Links used for this exercise 
# https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/

def repeated_letter_dict(string):
    # Makes all the letters in the strings lowercase
    string = string.lower()
    #Replace all of the spaces with no space at all
    string = string.replace(" ", "")

    # Create a dict that holds all the repeated letters 
    repeat_dict = {}
    # Create a for loop that will make x equal to each character
    for x in string:
        #Createz an if statement that then checks if x (each character of the string) is found within the dict 
        # if it's true then add one to the value of that specific character within the dict
        if x in repeat_dict:
            repeat_dict[x] = repeat_dict[x] + 1
        # if x (each character of the string) is not found in the dict then you add that character to the dict and set it equal 1
        else:
            repeat_dict[x] = 1
    
    print(repeat_dict)

# Allows you to test this function
user_string = input("Enter a string: ")
repeated_letter_dict(user_string)