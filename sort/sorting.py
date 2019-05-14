def insertion_sort(array):
    for i in range(0, len(array)):
        j = i - 1
        if array[j] > array[i]:
            key = array[i]
            array[i] = array[j]
            j -= 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
    return array


def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(0, i):
            if array[j + 1] < array[j]:
                temp = array[j + 1]
                array[j + 1] = array[j]
                array[j] = temp
    return array



if __name__ == "__main__":
    #A = [1, 3, 6, 2, 5]
    A = [1]
    A = bubble_sort(A)
    print(A)
