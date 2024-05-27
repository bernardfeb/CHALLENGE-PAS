#copy
data1 = [1,2,3,4]
data2 = ["a", "b", "c"]
dataList1 = data1
print(f"Data1 = {data1}")
print(f"DataList1 = {dataList1}")
data1[-1] = 100 
print(f"Data1    UPDATED = {data1}")
print(f"DataList1 UPDATED= {dataList1}")
print(f"Memory address data1 = {hex (id(data1))}")
print(f"Memory Address dataList1 = {hex(id(dataList1))}")
print("-"*15)
dataList2 = data2.copy()
print(f"memory address data2 = {hex(id(data2))}")
print(f"memory address dataList2= {hex(id(dataList2))}")
data2[0] = "xyz"
print(f"data2 UPDATED = {data2}")
print(f"dataList2 updated = {dataList2}")
 
print("+"*20 , "Nested list")
data1 = ["I","G","S"]
data2 = [10,11,12]
datalist = [data1 , "x" , "y" , "z" , data2]
print(f"datalist = {datalist}")
print(f"datalist[0] = {datalist[0]}")
print(f"datalist[0][1] = {datalist[0][2]}")
datalist_copy = datalist.copy()
print(f"Memory Address datalist = {hex(id(datalist))}")
print(f"Memory Address datalist_copy = {hex(id(datalist_copy))}")
datalist[-1][-1] = 100
print(f"datalist updated = {datalist}")
print(f"datalist_copy updated = {datalist_copy}")
 
print("-"*20, "deepcopy")
from copy import deepcopy
datals = deepcopy(datalist)
print(f"datalist = {datalist}")
print(f"datals = {datals}")
datalist [-1 ][ 0 ] = 777
print(f"datalist updated= {datalist}")
print(f"datals updated = {datals}")
 
print("-"*15,"comprehension")
data = [i for i in range(5)]
print(data)