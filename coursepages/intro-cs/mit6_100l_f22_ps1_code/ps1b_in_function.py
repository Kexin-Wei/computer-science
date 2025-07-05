def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	
	portion_down_payment = 0.25
	r = 0.05
	amount_saved = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	
	down_payment = portion_down_payment * cost_of_dream_home
	
	months = 0
	
	while amount_saved < down_payment:
	    monthly_saved_salary = yearly_salary * portion_saved / 12
	    new_money = amount_saved * r / 12
	    amount_saved += monthly_saved_salary
	    amount_saved += new_money
	    if months > 0 and months % 6 == 0:
	        yearly_salary *= 1 + semi_annual_raise
	    months += 1
	return months