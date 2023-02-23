#main.py
import random
import math
from mpl_toolkits import mplot3d
import functions as fun

banyakTitik = int(input("banyak titik : "))
setOfTitik = fun.setOfTitik(banyakTitik)
print(setOfTitik)
print("distance between :", setOfTitik[0], "and", setOfTitik[-1], ":", fun.euclideanDistance(setOfTitik[0], setOfTitik[-1]))