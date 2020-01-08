#phone book
#display menu
def print_menu():
    print()
    print("#######################")
    print("MYPY PHONE BOOK ")
    print("#######################")
    print("1 : Add New Entry")
    print("2 : Delete Entry")
    print("3 : Update Entry")
    print("4 : Lookup Number")
    print("5 : QUIT")

#choice
def print_choice():
    while True:
        choice = input("would you like to add this entry? (y/n) : ")
        if(choice.lower() == "y"):
            return True
        elif(choice.lower() == "n"):
            return False   
        else:
            print("y/n only!")

#adding a new entry to the phone book
def add_new_entry(phone_book, user_name, user_phone_number):
    if not phone_book:
        phone_book[user_phone_number] = user_name
        print("Added to phone book.")
        return
    if(user_phone_number in phone_book):
        #restricts the user from adding duplicate number
        print("We already have this phone number registered")
    else:
        phone_book[user_phone_number] = user_name
        print("Added to phone book.")


'''Updates the phone book entry. If The phone_book is empty, gives an option to user to add it.
   If a number is found, user is updating the name. If A name is found in the value, user must be updating the number.
   Incase of number update, the old number key is deleted. A new entry is added to phone_book.
'''
#updating an entry
def update_entry(phone_book,user_name,user_phone_number):
    if not phone_book:
        print("The phone book seems empty at the moment")
        if(print_choice()):
                phone_book[user_phone_number]= user_name
    else:
        #if the phone number is same, user is updating the name
        if(user_phone_number in phone_book.keys()):
            phone_book[user_phone_number] = user_name
            print("Updated phone book.")
        else:
            for key,value in phone_book.items():
                if(user_name == value):
                    key_to_delete = key
                    found_key = True
            if(found_key):
                try:
                    #remove the entry
                    del phone_book[key_to_delete]
                    #add new one
                    phone_book[user_phone_number] = user_name
                    print("Updated phone book.")
                except KeyError as e:
                    print("Key error: phone number not found to delete")    
            else:
                #if nothing matches, just add it as a new one
                print("No matches found to update! ")
                if(print_choice()):
                    phone_book[user_phone_number]= user_name
                    print("Added to phone book.")


'''Looks up a phone number in the phone_book. If not found asks the user if they want to add it.
If found displays the full name and number'''
#loookup
def look_up(user_phone_number, phone_book):
    if(user_phone_number in phone_book):
        print(str(phone_book.get(user_phone_number))+" :: "+str(user_phone_number))
    else:
        print("No matches found!")
        if(print_choice()):
            user_name = get_user_input_name("Please enter the user name : ")
            phone_book[user_phone_number]= user_name
            print("Added to phone book.")


'''Deletes by namme or number, based on user choice'''
#delete
def delete(phone_book):
    print("1. Delete by Name ")
    print("2. Delete by Number ")
    u_inp = input("Enter mode of delete : ")

    if(u_inp =="1"):
        #if delete by name, ask user to input name
        u_name = get_user_input_name("Enter name: ")
        #loop through the phone_book values to get a match
        #if a match found note the key
        to_be_deleted = None
        for key,value in phone_book.items():
            if(str(value).lower() == str(u_name).lower()):
                to_be_deleted = key
            
        if(to_be_deleted is not None):
            #deletes the noted key.       
            del phone_book[to_be_deleted]   
            print("Entry deleted.") 
        else:
            print("Name not found!")

    elif(u_inp =="2"):
        #if delete by number, ask user to input number
        user_phone_number = get_user_input_number("Enter the number: ")
        #if found in phone_book, delete by key
        if(user_phone_number in phone_book.keys()):
            del phone_book[user_phone_number]
            print("Entry deleted.")   
        else:
            print("Number not found!")    

#input function for name, defined separately in case user name validation takes place
def get_user_input_name(message):
    #place for any validation that can take place on user name
    #sample validation of length check
    while True:
        u_input = input(message)
        if(len(u_input) > 100):
            print("Name too long!")
            continue
        return u_input

#input function for number, validates number
def get_user_input_number(message):
    while True:
        try:
            u_input = (int)(input(message))
        except ValueError:
            print("Please enter a number ")
        else:
            if(len(str(u_input)) > 10):
                print("Seems like the number is greater than 10 digits, please check!")
                continue
            return u_input

#An empty dictionary
phone_book ={}

while(True):
    print_menu()
    user_choice = input("Enter your choice : ")
    if(user_choice == "5"):
        print(phone_book)
        print("bye!")
        break
    elif(user_choice == "1"):
        user_name = get_user_input_name("Please enter user full name : ")
        user_phone_number = get_user_input_number("Please enter user phone number : ")
        add_new_entry(phone_book,user_name,user_phone_number)
    elif(user_choice =="2"):
        delete(phone_book)
    elif(user_choice =="3"):
        user_name = get_user_input_name("Please enter user full name : ")
        user_phone_number = get_user_input_number("Please enter user phone number : ")
        update_entry(phone_book,user_name,user_phone_number)
    elif(user_choice =="4"):
        user_phone_number = get_user_input_number("Please enter user phone number : ")
        look_up(user_phone_number,phone_book)
    else:
        print("Wrong choice!")

