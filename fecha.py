from datetime import datetime

class Fecha:
	MESES = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre" , "Noviembre", "Diciembre")

	def __init__(self, *args):
		fecha = datetime.now()

		if len(args) != 3:
			self.dia = fecha.day
			self.mes = fecha.month
			self.anio = fecha.year

		else:
			if self.validar_anio(args[0]):
				self.anio = args[0]

				if self.validar_mes(args[1]):
					self.mes = args [1]

					if self.validar_dia(args[2]):
						self.dia = args [2]

					else:
						self.dia = fecha.day
				else:
					self.mes = fecha.month
			else:
				self.anio = fecha.year


	def validar_anio(self, anio):
		if anio > 0:
			return True
		return False


	def validar_mes(self, mes):
		if 1 <= mes <= 12:
			return True
		return False


	def validar_dia(self, dia):
		if self.mes in [4,6,9,11]:
			if 1 <= dia <= 30:
				return True


		elif self.mes in [1,3,5,7,8,10,12]:
			if 1 <= dia <= 31:
				return True


		elif self.mes in 2:
			if self.is_leap(self.anio):
				if 1 <= dia <= 29:
					return True

			else:
				if 1 <= dia <= 28:
					return True

		return False



	def es_bisisto(self, anio):
		if anio % 4 ==0 and (anio % 100 !=0 or anio %400 ==0):
			return True
		return False



	def actualizar_fecha(self, anio, mes, dia):
		if self.validar_anio(anio):
			self.anio = anio

		if self.validar_mes(mes):
			self.mes = mes

		if self.validar_dia(dia):
			self.dia = dia


	def visualizar_fecha(self):
		print("Fecha: %d/%s/%s" %(self.dia, Fecha.MESES[self.mes -1], self.anio))



