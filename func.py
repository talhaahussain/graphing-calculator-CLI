import math
import subprocess

def func(start, end, step, function):
    x = [xi for xi in range(start, end + 1, step)]
    y = list(map(function, x))
    return x, y

x, y = func(0, 10, 1, lambda x : math.sqrt(x))

res = subprocess.call(f"Rscript ~/plotting/plot.R {x} {y}", shell=True)
