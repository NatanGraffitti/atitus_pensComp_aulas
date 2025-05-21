def valor_pgto(valor, forma_pgto):
  valor = float(input("Digite o valor a ser pago:")
  print("Formas de pagamento: ")
  print("1 - para PIX")
  print("2 - Para À Vista")
  print("3 - Parcelado em 2x sem juros")
  print("4 - Parcelado em 3x ou mais com juros")
  pagamento = int(input("Digite o número relacionado com a forma de pagamento que sera realizada."))

  if pagamento = 1:
      resultado = valor - (valor * (15 / 100))
      print (f"Valor com desconto de 15%: {resultado}")
  elif pagamento == 2:
      resultado = valor - (valor * (10 / 100))
      print(f"Valor com desconto de 10%: {resultado}")
  elif pagamento == 3:
      print(f"Parcelado em 2x sem juros. Valor total {valor}")
  elif pagamento == 4:
      resultado = valor + (valor * (10 / 100))
      print(f"Valor com acréscimo de 10%: {resultado}")
  else:
    print("Opção inválida. Por favor, escolha uma das opções listadas.")



def test ():
  assert valor_pgto(100, 1) == 85
  assert valor_pgto(100, 2) == 90
  assert valor_pgto(100, 3) == 100
  assert valor_pgto(100, 4) == 110
