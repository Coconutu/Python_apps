from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class Lista_shop(App):
    def build(self):
        def load_from_file():
            try:
                fp=open('shopping.txt', 'r')
                continut=fp.read()
                lista_cumparaturi.text=continut
                fp.close()
            except:
                umplutura.text='Eroare. Nu gasesc fisierul shopping.txt!'


        marime_font=50

        super_box=BoxLayout(orientation='vertical')

        lista_box=BoxLayout(orientation='vertical',size_hint=(1.0,0.5))
        lista_butoane=BoxLayout(orientation='horizontal',size_hint=(1.0,0.1))
        caseta_text_box=BoxLayout(orientation='horizontal',size_hint=(1.0,0.1))
        umplutura=Label(text='Botz shopping list',font_size=marime_font,size_hint=(1.0,0.3))


        buton_add=Button(text='Adauga',font_size=marime_font,color='pink')
        buton_sterge=Button(text='Șterge',font_size=marime_font,color='red')
        caseta_text=TextInput(multiline=False,font_size=marime_font+10,
                              foreground_color=(1, 0.9,0.1), background_color=(0, 0.3, 1))

        lista_cumparaturi=TextInput(multiline=True,font_size=marime_font,foreground_color=(1, 0.9,0.4),background_color=(0, 0.5, 1))

        buton_add.bind(on_press=lambda x: adauga())
        buton_sterge.bind(on_press=lambda x: sterge())


        lista_box.add_widget(lista_cumparaturi)
        lista_butoane.add_widget(buton_add)
        lista_butoane.add_widget(buton_sterge)

        caseta_text_box.add_widget(caseta_text)

        super_box.add_widget(caseta_text_box)
        super_box.add_widget(lista_butoane)
        super_box.add_widget(lista_box)
        super_box.add_widget(umplutura)
        load_from_file()

        def sterge_linii_goale(string_with_empty_lines):

            lines = string_with_empty_lines.split("\n")
            non_empty_lines = [line for line in lines if line.strip() != ""]

            string_without_empty_lines = ""
            for line in non_empty_lines:
                string_without_empty_lines += line + "\n"

            string_without_empty_lines=string_without_empty_lines.strip('\n')

            return string_without_empty_lines

        def adauga():
            if caseta_text.text!='':
                if lista_cumparaturi.text=='':
                    lista_cumparaturi.text = caseta_text.text
                else:
                    lista_cumparaturi.text=lista_cumparaturi.text+'\n'+caseta_text.text
                caseta_text.text=''
                caseta_text.focus=True
                salveaza_in_fisier()

        def sterge():

            lista_cumparaturi.delete_selection()
            lista_cumparaturi.text=sterge_linii_goale(lista_cumparaturi.text)
            salveaza_in_fisier()

        def salveaza_in_fisier():
            try:
                fp = open('shopping.txt', 'w')
                fp.write(lista_cumparaturi.text)
                fp.close()
            except:
                umplutura.text='Eroare'

        return super_box

if __name__=='__main__':
    root=Lista_shop()
    root.run()