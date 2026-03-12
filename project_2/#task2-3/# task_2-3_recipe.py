# task_2-3_recipe
medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(medium_name + "\n")
    file.write(f"\tКонцентрация агара:\t{agar_concentration}%\n")
    file.write(f"\tТемпература стерилизации:\t{sterilization_temp}К\n")
print("Файл 'recipe.txt' успешно сформирован!")
