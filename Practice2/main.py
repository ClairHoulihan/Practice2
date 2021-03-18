'''
Basics
1. What is an expression?
  - An expression evaluates to a value. It can take multiple other values to create the new value.
2. What is a syntax error?
  - A syntax error occurs when a program is unable to interpret or compile an expression or statement
3. What is PEP8?
  - PEP8 stands for Python Enhancement Proposal, and attempts to create a standard for writting Python programs
4. What does a linter do?
  - linter is a tool that detects errors in a running application
5. What is the result of this expression: “*” * 10
  - Output: **********
6. What is CPython?
  - CPython is a reference implementation of Python, it allows for formatting of code to fit other specifications rather than the one it is designed for.
7. How is CPython different from Jython?
  - CPython is written in C, whereas Jython is written in Java
8. How is CPython different from IronPython?
  - Similar to last except IronPython is written in C#
'''

'''
Primitive Types
1. What is a variable?
  - A variable is a container for a value
2. What are the primitive built-in types in Python?
  - Int, Float, String, Boolean
3. When should we use “”” (tripe quotes) to define strings?
  - Triple quotes denote that we want to use all of the literal characters (ex: \ is not an escape character)
4. Assuming (name = “John Smith”), what does name[1] return?
- Output: o
5. What about name[-2]?
  - Output: t
6. What about name[1:-1]?
  - Output: ohn Smith
7. How to get the length of name?
  - len(name)
8. What are the escape sequences in Python?
  # - \\ , \' , \" , \a , \b , \f , \n , \r , \t , \v 
9. What is the result of f“{2+2}+{10%3}”?
  - Output: 4+1
10. Given (name = “john smith”), what will name.title() return?
  - Output: John Smith
11. What does name.strip() do?
  - Output: john smith
12. What will name.find(“Smith”) return?
  - Output: 5
13. What will be the value of name after we call name.replace(“j”, “k”)?
  - Output: kohn smith
14. How can we check to see if name contains “John”?
  - name.find("John") != -1
15. What are the 3 types of numbers in Python?
  - Integer, Float, and Complex
'''

'''
Control Flow
1. What is the difference between 10 / 3 and 10 // 3?
  - 10/3 will return 3.33333, 10//3 will return 3
2. What is the result of 10 ** 3?
  - Output: 1000
3. Given (x = 1), what will be the value of after we run (x += 2)?
  - Output: 3
4. How can we round a number?
  - round(number, digits)
5. What is the result of float(1)?
  - converts 1 to a float i.e. 1.0
6. What is the result of bool(“False”)?
  - Output: True
  - Explanation -> bool checks to see if there is anything given, so because we are giving it something, it prints True (If we give an empty string, it will return False)
7. What are the falsy values in Python?
  - Empty strings, integer value 0, empty list, tuple, etc.
8. What is the result of 10 == “10”?
  - False
  - Explanation -> integer value 10 is not the same as string value 10
9. What is the result of “bag” > “apple”?
  - Output: True
  - Explanation -> Evaluates to True since the ASCII value of 'b' is greater than 'a'
10. What is the result of not(True or False)?
  - Output: False
  - True is evaluated in the parenthesis, then not evaluates True to False
11. Under what circumstances does the expression 18 <= age < 65 evaluate to True?
  - When age = 18 or greater but less than 65
12. What does range(1, 10, 2) return?
  - Output: 1, 3, 5, 7, 9
13. Name 3 iterable objects in Python.
  - List, tuple, dictionary, set
'''

'''
Functions
1. What is the difference between a parameter and an argument?
  - The terms are very similar, a parameter is a value sent in through the parenthesis after a function name, where an argument is the value that is sen to the function when it is called
2. All functions in Python by default return ...?
  - Python functions return None by default
3. What are keyword arguments and when should we use them?
  - keyword arguments are values passed into a function using the *key = value* syntax
4. How can we make a parameter of a function optional?
  - When creating a function in Python, you can assign a default value using the = sign in the function creation. Ex:
    func1(x=5):
5. What happens when we prefix a parameter with an asterisk (*)?
  - That means that the arguments will be taken into a tuple that can be unpacked in the function
6. What about two asterisks (**)?
  - ** will capture any keyword arguments given into a key -> value format
7. What is scope?
  - Scope refers to the way variables are accessed across an application
8. What is the difference between local and global variables?
  - Local variables are only in the stack of the function using it, global variables are in the program memory, so they are accessible anywhere
9. Why is using the global statement a bad practice?
  - global variables are considered bad practice since they are difficult to manage as the code base of an application grows
'''

