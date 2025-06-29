
#hw from 1 to 11

def greet():
    print("Hello, world!")

def greet(name):
    print(f"Hello, {name}!")

def add_numbers(a, b):
    return a + b

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def average(numbers):
    if len(numbers) == 0:
        return 0  
    return sum(numbers) 

def string_length(text):
    return len(text)

def reverse_list(lst):
    return lst[::-1]

def to_uppercase(text):
    return text.upper()

def max_number(a, b):
    return max(a, b)

def is_negative(number):
    return number < 0

