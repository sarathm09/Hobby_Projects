from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout

class MyAppApp(App):
	def build(self):
                f = FloatLayout()
                s = Scatter()
                l = Label(text = "Hello World")
                f.add_widget(s)
                s.add_widget(l)
                return f

MyAppApp().run()
