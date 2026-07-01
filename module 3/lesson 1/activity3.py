# 1) Define a function `add(P, Q)` that returns the sum of two numbers (P + Q).
def add(num_1,num_2):
    sum=num_1+num_2
    return sum
# 2) Define a function `subtract(P, Q)` that returns the difference of two numbers (P - Q).
def  subtract(num_1,num_2):
    diff=num_1-num_2
    return diff
# 3) Define a function `multiply(P, Q)` that returns the product of two numbers (P * Q).
def  multiply(num_1,num_2):
    multi=num_1*num_2
    return multi
# 4) Define a function `divide(P, Q)` that returns the division result of two numbers (P / Q).
def  division(num_1,num_2):
    divi=num_1/num_2
    return divi
print ("Please select the operation.")

print ("a. Add")

print ("b. Subtract")

print ("c. Multiply")

print ("d. Divide")


choice = input("Please enter choice (a/ b/ c/ d): ")


num_1 = int (input ("Please enter the first number: "))

num_2 = int (input ("Please enter the second number: "))


if choice == 'a':

  print (num_1, " + ", num_2, " = ",add(num_1,num_2))


elif choice == 'b':

  print (num_1, " - ", num_2, " = ",subtract(num_1,num_2) )


elif choice == 'c':

  print (num_1, " * ", num_2, " = ",multiply(num_1,num_2) )

elif choice == 'd':

  print (num_1, " / ", num_2, " = ",division (num_1,num_2))

else:

  print ("This is an invalid input")
  