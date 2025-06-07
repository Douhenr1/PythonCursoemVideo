km = float(input('quantos Km o seu veiculo percorreu ?'))
dias = float(input('quantos dias o carro foi alugado ?'))


pago = (dias * 60) + (km * 0.15)

print('O total a pagar é de R$ {:.2f}'.format(pago))