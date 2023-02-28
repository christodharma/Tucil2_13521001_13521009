import random
import math


def sortArr(titik, sumbu) : #quicksort dengan x sebagai pembandingnya
    if(len(titik)) < 2 :
        return titik
    else :
        pointer = titik[0][sumbu]
        l = []
        r = []
        for i in range(1, len(titik)) :
            if (titik[i][sumbu] < pointer) : l.append(titik[i])
            else : r.append(titik[i])
        
        # print(l, titik[0], r)
        # print()
        return sortArr(l,sumbu) + [titik[0]] + sortArr(r,sumbu)


def euclideanDistance(titik1,titik2) :
    panjang = 0.0
    for i in range(len(titik1)) :
        panjang += (titik1[i] - titik2[i])**2
    return math.sqrt(panjang)

def shortestDistance(titik, dimensi) :
    # print("titik0 :", titik[0])
    # print("titik1 :", titik[1])
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
        #note: urutkan berdasarkan absis dari kecil membesar
        #my method: mengurutkan ngga selalu pake absis, tapi juga sumbu2 berikutnya sampe dia kepotong kecil
        #tujuannya buat ngurangi titik dengan jarak x rendah tapi ada di y/z yang jauh
        kiri =  titik[:long//2]
        kanan = titik[long//2:]

        # ini buat minimum kiri sama minimum kanan
        titikkiri, jarakkiri = shortestDistance(kiri, dimensi)
        titikkanan, jarakkanan = shortestDistance(kanan, dimensi)

        
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


        for k in range(dimensi-1,0,-1) :
            midpoint = sortArr(midpoint,k)
            for i in range(len(midpoint)) :
                for j in range(i+1, len(midpoint)) :
                    if(abs(midpoint[i][0] - midpoint[j][0]) < jarak or abs(midpoint[i][k] - midpoint[j][k]) < jarak) :
                        pasangan2, jarak2 = (midpoint[i], midpoint[j]), euclideanDistance(midpoint[i], midpoint[j])
                        if jarak2 < jarak : pasangan, jarak = pasangan2, jarak2

        return pasangan, jarak


def bruteforce(titik) :
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


        












m = int(input("dimensi = "))
n = int(input("angka = "))
while(n < 2) :
    print("minimal titik 2!!!")
    n = int(input("angka = "))

titik = []
for i in range(n) :
    point = [random.randint(0,1000) for j in range(m)]
    titik.append(point)


# for i in range(len(titik)) :
#     print(titik[i])

# print("----aaa-----")
titik = sortArr(titik,0)
# print("----sds-----")

# for i in range(len(titik)) :
#     print(titik[i])

pasangan, jarak = shortestDistance(titik,m)
print(pasangan)
print(jarak)

print("=================================")
pasangan2, jarak2 = bruteforce(titik)
print(pasangan2)
print(jarak2)
