"""
program Life Insurance Calculator.py
author:  Lisa Kilmer
last modified:
This is a Life Insurance Calculator that helps the client determine how much more life insurance they need to protect
their family if they die.  It considers annual income that family needs and subtracts other income the family has like
other spouse income or interest and dividends or social security.  Takes that amount and calculates how much capital
there needs to be if invested at 5% return to generate the amount needed.  It doesn't use the principle.  Adds in final
expenses, college costs for children if they want and debt that would want paid off if they died.  totals all the assets
nonqualified and qualified and the present amount of life insurance.  Subtracts need from assets to determine additional
life insurance needed if any.
"""

import tkinter as tk
from tkinter import *
from tkinter import ttk
import os
data = {}
college_cost = {}
class LifeInsuranceCalculator(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Life Insurance Need Calculator')

        container = ttk.Frame(self)
        container.grid(padx=60, pady=30, sticky='EW')

        frame = Calculator(container)
        frame.grid(row=0, column=0, sticky="NSEW")


class Calculator(ttk.Frame):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)

        self.text = tk.Text(self, width=75, height=10, wrap=WORD)
        self.text.grid(row=10, column=0, columnspan=4)

        label = tk.Label(self, text="Calculator to determine how much life insurance you need to protect your family")
        label.grid(row=0, column=0, sticky='W')

        self.income_value = tk.IntVar()
        self.other_inc_value = tk.IntVar()
        self.answer = tk.StringVar()
        self.college_cost = tk.IntVar()
        self.debt = tk.IntVar()
        self.savings = tk.IntVar()
        self.retirement = tk.IntVar()
        self.present_amount = tk.IntVar()

        ttk.Label(self, text="Total annual income your family needs: ").grid(row=1, column=0, sticky=W)
        ttk.Entry(self, width=10, textvariable=self.income_value).grid(row=1, column=1, sticky=W)

        ttk.Label(self, text="annual income your family has besides your income: ").grid(row=2, column=0, sticky=W)
        ttk.Entry(self, width=10, textvariable=self.other_inc_value).grid(row=2, column=1, sticky=W)
        Button(self, text="Submit", command=self.family_need).grid(row=2, column=3, sticky=E)

        ttk.Label(self, text="Do you want to consider college cost for your children: Y/N").grid(row=3, column=0, sticky=W)
        ttk.Entry(self, width=10, textvariable=self.answer).grid(row=3, column=1, sticky=W)

        ttk.Label(self, text="College costs for children: ").grid(row=4, column=0, sticky=W)
        ttk.Entry(self, width=10, textvariable=self.college_cost).grid(row=4, column=1, sticky=W)
        Button(self, text="Submit", command=self.college).grid(row=4, column=3, sticky=E)

        ttk.Label(self, text="total debt, mortgage and other:  ").grid(row=5, column=0, sticky=W)
        ttk.Entry(self, width=10, textvariable=self.debt).grid(row=5, column=1, sticky=W)
        Button(self, text="Submit", command=self.cap_required).grid(row=5, column=3, sticky=E)

        ttk.Label(self, text="Total saving and investments: ").grid(row=6, column=0, sticky=W)
        ttk.Entry(self, width=10, textvariable=self.savings).grid(row=6, column=1, sticky=W)
        ttk.Label(self, text="Total Retirement savings: ").grid(row=7, column=0, sticky=W)
        ttk.Entry(self, width=10, textvariable=self.retirement).grid(row=7, column=1, sticky=W)
        ttk.Label(self, text="Present amount of life insurance you have: ").grid(row=8, column=0, sticky=W)
        ttk.Entry(self, width=10, textvariable=self.present_amount).grid(row=8, column=1, sticky=W)
        Button(self, text="Submit", command=self.assets).grid(row=8, column=3, sticky=E)

        Button(self, text="reset", command=self.restart_program).grid(row=9, column=2, sticky=E)
        # finds income to be replaced, determines capitol invested at 5% to generate income needed. Doesn't use principle
    def family_need(self):
        a = self.income_value.get()
        b = self.other_inc_value.get()
        annual_need = a-b
        family_needs = annual_need / .05
        data.update({'family_need': family_needs})
        self.text.insert(tk.INSERT, "Total family needs: $" + str(family_needs))

    def college(self):  #determines college need for children if client died
        if self.answer.get().upper() == 'Y':
            total_college_cost = self.college_cost.get()
            data.update({'college': total_college_cost})
            self.text.insert(tk.INSERT, '\nTotal college costs: $' + str(total_college_cost))
        else:
            self.text.insert(tk.INSERT, "\nNo college costs")

    def cap_required(self):  #total capital need:  final expenses, debt, college, famiy need
        final_expenses = 25000
        debt = self.debt.get()
        sub_cap_required = debt + final_expenses
        data.update({'cap_required': sub_cap_required})
        self.text.insert(tk.INSERT, '\nOther costs include final expenses, $' + str(final_expenses) + ' and debt $' +
            str(debt) + ' totaling $' + str(sub_cap_required))

        total_capital = sum(data.values())
        data.update({'total_capital_required': total_capital})
        self.text.insert(tk.INSERT, '\nTotal capital required is $' + str(total_capital))

    def assets(self):  # totals all the assets available for family need and subtracts from capital required
        savings = self.savings.get()
        retirement = self.retirement.get()
        present_amount = self.present_amount.get()
        total_assets = savings + retirement + present_amount
        data.update({'assets': total_assets})
        self.text.insert(tk.INSERT, '\nTotal assets available are $' + str(total_assets))

        t = data.get('total_capital_required')
        a = data.get('assets')
        life_insurance = t - a
        if life_insurance > 0:
            self.text.insert(tk.INSERT, '\nAdditional life insurance need: $' + str(life_insurance))
        else:
            self.text.insert(tk.INSERT, '\nNo additional life insurance needed')

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return or save data"""
        python = sys.executable
        os.execl(python, python, *sys.argv)


root = LifeInsuranceCalculator()
root.mainloop()

"""
test data
set1: 150,000: 50,000: Y: 60,000: 300,000: 50,000: 250,000: and 100,000 = $2,385,000 additional need
set2: 100,000: 50,000: n: 0 college cost: 100,000: 500,000: 500,000: 200,000 = no additional life insurance needed
"""