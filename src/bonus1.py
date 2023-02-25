import math
import random
import time
import matplotlib.pyplot as plt

euclideancount = 0
startTime = time.time()


def showcartesian(titikterdekat,titik) :
    fig = plt.figure()
    x = []
    y = []
    z = []
    xclose = []
    yclose = []
    zclose = [] 

    # masukin yg pasangan terdekat
    for i in range(len(titikterdekat)) :
        for j in range(0,3) :
            if(j == 0) :
                xclose.append(titikterdekat[i][j])
            elif(j == 1) :
                yclose.append(titikterdekat[i][j])
            else :
                zclose.append(titikterdekat[i][j])

    # masukin yg lain
    for i in range(len(titik)) :
        for j in range(0,3) :
            if(j == 0 and titik[i][j] != xclose[0] and titik[i][j] != xclose[1]) :
                x.append(titik[i][j])
            elif(j == 1 and titik[i][j] != yclose[0] and titik[i][j] != yclose[1]) :
                y.append(titik[i][j])
            elif(j == 2 and titik[i][j] != zclose[0] and titik[i][j] != zclose[1]) :
                z.append(titik[i][j])
    ax = plt.axes(projection='3d')
    ax.scatter(x,y,z, c = 'k')
    ax.scatter(xclose,yclose,zclose, c = 'r')
    

    ax.set_title('Diagram kartesian')
    ax.set_xlabel('Sumbu X')
    ax.set_ylabel('Sumbu Y')
    ax.set_zlabel('Sumbu Z')

    plt.show()




# caclculate distance
def hitungjarak(point1, point2) :
    global euclideancount
    euclideancount += 1
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)


# find closest point
def closestpoint(titik) :
    
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
        bagiankiriterdekat, jarbagiankiriterdekat = closestpoint(bagiankiri)
        bagiankananterdekat, jarbagiankananterdekat = closestpoint(bagiankanan)

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

g = int(input("\nmau tampilin grafik ? 1.ya, 2.tidak : "))

if(g == 1) :
    showcartesian(titikterdekat,titik)
    print("ok.")
else :
    print("ok.")