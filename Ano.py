name = str(input('Informe o seu nome: '))
ano = int(input('Sr(a){} Qual o ano o senhor  Gostaria de analisar: '.format(name)))

if ano % 4 == 0:
    print('O ano {} é  bissesto '.format(ano))
else:
    print('O ano {} não é bissesto'.format(ano))
