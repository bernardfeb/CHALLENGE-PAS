def mean(*args):
    return sum(args) / len(args)
 
info = ["Masukan Angka "]
datas = []
 
while True:
    data = {a: "" for a in info}
    for a in info:
        data[a] = float(input(f"{a} = "))
    datas.append(data)
    user_input = input("lanjut (y/n): ")
    if user_input != 'y':
        break
numbers = [data["Masukan Angka "] for data in datas]
average = mean(*numbers)
 
print(f"mean : {average}")
