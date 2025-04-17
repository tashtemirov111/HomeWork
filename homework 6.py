def bubble_sort(arr):

    n = len(arr)
    result = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:

                result[j], result[j + 1] = result[j + 1], result[j]
    return result

def binary_search(target, arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            print(f"Элемент {target} найден на позиции {mid}.")
            return
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"Элемент {target} не найден в списке.")

unsorted_list = [64, 25, 12, 22, 11]

sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)

binary_search(22, sorted_list)
