
my_list = [5, 2, 9, 1]
my_list.sort()
print(my_list)  


text = "12345"
print(text.isnumeric())  #True


numbers = [8, 3, 7, 2]
sorted_list = sorted(numbers)
print(sorted_list) 


values = [4, 1, 6, 9]
print(min(values)) 


values = [4, 1, 6, 9]
print(max(values))  



def manual_max(lst):
    max_value = lst[0]
    for item in lst:
        if item > max_value:
            max_value = item
    return max_value


numbers = [3, 7, 2, 9, 5]
print(manual_max(numbers))  

