# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

# Links used for this exercise 
# https://www.quora.com/How-can-I-make-the-user-input-key-and-value-dictionary-in-Python-e-g-classe_list-input-name-score-wrong-syntax

from operator import itemgetter

#function that adds dict items with common keys
def get_combined_dict(dict_1, dict_2):
    # creates an empty dictionary
    firstdict = {}
    # combine dictionary elements with a common key
    for k, v in dict_1.items():
        if (k in dict_2.keys()):
            firstdict[k] = v + dict_2[k]
    # returns the new dictionary
    return firstdict

# Gets users to input how many elements they want in the dict
num = int(input("Enter number of elements for the dict: "))

#Takes user input and add them to dict1
class_dict_1 = dict()
for x in range(num): 
    data = input('Enter name & score separated by for dict1 ":" ') 
    temp = data.split(':') 
    class_dict_1[temp[0]] = int(temp[1]) 

#Takes user input and add them to dict2
class_dict_2 = dict()
for x in range(num): 
    data = input('Enter name & score separated by for dict2 ":" ') 
    temp = data.split(':') 
    class_dict_2[temp[0]] = int(temp[1]) 

# Displays the dictionary 
print('The content of dict 1 is: ') 
print(class_dict_1)
print('The content of dict 2 is: ')
print(class_dict_2)

#Calls the function
combined_dict = get_combined_dict(class_dict_1, class_dict_2)
print('The content of combined dict is: ')
print(combined_dict)