
LoanAmount = int(input("Enter loan amount: "))
AnnualInterestRate = int(input("Enter annual interest rate: ")) / 100
LoanYearTerm = int(input("Enter loan term in years: "))

def CalcFixedMonthlyRate(Loan, AnnIntRate, LoanYearMaturity):
    LoanMonthMaturity = LoanYearMaturity * 12
    MonIntRate = AnnIntRate / 12
    DiscountValue = (1 + MonIntRate) ** LoanMonthMaturity
    MonthlyRepayments = 1 / (DiscountValue - 1)
    MonthlyRepayments = MonthlyRepayments * (MonIntRate * DiscountValue)
    MonthlyRepayments *= Loan

    return MonthlyRepayments


FixedMonthRepay = int(CalcFixedMonthlyRate(LoanAmount,  AnnualInterestRate, LoanYearTerm))
print("Your fixed monthly payments are: £" + str(FixedMonthRepay))
