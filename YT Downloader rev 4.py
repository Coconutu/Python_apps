from pytube import YouTube
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class MainApp(App):

    def build(self):


        superbox=BoxLayout(orientation='vertical')
        textinput_pentru_link = TextInput(multiline=False, font_size=20)
        buton_download = Button(text="Download *.MP3", background_color=(1, 0.2,1),font_size=60)
        buton_clear = Button(text="Șterge link", background_color=(0.2,1,0.2),font_size=60)
        buton_download.bind(on_press=lambda x: descarca_mp3())
        buton_clear.bind(on_press=lambda x: curata())
        status=Label(text='Status',font_size=40)
        superbox.add_widget(buton_download)

        superbox.add_widget(textinput_pentru_link)
        superbox.add_widget(buton_clear)
        superbox.add_widget(status)


        def descarca_mp3():
            try:
                link=YouTube(textinput_pentru_link.text)
                video = link.streams.filter(only_audio=True).first()
                destination ='.'
                out_file = video.download(output_path=destination)
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                status.text='Melodia fost descărcată cu succes.'
            except:
                status.text='Eroare'

        def curata():
            textinput_pentru_link.text=''
            status.text='Status'



        return superbox

if __name__=='__main__':
    root=MainApp()
    root.run()