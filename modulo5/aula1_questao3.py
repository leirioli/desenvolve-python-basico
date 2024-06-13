import random

randnumb = random.randint(1,10)

while True:
    palpite = int(input('Adivinhe o número entre 1 e 10: '))
    if palpite > randnumb:
        print('Muito alto, tente novamente!')
    elif palpite < randnumb:
        print('Muito baixo, tente novamente!')
    else:
        print('Correto! O número é', randnumb)
        break