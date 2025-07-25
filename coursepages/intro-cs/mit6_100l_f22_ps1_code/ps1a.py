## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
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
