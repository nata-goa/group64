sum = 0
for num in range (1, 21):
    sum += num 

num1 = int(input("enter first number: "))
num2 = int(input("enter second number:"))

for i in range(num1, num2 + 1): 
    print(i) 

    password = "mypassword"

    while true: 
        user_input = input("enter password:")
        if user_input == password:
            print("password correct!") 