def part_c(initial_deposit):
	#########################################################################
	down_payment = 800000 * 0.25
	months = 36
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	steps = 0
	r_range = [0, 1]
	r = 0
	# f(r) = initial_deposit * (1 + r/12) - down_payment <=0
	# f'(r) = initial_deposit / 12
	
	threshold = 100
	while 1:
	    if steps == 0 and (
	        initial_deposit > down_payment or initial_deposit > (down_payment - threshold)
	    ):
	        r = 0
	        break
	    if steps == 0 and initial_deposit * (1 + 1 / 12) ** months < down_payment:
	        r = None
	        break
	
	    r = (r_range[0] + r_range[1]) / 2
	    amount_saved = initial_deposit * (1 + r / 12) ** months
	
	    if abs(amount_saved - down_payment) < 100:
	        break
	
	    if amount_saved > down_payment:
	        r_range[1] = r
	    else:
	        r_range[0] = r
	    print(f"steps: {steps}, amount: {amount_saved}, down: {down_payment} r: {r}")
	    steps += 1
	print(r)
	return r, steps