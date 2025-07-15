
student = {
    "name": "ნინო",
    "hobby": "მუსიკა",
    "height": 170,
    "weight": 60
}

name_value = student.get("name")

height_value = student.pop("height")

# შედეგის გამოტანა
print("Name:", name_value)
print("Height removed:", height_value)
print("Updated student dict:", student)
