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


def merge(left, right):
    len_l = len(left)
    len_r = len(right)
    combo = []
    l = 0
    r = 0
    while l < len_l and r < len_r:
        if left[l] < right[r]:
            combo.append(left[l])
            l += 1
        else:
            combo.append(right[r])
            r += 1

    combo = combo + left[l:] + right[r:]
    return combo


def merge_sort(array):
    if len(array) == 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge(left, right)


if __name__ == "__main__":
    A = [1, 3, 6, 2, 5, 8]
    #A = [1]
    A = merge_sort(A)
    print(A)
