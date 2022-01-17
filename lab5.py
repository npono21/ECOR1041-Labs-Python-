#Completed November 17th, 2020
#Last Edited November 21st, 2020
#Author: Nicholai Ponomarev
#Student #101182048

#Excerise 1________________________________________________
def min_RRIF_withdrawl(balance: int, age: int) -> float:
    """Return the value of the minimum withdrawl from a RRIF
    >>>min_RRIF_withdrawal(4000.00)
    114.29
    >>>min_RRIF_withdrawal(3757.22)
    107.35
    >>>min_RRIF_withdrawal(0.00)
    0.0
    """
    return (balance)/(90-age)

#Exercise 2________________________________________________
def accrued_amount(principal: int, rate: int, period: int, time: int) -> float:
    """Return the accrued amount from an interest account. For logic purposes
    all inputs must be positive numbe or 0
    >>>accrued_amount(5000.00, 0.05, 4, 1)
    5254.73
    >>>accrued_amount(0.00, 0.50, 6, 2)
    0.0
    >>>accrued_amount(1000000.00, 0.1, 25, 30)
    19965703.01
    """
    return (principal)*((rate/period)+1)**(period*time)

#Exercise 1________________________________________________
min = min_RRIF_withdrawl(4000.00, 55)
print("The minimum withdrawl must be: $",round(min,2), "!")
#Produce a correct result, this is the most likely scenario.

min = min_RRIF_withdrawl(-4000.00, 55)
print("The minimum withdrawl must be: $",round(min,2), "!")
#Produces a mathematially correct answer but not logically correct.
#I would use some if statements here to make sure the user input is a positive
#or 0 number as well as the age is in beween 55 and 70.

min = min_RRIF_withdrawl(3757.22, 55)
print("The minimum withdrawl must be: $",round(min,2), "!")
#Input can also be a floating point value.

min = min_RRIF_withdrawl(0.00, 55)
print("The minimum withdrawl must be: $",round(min,2), "!")
#This is answer is both mathematically and logically correct. 
#If you have $0.00 in your account to begin with, you cannot withdraw anything.

#__________________________________________________________

#Excerise 2
principal_amount = accrued_amount(5000.00, 0.05, 4, 1)
print("The accrued amount is: $", round(principal_amount,2), "!")
#Any whole number int or float works.

principal_amount = accrued_amount(0.00, 0.50, 6, 2)
print("The accrued amount is: $", round(principal_amount,2), "!")
#An input of 0 does provide a logical answer.

principal_amount = accrued_amount(1000000.00, 0.1, 25, 30)
print("The accrued amount is: $", round(principal_amount,2), "!")
#Shows that the input is only limited by memory space.

principal_amount = accrued_amount(1000.00, -0.1, -25, 30)
print("The accrued amount is: $", round(principal_amount,2), "!")
#Shows that a negative rate and period still provide a mathematically correct
#answer according to the formula but it is an illogical operation because
#you cannot have a negative rate and you also cannot have a negative amount
#of compounding periods.

#__________________________________________________________

#Fun little twist:
principal_1 = int(input("What is the principle amount:"))
rate_1 = float(input("What is the rate of the investement:"))
period_1 = int(input("How many compounding periods are there:"))
time_1 = int(input("How many year would you like to invest for:"))
principal_amount = accrued_amount(principal_1, rate_1, period_1, time_1)
print(principal_amount)
print("The accrued amount is: $", round(principal_amount,2), "!")
#Fun little thing with user input. Much more lively program. 
#Works with the inputs of  5000, 0.05, 4, 1.