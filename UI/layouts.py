#File name: floatlayout.py

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
class FloatLayoutApp(App):
	def build(self):
		return FloatLayout()

FloatLayoutApp().run()