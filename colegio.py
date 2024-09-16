from laboratorio import Laboratorio
from estudiante import Estudiante
from asistencialaboratorio import AsistenciasLaboratorio



class Colegio:

	def __init__(self, nombre):
		self.__nombre = nombre
		self.__estudiantes = []
		self.__laboratorios = []
		self.__asistencias = []


	def set_nombre(self, nombre):
		self.__nombre = nombre


	def get_nombre(self):
		return self.__nombre


	def get_laboratorio(self, posicion):
		return self.__laboratorios[posicion]


	def get_estudiante(self, posicion):
		return self.__estudiantes[posicion]



	def get_estudiantes(self):
		return self.__estudiantes


	def get_laboratorios(self):
		return self.__laboratorios


	def get_asistencias(self):
		return self.__asistencias


	def adicionar_estudiante(self, estudiante):
		if self.buscar_estudiante(estudiante.get_codigo()) == -1:
			self.__estudiantes.append(estudiante)
			return True
		return False 


	def buscar_estudiante(self, estudiante_codigo):
		for i in range (len(self.__estudiantes)):
			if self.__estudiantes[i].get_codigo() == estudiante_codigo:
				return i 
		return -1


	def adicionar_laboratorio(self, laboratorio):
		if self.buscar_laboratorio(laboratorio.codigo) == -1:
			self.__laboratorios.append(laboratorio)
			return True
		return False 


	def buscar_laboratorio(self, codigo_laboratorio):
		for i in range (len(self.__laboratorios)):
			if self.__laboratorio[i].codigo == codigo_laboratorio:
				return i 
		return -1


	def adicionar_asistencia(self, asistencia):
		if self.buscar_asistencia(asistencia) == -1:
			self.__asistencias.append(asistencia)
			return True
		return False 


	def buscar_asistencia(self, asistencia):
		for item_asistencia in self.__asistencias:
			if item_asistencia.get_codigo() == asistencia.get_codigo():
				return True 
		return -1


	def get_asistencia_laboratorio(self, codigo_laboratorio):
		asistencia_laboratorio = []
		for asistencia in self.__asistencias:
			if asistencia.get_laboratorios().codigo == codigo_laboratorio:
				asistencia_laboratorio.append(asistencia)
		return asistencia_laboratorio
