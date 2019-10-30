print  (" program menentukan bilangan terbesar dari 3 buah bilangan ")

x =int(input("masukan bilangan x:"))
y =int(input("masukan bilangan y:"))
z =int(input("masukan bilangan z:"))

if x > y and x > z:
    print("bilangan terbesar adalah:", x)
elif y > x and y > z:
    print("bilangan terbesar adalah:", y)
else:
    print("bilangan terbesar adalah:", z)
