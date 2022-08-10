__author__= "Mamadou WONE :)"
my_array = [20, 35, -15, 7, 55, 1, -22]

def swap(int_array, i, j):
    temp = int_array[i]
    int_array[i] = int_array[j]
    int_array[j] = temp

def bubble_sort(int_array):
    for i in range(len(int_array)):
        for j in range(i + 1, len(int_array), 1):
            if int_array[i] > int_array[j]:
                swap(int_array, i, j)

print(my_array)
bubble_sort(my_array)
print(my_array)      