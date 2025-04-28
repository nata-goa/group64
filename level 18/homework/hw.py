#1
for i in range(0, 21):
    if i % 2 == 0:
        print(f"{i} even")
    else:
        print(f"{i} odd")

#2
i = 0
while i <= 20:
    if i % 2 == 0:
        print(f"{i} even")
    else:
        print(f"{i} odd")
    i += 1

#3
my_name = "natali"  
user_name = input("enter ur name: ")

if user_name == my_name:
    print("coincidence")


#4
score = int(input("enter ur score: "))

if score > 70:
    print("passed")
else:
    print("failed")


#5
    score = int(input("enter score: "))

if score > 80:
    grade = "A"
elif score > 60:
    grade = "B"
elif score > 40:
    grade = "C"
elif score > 20:
    grade = "D"
else:
    grade = "F"

print(f"ur score is: {grade}")


