weight_pounds = float(input("Введите вес в фунтах: "))
height_inches = float(input("Введите рост в дюймах: "))
weight_kg = weight_pounds * 0.4535
height_m = height_inches * 0.0254
bmi = weight_kg / (height_m ** 2)
bmi_rounded = round(bmi, 2)

print("Индекс массы тела (ИМТ):", bmi_rounded)
