import math
import subprocess

def func(start, end, step, function):
    x = [xi for xi in range(start, end + 1, step)]
    y = list(map(function, x))
    return x, y

x, y = func(0, 720, 1, lambda x : math.sin(math.radians(x)))

res = subprocess.call(f"Rscript ~/graphing-calculator-CLI/plot.R \"{x}\" \"{y}\"", shell=True)
