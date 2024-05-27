data = "Ignatius Global School"

# Menghitung jumlah string
print(f"jumlah str di data : {len(data)}")

# in - not in , mengetahui str
print(f"apakah ada 'I' di str : { 'I' in data}")
print(f"apakah ada 'z' di str : { 'z' in data}")

# min / max pada str
print(f"max pada data : {max(data)}")
print(f"min pada data : {min('cbbcccdddd')}")

#menghitung karakter str :
print(f" 'o' pada data : {data.count('o')}")

data1 = "Ini huruf kecil"
data2 = "INI HURUF BESAR"
print(f"data1: {data1.upper()}")
print(f"data2: {data2.lower()}")

data3 = "abc123"
print(f"data1 is alpha : {data1.isalpha()}")
print(f"data3 is alpha : {data3.isalpha()}")

#Index in str
print(f"data ke-0 : {data[0]}")
print(f"data ke-2 : {data[2]}")
print(f"data ke-0,7 : {data[0:7]}")#ignatiu
print(f"data ke-0,7,2 : {data[0:7:2]}")#intu