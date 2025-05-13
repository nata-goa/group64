#2
number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")


#3
sum_of_positives = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break
    elif number > 0:
        sum_of_positives += number


#4
even_count = 0
odd_count = 0

while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
        break
    else:
        if number % 2 == 0:
            even_count += 1  
        else:
            odd_count += 1   

#6
sum = 0
count = 0
num = int(input("enter -1): "))

while num != -1:
    sum += num
    count += 1
    num = int(input("enter -1): "))

if count > 0:
    print(sum / count)
else:
    print("numbers weren't entered.")

#7
vowels = "aeiou"
sentance = input("enter a sentance")

vowel_count = 0
consonant_count = 0
length = 0

for char in sentance:
    if char in vowels:
        vowel_count += 1
    else:
        consonant_count += 1
    length += 1

print(f"Vowels in total: {vowel_count}")
print(f"Consonants in total: {consonant_count}")
print(f"Sentence length: {length}")





