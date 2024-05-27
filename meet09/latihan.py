def is_valid_number(number):
    return (10 < number < 15) or (20 < number < 25) or (35 < number < 40)

print ("<<<      Identifikasi Bilangan       >>>")
print ("Identifikasi nilai jika nilai 10 - 15 atau 20 - 25 atau 35 - 40")
print ("-"*70)
while True:
    number = int(input("Masukkan Bilangan : "))
    if is_valid_number(number):
        print("Benar")
    else:
        print("Salah")