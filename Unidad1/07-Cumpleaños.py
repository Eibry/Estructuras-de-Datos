def birth():
    variables = ('dia', 'mes', 'año')
    cumpleaños = ()
    for i in variables:
        birth = int(input(f'¿En qué {i} naciste? '))
        cumpleaños += (birth,)
    return cumpleaños

meses = ('', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

dia, mes, año = birth()
print(f'Naciste el {dia} del {meses[mes]} del {año}')

if __name__ == '__main__':
    birth()