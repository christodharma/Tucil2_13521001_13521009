import math
import random
import time
import functions as fun
import bonus1
# calculate distance
def hitungjarak(point1, point2) :
    global euclideancount
    euclideancount += 1
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


# find closest point
def closestpoint(titik, divideandconquer=True, sumbudivide=1) :
    if(divideandconquer):    
        banyaktitik = len(titik)
        if banyaktitik <=3 : # memakai bruteforce kalau ada 3 atau kurang titik
            # print("<",end='')
            jarakminimum = float("inf")
            for i in range(banyaktitik) :
                for j in range(i+1, banyaktitik) :
                    jar = hitungjarak(titik[i],titik[j]) 
                    if(jar < jarakminimum) :
                        jarakminimum = jar
                        titikterdekat = (titik[i], titik[j])
            # print(jarakminimum, ">", sep='', end="")
            return titikterdekat, jarakminimum
        else :
            # mengurutkan set titik berdasarkan suatu sumbu
            sortedTitik = fun.sortBySumbu(titik,sumbudivide)
            # membagi titik jadi 2 bagian
            tengah = banyaktitik //2
            bagiankiri = sortedTitik[:tengah]
            bagiankanan = sortedTitik[tengah:]

            # manggil fungsi closestpoint lagi untuk tiap bagian
            # print("kiri ->", end=" ")
            # print(sumbudivide+1, end= ' ') if sumbudivide+1 <= 3 else print(sumbudivide+1, "->", 1, end=' ')
            bagiankiriterdekat, jarbagiankiriterdekat = closestpoint(bagiankiri,True,sumbudivide+1 if sumbudivide+1 <= 3 else 1)
            # print("kanan ->", end=" ")
            # print(sumbudivide+1, end= ' ') if sumbudivide+1 <= 3 else print(sumbudivide+1, "->", 1,end=' ')
            bagiankananterdekat, jarbagiankananterdekat = closestpoint(bagiankanan,True,sumbudivide+1 if sumbudivide+1 <= 3 else 1)
            # print("\npass")
            # jarak terdekat antara bagian kiri dan kanan
            jarak = min(jarbagiankiriterdekat, jarbagiankananterdekat)

            # pasangan titik terdekat yang ada didekat garis pembagi
            titikgaristengah = (titik[tengah][0], titik[tengah][1], titik[tengah][2])
            titiktengah = []
            for n in titik :
                if abs(n[0] - titikgaristengah[0]) < jarak :
                    titiktengah.append(n)
            
            jaraktitiktengahterdekat = float("inf")
            for i in range(len(titiktengah)) :
                for j in range(i+1, min(i + 8, len(titiktengah))) :
                    jarakTengah = hitungjarak(titiktengah[i], titiktengah[j]) #ky e salah ndek iki, nimbun jarak dari dnc
                    if(jarakTengah < jaraktitiktengahterdekat) :
                        jaraktitiktengahterdekat = jarakTengah
                        titiktengahterdekat = (titiktengah[i], titiktengah[j])
            # print("[",jaraktitiktengahterdekat,"]")
            # return pasangan titik terdekat
            jarakKiriTerdekat = hitungjarak(bagiankiriterdekat[0], bagiankiriterdekat[1])
            jarakKananTerdekat = hitungjarak(bagiankananterdekat[0], bagiankananterdekat[1])
            if jaraktitiktengahterdekat < jarak :
                return titiktengahterdekat, jaraktitiktengahterdekat
            elif jarakKiriTerdekat < jarakKananTerdekat :
                return bagiankiriterdekat, jarakKiriTerdekat
            else : return bagiankananterdekat, jarakKananTerdekat  
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
n = int(input("Masukkan jumlah titik : "))
titik = []
for i in range(n) :
    x = round(random.uniform(0,1)*10,2)
    y = round(random.uniform(0,1)*10,2)
    z = round(random.uniform(0,1)*10,2)
    # x = random.randint(-10,10)
    # y = random.randint(-10,10)
    # z = random.randint(-10,10)
    titik.append((x,y,z))

euclideancount = 0
startTime = time.time()
titikterdekat, jaraktitikterdekat = closestpoint(titik)
stopTime = time.time()
print("Pasangan titik terdekat : ", titikterdekat)
print("Jaraknya : ", jaraktitikterdekat)
print("banyak perhitungan euclidean : ", euclideancount)
print(f"Lama program berjalan : {(stopTime-startTime)*(1000):.6f} ms")

euclideancount = 0
startTimeB = time.time()
titikterdekat_bruteforce, jaraktitikterdekat_bruteforce = closestpoint(titik, False)
stopTimeB = time.time()
print("---------------BRUTEFORCE---------------")
print("Pasangan titik terdekat : ", titikterdekat_bruteforce)
print("Jaraknya : ", jaraktitikterdekat_bruteforce)
print("banyak perhitungan euclidean : ", euclideancount)
print(f"Lama program berjalan : {(stopTimeB-startTimeB)*(1000):.6f} ms")
# vis = input("Visualisasikan hasil? (Y/N) ")
vis = "n"
if (vis in "Yy"):
    print("Visualisasi hasil Divide and Conquer")
    bonus1.showcartesian(titikterdekat,titik)
    print("Visualisasi hasil Bruteforce")
    bonus1.showcartesian(titikterdekat_bruteforce,titik)
elif (vis in "Nn"):
    print("Tidak divisualisasikan")