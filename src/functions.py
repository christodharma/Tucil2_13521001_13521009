#functions.py
import random
import math
from mpl_toolkits import mplot3d

#constructor set of titik
#nTitik mewakilkan berapa titik yang diinginkan
#nDimensi mewakilkan berapa dimensi titik dibuat (default: 3)
def setOfTitik(nTitik, nDimensi=3):
    result = []
    for i in range(nTitik):
        point = [random.randint(0,10) for j in range(nDimensi)]
        result.append(point)
    return result

#diketahui 2 titik dengan dimensi yang sama
#mengembalikan euclidean distance dari kedua titik
def euclideanDistance(aTitik, bTitik):
    result = 0
    if len(aTitik) == len(bTitik):
        for i in range(len(aTitik)):
            result += (aTitik[i]-bTitik[i])**2
        return math.sqrt(result)

#static int callEuclideanctr