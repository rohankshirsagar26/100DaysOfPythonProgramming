print('Welcome to the tip calculator.')
billAmount = input('What was the total bill? $')
tipPercentage = input('What percentage tip would you like to give? 10, 12, or 15? ')
noOfPeople = input('How many people to split the bill? ')
eachPersonContribution = (float(billAmount) / int(noOfPeople)) * ((100+int(tipPercentage))/100)
print(f'Each person should pay: ${round(eachPersonContribution, 2)}')