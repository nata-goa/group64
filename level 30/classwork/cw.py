
text = "hay"
print(len(text))  # შედეგი: 9

fruits = ["berry", "banana"]
fruits.append("kiwi")
print(fruits)  

numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)  # [1, 2, 3, 4]

colors = ["red", "b;ue", "green"]
removed_color = colors.pop()
print(removed_color)  
print(colors)         

animals = ["dog", "cat", "rabbit"]
animals.remove("car")
print(animals)  


def greet():
    print("Hello")
    print("Welcome")



#გამოძახება ორჯერ
greet()
greet()



def new_greet(first_name, last_name):
    print(f"Greetings {first_name} {last_name}")

# ფუნქციის გამოძახება ორჯერ არგუმენტებით
new_greet("nata", "li")
new_greet("natali", "bajelidze")

#Greetings nata li
#greetings natali bajelidze

