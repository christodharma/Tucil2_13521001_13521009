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
            jarakminimum = float("inf")
            for i in range(banyaktitik) :
                for j in range(i+1, banyaktitik) :
                    jar = hitungjarak(titik[i],titik[j]) 
                    if(jar < jarakminimum) :
                        jarakminimum = jar
                        titikterdekat = (titik[i], titik[j])
            return titikterdekat, jarakminimum
        

        else :
            # mengurutkan set titik berdasarkan suatu sumbu
            print(sumbudivide)
            sortedTitik = fun.sortBySumbu(titik,sumbudivide)
            # membagi titik jadi 2 bagian
            tengah = banyaktitik //2
            bagiankiri = sortedTitik[:tengah]
            bagiankanan = sortedTitik[tengah:]

            # manggil fungsi closestpoint lagi untuk tiap bagian
            print("kiri", end=" ")
            print(sumbudivide+1, end= ' ') if sumbudivide+1 <= 3 else print(sumbudivide+1, "->", 1)
            bagiankiriterdekat, jarbagiankiriterdekat = closestpoint(bagiankiri,True,sumbudivide+1 if sumbudivide+1 <= 3 else 1)
            print("kanan", end=" ")
            print(sumbudivide+1, end= ' ') if sumbudivide+1 <= 3 else print(1)
            bagiankananterdekat, jarbagiankananterdekat = closestpoint(bagiankanan,True,sumbudivide+1 if sumbudivide+1 <= 3 else 1)
            print("pass")
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
bonus1.showcartesian(titikterdekat,titik)

euclideancount = 0
startTimeB = time.time()
titikterdekat_bruteforce, jaraktitikterdekat_bruteforce = closestpoint(titik, False)
stopTimeB = time.time()
print("---------------BRUTEFORCE---------------")
print("Pasangan titik terdekat : ", titikterdekat_bruteforce)
print("Jaraknya : ", jaraktitikterdekat_bruteforce)
print("banyak perhitungan euclidean : ", euclideancount)
print(f"Lama program berjalan : {(stopTimeB-startTimeB)*(1000):.6f} ms")
bonus1.showcartesian(titikterdekat_bruteforce,titik)