"""
program:  life_insurance_calculator.py
author:  Lisa Kilmer
last modified:  7/15/2020
This is the basic functions for my life insurance calculator.  I will build my GUI around this and modify where needed.
"""


college_cost = {}
data = {}

    # finds income to be replaced, determines capitol invested at 5% to generate income needed. Doesn't use principle
def family_need():
    annual_income = int(input("Total Annual income that your family needs: "))
    other_sources = int(input("amount of annual income your family has besides your income: "))
    annual_need = annual_income - other_sources
    family_needs = annual_need/.05
    data.update({'family_need': family_needs})
    print("Total family needs: $" + str(family_needs))

    #college costs for children if want to include.  It lets them determine how much want to cover of costs
def college():

    answer = input("Would you like to consider college costs for your children? Y/n:  ")
    if answer == 'Y':
        n = int(input("How many children: "))
        for i in range(n):
            child_name = input("What is your child's name: ")
            cost_school = int(input("College cost for " + child_name + ' $'))
            college_cost.update({child_name: cost_school})
            total_college_cost = sum(college_cost.values())
            data.update({'college': total_college_cost})
        print('Total college costs: $' + str(total_college_cost))

    else:
        print("No college costs")

        # adds in final expenses and debt to payoff
def cap_required():
    final_expenses = 25000
    debt = int(input("How much is your total debt, mortgage and other: "))
    sub_cap_required = debt + final_expenses
    data.update({'cap_required': sub_cap_required})
    print('Other costs include final expenses, $' + str(final_expenses) + ' and debt $' + str(debt) + ' totaling $' + str(sub_cap_required))

        #adds the final expenses, debt, college costs, and family income needs
def total_capital_required():
    total_capital = sum(data.values())
    data.update({'total_capital_required': total_capital})
    print('Total capital required is $' + str(total_capital))

    #total existing assets
def assets():
    savings = int(input("Total saving and investments: "))
    retirement = int(input("Total Retirement savings: "))
    present_amount = int(input("Present amount of life insurance you have: "))
    total_assets = savings + retirement + present_amount
    data.update({'assets': total_assets})
    print('Total assets available are $' + str(total_assets))

    # Total capital required minus assets
def additional_needed():
    t = data.get('total_capital_required')
    a = data.get('assets')
    life_insurance = t - a
    print('Additional life insurance need: $' + str(life_insurance))


if __name__ == '__main__':
    family_need()
    college()
    cap_required()
    total_capital_required()
    assets()
    additional_needed()




