#encoding: utf-8
#elif es una contracci�n de else if, por lo tanto elif numero > 0 puede leerse como "si no, si numero es mayor que 0". 
#Es decir, primero se eval�a la condici�n del if. 
#Si es cierta, se ejecuta su c�digo y se contin�a ejecutando el c�digo posterior al condicional; si no se cumple, se eval�a la condici�n del elif.
i = 3

if i > 0:
	print "tenemos un numero positivo"
elif i < 0:
	print "tenemos un numero negativo"
else:
	print "tenemos cero"
