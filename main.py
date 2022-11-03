set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
set_c = {7, 8, 9, 10, 11}

# Використовуючи set_a, set_b, set_c
# 1. Отримати загальний set
# res = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
res = {*set_a, *set_b, *set_c}

# 2. Отримати різницю між set_a і set_b, set_b і set_c
res_a_b = set_a.difference(set_b)
res_b_c = set_b.difference(set_c)
res_a_c = set_a.difference(set_c)

# 3. Отримати загальні елементи між set_a і set_b, set_b і set_c
union_res_a_b = set_a.intersection(set_b)
union_res_b_c = set_b.intersection(set_c)
union_res_a_c = set_a.intersection(set_c)

# 4. Перевірити чи є set {1, 2} підмножиною кожного set_a, set_b, set_c
searched_subset = {1, 2}

is_searched_in_a = searched_subset.issubset(set_a)
is_searched_in_b = searched_subset.issubset(set_b)
is_searched_in_c = searched_subset.issubset(set_c)

# 5. Використовуючи результат res з задачі 1 створити два set res_1, res_2
# res_1 тільки парні, res_2 тільки непарні.
# res_1 = {0, 2, 4, 6, 8, 10}
# res_2 = {1, 3, 5, 7, 9, 11}

res_1 = set()
res_2 = set()

for item in res:
    if item % 2 == 0:
        res_1.add(item)  # attention!: кортеж из задания 1 не содержит значение "0"
    else:
        res_2.add(item)

# DICT
dict_a = {
    'key_1': 'value_1',
    'key_2': 'value_2',
    'key_3': 'value_3',
    'key_4': 'value_4',
    'key_5': 'value_5'
}
dict_b = {
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8',
    'key_9': 'value_9',
    'key_10': 'value_10'
}
dict_c = {
    'key_4': 'value_4',
    'key_5': 'value_5',
    'key_6': 'value_6',
    'key_7': 'value_7',
    'key_8': 'value_8'
}

# Використовуючи словники dict_a і dict_b
# 1. Зробити загальний словник
dict_a_b = {[*dict_a.items(), *dict_b.items()]}
# или так, но это я увидел когда гуглил и такую распаковку мы не проходили, кажется
# dict_a_b = {**dict_a, **dict_b}

# 2. Взяти ключі словника dict_a і значення словника dict_b і зробити загальний словник:
# res = {'key_1': 'value_6', 'key_2': 'value_7', 'key_3': 'value_8', 'key_4': 'value_9', 'key_5': 'value_10'}
dict_res = {zip(dict_a.keys(), dict_b.values())}
