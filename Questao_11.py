preco = float(input('Informe o preço total:'))
desconto = float(input('Informe o desconto:'))

ValorDesconto = preco * desconto / 100
NovoPreco = preco - ValorDesconto

print ('O valor do desconto é:', ValorDesconto)
print('E o valor total com o desconto é:', NovoPreco)
