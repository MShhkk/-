# task_2-4_bmi
weight = float(input("Введите ваш вес (в кг):"))
height = float(input("Введите ваш рост (в м):"))
bmi = weight / (height ** 2) 

print("--- Отчет о состоянии здоровья ---")
print(f"Рост:\t{weight}\nВес:\t{height}\nИндекс массы тела:\t{bmi:.2f}")