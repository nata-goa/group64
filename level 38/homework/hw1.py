#5
animals = ("dog", "cat", "elephant", "dog", "tiger", "cat", "dog")

dog_count = animals.count("dog")
print("dog რაოდენობა:", dog_count)

cat_index = animals.index("cat")
print("პირველი 'cat'-ის ინდექსი:", cat_index)


#6
def tuple_info(t):
    print("სიგრძე:", len(t))
    print("პირველი ელემენტი:", t[0])
    print("ბოლო ელემენტი:", t[-1])


#7
my_list = ["apple", "banana", "cherry"]
print("საწყისი სია:", my_list)

my_tuple = tuple(my_list)
print("tuple()-ით გარდაქმნილი:", my_tuple)

new_list = list(my_tuple)
print("list()-ით დაბრუნებული:", new_list)