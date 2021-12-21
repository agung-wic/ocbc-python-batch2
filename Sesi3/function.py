# Python Function

# # Function definition
# def my_function(p, l):
#     '''Function to calculate area of square'''
#     print(p*l)

# def printme( str_input):
#     '''THis prints a passed string into this function'''
#     print(str_input)

# # Calling a Function
# def printme(str_input):
#     '''This prints a passed string into this function'''
#     print(str_input)

# printme("I'm first call to user defined function!")
# printme("Again second all to the same function")

# # Pass by reference vs value
# def changeme (my_list):
#     '''This changes a passed list into this function'''
#     my_list = my_list+[1,2,3,4]
#     print("\nValues inside the function: ", my_list)
#     return my_list

# my_list = [10,20,30]
# print("\nValues outside the function - before : ", my_list)

# my_list = changeme(my_list)
# print("\nValues outside the function - after : ", my_list)

# def changeour( mylist ):
#    '''This changes a passed list into this function'''
#    mylist = [1, 2, 3, 4] # This would assign new reference in mylist
#    print("Values inside the function (reference)  : ", mylist)

# # Now you can call changeour function (reference)
# mylist = [10, 20, 30]
# changeour( mylist )
# print("Values outside the function (reference) : ", mylist)

# # Function Arguments

# # required arguments
# def printme( str_input):
#     '''this prints a passed string into this function'''
#     print(str_input)

# printme("Hallo")

# # keyword argunment
# def printme( str_input):
#     '''this prints a passed string into this function'''
#     print(str_input)

# printme(str_input="Hactiv8")

# # default argument
# def printinfo( name, age=21):
#     ''' this prints a passed info into this function'''
#     print("Name : ", name)
#     print("Age : ", age)
#     print("")

# printinfo(age=50, name="Hactiv8")
# printinfo(name="Hactiv")

# # Variable length argument

# # *variable = tuple
# def printinfo( arg1, *vartuple ):
# # def printinfo(arg1, arg2, arg3, arg4):
#    '''This prints a variable passed arguments'''
#    print('arg1     : ', arg1)
#    print('vartuple : ', vartuple)
#    print('type vartuple : ', type(vartuple))
#    print('')

#    for var in vartuple:
#       print('isi vartuple : ', var)
# printinfo( 10 )
# printinfo( 70, 60, 50, "a" )

# # **variable = dictionary
# def person_car(total_data, **kwargs):
#   '''Create a function to print who owns what car'''
#   print('Total Data : ', total_data)
#   print("kwargs : ", kwargs)
#   print("type kwargs : ", type(kwargs))
#   for key, value in kwargs.items():
#     print('Person : ', key)
#     print('Car    : ', value)
#     print('')

# person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
# person_car(3)

# # The Anonymous Functions
# diff = lambda a, b : a-b

# print(type(diff))
# print(diff(10,2))
# print(diff(100,27))

# # return statement
# def multiply(a, b):
#     mul = a*b
#     return mul

# mul = multiply(10, 3)
# print("Function result ", mul)

# # global vs local variable
# total = 0
# def sum( arg1, arg2 ):
#    total = arg1 * arg2; 
#    print("Inside the function local total   : ", total)
#    return total

# # Call a function
# print("Outside the function global total - before : ", total)
# total = sum( 10, 20 )
# print("Outside the function global total - after : ", total)

# # doc string
# def sum_number(num1, num2):
#   '''
#   This function is used to sum of 2 variables.
#   :param num1: Input number 1 | int or float
#   :param num2: Input number 2 | int or float
  
#   :return: num3: Sum of number | int or float
#   '''

#   num3 = num1 + num2
#   return num3

# print(sum_number.__doc__)

def myFunction (a, b):
  sum = a+b
  subt = a-b
  return sum, subt

myNumber = myFunction(10, 2)

print(myNumber[0])