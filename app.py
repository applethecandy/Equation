from math import sqrt

def equation(a, b, c):
    d = b ** 2 - 4 * a * c
    
    if d > 0:
        return [(-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)]
    elif d == 0:
        return [-b / (2 * a), -b / (2 * a)]
    else:
        return []