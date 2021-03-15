import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
	# Initialize infinite keywords
	# Call grid layout constructor
	def __init__(self, **kwargs):
		super(MyGridLayout, self).__init__(**kwargs)

		# Set columns
		self.cols=2

		# Add widgets
		self.add_widget(Label(text="Name"))
		# Add Input Box
		self.name = TextInput(multiline=True)
		self.add_widget(self.name)

		self.add_widget(Label(text="Favorite Pizza"))
		self.pizza = TextInput(multiline=True)
		self.add_widget(self.pizza)

		self.add_widget(Label(text="Favorite Color"))
		self.color = TextInput(multiline=True)
		self.add_widget(self.color)

		# Create a Submit Button
		self.submit = Button(text="Submit", font_size=32)
		# Bind the button
		self.submit.bind(on_press=self.press)
		self.add_widget(self.submit)

	def press(self, instance):
		name = self.name.text
		pizza = self.pizza.text
		color = self.color.text

		# print(f'Hello {name}, you like {pizza}, and your favorite color is {color}') 
		# Print it ot the scren
		self.add_widget(Label(text=f'Hello {name}, you like {pizza}, and your favorite color is {color}'))

class MyApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MyApp().run()

