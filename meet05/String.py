data = "ini string"
print( "data =", type(data))

# Ada 2 cara membuat string di python,
#1. Double Quote
#2. Single Quote
data = " Ini menggunakan Double Quote "
print(data)
data = " Ini menggunakan Single Quote "
print(data)

print( "' Tester 1 '" )
print( '" Tester 2 "' )

#String dengan simbol \
print( " Hari jum'at" )
print( 'Hari jum\'at' )

#\n
print( "\nKalimat Pertama \nKalimat Kedua\nKalimat ketiga" )

#backslash
print( "c:\\user\\nat " )

#backspace
print("Lebih \bDekat")

#Literal String
print("""
Nama : nat
Kelas : 10
""")
# raw : untuk mengabaikan string apapun yang tampil
print( r"c:\new folder" )

#Literal String and Raw
print("""
Nama : nit
Kelas : 9\nine
alamat : plg
""")