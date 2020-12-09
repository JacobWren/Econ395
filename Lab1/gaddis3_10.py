# Programming Exercise 3-10

# Global variables
PENNY_VALUE = .01
NICKEL_VALUE = .05
DIME_VALUE = .10
QUARTER_VALUE = .25


def makes_a_dollar(num_pennies, num_nickels, num_dimes, num_quarters):
    #add up value for each coin
    penny_value = PENNY_VALUE * num_pennies
    nickel_value = NICKEL_VALUE * num_nickels
    dime_value = DIME_VALUE * num_dimes
    quarter_value = QUARTER_VALUE * num_quarters
    total_cent_value = quarter_value + dime_value + nickel_value + penny_value
    #return total_cent_value
    #boolean expression!
    if  total_cent_value == 1:
        return True
    else:
        return False
#print(makes_a_dollar(0,0,0,4))
    
