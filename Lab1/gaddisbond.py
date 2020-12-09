# Programming Exercise Bond Value

def bond_value(C, i, M, N):
        PV_value_of_coupons = 0 # have to define this in the function
#because we have an assignment statement below. When you have an assignment
#statement in a function it ignores any variables defined outside of the
#function.
        for j in range(1,N+1):
                #this is an assignment statement
                PV_value_of_coupons = PV_value_of_coupons + C/(1+i)**j
                #print(PV_value_of_coupons)
        PV_face_value = M/(1+i)**N #this is outside the for loop, only 1 coupon
        Price = round(PV_value_of_coupons + PV_face_value,2)
        return Price

      
	
