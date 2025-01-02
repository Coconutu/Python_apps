# n=int(input("n="))
# if n>0:
#     print("Mai mare ca 0")
# elif n==0:
#     print("Egal cu 0")
# else:
#     print("Mai mic sau egal cu 0")

# print(7>3)
# print(5.1<=5)
# print(2.1==5)
# print(2!=3)
# print(4+7!=10+1)
# print(false)
# operatorii logici sunt not, and, or
# print(not True)
# print(not 3>7)
# print(True and False)
# print(True or False)
# a=4>3
# b=True
# print(a and b)
# ---------------------------------------------------------

# print("Se citesc de la tastatură două numere întregi diferite. Să se afișeze care este mai mare dintre ele.")
# n=int(input("n="))
# p=int(input("p="))
# if n>p:
#     print(n," este mai mare decat ",p)
# else:
#     print(p," este mai mare decat " ,n)


# ---------------------------------------------------------

# Să se scrie un program care citeşte un număr natural (comanda).
# Dacă acesta este 0 se vor citi două numere întregi a şi b şi se va tipări suma lor;
# contrar se vor citi două numere reale x şi y şi se va tipări produsul lor.

# n=int(input("n="))
# if n==0:
#     a = int(input("a="))
#     b = int(input("b="))
#     print("a+b=",a+b)
# else:
#     x = float(input("x="))
#     y = float(input("y="))
#     print("x*y=",x*y)

# ---------------------------------------------------------

# Se citeşte o valoare întreagă. În cazul în care aceasta este pară (se împarte exact la 2)
# se va tipări mesajul "am citit un număr par". Altfel, programul nu va oferi nicun mesaj.

# b = int(input("b="))
# if b%2==0:
#     print("am citit un numar par")
#
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
# d = float(input("d="))
# if c+d>0:
#     print (a+b)
# elif c+d==0:
#     print(a - b)
# else:
#     print (a*b)
# ---------------------------------------------------------

# print("Se citesc 3 numere întregi. Câte sunt pare?")
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
# p=0
# if a%2==0:
#     p=p+1
# if b%2==0:
#     p=p+1
# if c%2==0:
#     p=p+1
# print ("Sunt ",p,"numere pare")
# ---------------------------------------------------------

# x = int(input("x="))
# if x<0:
#     E=x+1
# else:
#     E=x-1
# print(E)
# ---------------------------------------------------------
# r=int(input("Cat face 7x8 ?"))
# if r==56:
#     print("Corect!")
# else:
#     print ("Incorect!")
# ---------------------------------------------------------
x = float(input("x="))
if x<0:
    print(x)
elif 0<=x<10:
    print (2*x)
elif 10<=x<100:
    print(3 * x)
else:
    print (4 * x)