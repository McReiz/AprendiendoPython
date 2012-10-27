#encoding: utf-8
#elif es una contracción de else if, por lo tanto elif numero > 0 puede leerse como "si no, si numero es mayor que 0". 
#Es decir, primero se evalúa la condición del if. 
#Si es cierta, se ejecuta su código y se continúa ejecutando el código posterior al condicional; si no se cumple, se evalúa la condición del elif.
i = 3

if i > 0:
	print "tenemos un numero positivo"
elif i < 0:
	print "tenemos un numero negativo"
else:
	print "tenemos cero"
