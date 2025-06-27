

def greeting():
    return "Hello world"

message = greeting()
print(message)




def square_properties(length=10):
    area = length ** 2
    perimeter = 4 * length
    return area, perimeter

result1 = square_properties()
result2 = square_properties(5)

print("Result 1 (default length):", result1)
print("Result 2 (length = 5):", result2)
