#1
words = ["apple", "banana", "cherry"]
new_list = [w.upper() for w in words]
print(new_list)  # ['APPLE', 'BANANA', 'CHERRY']


#2
words = ['apple', 'banana', 'cat', 'elephant', 'dog', 'grapefruit']
new_list = []

for word in words:
    if len(word) > 5:
        new_list.append(word)

print(new_list)  # ['banana', 'elephant', 'grapefruit']


#3
nums = list(range(1, 21))
squares = []

for n in nums:
    squares.append(n ** 2)

print(squares)


#4
mixed = [2, 5, 8, 11, 14, 17, 20]

evens = [n for n in mixed if n % 2 == 0]   # ლუწები
odds = [n for n in mixed if n % 2 != 0]    # კენტები

print(evens)  # [2, 8, 14, 20]
print(odds)   # [5, 11, 17]


#5
try:
    num = 10
    result = num / 0
    print(result)
except ZeroDivisionError:
    print("ნულზე გაყოფა არ შეიძლება")


#6
my_list = [5, 10, 15]

try:
    print(my_list[5])  # ინდექსი 5 არ არსებობს
except IndexError:
    print("ინდექსი არასწორია")


