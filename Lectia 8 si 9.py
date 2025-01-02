# # Siruri de caractere in python - lectia 8
# a="Serafim"
# b="Maria"
# # print(a+" si "+b)
# # print((a+" ")*30)
# # print((b+" ")*30)
# for i in a:
#     print(i)
#
# print("-------------------------------------")
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# # index negativ -de la dreapta la stanga, ultima litera are index -1
# print(a[-1])
# print(a[-2])
# print(a[-3])
# print(a[-4])
# print(len(a))
#
# sw = "Îmi place Star Wars!"
# print("Star" in sw)
# print("StarWars" in sw)
# print("Star" not in sw)
# # Subșiruri - lectia 9
#
# s1 = "La Sinaia este zapada!"
# print(s1[3:9])
# print(s1[15:21])
# #ne jucăm apoi cu șirurile
# s2 = s1[3:9] #Sinaia
# s3 = s2[0:3] #Sin
# s4=s1[15:21]
# print(s4)
# print(s3,"se traduce ca pacat in engleza.")
# #inversul sirului
# print(s1[::-1])
# a = "Game Of Thrones - GOT"
# print(a.capitalize())
# print(a.lower())
# print(a.upper())
# print(a.swapcase())
# print(a.count("s"))
# print(a.find("me"))
# b=a.replace("GOT","Urzeala tronurilor")
# print(b)

#  Realizați un program care citește de la tastatură un șir de caractere și afișează
#  de câte ori apare litera "a" în text.

# sir=input("Introduceti o propozitie ca sa afisez cate vocale apar")
# print("Textul introdus este ",sir)
# print("-------")
# print("Vocale:")
# a=sir.count("a")
# print("a - ",a)
# e=sir.count("e")
# print("e - ",e)
# i=sir.count("i")
# print("i - ",i)
# o=sir.count("o")
# print("o - ",o)
# u=sir.count("u")
# print("u - ",u)
# print("-------")
# print("Total vocale")
# print(a+e+i+o+u)
# print("Lungimea sirului :",len(sir))
# print("Consoana x apare de ",sir.count("x")," ori")
# if sir[0]=="A":
#     print("Sirul incepe cu A")
# elif sir[0]=="a":
#     print("Sirul incepe cu a")
# else:
#     print("Sirul nu incepe cu a")
# if sir[-1]==".":
#     print("Sirul se termina cu punct")
# else:
#     print("Sirul nu se termina cu punct")
# print(len(sir)>20)
oras=input("Introduceti numele orasului")
tara=input("Introduceti numele tarii")
cifra=int(input("Introduceti cifra"))
print("Super. Si eu am vizitat ",tara,", iar in ",oras," am petrecut minunat ",cifra," zile.")
print("Afisare cu majuscule de la dreapta la stanga")
majuscule=oras.upper()
print(majuscule[::-1])
print("Primul caracter este la fel cu ultimul?")
print(oras[0]==oras[-1])
