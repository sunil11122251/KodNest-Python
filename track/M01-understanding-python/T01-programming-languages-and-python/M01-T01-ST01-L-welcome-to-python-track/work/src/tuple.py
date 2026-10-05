names=("Bob","Alice","Sindhu","Indhu","Bob")
print(names,type(names),len(names))
print(names.count("Bob"))
print(names.index("Bob"))
new=names[1:3]
print(new,type(new))

for i in names:
    print(i)

fruits=('apple',"bananna","cherry")
f1,*f2=fruits
print(f1,type(f1))
print(f2,type(f2))

a=10
b=20
c=30
numbers=(a,b,c)   #packing of tuple
print(numbers,type(numbers))

a1,b1,c1=numbers   #unpacking of tuple
print(a1,b1,c1) 
