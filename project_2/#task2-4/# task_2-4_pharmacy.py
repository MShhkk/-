# task_2-4_pharmacy
quantity_capsules = int(input("Введите общее количество произведенных капсул:"))
capacity = int(input("Введите количество капсул в одной упаковке:"))
full_packaging = quantity_capsules // capacity
remains =  quantity_capsules % capacity
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t{full_packaging}\nОстаток капсул:\t{remains}")
