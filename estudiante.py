
class Estudiante:
	
	def __init__(self, nombre, apellido, codigo):
		self.__nombre = nombre
		self.__apellido = apellido
		self.__codigo = codigo


	def set_nombre(self, nombre):
		self.__nombre = nombre


	def get_nombre(self):
		return self.__nombre


	def set_apellido(self, apellido):
		self.__apellido = apellido

	def get_apellido(self):
		return self.__apellido


	def set_codigo(self, codigo):
		self.__codigo = codigo


	def get_codigo(self):
		return self.__codigo

		
	def visualizar_estudiante(self):
		print("Nombre : %s" %(self.__nombre))
		print("Apellido : %s" %(self.__apellido))
		print("Codigo : %s" %(self.__codigo))