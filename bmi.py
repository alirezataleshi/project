weight = float(input("vazn ra vared konid"))
height = float(input("ghad khod ra vared konid"))
bmi = weight / (height * height)

print(bmi)

if bmi>30:print("obesity")



if bmi<18.5:print("underweight")




if 18.5<bmi<25:print("normal")




if 25<bmi<30:print("overwight")

