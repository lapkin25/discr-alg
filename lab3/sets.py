# Универсум - {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# структура данных "множество как двоичный вектор"
A_bin = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1]

# структура данных "множество как список значений"
A = [1, 2, 4, 6, 9]

# преобразует множество из одного представления в другое -
#  двоичный вектор в список
def SET_convert_bin_to_list(M_bin):
    assert(len(M_bin) == 10)
    M_list = []
    for i in range(0, 10):
        if M_bin[i]:
            M_list.append(i)
    return M_list

# преобразует множество из одного представления в другое -
#  список в двоичный вектор
def SET_convert_list_to_bin(M_list):
    M_bin = [0] * 10
    for elem in M_list:
        M_bin[elem] = 1
    return M_bin

# возвращает объединение двух множеств, представленных
#  в виде двоичных векторов
def SET_bin_union(A, B):
    return [0] * 10  # заглушка

# возвращает пересечение двух множеств, представленных
#  в виде двоичных векторов
def SET_bin_intersection(A, B):
    return [0] * 10  # заглушка

# возвращает разность двух множеств, представленных
#  в виде двоичных векторов
def SET_bin_difference(A, B):
    return [0] * 10  # заглушка

# возвращает симметрическую разность двух множеств, представленных
#  в виде двоичных векторов
def SET_bin_symm_difference(A, B):
    return [0] * 10  # заглушка

def SET_bin_complement(A):
    return [0] * 10  # заглушка

def test_set_operations(A_list, B_list):
    A_bin = SET_convert_list_to_bin(A_list)
    B_bin = SET_convert_list_to_bin(B_list)
    print("Множества:", SET_convert_bin_to_list(A_bin), SET_convert_bin_to_list(B_bin)) 
    print("Объединение:", SET_convert_bin_to_list(SET_bin_union(A_bin, B_bin)))
    print("Пересечение:", SET_convert_bin_to_list(SET_bin_intersection(A_bin, B_bin)))
    print("Разность:", SET_convert_bin_to_list(SET_bin_difference(A_bin, B_bin)))
    print("Симметрическая разность:", SET_convert_bin_to_list(SET_bin_symm_difference(A_bin, B_bin)))
    print("Дополнение:", SET_convert_bin_to_list(SET_bin_complement(A_bin)))

print(SET_convert_bin_to_list(A_bin))
print(SET_convert_list_to_bin(A))

# тестирование
A = [4, 5, 3, 1, 9]
B = [1, 2, 3, 4, 5]
test_set_operations(A, B)

