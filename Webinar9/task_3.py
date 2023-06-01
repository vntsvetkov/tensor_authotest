# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", "r", encoding="utf-8") as file:
    line_list = file.readlines()
    temp_list = ''.join(line_list).split("\n\n")
    three_purchases = sorted([sum([int(y) for y in x.strip().split("\n")]) for x in temp_list])[-3:]
    three_most_expensive_purchases = sum(three_purchases)

assert three_most_expensive_purchases == 202346
print("Всё ок")
