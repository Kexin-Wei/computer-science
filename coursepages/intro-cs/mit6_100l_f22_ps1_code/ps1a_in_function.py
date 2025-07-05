def part_a(yearly_salary, portion_saved, cost_of_dream_home):
	#########################################################################
	
	portion_down_payment = 0.25
	amount_saved = 0
	r = 0.05
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	
	down_payment = portion_down_payment * cost_of_dream_home
	monthly_saved_salary = yearly_salary * portion_saved / 12
	
	months = 0
	while amount_saved < down_payment:
	    new_money = amount_saved * r / 12
	    amount_saved += monthly_saved_salary
	    amount_saved += new_money
	    months += 1
	return months