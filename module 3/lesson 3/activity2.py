#define function to calculate cube


#define a function which will execute cube function if the user entered number is divisible by 3

# if number %3 ==0:

#call the cube function and return the result

# else

#return False

#call the function
def cube (number):
    return number*number*number
def by_three(number):
    if number%3==0:
        return cube (number)
    else:
        return False
by_three(9)    
print(by_three(9))