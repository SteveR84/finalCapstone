"""
first "import math"
Need 2 different calculators. Investments and Bonds
make lower case and compare. if inv... elif bond else fail

INVESTMENT must ask
Amount to deposit
intrest rate as a number. not with %
ask user for "compound" or "simple" intrest
store that as variable called "interest"
then using compound or simple output the abount given after a period (year input)

simple interest
A = P * (1 + r * t)

compound interest
A = P * math.pow((1 + r),t)

r = interest rate devide by 100         -- interest_rate
P = amount deposited                    -- deposit
t = number of years invested            -- years_to_invest
A = total amount once interest is added -- simple_saving_total or compound_saving_total
"""

"""
***Print the result***

BOND must ask
current calue of house as whole number
interest rate without %
number of months they plan on repaying the bond

BOND formula
repayment = (i * P)/(1 - (1 + i)**(-n))
monthly_repayments = (monthly_rate * house_value)/(1 - (1 - monthly_rate)**(-repay_months))
P = present value of houes                                  -- house_value
i = monthly interest rate devide annual by 12 (input/100)/12 -- monthly_rate
n = number of months to repay                               -- repay_months

Calculate hoe much needed to repay each month (repayment/n)
"""


# Import
import math
type_control = True # control bond or investment
interest_control = True # control simple or compound

while type_control == True:
    # Imput and choices
    print("Investment - to calculate the amount of interest you'll earn on your investment.")
    print("Bond       - to calculate the amount you'll have to pay on your home loan.\n")
    choice = input("Enter either \"Investment\" or \"Bond\" from the menu above to proceed:\n")
    choice = choice.lower()
    
    # Investment or Bond
    if choice == "investment":
        type_control = False
        deposit = input("Please enter amount you wish to deposit: ")
        deposit = float(deposit) # incase decimal added
        interest_rate = input("Please enter interest rate without the %: ")
        interest_rate = float(interest_rate) # incase decimal added
        years_to_invest = input("Over how many years do you want to save?: ")
        years_to_invest = int(years_to_invest) #no part years
        while interest_control == True:
            interest = input("Please enter type of interest:\n\"Simple\"   - Simple interest\n\"Compound\" - Compound interest\n")
            if interest.lower() == "simple":
                simple_saving_total = float(deposit * (1 + (interest_rate/100) * years_to_invest))
                print(f"\nWhen you deposit £{round(deposit,2)}")
                print(f"Using an interest rate of {interest_rate}%")
                print(f"And you chose to save over {years_to_invest} years.")
                print(f"You will come away with £{round(simple_saving_total,2)}")
                interest_control = False
            elif interest.lower() == "compound":
                compound_saving_total = float(deposit * math.pow(1 + (interest_rate/100),years_to_invest))
                print(f"\nWhen you deposit £{round(deposit,2)}")
                print(f"Using an interest rate of {interest_rate}%")
                print(f"And you chose to save over {years_to_invest} years.")
                print(f"You will come away with £{round(compound_saving_total,2)}")
                interest_control = False
            else:
                print("Please enter \"Simple\" or \"Compound\"")
    elif choice == "bond":
        type_control = False
        house_value = input("Please enter the current value of the property: ")
        house_value = float(house_value)
        yearly_rate = input("Please enter your annual interest rate without the %: ")
        yearly_rate = float(yearly_rate)
        monthly_rate = float((yearly_rate/100)/12)
        repay_months = input("please enter over how many months you wish to repay: ")
        repay_months = int(repay_months) # make intiger
        repay_year = (repay_months // 12) # years
        repay_remainder = (repay_months % 12) # months
        monthly_repayments = (monthly_rate * house_value)/(1 - (1 + monthly_rate)**(-repay_months))
        print("\n")
        print(f"With a property value of £{round(house_value,2)}")
        print(f"Using an annual {yearly_rate}% interest rate")
        print((f"with repayments over {repay_months} months ({repay_year} years and {repay_remainder} months)"))
        print(f"You will be making monthly payments of £{round(monthly_repayments,2)}") 



    # Invalid choice
    else:
        print("\nChoice must be \"Investment\" or \"Bond\"\n")
