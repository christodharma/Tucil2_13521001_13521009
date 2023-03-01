import platform
import psutil
import math
import random
import time
import bonus1
import getSpecs

def sortArr(titik, sumbu) : #quicksort dengan x sebagai pembandingnya
    if (sumbu == 'x' or sumbu == 'X'):
        sumbu = 0
    elif (sumbu == 'y' or sumbu == 'Y'):
        sumbu = 1
    elif (sumbu == 'z' or sumbu == 'Z'):
        sumbu = 2
    elif (sumbu<0): print("Error: Invalid sorting input")
    if(len(titik)) < 2 :
        return titik
    else :
        pointer = titik[0][sumbu]
        l = []
        r = []
        for i in range(1, len(titik)) :
            if (titik[i][sumbu] < pointer) : l.append(titik[i])
            else : r.append(titik[i])
        
        return sortArr(l,sumbu) + [titik[0]] + sortArr(r,sumbu)


def euclideanDistance(point1, point2) :
    jarak = 0.0
    for i in range(len(point1)) :
        jarak += (point1[i] - point2[i])**2
    global euclideancount
    euclideancount += 1
    return math.sqrt(jarak)

def closestPair(titik, dimensi=3, sumbudivide=0) :
    long = len(titik)
    if(long == 2): #ketika 2 titik
        pasangan = (titik[0], titik[1])
        jarak = euclideanDistance(titik[0], titik[1])
        return pasangan, jarak
    
    elif(long == 3) : #bruteforce 3 titik
        p1 = euclideanDistance(titik[0], titik[1])
        p2 = euclideanDistance(titik[0], titik[2])
        p3 = euclideanDistance(titik[1], titik[2])

        if(p1 < p2) :
            if(p1 < p3) :
                pasangan = (titik[0], titik[1])
                jarak = p1
                return pasangan, jarak
            else : 
                pasangan = (titik[1], titik[2]) 
                jarak = p3 
                return pasangan, jarak
        else :
            if(p2 < p3) :
                pasangan = (titik[0], titik[2])
                jarak = p2
                return pasangan, jarak
            else :
                pasangan = (titik[1], titik[2])
                jarak = p3
                return pasangan, jarak

    else : # lebih dari 3 maka dilakukan divide conquer
        if (dimensi>3):
            sortArr(titik,sumbudivide)
        kiri =  titik[:long//2]
        kanan = titik[long//2:]

        # ini buat minimum kiri sama minimum kanan
        # saat dimensi lebih dari 3, perlakuan divide dilakukan dilakukan pada sumbu-sumbu selain absis
        if (dimensi>3):
                titikkiri, jarakkiri = closestPair(kiri,dimensi,sumbudivide+1 if sumbudivide+1 < dimensi else 0)
                titikkanan, jarakkanan = closestPair(kanan,dimensi,sumbudivide+1 if sumbudivide+1 < dimensi else 0)
        else:
            titikkiri, jarakkiri = closestPair(kiri, dimensi)
            titikkanan, jarakkanan = closestPair(kanan, dimensi)

        # ambil minimum antara kiri atau kanan
        if(jarakkiri < jarakkanan) : 
            pasangan, jarak = titikkiri, jarakkiri
        else : pasangan, jarak = titikkanan, jarakkanan

        # titik titik didekat garis tengah
        d = titik[long//2][0]
        midpoint = []
        for i in range(len(kiri)) :
            if(kiri[i][0] >= d - jarak) : midpoint.append(kiri[i])
        for i in range(len(kanan)) :
            if(kanan[i][0] <= d + jarak) : midpoint.append(kanan[i])
        for k in range(dimensi-1,0,-1) :
            midpoint = sortArr(midpoint,k)
            for i in range(len(midpoint)) :
                for j in range(i+1, len(midpoint)) :
                    if(abs(midpoint[i][0] - midpoint[j][0]) < jarak or abs(midpoint[i][k] - midpoint[j][k]) < jarak) :
                        pasangan2, jarak2 = (midpoint[i], midpoint[j]), euclideanDistance(midpoint[i], midpoint[j])
                        if jarak2 < jarak : pasangan, jarak = pasangan2, jarak2
        return pasangan, jarak


def closestPair_bruteforce(titik) :
    long = len(titik)
    jarakminimum = float("inf")

    for i in range(long) :
        for j in range(i+1, long) :
            # print(i,"  ", j)
            # print(len(titik[2]))
            jar = euclideanDistance(titik[i],titik[j])
            if(jar < jarakminimum) :
                jarakminimum = jar
                titikterdekat = (titik[i], titik[j])
    return titikterdekat,jarakminimum


# main program
print("="*40, "WELCOME", "="*40)
while True:
    mauDimensi = input("apakah ingin menggunakan dimensi lain [default 3 dimensi] ? (Y/N) ")
    if (mauDimensi in "YyNn"): break
    else : print("Invalid!")
if (mauDimensi in "Yy"):
    dimensi = int(input("oke! masukkan dimensi : "))
    while(dimensi<1) :
        print("dimensi tidak valid! dimensi minimal adalah 1")
        dimensi = int(input("Masukkan dimensi :"))
elif (mauDimensi in "Nn"):
    print("baik! default ke 3")
    dimensi = 3
n = int(input("Masukkan jumlah titik : "))
if (n <= 1):
    # exception handle: titik yang dimasukkan tidak bisa dibuat pasangan
    while n<2:
        n = int(input("Invalid: Minimal titik harus 2. Input: "))
else :
    # inisialisasi titik-titik
    titik = []
    for i in range(n):
        point = [random.randint(0,1000) for j in range(dimensi)]
        titik.append(point)
    titik = sortArr(titik,0)
    #inisialisasi penghitungan operasi euclidean
    euclideancount = 0
    startTime = time.time()
    titikterdekat, jaraktitikterdekat = closestPair(titik, dimensi, 0)
    stopTime = time.time()
    print("="*40, "Strategi Divide and Conquer", "="*40)
    print("Pasangan titik terdekat : ", titikterdekat)
    print("Jaraknya : ", jaraktitikterdekat)
    print("banyak perhitungan euclidean : ", euclideancount)
    print(f"Lama program berjalan : {(stopTime-startTime)*(1000):.6f} ms")

    #inisialisasi penghitungan operasi euclidean
    euclideancount = 0
    startTimeB = time.time()
    titikterdekat_bruteforce, jaraktitikterdekat_bruteforce = closestPair_bruteforce(titik)
    stopTimeB = time.time()
    print("="*40, "Strategi Bruteforce", "="*40)
    print("Pasangan titik terdekat : ", titikterdekat_bruteforce)
    print("Jaraknya : ", jaraktitikterdekat_bruteforce)
    print("banyak perhitungan euclidean : ", euclideancount)
    print(f"Lama program berjalan : {(stopTimeB-startTimeB)*(1000):.6f} ms")
    if (dimensi == 3):
        vis = input("Visualisasikan hasil? (Y/N) ")
        if (vis in "Yy"):
            print("Visualisasi hasil Divide and Conquer")
            bonus1.showcartesian(titikterdekat,titik)
        elif (vis in "Nn"):
            print("Tidak divisualisasikan")
    elif (dimensi < 3 and dimensi > 3):
        print("Tidak Menvisualisasikan hasil")
    else:
        print("Dimensi abstrak, tidak divisualisasikan")
getSpecs.sysSpec()