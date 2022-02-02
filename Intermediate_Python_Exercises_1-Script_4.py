# Group Members: Ivory Steed, Paul Thottappilly, Hassan Chughtai, Tony Le, Shekar Balasubramaniam

# Links used for this exercise 
# https://stackoverflow.com/questions/55437419/how-to-use-the-try-except-command-in-a-while-loop-asking-for-user-input

endsum = 0
# Creates a for loop what will continue until user enters 5 ints
for x in range(5):
    # Using a while True block here allows the try block to always be executed to allow it to take in a user inputted integer
    while True:
        #Trys to take in the user input as an int and if it's an int it will add that number to the already existing endsum
        try:
            users_num = int(input("Please enter an integer: "))
            endsum = endsum + users_num
            break
        #If the user did not enter an int we will except a Value Error and tell the user to enter another int
        except ValueError:
            print("Invalid Input. Please enter an integer")
            continue

#Print out the sum
print('Your sum is:',endsum)