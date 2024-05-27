for i in range(5):
    print(" " * (5 - i - 1) + "*" * (2 * i + 1))
for i in range(5 - 2, -1, -1):
    print(" " * (5 - i - 1) + "*" * (2 * i + 1)) 

print("-"*10)

for i in range(1, 6):
    print("*" * i + " " * (10 - 2 * i) + "*" * i)
for i in range(4, 0, -1):
    print("*" * i + " " * (10 - 2 * i) + "*" * i)