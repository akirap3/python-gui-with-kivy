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
		# Set MyGridLayout default height and width
		self.cols=1
		self.row_force_default=True
		self.row_default_height=120
		self.col_force_default=True
		self.col_default_width=100

		# Create a second gridlayout
		# Set top_grid default height and width
		self.top_grid = GridLayout(
			row_force_default=True,
			row_default_height=40,
			col_force_default=True,
			col_default_width=100)

		self.top_grid.cols=2

		# Add widgets
		self.top_grid.add_widget(Label(text="Name"))
		# Add Input Box
		self.name = TextInput(multiline=True)
		self.top_grid.add_widget(self.name)

		self.top_grid.add_widget(Label(text="Favorite Pizza"))
		self.pizza = TextInput(multiline=True)
		self.top_grid.add_widget(self.pizza)

		self.top_grid.add_widget(Label(text="Favorite Color"))
		self.color = TextInput(multiline=True)
		self.top_grid.add_widget(self.color)

		# Add the new top_grid to our app
		self.add_widget(self.top_grid)

		# Create a Submit Button
		# Explicit set height and width
		self.submit = Button(text="Submit", 
			font_size=32,
			size_hint_y=None,
			height=50,
			size_hint_x=None,
			width=200)

		# Bind the button
		self.submit.bind(on_press=self.press)
		self.add_widget(self.submit)

	def press(self, instance):
		name = self.name.text
		pizza = self.pizza.text
		color = self.color.text

		self.name.text = ""
		self.pizza.text = ""
		self.color.text = ""

		# print(f'Hello {name}, you like {pizza}, and your favorite color is {color}') 
		# Print it ot the scren
		self.add_widget(Label(text=f'Hello {name}, you like {pizza}, and your favorite color is {color}'))

class MyApp(App):
	def build(self):
		return MyGridLayout()

if __name__ == '__main__':
	MyApp().run()

