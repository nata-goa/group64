
programming_languages = ['Python', 'Java', 'C++', 'JavaScript', 'C', 'Swift', 'Go', 'Pervp', 'Kotlin', 'CSS']

desired_language = 'Rust'

print(programming_languages)



# 2) ცივი სასმელების სია
cold_drinks = ['Coca-Cola', 'Fanta', 'Sprite', 'Pepsi', 'Red Bull', 'Ice Tea', 'Lemonade', 'Mountain Dew', 'Lipton', 'Bora']

# ერთ-ერთი სასმელი ცვლადში
favorite_drink = cold_drinks[2]

# მომხმარებლის შემოტანილი სასმელი მაცივრისთვის
new_drink = input("შეიყვანეთ ცივი სასმელი, რომელიც გსურთ დაამატოთ მაცივარში: ")
cold_drinks.append(new_drink)

# მომხმარებლის არჩევანი
print(f"\nაირჩიეთ სასმელი სიიდან: {cold_drinks}")
choice = int(input("შეიყვანეთ სასმლის ინდექსი (0-დან დაწყებული): "))

# ინდექსის საშუალებით სასმლის გამოყვანა
print("თქვენი არჩეული სასმელია:", cold_drinks[choice])

# სახელი და სამი სიმბოლოს ამოღება
my_name = "გიორგი"
print("თქვენი სახელიდან ამოღებული სამი სიმბოლოა:", my_name[1:4])





sports = ['Football', 'Basketball', 'Tennis', 'Swimming', 'Volleyball', 'Boxing', 'Cycling', 'Running', 'Skiing', 'Wrestling']

print("1-5:", sports[1:6])       
print("3-8:", sports[3:9])      
print("-2-0:", sports[-2:])    
print("4-0:", sports[4:])       

print(":", sports[::-1])


