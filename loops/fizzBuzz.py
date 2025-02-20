# num % 3 == 0 return fizz
# num % 5 == 0 return buzz
# num % 3 == 0  num % 5 == 0 return fizzBuzz

def fizz_Buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
     print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
fizz_Buzz(30)

