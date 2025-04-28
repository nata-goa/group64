#2
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#3
sum_of_positives = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break
    elif number > 0:
        sum_of_positives += number


#4
even_count = 0
odd_count = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break
    else:
        if number % 2 == 0:
            even_count += 1  
        else:
            odd_count += 1   



