largura = float(input('largura da parece ? '))
altura  = float(input('Altura da parede ?'))


area = largura * altura
tinta = area / 2

print("sua parede tem a dimensão de {}x{} e a sua área é de {}m² " .format(largura, altura, area))
print("para pintar essa parede, voce precisa de {}l de tinta" .format(tinta))