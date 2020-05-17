# Find the xxx to xxx digit of pi

import math

from decimal import Decimal, getcontext


def pi_archimedes(n):
    polygon_edge_length_squared = Decimal(2)
    polygon_sides = 4
    for i in range(n):
        polygon_edge_length_squared = 2 - 2 * (1 - polygon_edge_length_squared / 4).sqrt()
        polygon_sides *= 2
    return polygon_sides * (polygon_edge_length_squared).sqrt()/2


getcontext().prec = 200
result = pi_archimedes(100)
getcontext().prec = 110
result = +result
result_str: str = str(result)
last_10_digits = result_str[101:110]

print(last_10_digits)
