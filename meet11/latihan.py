filtered_numbers = [i for i in range(1, 100) if (i>=10 and i<=20 and i%2 == 0) or (i >=90 and i <= 100 and i % 2 != 0)]

print("Latihan 1:")
print(filtered_numbers)

print("-"*60)

note_list = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"]
 
new_order = note_list[2:3] + note_list[:1] + note_list[3:] + note_list[1:2]
 
print("Latihan 2:")
print(new_order)

print("-"*60)

data = "IgNatIus"
 
result = [char for char in data if char.isupper()]
 
print("Latihan 3:")
print(result)
