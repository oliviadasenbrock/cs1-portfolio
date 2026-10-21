#LoanPayment.py



"""This program receives the loan principal, annual interest rate, number of
years, and returns the monthly loan payment to the user"""

def loan_payment(P, I, Y):
    loanPayment = (P * (I / 12)) / (1 - (1 + (I / 12)) ** (-12 * Y))
    return loanPayment


principal1 = int(input("Enter the loan amount:"))

interest1 = float(input("Enter annual rate as a decimal:"))

years1 = int(input("Enter the number of years of the loan:"))

print()

monthlypayment = loan_payment(principal1, interest1, years1)

totalpayment = monthlypayment * 12 * years1

totalinterest = totalpayment - principal1

print(f"The monthly payment will be ${monthlypayment:.2f}")

print(f"The total payments over {years1} years will be ${totalpayment:.2f}")

print(f"The total interest paid over {years1} years will be ${totalinterest:.2f}")

print()

print("Loan Amorization Table:")

print()

print("Month \t Interest Payment \t Principal Payment \t Remaining Balance")

remaining = principal1

for month in range(1, 12 * years1 + 1):
    interest = remaining * (interest1) * (1 / 12)
    P_payment = monthlypayment - interest
    remaining -= P_payment
    print(month, "\t \t", end="")
    print(round(interest, 2), "\t\t\t", end="")
    print(round(P_payment, 2), "\t\t\t\t", end="")
    print(round(remaining, 2), "\t")