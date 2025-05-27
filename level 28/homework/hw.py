#2
word = input("შეიყვანეთ სიტყვა: ")
print(word.lower())

#3
word1 = input("შეიყვანეთ პირველი სიტყვა: ")
word2 = input("შეიყვანეთ მეორე სიტყვა: ")

print(word1.lower() == word2.lower())


#4
countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for country in countries:
    print(country.lower())


#5
word = input("შეიყვანეთ სიტყვა: ")
print(word.upper())


#6
countries = ["Georgia", "Armenia", "Greece", "Norway", "Denmark"]

for country in countries:
    print(country.upper())


#7
ord = input("შეიყვანეთ სიტყვა: ")

if word.isupper():
    print("სიტყვა დიდი ასოებითაა.")
else:
    print("სიტყვა არ არის დიდი ასოებით.")


#8
sentence = input("შეიყვანეთ წინადადება: ")
print(sentence.capitalize())


#9
string = "gEoRGia"
result = string.capitalize()
print(result)


#10
countries = ["georgia", "aRMENIA", "greeCE"]

for country in countries:
    formatted = country.lower().capitalize()
    print(formatted)


#11
word = input("შეიყვანეთ სიტყვა: ")

position = word.find('a')

if position != -1:
    print(f"ასო 'a' პირველი გვხვდება პოზიციაზე: {position}")
else:
    print("ასო 'a' სიტყვაში არ არის.")


#12
text = "I visited Georgia, Armenia and Greece"
position = text.find("Armenia")

if position != -1:
    print(f"'Armenia' მდებარეობს პოზიციაზე: {position}")
else:
    print("'Armenia' ტექსტში არ არის.")


#13
text = "I visited Georgia, Armenia and Greece"
word = input("შეიყვანეთ საძიებელი სიტყვა: ")

position = text.find(word)

if position != -1:
    print(f"სიტყვა '{word}' მდებარეობს პოზიციაზე: {position}")
else:
    print("word not found")

