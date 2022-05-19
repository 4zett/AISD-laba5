import time
import numpy as np

try:
    K = int(input("Введите число К:"))
    N = int(input("Введите количество строк (столбцов) квадратной матрицы больше 3 и меньше 184:"))
    if (N >= 4) and (N <= 183):
        start = time.time()
        A = np.zeros((N, N), dtype=int)
        F = np.zeros((N, N), dtype=int)
        for i in range(N):     # Формируем матрицу А
            for j in range(N):
                A[i][j] = np.random.randint(-10, 10)
        print("Матрица A:\n", A)
        for i in range(N):      # Формируем матрицу F, копируя из матрицы А
            for j in range(N):
                F[i][j] = A[i][j]
        lit_range = N // 2         # Размерность подматрицы
        E = np.zeros((lit_range, lit_range), dtype=int)   # Формируем матрицу Е
        for i in range(lit_range):
            for j in range(lit_range):
                E[i][j] = A[i][j]
        print("Матрица Е:\n", E)
        amount = 0
        sum = 0
        for i in range(lit_range):
            for j in range(lit_range):
                if j % 2 == 0 and E[i][j] == 0:     # Количество 0 в нечетных столбцах
                    amount += 1
                if i % 2 == 1 and E[i][j] < 0:      # Количество отрицательных элементов в четных строках
                    sum += 1
        print("Количество 0 в нечетных столбцах:", amount, "\nКоличество отрицательных элементов в четных строках:", sum)
        if amount < sum:
            print("\nМеняем С и В симметрично")
            for i in range(lit_range):       # С и В симметрично
                for j in range(lit_range):
                    F[i][j] = A[N-i-1][N-j-1]
                    F[i][j] = A[i][N-j-1]
        else:
            print("\nМеняем B и E несимметрично")
            for i in range(lit_range):     # В и E несимметрично
                for j in range(lit_range):
                    F[i][j] = A[i][lit_range + j]
                    F[i][lit_range + j] = A[i][j]
        print("Матрица A:\n", A, "\nМатрица F:\n", F)
        print("Определитель матрицы А:", round(np.linalg.det(A)), "\nСумма диагональных элементов матрицы F:", np.trace(F))
        if np.linalg.det(A) == 0 or np.linalg.det(F) == 0:
            print("Нельзя вычислить т.к. матрица A или F вырождена")
        elif np.linalg.det(A) > np.trace(F):
            print("Вычисление выражения: A - 1 * AT – K * F")
            A = (np.linalg.inv(A) - np.transpose(A)) - (np.linalg.inv(F) * K)  # A - 1 * AT – K * F
        else:
            print("Вычисление выражения: (AТ + G - F - 1) * K")
            A = (np.transpose(A) + np.tril(A) - np.linalg.inv(F) - 1) * K   # (AТ + G - F - 1) * K
        print("\nРезультат:")
        for i in A:     # Вывод результата
            for j in i:
                print("%5d" % round(j), end=' ')
            print()
        finish = time.time()
        result = finish - start
        print("Время работы программы: " + str(result) + " секунды.")
    else:
        print("\nВы ввели неверное число.")
except ValueError:
    print("\nЭто не число")