firstnumb = float(input('Digite o primeiro número: '))
secondnumb = float(input('Digite o segundo número: '))

dif_absolute = abs(firstnumb - secondnumb)

result_round = round(dif_absolute,2)

print('A diferença absoluta entre os números é:', result_round)