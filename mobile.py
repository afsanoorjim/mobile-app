from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDLabel:
        text: 'Hello, World!'
        halign: 'center'
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
