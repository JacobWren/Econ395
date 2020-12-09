# Import the class Cobb Douglas class
# Create 2 instantiations of the class 
# Enter the information for each person using the objects into a dictionary
# Compute aggregate demand Total_Demand_x and Total_Demand_y
# Return both Total_Demand_x and Total_Demand_y

import string #because we use str to find the length of an int


# Make sure to copy and paste you CDDemand Class from the previous problem here

P_X = 10
P_Y = 20

class CDDemandException(Exception): pass


class CDDemand:
    def __init__(self, beta, income, ssn): 
        self.beta = beta
        self.income = income
        self.ssn = ssn
        if 0 >= self.beta >= 1 or len(str(self.ssn)) != 9:
            print("beta must be in the interval (0,1) and SSN is a 9 digit number")

    def demand_x(self):
        return ((1-self.beta)/(self.beta+(1-self.beta))) * (self.income/P_X)

    def demand_y(self):
        return ((self.beta)/(self.beta+(1-self.beta))) * (self.income/P_Y)


# start function. Why use a function here? Not needed but makes
# code resuability a bit easier

def main():
        #We instantiated 2 individuals. Remember the class is a blueprint
    #... Now we have actual people!
        person1 = CDDemand(0.5, 30000, 345677658)
        person2 = CDDemand(0.3, 100000, 222324529)
        #creat a nested dictionary
        demand_dict = {}
        # ssn is the main key. The 'key of keys'
        demand_dict[person1.ssn] = {}
        demand_dict[person1.ssn]['beta'] = person1.beta
        demand_dict[person1.ssn]['income'] = person1.income
        demand_dict[person1.ssn]['demand for x'] = person1.demand_x()
        demand_dict[person1.ssn]['demand for y'] = person1.demand_y()
        demand_dict[person2.ssn] = {}
        demand_dict[person2.ssn]['beta'] = person2.beta
        demand_dict[person2.ssn]['income'] = person2.income
        demand_dict[person2.ssn]['demand for x'] = person2.demand_x()
        demand_dict[person2.ssn]['demand for y'] = person2.demand_y()
	# Get aggregate demand for good x and y across the 2 individuals

        #Need to initialize incrementer variable
        Total_Demand_x = 0
        #for loop
        #k loops over each person via looping over their unique ssn
        # then once 'in' the ssn key (the main key) k finds the key named
        #demand for k. This key is nested and hence the double [][].
        #But remember, while k find the key, when we pass k and the nested key to the list
        #...demand_dict in our case. it returns the/a value.
        for k in demand_dict.keys():
                Total_Demand_x = Total_Demand_x + (demand_dict[k]['demand for x'])                      

        Total_Demand_y = 0 
        for k in demand_dict.keys():
                Total_Demand_y = Total_Demand_y + (demand_dict[k]['demand for y'])


        return(Total_Demand_y, Total_Demand_x)


