#3
def manual_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count

#4
fruits = ['apple', 'banana', 'orange', 'banana', 'kiwi']
colors = ['red', 'blue', 'green', 'blue', 'yellow']
numbers = [42, 17, 23, 42, 5, 99, 5]

print(fruits.index('banana'))
print(colors.index('blue'))
print(numbers.index(42))

print(fruits.count('banana'))
print(colors.count('blue'))
print(numbers.count(5))

fruits.sort()
print(fruits)

colors.sort()
print(colors)

numbers.sort()
print(numbers)

sorted_fruits = sorted(['apple', 'banana', 'orange', 'banana', 'kiwi'])
print(sorted_fruits)

print(min(fruits))
print(min(colors))
print(min(numbers))

print(max(fruits))
print(max(colors))
print(max(numbers))