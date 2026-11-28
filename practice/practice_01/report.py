import math


def relative_error(approx, exact):
    if exact == 0:
        return float('inf') if approx != 0 else 0.0
    return abs(approx - exact) / abs(exact)

def absolute_error(approx, exact):
    return abs(approx - exact)

approx_pi = 3.14
exact_pi = math.pi
print(f"π:\nΔx = {absolute_error(approx_pi, exact_pi)}\nδx = {relative_error(approx_pi, exact_pi)}\n")

approx_sum = 0.1 + 0.2
exact_sum = 0.3
print(f"0.1 + 0.2:\nΔx = {absolute_error(approx_sum, exact_sum)}\nδx = {relative_error(approx_sum, exact_sum)}\n")

n = 1_000_000
numbers_list = [0.1] * n
approx_million = sum(numbers_list)
exact_million = 100_000.0

print(f"1.000.000:\nΔx = {absolute_error(approx_million, exact_million)}\nδx = {relative_error(approx_million, exact_million)}")