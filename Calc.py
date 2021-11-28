from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

from kivy.config import Config
Config.set('graphics','resizable', 0)
Config.set('graphics','width', 1080)
Config.set('graphics','height', 2340)

from mpmath import besselj

class CalcApp(App):
	def build(self):
		self.formula = "0"
		bl = BoxLayout(orientation = 'vertical')
		gl = GridLayout(cols = 4, size_hint = (1, .6), spacing = 2)

		self.lbl = Label(text = '0', font_size = 100, size_hint = (1, .4), halign='right', valign='center',text_size = (1000, 2340*.4))
		
		bl.add_widget( self.lbl )

		gl.add_widget( Button(text = 'Jn', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '(m)', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '<—', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.deleting) )
		gl.add_widget( Button(text = '÷', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_operation) )
		
		gl.add_widget( Button(text = '7', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '8', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '9', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = 'x', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_operation) )

		gl.add_widget( Button(text = '4', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '5', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '6', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '-', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_operation) )

		gl.add_widget( Button(text = '1', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '2', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '3', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '+', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_operation) )

		gl.add_widget( Button(text = 'C', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.reset) )
		gl.add_widget( Button(text = '0', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_number) )
		gl.add_widget( Button(text = '.', font_size = 80, background_color = [1,1,1,1], background_normal = '', color = [0,0,0,1], on_press = self.add_operation) )
		gl.add_widget( Button(text = '=', font_size = 80, background_color = [.97,.51,.1,1], background_normal = '', color = [0,0,0,1], on_press = self.calc_result) )

		bl.add_widget(gl)

		return bl

	def add_number(self, instance):
		if( self.formula == "0"):
			self.formula = ""
		if(str(instance.text) == 'Jn'):
			self.formula += 'n = '
		elif(str(instance.text) == 'n'):
			self.formula += ','
		elif(str(instance.text) == '(m)'):
			self.formula += ', m = '
		else:
			self.formula += str(instance.text)
		self.update_label()

	def add_operation(self, instance):
		if( str(instance.text) == 'x'):
			self.formula += '*'
		elif(str(instance.text) == '÷'):
			self.formula += '/'
		
		else:
			self.formula += str(instance.text)
		self.update_label()

	def update_label(self):
		self.lbl.text = self.formula

	def calc_result(self, instance):
		if self.lbl.text:
			try:
				if('n' in self.lbl.text):
					self.lbl.text = self.lbl.text.replace("n = ", "besselj(")
					self.lbl.text = self.lbl.text.replace(", m = ", ",")
					self.lbl.text = str(self.lbl.text + ')')
				self.lbl.text = str(eval(self.lbl.text))
				self.formula = self.lbl.text
			except:
				self.lbl.text = "Error"

	def reset(self, instance):
		self.formula = "0"
		self.update_label()

	def deleting(self, instance):
		self.formula = self.formula[:-1]
		self.update_label()

CalcApp().run()