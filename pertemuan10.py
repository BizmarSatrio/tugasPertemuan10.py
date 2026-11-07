# LIST
# menggunakan kurung siku
data_list = [10,2,4,3,2]
print(data_list)
print()

# tuples
data_tuples = (7,8,10,11)
print(data_tuples)
print(data_tuples[1])
# tidak bisa dilakukan
# data_tuples[1] = "ucup"
# data_tuples.append(1)
print()

# sets (himpunan)
data_sets = {10,4,3,2,7,6,5}
print(data_sets)
# print(data_sets[0])  # Ini akan menyebabkan error karena set tidak memiliki indeks
print()

# dictionary
# list -> array mengakses menggunakan index 
data_list = ['ucup','rendi','salsa']
print(data_list)
print()

# dictionary (dict) -> associative array
# indentifier -> Key 

data_dict = {
    'key' : 'value',
    'cp':'ucup',
    'rd':'rendi',
    'sl':'salsa',
    'nmbr':100,
    'list':data_list
}

print(data_dict['cp'])
print(data_dict['nmbr'])
print(data_dict['list'])
print()

# --- Operasi Dictionary ---
data_dict = {
    "cup":"ucup surucup",
    "pet":"opet saripet",
    "ndo":"nando surundo"
}

# panjang dicrionary
lendict = len(data_dict)
print(f"panjang dictionary: {lendict}")
print()

# mengecek key exist atau tidak
key = "cup"
checkkey = key in data_dict
print(f"apakah {key} ada di data_dict: {checkkey}")
print()

# mengakses value(Read) dengan get 
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan"))
print()

# mengupdate data 
data_dict["cup"] = "ucup si ganteng"
print(data_dict)
data_dict["de"] = "ade si adek"
print(data_dict)
print()
data_dict.update({"cup":"ucup surucup"})
print(data_dict)
data_dict.update({"bar":"akbar mang keren"})
print(data_dict)
print()

# menghapus data 
del data_dict["bar"]
print(data_dict)
print()

# --- Looping Dictionary ---
teman_teman =  {
    "cup":"ucup surucup",
    "tong":"sotong surotong",
    "lur":"lur sedulur",
    "wel":"bung towel"
}

# looping first try (hanya key)
for teman in teman_teman:
    print(teman)
print()

# operator untuk mengambil item 
keys = teman_teman.keys()
print(keys)

for key in teman_teman.keys():
    print(teman_teman.get(key))
print()

values = teman_teman.values()
print(values)

for value in teman_teman.values():
    print(value)
print()
items = teman_teman.items()
print(items)

for item in teman_teman.items():
    print(item)
print()
for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")
print()