'''
Coding Exercises
1. Write a function that returns the maximum of two numbers.
2. Write a function called fizz_buzz that takes a number.
  1. If the number is divisible by 3, it should return “Fizz”.
  2. If it is divisible by 5, it should return “Buzz”.
  3. If it is divisible by both 3 and 5, it should return “FizzBuzz”.
  4. Otherwise, it should return the same number.
3. Write a function for checking the speed of drivers. This function should have one parameter:
speed.
  1. If speed is less than 70, it should print “Ok”.
  2. Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit
  point and print the total number of demerit points. For example, if the speed is 80, it
  should print: “Points: 2”.
  3. If the driver gets more than 12 points, the function should print: “License suspended”
4. Write a function called showNumbers that takes a parameter called limit. It should print all
the numbers between 0 and limit with a label to identify the even and odd numbers. For
example, if the limit is 3, it should print:
  o 0 EVEN
  o 1 ODD
  o 2 EVEN
  o 3 ODD
5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
6. Write a function called show_stars(rows). If rows is 5, it should print the following:
o *
o **
o ***
o ****
o *****
7. Write a function that prints all the prime numbers between 0 and limit where limit is a
parameter.
'''
# This variable is being used as a global to store demerit points (for the speedCheck method)
demerit = 0

'''
exercises():

runs a list of other functions that print out even and odd numbers, prime numbers, etc.

'''
def exercises():

  '''
  max(x, y):

  returns the maximum value of two varibles

  '''
  def max(x, y):
    if x >= y:
      return x
    elif y > x:
      return y

  print(max(5, 10))

  '''
  fizz_buzz(num):

  if a number is divisible by 3, return Fizz
  if a number is divisible by 5, return Buzz
  if a number is divisible by both, return FizzBuzz
  else return the original number
  '''
  def fizz_buzz(num):
    if (num % 3) == 0 and (num % 5) == 0:
      return "FizzBuzz"
    elif (num % 3) == 0:
      return "Fizz"
    elif (num % 5) == 0:
      return "Buzz"
    else:
      return str(num)

  print(fizz_buzz(15))

  '''
  speedCheck(speed):

  if speed is less than or equal to 70, print Ok
  if speed is between 70 to 75, print Slow Down
  if speed is 75 or greater, print demerit point value
  if demerit value is 12 or greater, print License Suspended
  '''
  def speedCheck(speed):

    global demerit

    if demerit >= 12:
      print("License Suspended")
      return

    if speed <= 70:
      print("Ok")
    elif speed > 70 and speed < 75:
      print("Slow Down")
    else:
      demerit += ((speed - 70) // 5)
      if demerit < 12:
        print("Points: " + str(demerit))
      else:
        print("License Suspended")

  speedCheck(100)

  speedCheck(100)

  '''
  showNumbers(limit):

  prints all of the numbers until the limit and whether they are odd or even
  '''
  def showNumbers(limit):
    for i in range(0, limit + 1):
      if (i % 2) == 0:
        print(str(i) + " EVEN")
      else:
        print(str(i) + " ODD")
    
  showNumbers(5)

  '''
  multi35sum(limit):

  prints all of the multiples of 3 and 5 until limit is reached
  '''
  def multi35sum(limit):
    sum = 0
    for i in range(0, limit + 1):
      if (i % 3):
        sum += i
      elif (i % 5):
        sum += i

  multi35sum(20)

  '''
  show_stars(row):

  prints rows and uses the row number to print that amount of stars
  '''
  def show_stars(row):
    for i in range(0, row + 1):
      print("*" * i)

  show_stars(5)

  '''
  primeNumbers(limit):

  prints prime numbers until the limit is reached
  '''
  def primeNumbers(limit):

    for i in range(0, limit + 1):
      prime = True
      if(i < 2):
        continue
      for j in range(2, i):
        if((i % j) == 0):
          prime = False
          break
      if(prime):
        print(i)

  primeNumbers(9)


exercises()
    





