file = open("Задание 24/24.txt")

x ="" #  предыдущий символ
m = 0  # максимальная длинна цепочки из разных символов
k = 0  # длинна текущей цепочки
for s in file:
    for i in s:
        if i == x:
            k = 1
        else:
            k += 1
            if k > m:
                m = k
            x = i
print(m)