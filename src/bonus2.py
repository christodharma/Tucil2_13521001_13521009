import math
import random
import time
import numpy as np

# calculate distance
def hitungjarak(point1, point2) :
    jarak = 0
    for i in range(len(point1)) :
        jarak += (point1[i] - point2[i])**2
    global euclideancount
    euclideancount += 1
    return math.sqrt(jarak)


# find closest point
def closestpoint(titik, dimensi, divideandconquer = True) :
    if (divideandconquer):    
        banyaktitik = len(titik)
        if banyaktitik <=3 : # memakai bruteforce kalau ada 3 atau kurang titik
            jarakminimum = float("inf")
            for i in range(banyaktitik) :
                for j in range(i+1, banyaktitik) :
                    jar = hitungjarak(titik[i],titik[j]) 
                    if(jar < jarakminimum) :
                        jarakminimum = jar
                        titikterdekat = (titik[i], titik[j])
            return titikterdekat, jarakminimum
        

        else :
            # membagi titik jadi 2 bagian
            tengah = banyaktitik //2
            bagiankiri = titik[:tengah]
            bagiankanan = titik[tengah:]

            # manggil fungsi closestpoint lagi untuk tiap bagian
            bagiankiriterdekat, jarbagiankiriterdekat = closestpoint(bagiankiri, dimensi)
            bagiankananterdekat, jarbagiankananterdekat = closestpoint(bagiankanan, dimensi)

            # jarak terdekat antara bagian kiri dan kanan

            jarak = min(jarbagiankiriterdekat, jarbagiankananterdekat)

            # pasangan titik terdekat yang ada didekat garis pembagi
            titikgaristengah = []
            for i in range(dimensi) :
                titikgaristengah.append(titik[tengah][i])

            titiktengah = []
            
            for n in titik :
                if abs(n[0] - titikgaristengah[0]) < jarak :
                    titiktengah.append(n)
            
            jaraktitiktengahterdekat = float("inf")
            for i in range(len(titiktengah)) :
                for j in range(i+1, min(i + 8, len(titiktengah))) :
                
                    jarak = hitungjarak(titiktengah[i], titiktengah[j])
                    if(jarak < jaraktitiktengahterdekat) :
                        jaraktitiktengahterdekat = jarak
                        titiktengahterdekat = (titiktengah[i], titiktengah[j])
            
            # return pasangan titik terdekat
            
            if jaraktitiktengahterdekat < jarak :
                return titiktengahterdekat, jaraktitiktengahterdekat
            elif hitungjarak(bagiankiriterdekat[0], bagiankiriterdekat[1]) < hitungjarak(bagiankananterdekat[0], bagiankananterdekat[1]) :
                return bagiankiriterdekat, hitungjarak(bagiankiriterdekat[0], bagiankananterdekat[1])
            else : return bagiankananterdekat, hitungjarak(bagiankananterdekat[0], bagiankananterdekat[1])  
    elif (not divideandconquer): #strategi bruteforce
        banyaktitik = len(titik)
        jarakminimum = float("inf")
        for i in range(banyaktitik) :
            for j in range(i+1, banyaktitik) :
                jar = hitungjarak(titik[i],titik[j]) 
                if(jar < jarakminimum) :
                    jarakminimum = jar
                    titikterdekat = (titik[i], titik[j])
        return titikterdekat, jarakminimum        


# main program
m = int(input("Masukkan dimensi :"))
n = int(input("Masukkan jumlah titik : "))
titik = np.empty((n,m))
for i in range(n) :
    for j in range(m) :
        titik[i][j] = random.uniform(0,1)

# i untuk banyak titik, j dimensinya
euclideancount = 0
startTime = time.process_time()
titikterdekat, jaraktitikterdekat = closestpoint(titik,m)
stopTime = time.process_time()
print("Pasangan titik terdekat : ", titikterdekat)
print("Jaraknya : ", jaraktitikterdekat)
print("banyak perhitungan euclidean : ", euclideancount)
print(f"Lama program berjalan : {(stopTime-startTime)*(1000):.6f} ms")

euclideancount = 0
startTime = time.process_time()
titikterdekat_bruteforce, jaraktitikterdekat_bruteforce = closestpoint(titik,m, False)
stopTime = time.process_time()
print("---------------BRUTEFORCE---------------")
print("Pasangan titik terdekat : ", titikterdekat_bruteforce)
print("Jaraknya : ", jaraktitikterdekat_bruteforce)
print("banyak perhitungan euclidean : ", euclideancount)
print(f"Lama program berjalan : {(stopTime-startTime)*(1000):.6f} ms")