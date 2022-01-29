
dias = int(input('Informe a quantidade de dias:'))
horas = int(input('Informe a quantidade as horas:'))
minutos = int(input('Informe a quantidade de minutos:'))
segundos = int(input('Informe a quantidade de segundos:'))

total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print ('O total em segundos é:', total)
