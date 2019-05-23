unit= input("aya metric estefade mikonid?:")
if unit=="y":
    weight = float(input("weight in metric?:"))
    height= float(input("height in metric?:"))
    bmi = weight / (height * height)
    print(bmi)

    if bmi > 30: print("obesity")

    if bmi < 18.5: print("underweight")

    if 18.5 < bmi < 25: print("normal")

    if 25 < bmi < 30: print("overwight")

elif unit=="n":
    weight = float(input("weight in imp?:"))
    height = float(input("height in imp?:"))
    bmi = (weight*703) / (height * height)
    print(bmi)
    if bmi > 30: print("obesity")

    if bmi < 18.5: print("underweight")

    if 18.5 < bmi < 25: print("normal")

    if 25 < bmi < 30: print("overwight")

