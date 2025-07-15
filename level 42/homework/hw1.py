def modify_set(s):
    s.add(10)
    s.add(20)
    s.add(30)
    s.remove(10)
    return s

my_set = {1, 2, 3}
result = modify_set(my_set)
print(result)

{2, 3, 20, 30, 1}
