"""
Personal Finance Calculator
Student: [Your Name]
Date: [Today's Date]
Purpose: Calculate monthly budget and savings
"""
#รับค่า
monthly_income =float(input("User's monthly income in THB : "))
rent_cost =float(input("Monthly rent/housing cost : "))
food_budget =int(input("Monthly food budget in THB : ")) 
transportation_cost =float(input("Monthly transportation expenses : "))
entertainment_budget =int(input("Monthly entertainment budget : "))
emergency_fund_percent =float(input("Percentage to save for emergency (e.g., 10.5) : "))
investment_percent =float(input("Percentage to invest (e.g., 15.0) : "))
#คำนวณค่าใช้จ่าย
TotalFixedExpenses = rent_cost + transportation_cost
TotalVariableExpenses = food_budget + entertainment_budget
TotalExpenses = TotalFixedExpenses + TotalVariableExpenses
RemainingIncome = monthly_income - TotalExpenses
#คำนวณเงินออมและเงินลงทุน
EmergencyFundAmount = monthly_income *(emergency_fund_percent / 100)
InvestmentAmount = monthly_income * (investment_percent / 100)
AvailableforSavings = RemainingIncome - EmergencyFundAmount - investment_percent
ExpenseRatio = (TotalExpenses / monthly_income) * 100
#แสดงค่าต่างๆ
print("=== MONTHLY BUDGET REPORT ===")
print("Income :",monthly_income," THB")
print("Fixed Expenses : ",TotalFixedExpenses," THB")
print("Variable Expenses : ",TotalVariableExpenses," THB")
print("Total Expenses : ",TotalExpenses," THB")
print("Remaining : ",RemainingIncome," THB")

print("=== SAVINGS BREAKDOWN ===")
print("Emergency Fund (10%) : ",EmergencyFundAmount," THB")
print("Investment (15%) : ",InvestmentAmount," THB")
print("Available for Savings : ",AvailableforSavings," THB")

print("=== ANALYSIS ===")
print("Expense Ratio : ",ExpenseRatio,"%")