# task_2-3_lab_journal
researcher = input("ФИО: ")
date = input("Дата: ")
experiment = input("Название эксперимента: ")
conclusion = input("Вывод: ")

with open("journal.txt", "w", encoding="utf-8") as file:
    file.write("+-------------------------------------------------------+\n")
    file.write("|\tЭлектронный лабораторный журнал\t\t\t|\n")
    file.write("+-------------------------------------------------------+\n")
    file.write(f"|ФИО исследователя\t:\t{name_researcher}\t\t|\n")
    file.write(f"|Дата\t\t\t:\t{date}\t\t|\n")
    file.write(f"|Название эксперимента\t:\t{experiment}\t|\n")
    file.write("+-------------------------------------------------------+\n")
    file.write(f"|Вывод\t\t\t:\t{conclusion}\t\t|\n")
    file.write("+-------------------------------------------------------+\n")

