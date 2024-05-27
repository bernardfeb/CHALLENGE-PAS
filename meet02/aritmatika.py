'''
Aritmatika Python :
1. + (penjumlahan)
2. - (pengurangan)
3. * (perkalian)
4. / (pembagian)
5. ** (pangkat)
6. % (modulus (sisa bagi))
7. // (floor division (hasil bagi))
'''

a = 4
b = 3

#penjumlahan
Hasil = a+b
print(a, "+",b, "=", Hasil)
print(a, "+",b, "=", a+b)

#pengurangan
Hasil2 = a-b
print(a, "-",b, "=", Hasil2)
print(a, "-",b, "=", a-b)

#perkalian
Hasil3 = a*b
print(a, "*",b, "=", Hasil3)
print(a, "*",b, "=", a*b)

#pembagian
Hasil4 = a/b
print(a, "/",b, "=", Hasil4)
print(a, "/",b, "=", a/b)

#modulus
Hasil5 = a%b
print(a, "%",b, "=", Hasil5)
print(a, "%",b, "=", a%b)

#pangkat
Hasil6 = a**b
print(a, "**",b, "=", Hasil6)
print(a, "**",b, "=", a**b)

#floor division
Hasil7 = a//b
print(a, "//",b, "=", Hasil7)
print(a, "//",b, "=", a//b)

'''
prioritas aritmatika
'''
1. ()
2. **
3. * / % //
4. + -

x = 4
y = 5
z = 6

hasil = x * (y - z) 
print( "x * (y - z) =", hasil)

hasil = (x + y) // (z - x) ** x
print( "(x + y) // (z - x) ** x =", hasil)
