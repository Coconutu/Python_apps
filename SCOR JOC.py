#pylint:disable=W0401
from tkinter import *
from tkinter import messagebox
window=Tk()
window.config(bg='yellow')
window.title('Scor TATI-MARIA')
pmaria=0
ptata=0
maxim=5


def inc_m():
    global pmaria
    pmaria=pmaria+1
    lm.config(text=f'Maria : {pmaria}')
    if pmaria==maxim:
    	messagebox.showinfo('FELICITARI','A CASTIGAT MARIA !')
    	reset()

def reset():
    global pmaria
    global ptata
    pmaria=0
    ptata=0
    lm.config(text=f'Maria : {pmaria}')
    lt.config(text=f'Tata : {ptata}')
def inc_t():
    global ptata
    ptata = ptata + 1
    lt.config(text=f' Tata  : {ptata}')
    if ptata==maxim:
    	messagebox.showinfo('FELICITARI','A CASTIGAT TATA !')
    	reset()

lab=Label(window,text='SCOR JOC',font=('Sans',14),bg='green')
bm=Button(window,text='+1 MARIA',fg='red',font=('Sans',29)
,command=inc_m)
bt=Button(window,text=' +1 TATA ',fg='blue',font=("Sans",29),command=inc_t)
br=Button(window,text='Reset',font=('Sans',19),command=reset)
lm=Label(window,text=f"Maria : {pmaria}",font=('Sans',39))
lt=Label(window,text=f"Tata : {ptata}",font=('Sans',39))
lab.pack(ipadx=250,ipady=20)
bm.pack(ipadx=30,ipady=30)
bt.pack(ipadx=30,ipady=30)
br.pack()
lm.pack(ipadx=10,ipady=50)
lt.pack(ipadx=10,ipady=50)
window.mainloop()


