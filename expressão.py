# Expressão

class Expressao:
	num1 = 0
	num2 = 0
	op = ""
	
	def __init__ (self):
		self.num1 = int(input(''))
		self.num2 = int(input(''))
		self.op = input('')

	def resolver (self):
		if self.op == '+':
			print(self.num1 + self.num2)
		elif self.op == '-':
			print(self.num1 - self.num2)
		elif self.op == '*':
			print(self.num1 * self.num2)
		elif self.op == '/':
			print(int(self.num1 / self.num2))

processo = Expressao()
processo.resolver()		








# # Expressão

# class Matematica:
# 	expressao = [ ]
	
# 	def __init__ (self):
# 		self.expressao.append(int(input('')))
# 		self.expressao.append(int(input('')))
# 		self.expressao.append(input(''))
# #		print(self.expressao)

# 	def resolver (self):
# 		n1 = self.expressao[0] 
# 		n2 = self.expressao[1]
# 		simb = self.expressao[2]
# 		if simb == '+':
# 			print(n1+n2)
# 		elif simb == '-':
# 			print(n1-n2)
# 		elif simb == '*':
# 			print(n1*n2)
# 		elif simb == '/':
# 			print(int(n1/n2))

# processo = Matematica()
# processo.resolver()		