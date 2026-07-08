#using a try and except

#try:

#input a number

# #print the number

#using value error

# except the value error and print the exception

#except ValueError as ex:

# print("Exception:", ex)
try:
    number=int(input("enter a number"))
    print(number)
except ValueError as ex:
    print("Exception:", ex) 