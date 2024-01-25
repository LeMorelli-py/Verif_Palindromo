frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if inverso == junto:
    print(f'O inverso de {junto} é {inverso}')
    print('Temos um Palindromo! ')
else:
    print('A frase não é palindromo!')