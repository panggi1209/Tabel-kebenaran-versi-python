#oprasi  logika atau boolean
#tabel kebenaran
#not,or,and,xor
#not
print("====Not=====")
a = True
c= not a
print("data boolean =" ,a)
print("======not")
print( "data  c =" ,c  ) 

#or (jika salah satu true maka hasilnya true)
print("====or=====")
a = False
b = False
c = a or b
print(a,"or",b,"=",c)
a = False
b = True
c = a or b
print(a,"or",b,"=",c)
a= True
b = False
c = a or b
print(a,"or",b,"=",c)
a = True
b = True
c = a or b
print(a,"or",b,"=",c)

#and (jika salah satu false maka hasilnya false)
print("====and=====")
a = False
b = False
c = a and b
print(a,"and",b,"=",c)
a = False
b = True
c = a and b
print(a,"and",b,"=",c)
a= True
b = False
c = a and b
print(a,"and",b,"=",c)
a = True
b = True
c = a and b
print(a,"and",b,"=",c)

#xor (akan true jika salah satu true dan false)
print("====xor=====")
a = False
b = False
c = a ^ b
print(a,"xor",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"xor",b,"=",c)
a= True
b = False
c = a ^ b
print(a,"xor",b,"=",c)
a = True
b = True
c = a ^ b
print(a,"xor",b,"=",c)

#operasi logika bisa di gabung
print("====gabungan=====")
a = True
b = False
c = True
d = a and b or c
print(a,"and",b,"or",c,"=",d)

