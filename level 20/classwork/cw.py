if num > 0:
    print("რიცხვი დადებითია.")
elif num < 0:
    print("რიცხვი უარყოფითია.")
else:
    print("რიცხვი ნეიტრალურია.")



num = int(input("შეიტანეთ რიცხვი: "))

if num > 0:
    print("რიცხვი დადებითია.")
    if num % 2 == 0:
        print("ლუწია.")
    else:
        print("კენტია.")
else:
    print("უარყოფითია ან ნულია.")



vegetables = ["Potato", "carrot", "cabbage", "tomato"]

print("Vegetable list:", vegetables)

print("\nEach vegetable in the list:")
print("0:", vegetables[0])
print("1:", vegetables[1])
print("2:", vegetables[2])
print("3:", vegetables[3])




