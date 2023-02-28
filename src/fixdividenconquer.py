import random
import math


def sortArr(titik) : #quicksort dengan x sebagai pembandingnya
    if(len(titik)) < 2 :
        return titik
    else :
        pointer = titik[0]
        l = []
        r = []
        for i in range(1, len(titik)) :
            if (titik[i] < pointer) : l.append(titik[i])
            else : r.append(titik[i])
        return sortArr(l) + [pointer] + sortArr(r)


def euclideanDistance(titik1,titik2) :
    return math.sqrt((titik1[0] - titik2[0])**2 + (titik1[1] - titik2[1])**2 + (titik1[2] - titik2[2])**2)

def divideanconquer(titik) :
    long = len(titik)
    if(long == 2): #bruteforce 2 titik
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

    else : # lebih dari 3 maka pake divide conquer
        kiri =  titik[:long//2]
        kanan = titik[long//2:]

        # ini buat minimum kiri sama minimum kanan
        titikkiri, jarakkiri = divideanconquer(kiri)
        titikkanan, jarakkanan = divideanconquer(kanan)

        
        # ambil minimum antara kiri atau kanan
        if(jarakkiri < jarakkanan) : 
            pasangan, jarak = titikkiri, jarakkiri
        else : pasangan, jarak = titikkanan, jarakkanan

        # titik titik dideakt garis tengah
        d = titik[long//2][0]
        midpoint = []
        for i in range(len(kiri)) :
            if(kiri[i][0] >= d - jarak) : midpoint.append(kiri[i])
        for i in range(len(kanan)) :
            if(kanan[i][0] <= d + jarak) : midpoint.append(kanan[i])

        for i in range(len(midpoint)) :
            for j in range(i+1, len(midpoint)) :
                if(abs(midpoint[i][0] - midpoint[j][0]) < jarak) :
                    pasangan2, jarak2 = (midpoint[i], midpoint[j]), euclideanDistance(midpoint[i], midpoint[j])
                    if jarak2 < jarak : pasangan, jarak = pasangan2, jarak2

        return pasangan, jarak


def bruteforce(titik) :
    long = len(titik)
    jarakminimum = float("inf")

    # for i in range(long) :
    #     print(titik[i])

    # print(titik[2])
    # print(titik[2][0])
    # print(titik[2][1])
    # print(titik[2][2])

    for i in range(long) :
        for j in range(i+1, long) :
            # print(i,"  ", j)
            # print(len(titik[2]))
            jar = euclideanDistance(titik[i],titik[j])
            if(jar < jarakminimum) :
                jarakminimum = jar
                titik = (titik[i], titik[j])
    
    return titik,jarakminimum


        













n = int(input("angka = "))
titik = []

for i in range(n) :
    x = random.randint(0,1000)
    y = random.randint(0,1000)
    z = random.randint(0,1000)
    titik.append((x,y,z))

titik = sortArr(titik)


pasangan, jarak = divideanconquer(titik)
print(pasangan)
print(jarak)

print("=================================")
for i in range(len(titik)) :
    print(titik[i])
pasangan2, jarak2 = bruteforce(titik)
print(pasangan2)
print(jarak2)