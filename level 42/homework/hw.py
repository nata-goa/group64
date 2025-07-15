numbers = set()

numbers.add(2)
numbers.add(5)

numbers.remove(2)
numbers.remove(5)

even_numbers = {2, 4, 6, 8}

numbers.add(4)
numbers.add(6)

union_result = numbers.union(even_numbers)
print("Union:", union_result)

intersection_result = numbers.intersection(even_numbers)
print("Intersection:", intersection_result)

difference_result = numbers.difference(even_numbers)
print("Difference:", difference_result)




