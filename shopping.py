from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

class Lista_shop(App):
    def build(self):
        def load_from_file():
            try:
                fp=open('shopping.txt', 'r')
                continut=fp.read()
                lista_cumparaturi.text=continut
                fp.close()
            except:
                lista_cumparaturi.text='Eroare. Nu gasesc fisierul shopping.txt!'


        marime_font=60

        super_box=BoxLayout(orientation='vertical')

        lista_box=BoxLayout(orientation='vertical',size_hint=(1.0,0.8))
        lista_butoane=BoxLayout(orientation='horizontal',size_hint=(1.0,0.1))
        caseta_text_box=BoxLayout(orientation='horizontal',size_hint=(1.0,0.1))
        scroll = ScrollView(size_hint=(1, None), size=(10,Window.height))

        buton_add=Button(text='Adauga',font_size=marime_font,color='pink')
        buton_sterge=Button(text='Șterge',font_size=marime_font,color='red')
        buton_salveaza = Button(text='Salveaza', font_size=marime_font, color='yellow')
        caseta_text=TextInput(multiline=False,font_size=marime_font,
                              foreground_color=(1, 0.9,0.1), background_color=(0, 0.5, 1))
        lista_cumparaturi=TextInput(multiline=True,font_size=marime_font,foreground_color=(1, 0.9,0.1),background_color=(0, 0.5, 1))
        buton_add.bind(on_press=lambda x: adauga())
        buton_sterge.bind(on_press=lambda x: sterge())
        buton_salveaza.bind(on_press=lambda x: salveaza_in_fisier())
        lista_box.add_widget(lista_cumparaturi)
        lista_butoane.add_widget(buton_add)
        lista_butoane.add_widget(buton_sterge)
        lista_butoane.add_widget(buton_salveaza)
        caseta_text_box.add_widget(caseta_text)
        caseta_text.add_widget(scroll)
      
        super_box.add_widget(caseta_text_box)
        super_box.add_widget(lista_butoane)
        super_box.add_widget(lista_box)
        load_from_file()

        def adauga():
            if caseta_text.text!='':
                if lista_cumparaturi.text=='':
                    lista_cumparaturi.text = caseta_text.text
                else:
                    lista_cumparaturi.text=lista_cumparaturi.text+'\n'+caseta_text.text
                caseta_text.text=''
                caseta_text.focus=True

        def sterge():
            lista_cumparaturi.delete_selection()

        def salveaza_in_fisier():
            try:
                fp = open('shopping.txt', 'w')
                fp.write(lista_cumparaturi.text)
                fp.close()
            except:
                lista_cumparaturi.text='Eroare'

            




        return super_box

if __name__=='__main__':
    root=Lista_shop()
    root.run()