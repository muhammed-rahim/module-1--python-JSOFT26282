r"""Python learning worksheet: algorithms, flowchart, and programs.

Largest-of-three flowchart shapes:

    (START)                         Oval: Start/End
       |
    / Read a,b,c /                  Parallelogram: Input/Output
       |
    < a >= b and a >= c? >         Diamond: Decision
      / Yes       \ No
     v             v
 [largest=a]   < b >= a and b >= c? >
  Rectangle      / Yes       \ No
               v             v
          [largest=b]    [largest=c]  Rectangle: Process
                 \       /
               / Print largest /     Parallelogram: Output
                      |
                    (END)
"""


def largest_of_three():
    """Find and return the largest of three numbers."""
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))

    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    print("Largest number:", largest)
    return largest


def check_prime():
    num = int(input("Enter a number to check prime: "))

    if num <= 1:
        print("Not a prime number")
        return

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Not a prime number")
            return

    print("Prime number")


def check_even_or_odd():
    num = int(input("Enter a number to check even or odd: "))
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def print_grade():
    mark = int(input("Enter your mark out of 100: "))

    if mark >= 90:
        print("Grade A")
    elif mark >= 75:
        print("Grade B")
    else:
        print("Grade C")


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def calculator():
    num1 = float(input("Enter the first calculator number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second calculator number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator")
        return

    print("Calculator result:", result)


def check_leap_year():
    year = int(input("Enter a year: "))

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap year")
    else:
        print("Not a leap year")


def factorial_program():
    num = int(input("Enter a number for factorial: "))

    if num < 0:
        print("Factorial is not defined for negative numbers")
        return

    factorial = 1
    for i in range(1, num + 1):
        factorial *= i

    print("Factorial:", factorial)


def main():
    # Datatypes
    x = "hello"       # str
    y = 5              # int
    c = 1.4            # float
    print("Datatypes:", type(x).__name__, type(y).__name__, type(c).__name__)

    # Arithmetic outputs
    print(213 + 413)          # 626
    print("213" + "214")      # 213214

    # Largest of three numbers
    largest_of_three()

    # Prime and even/odd programs
    check_prime()
    check_even_or_odd()

    # Grade program
    print_grade()

    # Print numbers from 20 to 50 inclusive.
    print("Numbers from 20 to 50:")
    for number in range(20, 51):
        print(number, end=" ")
    print()

    # Print each item in a list.
    messages = ["Hi", "Hello", "How are you"]
    for message in messages:
        print(message)

    # Add two numbers by passing values as arguments.
    print("Sum:", add(10, 20))

    # Fruit list: print the sixth fruit and change the second fruit to mango.
    fruits = [
        "Apple", "Orange", "Banana", "Grapes", "Pineapple",
        "Watermelon", "Papaya", "Guava", "Kiwi", "Strawberry"
    ]
    print("Sixth fruit:", fruits[5])
    fruits[1] = "Mango"
    print("Updated fruits:", fruits)

    # List uses [] and is mutable; tuple uses () and is immutable.
    example_list = [1, 2, 3]
    example_tuple = (1, 2, 3)
    print("List:", example_list, "Tuple:", example_tuple)

    # Leap year, calculator, and factorial programs
    check_leap_year()
    calculator()
    factorial_program()


if __name__ == "__main__":
    main()
