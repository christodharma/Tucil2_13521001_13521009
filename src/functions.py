#functions.py
import random
import math
from mpl_toolkits import mplot3d

#static int callEuclideanctr        how?

#constructor set of titik
#nTitik mewakilkan berapa titik yang diinginkan
#nDimensi mewakilkan berapa dimensi titik dibuat (default: 3)
def randomSetOfTitik(nTitik, nDimensi=3):
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

#sorting untuk proses divide
#selalu terurut membesar
#https://scripteverything.com/python-2d-list-sort-by-multiple-columns-code-examples-no-imports-one-liners/
#tidak mengubah data input
def sortBySumbu(setTitik, sumbu):
    if (sumbu == 'x' or sumbu == 'X'):
        sumbu = 1
    elif (sumbu == 'y' or sumbu == 'Y'):
        sumbu = 2
    elif (sumbu == 'z' or sumbu == 'Z'):
        sumbu = 3
    newSetTitik = sorted(setTitik, key=lambda row:(row[sumbu-1]))
    return newSetTitik

#divide
#membagi set titik menjadi 2 bagian pada bagian tengah
def divide(setTitik):
    half = len(setTitik)//2
    return setTitik[:half], setTitik[half:]

#divide and conquer
#mencari pasangan titik yang paling dekat
#belum memperhitungkan kalau yang terdekat tepat di garis divide
def findClosestPair(setTitik):
    if (len(setTitik) == 2):
        return euclideanDistance(setTitik[0], setTitik[1]), setTitik    #perlu bisa return setTitiknya itu sendiri buat visualisasi
    else:
        d1,d2 = divide(setTitik)
        return min(findClosestPair(d1), findClosestPair(d2))      #ini bisa terpengaruh kalo juga return setTitik
                                                                        #bisa pengaruh penggunaan memori?


def printTitik(titikAsArr):
    print("(", end = "")
    print(*titikAsArr, sep = ', ', end="")
    print(")", end="")