'''
Validates the user input and returns the splitted result.
If after split the list doesm't have 2 values, the input doesn't
satisfy the domain/username format.
'''
def validate_and_return(message):
    while True:
        user_name = input(message)
        #splits with '\'
        data = str(user_name).split("\\")
        if(len(data) != 2):
            print("Not in proper format")
            print("Expected:: Domain\\username")
            continue
        else:
            return data    

#user input and result
print("###################################")
print("WELCOME TO THE DBS CONSOLE")
print("###################################")
data = validate_and_return("Please enter the username: \n")
print("Domain : ",str(data[0]))
print("Username : ",str(data[1]))
