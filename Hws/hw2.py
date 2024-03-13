n = int(input("Ввод кол-ва строк: "))
strings = []
output_str = ""

print("Ввод самих строк: ")
for _ in range(n):
    strings.append(str(input()))

k = int(input("Номер буквы: "))
for string in strings:
    if k <= len(string):
        output_str += string[k - 1]
print(output_str)