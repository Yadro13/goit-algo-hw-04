# Перевірка, чи список відсортований
def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

# Злиття двох відсортованих списків
def merge_two_lists(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

# Сортування злиттям (merge sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge_two_lists(left, right)

# Головна функція: перевірка + сортування + злиття
def merge_k_lists(lists):
    if not lists:
        return []
    # Сортуємо списки, якщо потрібно
    sorted_lists = [merge_sort(lst) if not is_sorted(lst) else lst for lst in lists]
    # Зливаємо їх по черзі
    merged = sorted_lists[0]
    for i in range(1, len(sorted_lists)):
        merged = merge_two_lists(merged, sorted_lists[i])
    return merged

# Тест
lists = [[1, 4, 5], [1, 3, 17], [2, 6], [23, 0, 7, 8], [3, 5, 9], [4, 10, 11, 12]]
print("Відсортований список:", merge_k_lists(lists))