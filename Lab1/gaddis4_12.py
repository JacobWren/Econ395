# Programming Exercise 4-11


def factorial(number): #factorial function
    fact = number # set fact equal to number
    while (number > 1): # want to subtract 1 from number until number = 1
        number = number - 1
        #print(number)
        fact = round(fact * number, 2) # this is the part that computes the
        #factorial. 
        return fact
    #print(fact)
#print(factorial(3))



'''
7*6 = 42
42 * 5 = 210
210 * 4 = 840
840 * 3 = 2520
2520 * 2 = 5040
5040 * 1 = 5040
done
'''
