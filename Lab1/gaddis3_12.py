# Programming Exercise 3-12

# Named constants
RETAIL_PRICE = 99
disc_10_to_19 = .1
disc_20_to_49 = .2
disc_50_to_99 = .3
disc_100_plus = .4
#if elif else statements
def calculate_total_cost(purchase_count):
    if 9 < purchase_count < 20:
        discount_amount = RETAIL_PRICE * purchase_count * disc_10_to_19
    elif 19 < purchase_count < 50:
        discount_amount = RETAIL_PRICE * purchase_count * disc_20_to_49
    elif 49 < purchase_count < 100:
        discount_amount = RETAIL_PRICE * purchase_count * disc_50_to_99
    elif 99 < purchase_count:
        discount_amount = RETAIL_PRICE * purchase_count * disc_100_plus
    else: 
        discount_amount = 0
    #Total cost less the discount if any
    total_puchase_after_disc = (RETAIL_PRICE * purchase_count) - discount_amount
    #round to nearest cent
    total_puchase_after_disc = round(total_puchase_after_disc,2)
    discount_amount = round(discount_amount,2)
    
    return total_puchase_after_disc

#print(calculate_total_cost(12))
