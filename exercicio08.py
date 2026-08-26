''' Desconto no produto '''

print ("digite valor: ")
valor = float(input())

print (f'preço R$: {valor:.2fr}')
desconto = valor * 0.05
print (f'desconto R$: {desconto:.2f}')

precoFinal = valor - desconto
print (f'preço final R$: {precoFinal:.2f}')
