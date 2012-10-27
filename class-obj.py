#enconding: utf-8
#aqui hago un class con mi coche
class MiCoche:
	def __init__(self,arrancar):
		self.arrancar = arrancar
		arrancar = True
		print "ruuuun"
	def gas(self,gasolina):
		self.gasolina = gasolina
		if gasolina > 3:
			print "nos vamos de paseo"
		else:
			print "no podemos arrancar sin gasolina"

	def velocidad(self,velocidad):
		self.velocidad = velocidad
		while velocidad < 64:
			velocidad = velocidad + 2
			print "vamos a "+ str(velocidad) +"KM/h"
			if velocidad == 2:
				print "estamos accelerando"
			if velocidad == 10:
				print "ya puedo sentir la brisa"
			if velocidad == 30:
				print "woow vamos rapido"
			if velocidad == 50:
				print "nadie nos alcanza"
			if velocidad == 64:
				print "ya no podemos accelerar mas"
		
carro = MiCoche(True)
carro.gas(0)
carro.velocidad(0)