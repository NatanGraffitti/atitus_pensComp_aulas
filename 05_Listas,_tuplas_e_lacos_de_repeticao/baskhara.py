import math

def baskhara(a, b, c):
    delta = (b**2) - (4*a*c)
    if delta < 0:
        return None
    elif delta == 0:
        x = (-b + math.sqrt(delta)) / (2 * a)
        return [x]
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return sorted([x1, x2])

def test():
    assert baskhara(1, -3, 2) == [1.0, 2.0]
    assert baskhara(2, 3, -2) == [-2.0, 0.5]
    assert baskhara(1, -5, 6) == [2.0, 3.0]
    assert baskhara(1, -7, 10) == [2.0, 5.0]
    assert baskhara(1, 2, 3) is None
    assert baskhara(1, 0, 0) == [0.0]


print(baskhara(1, -3, 2))
