def baskhara(a, b, c):
  discriminante = b**2 - 4*a*c

  while True:
    if discriminante < 0:
        return False
    else:
        return True

    if discrimante = 0:
        return "Não é possível realizar a equação"

    x1 = (-b + ((b**2 - 4*a*c) * 1/2)) / (2 * a)
    x2 = (-b - ((b**2 - 4*a*c) * 1/2)) / (2 * a)

def test ():
  assert baskhara(1, -3, 2) == [2, 1]
  assert baskhara(2, 3, -2) == [-2, 0.5]
  assert baskhara(1, -5, 6) == [2, 3]
  assert baskhara(1, -7, 10) == [2, 5]

  assert baskhara(1, 2, 3) is None
  assert baskhara(1, 0, 0) == 0
