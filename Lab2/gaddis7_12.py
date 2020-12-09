# Questions: How do I remove the need for global count?

#start function
def is_prime(n):
    # define increment variable 
    count = 0
    # not prime if less than 1
    if n > 1:
        # check for divisibility - need to check every int up until n
        for i in range(2,n):
            if (n % i) == 0:
                count = count + 1          
    else:
        return False
    # count only incrments if n has a factor
    if count > 0:
        return False
    else:
        return True

# initialize an empty list. We will append to this list later on.
l = []
def list_primes(n):
    count1 = 0
    # all we are doing here is repeating what we did above but for every number
    #below n. And then if that number is prime, instead of returning True we
    #append that number to a list, l.
    # Notice, however in the range function we start at n and then increment
    #by -1
    for j in range(n,1,-1):
        if n > 1:
            for i in range(2,n):
                if (n % i) == 0:
                    count1 = count1 + 1

        if count1 == 0:
            l.append(n)
        count1 = 0
        n = n-1
    return l
