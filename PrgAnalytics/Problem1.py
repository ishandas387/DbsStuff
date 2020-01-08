#Get the extra hours worked based on user input and constant standard working week
def get_extra_hours(STANDARD_WORKING_WEEK, number_of_hours_worked):
    if(number_of_hours_worked > STANDARD_WORKING_WEEK):
        return number_of_hours_worked -STANDARD_WORKING_WEEK
    else:
        return 0

#gets the string back without whitespaces.
def valid_string(input):
    return str(input).strip()

'''
Gets the user input based on the message passed. A flag to check if string value is expected.
If A string is expected- normal none-empty validations takes place.
It is also expected for the user to input either float or integer for the numerical value input.
Validations in place for value err if, it is not a numeric value.
'''
def get_user_input(message, is_string_expected = False):
    while True:
        #gets the input
        u_input = input(message+" : ")
        try:
            #if string expected, validate with not empty.
            if(is_string_expected):
                if(valid_string(u_input)):
                    return u_input
                else:
                    print("Not a valid input. Empty!")
                    continue
            else:
                #if numeric value expected. Can be float or int
                if "." in u_input :
                    u_input = float(u_input)
                else:
                    u_input = int(u_input)
                return u_input
        #catches any level of value err.        
        except ValueError:
            print("Invalid value, Please enter again.")                    

#Gets the earnings based on hours worked and hourly rate.
def get_earning(STANDARD_WORKING_WEEK, number_of_hours_worked, hourly_rate):
    if(STANDARD_WORKING_WEEK < number_of_hours_worked):
        return STANDARD_WORKING_WEEK * hourly_rate
    else:
        return number_of_hours_worked * hourly_rate

#Gets the earning for overtime if any extra hour.
def get_earning_overtime(extra_hours,overtime_rate):
    if(extra_hours > 0):
        return extra_hours * overtime_rate
    else:
        return 0    

#Checks if non zero tax rate. Return the calculted value on normal.
def get_tax_on_normal(earning_normal,standard_tax_rate):
    if(standard_tax_rate != 0):
        return (earning_normal * standard_tax_rate)/100

#Checks if non zero tax rate. Return the calculated value on overtime.
def get_tax_on_overtime(earning_overtime,overtime_tax_rate):
    if(overtime_tax_rate != 0 and overtime_tax_rate != 0):
        return (earning_overtime * overtime_tax_rate)/100

#Prints the payslips with alignment. Takes a dictionary with all the values pre calculated.
def print_payslip(dict_of_payslip):
    total_pay = dict_of_payslip.get("earning_normal")+dict_of_payslip.get("earning_overtime")
    total_deduction = dict_of_payslip.get("tax_on_normal")+dict_of_payslip.get("tax_on_overtime")
    net_pay = total_pay - total_deduction

    print("\t\t\t\t\t P A Y S L I P \t\t\t\t\t")
    print("WEEK ENDING ",dict_of_payslip.get("weekending"))
    print("Employee: ",dict_of_payslip.get("name"))
    print("Employee Number: ",dict_of_payslip.get("number"))
    print("\t\t\t\tEarnings\t\t\tDeductions ")
    print("\t\t\t\tHours\tRate\tTotal ")
    print("Hours (normal)\t\t\t"+str(dict_of_payslip.get("number_of_hours_worked"))+"\t"+str(dict_of_payslip.get("hourly_rate"))+"\t"+str(dict_of_payslip.get("earning_normal"))+"\t\tTax @ "+str(dict_of_payslip.get("standard_tax_rate"))+"% "+str(dict_of_payslip.get("tax_on_normal")))
    print("Hours (overtime)\t\t"+str(dict_of_payslip.get("extra_hours"))+"\t"+str(dict_of_payslip.get("overtime_rate"))+"\t"+str(dict_of_payslip.get("earning_overtime"))+"\t\tTax @ "+str(dict_of_payslip.get("overtime_tax_rate"))+"% "+str(dict_of_payslip.get("tax_on_overtime"))+"\n")
    print("\t\t\t\tTotal Pay:\t\t\t\t"+str(total_pay))
    print("\t\t\t\tTotal deduction:\t\t\t"+str(total_deduction))
    print("\t\t\t\tNet Pay:\t\t\t\t"+str(net_pay))
  
#Get the user inputs   
employee_name = get_user_input("Enter employee name", True)
employee_number = get_user_input("Enter employee number",True)
STANDARD_WORKING_WEEK = 37.5
#A dictionary for storing values.
dict_of_payslip ={"name": employee_name, "number": employee_number}
dict_of_payslip["weekending"] = get_user_input("Enter weekending DD/MM/YYYY",True)
dict_of_payslip["number_of_hours_worked"] = get_user_input("Enter number of hours worked")
dict_of_payslip["hourly_rate"] = get_user_input("Enter hourly rate")
dict_of_payslip["overtime_rate"] = get_user_input("Enter overtime rate")
dict_of_payslip["standard_tax_rate"] = get_user_input("Enter standard tax rate")
dict_of_payslip["overtime_tax_rate"] = get_user_input("Enter overtime tax rate")
dict_of_payslip["extra_hours"] = get_extra_hours(STANDARD_WORKING_WEEK, dict_of_payslip.get("number_of_hours_worked"))
dict_of_payslip["earning_normal"] = get_earning(STANDARD_WORKING_WEEK, dict_of_payslip.get("number_of_hours_worked"), dict_of_payslip.get("hourly_rate"))
dict_of_payslip["earning_overtime"] = get_earning_overtime(dict_of_payslip.get("extra_hours"), dict_of_payslip.get("overtime_rate"))
dict_of_payslip["tax_on_normal"] = get_tax_on_normal(dict_of_payslip.get("earning_normal"), dict_of_payslip.get("standard_tax_rate"))
dict_of_payslip["tax_on_overtime"] = get_tax_on_overtime(dict_of_payslip.get("earning_overtime"), dict_of_payslip.get("overtime_tax_rate"))
#print the payslip
print_payslip(dict_of_payslip)


