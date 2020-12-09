# Programming Exercise 4-11


def factorial(number): # factorial function
    fact = number # set fact equal to number
    while (number > 1): # want to subtract 1 from number until number = 1
        number = number - 1
        fact = round(fact * number, 2) # this is the part that computes the factorial. 
        return fact
    
#print(factorial(3))

