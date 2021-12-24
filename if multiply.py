a = int(input("Get one number from user"))
if a%3==0 and a%5==0:
    print ("your number is FizzBuzz")
elif a%3==0:
    print ("your number is Fizz")
elif a%5==0:
    print ("your number is Buzz")
else:
    print ("your number is invalid")

