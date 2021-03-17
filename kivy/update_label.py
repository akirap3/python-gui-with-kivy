import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.floatlayout import FloatLayout

Builder.load_file('update_label.kv')

class MyLayout(Widget):
	def press(self):
		# Create variables for our widget
		name = self.ids.name_input.text

		# Update the label
		self.ids.name_label.text = f'Hello, {name}'

		# Clear Input box
		self.ids.name_input.text = ''

class AwesomeApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	AwesomeApp().run()

