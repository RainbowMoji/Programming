n = int(input("Кол-во входных чисел: "))
l0 = []
l1 = []

print(f"Введите числа, в количестве {n}: ")
for _ in range(n):
    l0.append(int(input()))

for cur_num in range(n - 1):
    l1.append(l0[cur_num] + l0[cur_num + 1])
print(l1)
