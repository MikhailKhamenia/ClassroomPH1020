Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Ввод():
	def __call__(self, *args, **kwargs):
		reuturn input
		
SyntaxError: invalid syntax
>>> class Ввод():
	def __call__(self, *args, **kwargs):
		return input(*args, **kwargs)

	
>>> ввод_имени=Ввод()
>>> ввод_возраста=Ввод()
>>> имя=ввод_имени("Введите ваше имя")
Введите ваше имяМихаил Хаменя
>>> возраст=ввод_возраста("Сколько лет")
Сколько лет18
>>> возраст
'18'
>>> 