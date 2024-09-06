from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class AndroidApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, app from Sema4ka0", halign="center")


AndroidApp().run()