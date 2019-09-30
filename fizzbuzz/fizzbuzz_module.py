""" 
Exercise:

1. Write a program, that prints the numbers from 1 to 100. (Implement the `main` function).

2. Modify the program as following:
   - for multiples of three, print "Fizz" instead of the number,
   - for the multiples of five, print "Buzz",
   - for numbers which are multiples of both three and five, print "FizzBuzz".

   Implement the `fizzbuzz` function so that it returns the correct value to print.
 """

def fizzbuzz(number):
    if (number % 3) == 0 and (number % 5) == 0:
        return "FizzBuzz"
    elif (number % 3) == 0:
        return "Fizz"
    elif (number % 5) == 0:
        return "Buzz"
    else:
        return number


def main():
    for i in range(100):
        print(fizzbuzz(i + 1))
    return

if __name__ == '__main__':
    main()