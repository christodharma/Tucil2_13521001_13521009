import platform
import psutil
import math
import random
import time
import bonus1
#program sudah diintegrasikan dengan bonus2

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
# calculate distance
# def hitungjarak(point1, point2) :
#     global euclideancount
#     euclideancount += 1
#     x1, y1, z1 = point1
#     x2, y2, z2 = point2
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
def hitungjarak(point1, point2) :
    jarak = 0
    for i in range(len(point1)) :
        jarak += (point1[i] - point2[i])**2
    global euclideancount
    euclideancount += 1
    return math.sqrt(jarak)

#sorting untuk proses divide
#selalu terurut membesar
#tidak mengubah data input
def sortBySumbu(setTitik, sumbu):
    if (sumbu == 'x' or sumbu == 'X'):
        sumbu = 1
    elif (sumbu == 'y' or sumbu == 'Y'):
        sumbu = 2
    elif (sumbu == 'z' or sumbu == 'Z'):
        sumbu = 3
    newSetTitik = sorted(setTitik, key=lambda row:(row[sumbu-1 if sumbu<=len(setTitik[0]) else 0]))
    return newSetTitik

# find closest point
def closestpoint(titik, divideandconquer=True,dimensi = 3, sumbudivide=1) :
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
            sortedTitik = sortBySumbu(titik,sumbudivide)
            # membagi titik jadi 2 bagian
            tengah = banyaktitik //2
            bagiankiri = sortedTitik[:tengah]
            bagiankanan = sortedTitik[tengah:]

            # manggil fungsi closestpoint lagi untuk tiap bagian
            # print("kiri ->", end=" ")
            # print(sumbudivide+1, end= ' ') if sumbudivide+1 <= 3 else print(sumbudivide+1, "->", 1, end=' ')
            bagiankiriterdekat, jarbagiankiriterdekat = closestpoint(bagiankiri,True,dimensi,sumbudivide+1 if sumbudivide+1 <= dimensi else 1)
            # print("kanan ->", end=" ")
            # print(sumbudivide+1, end= ' ') if sumbudivide+1 <= 3 else print(sumbudivide+1, "->", 1,end=' ')
            bagiankananterdekat, jarbagiankananterdekat = closestpoint(bagiankanan,True,dimensi,sumbudivide+1 if sumbudivide+1 <= dimensi else 1)
            # print("\npass")
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
                    jarakTengah = hitungjarak(titiktengah[i], titiktengah[j])
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
print("="*40, "WELCOME", "="*40)
while True:
    mauDimensi = input("apakah ingin menggunakan dimensi lain [default 3 detik] ? (Y/N) ")
    if (mauDimensi in "YyNn"): break
    else : print("Invalid!")
if (mauDimensi in "Yy"):
    dimensi = int(input("oke! masukkan dimensi: "))
elif (mauDimensi in "Nn"):
    print("baik! default ke 3")
    dimensi = 3
n = int(input("Masukkan jumlah titik : "))
if (n <= 1):
    # exception handle: titik yang dimasukkan tidak bisa dibuat pasangan
    euclideancount = 0
    startTime = time.time()
    stopTime = time.time()
    print("Pasangan titik terdekat : ", "NULL")
    print("Jaraknya : ", 0)
    print("banyak perhitungan euclidean : ", euclideancount)
    print(f"Lama program berjalan : {(stopTime-startTime)*(1000):.6f} ms")
else :
    # inisialisasi titik-titik
    titik = []
    for i in range(n):
        point = [random.randint(0,1000) for j in range(dimensi)]
        titik.append(point)
    #inisialisasi penghitungan operasi euclidean
    euclideancount = 0
    startTime = time.time()
    titikterdekat, jaraktitikterdekat = closestpoint(titik, True, dimensi, 1)
    stopTime = time.time()
    print("="*40, "Strategi Divide and Conquer", "="*40)
    print("Pasangan titik terdekat : ", titikterdekat)
    print("Jaraknya : ", jaraktitikterdekat)
    print("banyak perhitungan euclidean : ", euclideancount)
    print(f"Lama program berjalan : {(stopTime-startTime)*(1000):.6f} ms")

    #inisialisasi penghitungan operasi euclidean
    euclideancount = 0
    startTimeB = time.time()
    titikterdekat_bruteforce, jaraktitikterdekat_bruteforce = closestpoint(titik, False, dimensi, 1)
    stopTimeB = time.time()
    print("="*40, "Strategi Bruteforce", "="*40)
    print("Pasangan titik terdekat : ", titikterdekat_bruteforce)
    print("Jaraknya : ", jaraktitikterdekat_bruteforce)
    print("banyak perhitungan euclidean : ", euclideancount)
    print(f"Lama program berjalan : {(stopTimeB-startTimeB)*(1000):.6f} ms")
    if (dimensi <= 3 and dimensi > 0):
        vis = input("Visualisasikan hasil? (Y/N) ")
        if (vis in "Yy"):
            print("Visualisasi hasil Divide and Conquer")
            bonus1.showcartesian(titikterdekat,titik)
            print("Visualisasi hasil Bruteforce")
            bonus1.showcartesian(titikterdekat_bruteforce,titik)
        elif (vis in "Nn"):
            print("Tidak divisualisasikan")
    else:
        print("Dimensi abstrak, tidak divisualisasikan")
print("="*40, "Spesifikasi perangkat", "="*40)
my_system = platform.uname()
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")
# let's print CPU information
print("="*40, "CPU Info", "="*40)
# number of cores
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
# Memory Information
print("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")