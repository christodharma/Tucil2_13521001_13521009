#main.py
import random
import math
from mpl_toolkits import mplot3d
import functions as fun

banyakTitik = int(input("banyak titik : "))
if (input("3 dimensi atau tidak? (Y/N) ") not in "Yy"):
    setOfTitik = fun.randomSetOfTitik(banyakTitik, int(input("oke! masukkan dimensi: ")))
else:
    setOfTitik = fun.randomSetOfTitik(banyakTitik)  
print("setOfTitik:\n",setOfTitik)

#nyoba 2 dimensi
newSetOfTitik = fun.sortBySumbu(setOfTitik, 'x')
closestDistance, closestPair = fun.findClosestPair(newSetOfTitik)
print("Divide and conquer untuk mencari pasangan titik terdekat dari\n", newSetOfTitik, "\ndidapat jarak terdekat:", closestDistance, "dengan titik terdekatnya adalah", end = " ")
fun.printTitik(closestPair[0])
print(" dan ", end="")
fun.printTitik(closestPair[1])

#buat dimensi 3 atau lebih caranya gimana?
#bagi set titik berdasarkan sumbu x, y, z (slice horizontal, vertical, etc) secara gantian
#jadi percabangannya bukan 2 kali tapi jadi 8 kali ...(percabangan = rekursi)
#banyak percabangannya jadi 2^n-1 dimensi??