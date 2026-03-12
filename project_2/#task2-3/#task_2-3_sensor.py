#task_2-3_sensor 
operator_name = input("Введите имя оператора: ")
pressure_sensor = input("Введите текущее значение датчика давления (Па): ")

with open("sensor_log.txt", "a", encoding="utf-8") as file:
    file.write(f"ОПЕРАТОР:\tЗНАЧЕНИЕ:\n{operator_name}\t{pressure_sensor} Па")

print("Данные успешно сохранены в sensor_log.txt")
