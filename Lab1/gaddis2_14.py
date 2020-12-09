# This program calculates the ending principal in a bank
# account after compounding the interest.

# intialize function
def calculate_principal_post_interest(principal, annual_interest_rate, compounds_per_year, years):
    # solve for the amount of money in the account after the specified number of years
    A = round(principal * (1 + (annual_interest_rate / 100) / compounds_per_year) ** (compounds_per_year * years), 2)
    return A


# What the user will input. We need four inputs
p = float(input("Enter the amount of principal originally deposited into the account: "))
r = int(input("Enter the annual interest rate paid by the account as a percentage: ")) / 100
n = int(input("Enter the number of times per year that the interest is compounded (For example, \n "
              "if interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.): "))
t = int(input("Enter the number of years the account will be left to earn interest: "))

Value = calculate_principal_post_interest(p, r, n, t)  # passing arguments to the ...
# function 'calculate_principal_post_interest'

# if statement to determine if year should be plural or not
if (t > 1):
    print("After ", t, " years, the amount of money that will be in the account will be $", format(Value, '.2f'), sep='')
else:
    print("After ", t, " year, the amount of money that will be in the account will be $", format(Value, '.2f'), sep='')
