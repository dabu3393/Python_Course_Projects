#Follows PEMDASLR

print('Welcome to the Tip Calculator')
bill = input('What was the total bill?')
tip_percentage = input('What percentage tip would you like to give? 10, 12, or 15?')
amount_people = input('How many people will split the bill?')

bill_float = float(bill)
percentage_int = int(tip_percentage)
people_int = int(amount_people)

total_bill = bill_float + (bill_float * (percentage_int/100))
payment = round(total_bill / people_int, 2)
print(f'Each person should pay: {payment}')