print("Interschimbare valori")
print("Metoda variabilei aditionale")
a=1
b=2
print("a = ",a)
print("b = ",b)
c=a
a=b
b=c
print("a devine",a,"b devine ",b)

print("Metoda fara variabila aditionala")
a=1
b=2
print("a = ",a)
print("b = ",b)
a=a+b
b=a-b
a=a-b

print("a devine",a,"b devine ",b)

print("Metoda eleganta")
a=1
b=2
print("a = ",a)
print("b = ",b)
a,b=b,a

print("a devine",a,"b devine ",b)
