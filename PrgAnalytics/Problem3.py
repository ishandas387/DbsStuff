'''
Gets the number of occurances of each item in the list.
Calculates it based on storing it in a dictionary of item and count.
Prints the occurances looping through the dictionary.
'''
def find_number_of_occurances(list_of_items):
    dict_count={}
    for i in list_of_items:
        if(i in dict_count):
            dict_count[i] = dict_count.get(i) + 1
        else:
            dict_count[i] = 1
    print("The frequency of all elements in the list : ")
    for key,value in dict_count.items():
        print(str(key)+" occurs "+str(value)+" times")    

'''
Gets the user input based on validations.
If the input is list size, validates non zero and not negative.
For list item inputs, validates for value error as the list is 
expected for integers only.
'''
def get_user_input_with_validation(message,is_size_of_list_check = False):
    while True:
        try:
            u_input = (int)(input(message))
            if(is_size_of_list_check and u_input <= 0):
                print("Integer value greater than 0 expected!")
            else:
                return u_input
                
        except ValueError as v:
            print("Integer value expected!")    

#Displays the console and asks user for input.
print("#####################################")
print("WELCOME TO THE DBS CONSOLE")
print("#####################################")
number_of_items = get_user_input_with_validation("Input the number of elements to be stored in the list : ", True)
#empty list
list_of_items = []
print("Input "+str(number_of_items)+" elements in the list: ")
#add items to list from range zero to 
for i in range(0,number_of_items):
    item = get_user_input_with_validation("element - "+str(i+1)+" : ")
    list_of_items.append(item)

find_number_of_occurances(list_of_items)
