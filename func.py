#from matplotlib.pyplot import plt
import math
import subprocess

def func(start, end, step, function):
    x = [xi for xi in range(start, end + 1, step)]
    y = list(map(function, x))
    # plt.plot(x, y)
    print(x)
    print(y)
    return 0

func(0, 10, 1, lambda x : math.sqrt(x))

for i in range(5):
    print("\n")



res = subprocess.call("Rscript ~/plotting/plot.R 0 0", shell=True)
