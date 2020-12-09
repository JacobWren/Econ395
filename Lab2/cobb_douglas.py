# Part I: Define global vars, which are the prices
P_X = 10
P_Y = 20

# Define the class Cobb Douglas demand


class CDDemand:
    # these are the attributes. We want the attributes to initiliaze when we
    # call the class automatically (and they do!).
    def __init__(self, beta, income, ssn):
        # self is a place holder for when we instantiate the class!
        # For example, try vera (see below)
        self.beta = beta
        self.income = income
        self.ssn = ssn
        # conditional interval
        if 0 >= self.beta >= 1 or len(str(self.ssn)) != 9:
            print("beta must be in the interval (0,1) and SSN is a 9 digit number")
    # methods. They don't take any parameters
    def demand_x(self):
        return ((1-self.beta)/(self.beta+(1-self.beta))) * (self.income/P_X)

    def demand_y(self):
        return ((self.beta)/(self.beta+(1-self.beta))) * (self.income/P_Y)


# Test out your CDDemand class by instantiating a few instances of it.  
# vera = CDDemand(0.2, 100000, 123345611)
