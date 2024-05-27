print ("TIKET BUS")
kota=int(input("kota\n1.Prabumulih\n2.Muara enim\n3.Lubuklinggau\n-------------\n pilih kota (1/2/3): "))
kelas =int(input("kelas \n1.ekonomi\n2.bisnis\n3.eksekutif\n---------------\n pilih kelas  (1/2/3): "))
jumlah_tiket=int(input("Masukan jumlah tiket: "))

if kota == 1 and kelas  == 1 : 
    print(f"harga tiket \t:{100000}\n total :{100000*jumlah_tiket}")
elif kota==1 and kelas ==2: 
    print(f"Harga tiket\t:{400000}\n total:{400000*jumlah_tiket}")
elif kota==1 and kelas ==3: 
    print(f"harga tiket\t{700000}\n total:{700000*jumah_tiket}")

elif kota == 2 and kelas == 1:
    promo=input("masukan kode\t: ").lower()
    if promo=="igs":
        print(f"diskon\t{200000*0.10}")
        print(f"harga tiket\t:{200000}\n total:{(200000*jumlah_tiket)*0.10}")
    else :
        print(f"diskon\t:0")
        print(f"harga tiket\t:{200000}\n total:{(200000*jumlah_tiket)}")


elif kota==2 and kelas ==2:print(f"harga tiket\t:{500000}\n total:{500000*jumlah_tiket}")
elif kota ==2 and kelas ==3:print(f"Harga tiket\t:{800000}\n total:{800000*jumlah_tiket}")

elif kota==3 and kelas ==1: print(f"harga tiket\t:{300000}\n total:{300000*jumlah_tiket}")
elif kota==3 and kelas ==2: print(f"harga tiket\t:{600000}\n total:{600000*jumlah_tiket}")
elif kota==3 and kelas ==3:
    promo= input("masukan kode\t: ").lower()
    if promo== "igs":
        print(f"diskon\t{900000*0.10}")
        print(f"harga tiket\t:{900000}\n total:{(900000*jumlah_tiket)*0.90}")
    else:
        print(f"diskon\t:0")
        print(f"harga tiket\t:{900000}\n total:{(900000*jumlah_tiket)}")

        