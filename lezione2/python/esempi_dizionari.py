esempio_dizionario = {'Enrico': 149, 'Martina': 581}

altro_dizionario = dict([('Martina', 581), ('Enrico', 149)])

print(esempio_dizionario)

esempio_dizionario['Emanuele'] = 215

del esempio_dizionario['Enrico']

print(esempio_dizionario)

print('Emanuele' in esempio_dizionario)

print('Emanuele' in altro_dizionario)