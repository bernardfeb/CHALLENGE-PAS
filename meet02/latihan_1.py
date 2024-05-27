a = int(input("Masukkan nilai a : "))
b = int(input("Masukkan nilai b : "))
c = int(input("Masukkan nilai c : "))

hasil_1 = float(a*b-c)
hasil_2 = float(a+b/23//(a+c)*hasil_1)
hasil_3 = float(127+(a-c+b)%hasil_2**hasil_1)

print("Hasil 1 :", a,"*",b,"-",c,"=",hasil_1)
print("Hasil 2 :", a,"+",b,"/",23,"//","(",a,"+",c,")","*","=",hasil_2)
print("Hasil 3 :", "127","+","(",a, "-" ,c,"+",b,")","%",hasil_2,"**","=",hasil_3)