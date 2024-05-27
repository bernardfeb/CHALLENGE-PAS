input_angka = int(input("Masukkan jumlah angka : "))

fib_list = []
a, b = 1, 1

for _ in range(input_angka):
    fib_list.append(a)
    a, b = b, a + b

print("Deret Fibonacci:", fib_list)

input_angka = int(input("Masukkan jumlah angka : "))

fib_list = [1, 1]
[fib_list.append(fib_list[-1] + fib_list[-2]) for _ in range(2, input_angka)]
print( fib_list)