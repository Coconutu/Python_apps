'''x + y	Adunare
x – y	Scadere
x * y	Inmultire
x / y	Impartire
x // y	Catul impartirii
x % y	Restul impartirii
x ** y	Ridicare la putere'''
import os
import colorama
from colorama import Fore
import math
calc=True
while calc==True:
	try:
		print(Fore.GREEN,'')
		a=input('Scrie expresia si apasa Enter!\n')
		rezultat=eval(a)
		print(Fore.RED,f'Raspuns: {rezultat}')
		if rezultat in range(0,45):
			print(Fore.BLUE,'Insuficient')
		elif rezultat in range(44,65):
			print(Fore.BLUE,'Suficient')
		elif rezultat in range(64,80):
			print(Fore.BLUE,'Bine')
		elif rezultat in range(79,101):
			print(Fore.BLUE,'Foarte bine')
		print('\n\n\nApasa Enter')
		a=input()
		os.system('clear')
		
	except:
		print('Eroare')
	
	
	