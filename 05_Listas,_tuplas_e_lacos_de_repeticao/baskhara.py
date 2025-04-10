def baskhara(a, b, c):
   if a == 0:
        return None
    
    delta = (b ** 2) - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        return sorted([x1, x2])

def test():
    assert baskhara(1, -3, 2) == [2, 1]
    assert baskhara(2, 3, -2) == [-2, 0.5]
    assert baskhara(1, -5, 6) == [2, 3]
    assert baskhara(1, -7, 10) == [2, 5]

    assert baskhara(1, 2, 3) is None
    assert baskhara(1, 0, 0) == 0
