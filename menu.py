from os import system
from estudiante import Estudiante
from colegio import Colegio
from laboratorio import Laboratorio
from fecha import Fecha 
from asistencialaboratorio import AsistenciasLaboratorio



class Menu:

	def __init__(self, nombre_colegio):
		self.colegio = Colegio(nombre_colegio)



	def listar_estudiante(self):
		system("clear")
		print("**********************")
		print("**********************")
		print("   LISTAR ESTUDIANTES   ")
		print("**********************")
		print("**********************")
		print()

		for estudiante in self.colegio.get_estudiantes():
			print("**********************")
			print("Nombre : %s" %(estudiante.get_nombre()))
			print("Apellido : %s" %(estudiante.get_apellido()))
			print("Codigo : %s" %(estudiante.get_codigo()))
			print("**********************")
		input()




	def listar_laboratorios(self):
		system("clear")
		print("**********************")
		print("**********************")
		print("   LISTAR LABORATORIO ")
		print("**********************")
		print("**********************")
		print()

		for laboratorio in self.colegio.get_laboratorios():
			print("**********************")
			print("Nombre : %s" %(laboratorio.nombre))
			print("Codigo : %s"% (laboratorio.codigo))
			print("capacidad : %s" %(laboratorio.capacidad))
			print("**********************")
		input()



	def listar_asistencias(self):
		system("clear")
		print("**********************")
		print("**********************")
		print("   LISTAR ASISTENCIAS ")
		print("**********************")
		print("**********************")
		print()

		for asistencia in self.colegio.get_asistencias():
			print("**********************")
			asistencia.visualizar_asistencia()
			print("**********************")
		input()



	def listar_asistencias_laboratorio(self):
			system("clear")
			print("*****************************************")
			print("*****************************************")
			print("   LISTAR ASISTENCIAS POR LABORATORIO    ")
			print("*****************************************")
			print("*****************************************")
			print()

			codigo_laboratorio = input("Ingrese el codigo del laboratorio : ")
			pos = self.colegio.buscar_laboratorio(codigo_laboratorio)
			if pos != -1:
				for asistencia in self.colegio.get_asistencia_laboratorio(codigo_laboratorio):
					print("**********************")
					asistencia.visualizar_asistencia()
					print("**********************")
				input()

			else:
				print("**********************")
				print("  El laboratorio ingresado no existe ")
				print("**********************")
				input()



	def crear_estudiante(self):
		system("clear")
		print("**********************")
		print("**********************")
		print("   CREAR ESTUDIANTE   ")
		print("**********************")
		print("**********************")
		print()

		nombre_estudiante = (input("Ingrese el nombre del estudiante : "))
		apellido_estudiante = (input("Ingrese el apellido del estudiante : "))
		codigo_estudiante = (input("Ingrese el codigo del estudiante : "))
		estudiante = Estudiante(nombre_estudiante, apellido_estudiante, codigo_estudiante)
		self.colegio.adicionar_estudiante(estudiante)

		print()
		print("**********************")
		print(" ¡El estudiante fue agregado correctamente! ")
		print("**********************")
		input()


	def crear_laboratorio(self):
		system("clear")
		print("**********************")
		print("**********************")
		print("  CREAR LABORATORIO  ")
		print("**********************")
		print("**********************")
		print()

		nombre_laboratorio = (input("Ingrese el nombre del laboratorio : "))
		codigo_laboratorio = (input("Ingrese el codigo del laboratorio : "))
		capacidad_laboratorio = (input("Ingrese la capacidad del laboratorio : "))

		laboratorio = Laboratorio(nombre_laboratorio, codigo_laboratorio, capacidad_laboratorio)
		self.colegio.adicionar_laboratorio(laboratorio)
		print()
		print("**********************")
		print(" ¡El laboratorio fue agregado correctamente!")
		print("**********************")
		input()


	def crear_asistencia_laboratorio(self):
		system("clear")
		print("**********************")
		print("**********************")
		print("  CREAR ASISTENCIA LABORATORIO  ")
		print("**********************")
		print("**********************")
		print()

		codigo_laboratorio = input("Ingrese el codigo del laboratorio : ")
		pos_laboratorio = self.colegio.buscar_laboratorio(codigo_laboratorio)
		
		if pos_laboratorio != -1:
			try:
				dia = int(input("Ingrese el dia : "))
				mes = int(input("Ingrese el mes : "))
				anio = int(input("Ingrese el año : "))

				fecha = Fecha(anio, mes , dia)
				codigo_asistencia = int(input("Digite el codigo de asistencia : "))
				asistencia_laboratorio = AsistenciasLaboratorio(fecha, self.colegio.get_laboratorio(pos_laboratorio),codigo_asistencia)

				while True:
					print("**********************")
					print("  ASISTENCIA ESTUDIANTE  ")
					print("**********************")
					print("**********************")
					print(" 1 = Ingresar la asistencia del estudiante : ")
					print("**********************")
					print(" 2 = Salir Del Sistema")
					print("**********************")
					print()


					op = int(input("Digite la opcion a utilizar : "))

					if op == 1:
						codigo_estudiante = input("Digite el codigo del estudiante : ")
						pos_estudiante = self.colegio.buscar_estudiante(codigo_estudiante)



						if pos_estudiante != -1:
							asistencia_laboratorio.adicionar_estudiante(self.colegio.get_estudiante(pos_estudiante))



						else:
							print("**********************")
							print(" Error - El estudiante no existe")
							print("**********************")


					elif op == 2:
						break 

					else:
						print("**********************")
						print("  Error - El laboratorio no existe  ")
						print("**********************")

				self.colegio.adicionar_asistencia(asistencia_laboratorio)



			except ValueError:
				print("**********************")
				print("  La opcion debe ser un valor numericos")
				print("**********************")
				print()
				input()

		
		else:
			print("**********************")
			print("  El laboratorio no existe")
			print("**********************")
			print()

			laboratorio = Laboratorio(nombre_laboratorio, codigo_laboratorio, capacidad_laboratorio)



	def mostrar_menu(self):
		while True:
			system("clear")
			print("**********************")
			print("**********************")
			print("*****   SENA    ******")
			print("**********************")
			print("**********************")
			print("****    MENU   ******")
			print("**********************")
			print(" 1 = Crear Estudiante")
			print("**********************")
			print(" 2 = Crear Laboratorio")
			print("**********************")
			print(" 3 = Crear Asistencia Del Laboratorio")
			print("**********************")
			print(" 4 = Listar Estudiantes")
			print("**********************")
			print(" 5 = Listar Laboratorio")
			print("**********************")
			print(" 6 = Listar Asistencia")
			print("**********************")
			print(" 7 = Listar Asistencia De Laboratorio")
			print("**********************")
			print(" 10 = Salir Del Sistema")
			print("**********************")
			print()

			try:
				print("**********************")
				op = int(input("Ingrese la opcion a utilizar : "))
				print("**********************")
				print()



				if op == 1:
					self.crear_estudiante()


				elif op == 2:
					self.crear_laboratorio()



				elif op == 3:
					self.crear_asistencia_laboratorio()


				elif op == 4:
					self.listar_estudiante()


				elif op == 5:
					self.listar_laboratorios()


				elif op == 6:
					self.listar_asistencias()


				elif op == 7:
					self.listar_asistencias_laboratorio()



				elif op == 10:
					break



				else:		
					print("**********************")
					print(" Error. Solo Valores Numericos")
					print("**********************")
					input()



			except ValueError:
				print()
				print("**********************")
				print("Valores Ingresados Incorrectamente")
				print("**********************")
				input()



if __name__ == '__main__':
	colegio = Colegio("SENA")
	menu = Menu(colegio)
	menu.mostrar_menu()










