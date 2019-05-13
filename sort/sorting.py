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


if __name__ == "__main__":
    A = [1, 3, 6, 2, 5]
    A = insertion_sort(A)
    print(A)
