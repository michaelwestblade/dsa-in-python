brands = ["tesla", "skoda", "Toyota", "Suzuki"]

for brand in brands:
    print(brand)

[print(brand) for brand in brands]

# without list comp
elist = []
elistcubed = []
for i in range(10):
    elist.append(i)
    elistcubed.append(i**3)
print(elist)
print(elistcubed)

# with list comp
li = [x for x in range(10)]
licubed = [x**3 for x in range(10)]
print(li)
print(licubed)

list_of_10 = [5]*10
print(list_of_10)

list_of_zeroes = [0]*10
print(list_of_zeroes)

tup_list = [(i, j) for i in range(5) for j in range(4)]
print(tup_list)

tup_list_squared = [(i**2, j) for i in range(5) for j in range(4)]
print(tup_list_squared)

multi_dim = [[i for i in range(5) if i != j] for j in range(4)]
print(multi_dim)

list_to_slice = [ i for i in range(0, 101)]
print(list_to_slice[80:])
print(list_to_slice[:30])
print(list_to_slice[10:20:2])

print([i for i in range(10)][-1:])