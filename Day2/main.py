#Data Types

#String

print('Hello'[4])
print('123'+'345')

#Integer

print(123 + 345)

#Float

3.1428

#Boolean

True
False


num_char = len(input('What is your name? '))

# type checking
print(type(num_char))

# string conversion

print('Your name has ' + str(num_char) + ' characters')

a = 123
print(type(a))

a = str(123)
print(type(a))

# mathematical functions

print(8/3)
print(int(8/3))
print(round(8/3))
print(round(8/3, 2))

print(8/3, 8//3)
print(type(8/3), type(8//3))

# f-String

score = 0
height = 1.8
isWinning = True

print('Your score is ' + str(score) + ', your height is ' + str(height) + ', you are winning ' + str(isWinning))

print(f'Your score is {score}, your height is {height}, you are winning {isWinning}')