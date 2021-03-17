import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

# Set the app size
Window.size = (500, 700)


Builder.load_file('calc.kv')

class MyLayout(Widget):
	def clear(self):
		self.ids.calc_input.text = "0"

	# Create a button pressing function
	def button_press(self, button):
		# create a variable that contains whatever
		prior = self.ids.calc_input.text

		# determine if 0 is sitting there
		if prior == "0":
			self.ids.calc_input.text = ''
			self.ids.calc_input.text = f'{button}'
		else:
			self.ids.calc_input.text = f'{prior}{button}'

	# Create addition function
	def math_sign(self, sign):
	# create a variable that contains whatever
		prior = self.ids.calc_input.text

	# slap a plus sign to the text
		self.ids.calc_input.text = f'{prior}{sign}'

	# Create Function to remove last character in text box
	def remove(self):
		prior = self.ids.calc_input.text
		# Remove The last item in the textbox
		prior = prior[: -1]
		# Output back to the textbox
		self.ids.calc_input.text = prior

	# Create function to make text box positive or negative
	def pos_neg(self):
		prior = self.ids.calc_input.text
		# Test to see if there's a - sign already
		if '-' in prior:
			self.ids.calc_input.text = f'{prior.replace("-", "")}'
		else:
			self.ids.calc_input.text = f'-{prior}'





	# Create decimal function
	def dot(self):
		prior = self.ids.calc_input.text
		# Add a decimal to the end of the text

		if "." in prior:
			pass
		else:
			prior = f'{prior}.'
			# Output back to the text box
			self.ids.calc_input.text = prior


	# Create equals to  function
	def equals(self):
	# create a variable that contains whatever
		prior = self.ids.calc_input.text

		# Additon
		if "+" in prior:
			num_list = prior.split("+")
			answer = 0.0
			# loop thru our list
			for number in num_list:
				answer = answer + float(number)

			# print the anser in the text box
			self.ids.calc_input.text = str(answer)

class CalculatorApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	CalculatorApp().run()