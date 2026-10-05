names=("Bob","Alice","Sindhu","Indhu","Bob")
print(names,type(names),len(names))
print(names.count("Bob"))
print(names.index("Bob"))
new=names[1:3]
print(new,type(new))

for i in names:
    print(i)

fruits=('apple',)
print(fruits*3)
print(type(fruits))
