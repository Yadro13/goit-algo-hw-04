import random
import timeit
import matplotlib.pyplot as plt
import pandas as pd

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Time measurement
def time_algorithm(algorithm, data):
    def wrapped():
        algorithm(data.copy())
    return timeit.timeit(wrapped, number=1)

# Набори розмірів
sizes = [100, 500, 1000, 2000, 5000]
results = {"Size": [], "Merge Sort": [], "Insertion Sort": [], "Timsort": []}

# Генерація даних та вимірювання часу виконання
for size in sizes:
    data = [random.randint(0, size) for _ in range(size)]
    results["Size"].append(size)
    results["Merge Sort"].append(time_algorithm(merge_sort, data))
    results["Insertion Sort"].append(time_algorithm(insertion_sort, data))
    results["Timsort"].append(time_algorithm(sorted, data))

# Таблиця результатів
df = pd.DataFrame(results)
print(df)

# Побудова графіка
plt.plot(df["Size"], df["Merge Sort"], label="Merge Sort")
plt.plot(df["Size"], df["Insertion Sort"], label="Insertion Sort")
plt.plot(df["Size"], df["Timsort"], label="Timsort (Python)")
plt.xlabel("Кількість елементів")
plt.ylabel("Час виконання (сек)")
plt.title("Порівняння алгоритмів сортування")
plt.legend()
plt.grid(True)
plt.show()
