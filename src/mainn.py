import math
import random
import time

euclideancount = 0
startTime = time.time()


# caclculate distance
def hitungjarak(point1, point2) :
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


# find closest point
def closestpoint(titik) :
    global euclideancount
    banyaktitik = len(titik)
    if banyaktitik <=3 : # memakai bruteforce kalau ada 3 atau kurang titik
        jarakminimum = float("inf")
        for i in range(banyaktitik) :
            for j in range(i+1, banyaktitik) :
                euclideancount += 1
                if(hitungjarak(titik[i],titik[j]) < jarakminimum) :
                    jarakminimum = hitungjarak(titik[i], titik[j])
                    titikterdekat = (titik[i], titik[j])
        return titikterdekat, jarakminimum
    

    else :
        # membagi titik jadi 2 bagian
        tengah = banyaktitik //2
        bagiankiri = titik[:tengah]
        bagiankanan = titik[tengah:]

        # manggil fungsi closestpoint lagi untuk tiap bagian
        bagiankiriterdekat, _ = closestpoint(bagiankiri)
        bagiankananterdekat, _ = closestpoint(bagiankanan)

        # jarak terdekat antara bagian kiri dan kanan
        euclideancount += 2
        jarak = min(hitungjarak(bagiankiriterdekat[0], bagiankiriterdekat[1]),
                            hitungjarak(bagiankananterdekat[0], bagiankanan[1]))

        # pasangan titik terdekat yang ada didekat garis pembagi
        titikgaristengah = (titik[tengah][0], titik[tengah][1], titik[tengah][2])
        titiktengah = []
        for n in titik :
            if abs(n[0] - titikgaristengah[0]) < jarak :
                titiktengah.append(n)
        
        jaraktitiktengahterdekat = float("inf")
        for i in range(len(titiktengah)) :
            for j in range(i+1, min(i + 8, len(titiktengah))) :
               euclideancount += 1
               jarak = hitungjarak(titiktengah[i], titiktengah[j])
               if(jarak < jaraktitiktengahterdekat) :
                   jaraktitiktengahterdekat = jarak
                   titiktengahterdekat = (titiktengah[i], titiktengah[j])
        
        # return pasangan titik terdekat
        euclideancount += 1
        if jaraktitiktengahterdekat < jarak :
            return titiktengahterdekat, jaraktitiktengahterdekat
        elif hitungjarak(bagiankiriterdekat[0], bagiankiriterdekat[1]) < hitungjarak(bagiankananterdekat[0], bagiankananterdekat[1]) :
               return bagiankiriterdekat, hitungjarak(bagiankiriterdekat[0], bagiankananterdekat[1])
        else : return bagiankananterdekat, hitungjarak(bagiankananterdekat[0], bagiankananterdekat[1])  



# main program
n = int(input("Masukkan jumlah titik : "))
titik = []
for i in range(n) :
    x = random.uniform(0,1)
    y = random.uniform(0,1)
    z = random.uniform(0,1)
    titik.append((x,y,z))

titikterdekat, jaraktitikterdekat = closestpoint(titik)

stopTime = time.time()
print("Pasangan titik terdekat : ", titikterdekat)
print("Jaraknya : ", jaraktitikterdekat)
print("banyak perhitungan euclidean : ", euclideancount)
print(f"Lama program berjalan : {stopTime-startTime:.6f} detik")