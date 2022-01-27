def threeNumberSum(array, targetSum):
    answers = []
    array.sort()
    for idx in range(len(array) - 2):
        leftIdx = idx + 1
        rightIdx = len(array) - 1
        while leftIdx < rightIdx:
            sum_of_nums = array[idx] + array[leftIdx] + array[rightIdx]
            if sum_of_nums == targetSum:
                answers.append([array[idx], array[leftIdx], array[rightIdx]])
                leftIdx += 1
                rightIdx -= 1
            elif sum_of_nums < targetSum:
                leftIdx += 1
            elif sum_of_nums > targetSum:
                rightIdx -= 1
    return answers
            