# def is_valid_number(number):
#     return (number % 2 != 0) and (number > 20)

# while True:
#     number = int(input("Masukkan Bilangan : "))
#     if is_valid_number(number):
#         print("Benar")
#         break
#     else:
#         print("Salah")

num = int( (input( "Masukkan nilai ganjil diatas 20 : ")) )

while (num % 2 == 0) or ( num < 20 )  :
    #FALSE : GENAP - dibawah 20
    num = int( (input( "Masukkan nilai ganjil diatas 20 : ")) )
    print( "Salah..." )

else:
    print( "Benar..." )
