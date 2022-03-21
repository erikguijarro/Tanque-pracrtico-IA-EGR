#41
colores = input('Introduce tu color favorito:\n')
tupla_colores = ('verde', 'azul', 'negro', 'rojo')

if colores in tupla_colores[0]:
	print('El color verde está admitido')
elif colores in tupla_colores[1]:
	print('El color azul está admitido')
elif colores in tupla_colores[2]:
	print('El color negro está admitido')
elif colores in tupla_colores[3]:
	print('El color rojo está admitido')
else:
	print('Color no admitido')
