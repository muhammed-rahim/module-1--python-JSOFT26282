"""Largest of three numbers.

Algorithm:
1. Read a, b, and c.
2. If a >= b and a >= c, largest is a.
3. Else if b >= a and b >= c, largest is b.
4. Otherwise, largest is c.
5. Display largest.

Flowchart shapes:
(START/END) = Oval
/ Read or Print / = Parallelogram
< Question? > = Diamond
[ Process ] = Rectangle

Flowchart:
(START) -> /Read a,b,c/ -> <a>=b and a>=c?>
  Yes -> [largest=a] -> /Print largest/
  No  -> <b>=a and b>=c?>
          Yes -> [largest=b] -> /Print largest/
          No  -> [largest=c] -> /Print largest/
/Print largest/ -> (END)
"""

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("The largest number is:", largest)
