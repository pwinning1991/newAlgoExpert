def insertionSort(array):
    for i in range(1, len(array)):
        currentIdx = i
        while currentIdx > 0 and array[currentIdx] < array[currentIdx - 1]:
            swap(currentIdx, currentIdx - 1, array)
            currentIdx -= 1
    return array


def swap(i,j, array):
    array[i], array[j] = array[j], array[i]