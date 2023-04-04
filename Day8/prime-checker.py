#Approach 1
#Write your code below this line 👇

def prime_checker(number):
    count = 0
    for n in range(number):
        if number % (n+1) == 0:
            count += 1
    if count == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#Approach 2
#Write your code below this line 👇

def prime_checker(number):
    for n in range(number-2):
        if number % (n+2) == 0:
            print("It's not a prime number.")
            return
    print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)