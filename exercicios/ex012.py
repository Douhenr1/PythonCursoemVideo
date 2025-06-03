produto = float(input('Qual o valor do seu produto ?'))

desconto = (5 / 100) * produto
descontofinal = produto - desconto

print ("meu produto custa R${} com o desconto fica R${}" .format(produto, descontofinal))