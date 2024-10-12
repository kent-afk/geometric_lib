import circle
import square


figs = ['circle', 'square'] # создание класса функций circle / square
funcs = ['perimeter', 'area'] # создание класса функций perimeter / area
sizes = {} # создание словаря размеров

def calc(fig, func, size):
	'''Принимает 3 значения fig - class funcs - class sizes '''
	assert fig in figs 
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})') #считывает тип форматированных строк
	print(f'{func} of {fig} is {result}') #выводит название функции perimeter or are для circle or square и выводит результат этих операций 

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		'''пока не инициализирована тип фигуры ждем input пользователя после ввода запоминаем выбор в fig'''
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		'''ждем пока пользователь введет функцию которую хочет произвести'''
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)



