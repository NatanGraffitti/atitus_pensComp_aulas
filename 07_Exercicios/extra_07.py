def fahrenheit_para_celsius(valor):
  temp = float(input("Diga a temperatura em Fahrenheit: "))
  f_para_c = (temp - 32) / 1.8
  print(f"A temperatura em graus Celcius é:  {f_para_c}C°")


def celsius_para_farenheit(valor):
  temp = float(input("Diga a temperatura em Celsius: "))
  c_para_f = (1.8 * temp) + 32
  print(f"A temperatura em graus Fahrenheit é: {c_para_f}F°")

def test():
  assert fahrenheit_para_celsius(104) == 40
  assert fahrenheit_para_celsius(-13) == -25

  assert celsius_para_fahrenheit(40) == 104
  assert celsius_para_fahrenheit(-25) == -13

  assert celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30
