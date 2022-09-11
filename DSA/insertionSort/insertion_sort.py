__author__= "Mamadou WONE"
my_array = [20, 35, -15, 7, 55, 1, -22]

def insertion_sort(int_array):
    for firstUnsortedIndex in range(1, len(int_array), 1):
        new_element = int_array[firstUnsortedIndex]
        i = firstUnsortedIndex
        while(i > 0 and int_array[i - 1] > new_element):
            int_array[i] = int_array[i - 1]
            i -= 1       
        int_array[i] = new_element     

print(my_array)
insertion_sort(my_array)
print(my_array)        