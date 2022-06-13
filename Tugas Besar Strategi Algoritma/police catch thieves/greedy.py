"""_____________________________________________________________
Permasalahan Policeman Catch Thieves Menggunakan Strategi Greedy|
Kelompok 8:                                                     |
MUHAMMAD RAFI ANDEO PRAJA (1301200278)                          |
M NAUFAL RIFQI RAMDHANI (1301201572)                            |
RIZKY FERDIAN PRASETYO (1301204229)                             |
________________________________________________________________|"""
 
# Function untuk menentukan index awal dari polisi
def polisipertama(arr, n, polisi):
    for i in range(n):
        if (arr[i] == 'P'):
            polisi = i
            return polisi

# Function untuk menentukan index awal dari pencuri
def pencuripertama(arr, n, pencuri):
    for i in range(n):
        if (arr[i] == 'T'):
            pencuri = i
            return pencuri

# Function untuk menentukan jumlah maksimum pencuri yang dapat ditangkap
def tangkapPencuri(arr, n, k):
    index_polisi = -1
    index_pencuri = -1
    tertangkap = 0
    polisi = polisipertama(arr, n, index_polisi)
    pencuri = pencuripertama(arr, n, index_pencuri)
    if (pencuri == -1 or polisi == -1):
        return 0
    while (polisi < n and pencuri < n):
        if (abs(polisi - pencuri) <= k):
 
            polisi += 1
            while (polisi < n and arr[polisi] != 'P'):
                polisi += 1
 
            pencuri += 1
            while (pencuri < n and arr[pencuri] != 'T'):
                pencuri += 1
 
            tertangkap += 1
        elif (pencuri < polisi):
            pencuri += 1
            while (pencuri < n and arr[pencuri] != 'T'):
                pencuri += 1
        else:
            polisi += 1
            while (polisi < n and arr[polisi] != 'P'):
                polisi += 1
    return tertangkap

# Main program
if __name__=='__main__':
    arr1 = ['P', 'T', 'P', 'P', 'T', 'T']
    k = 2
    n = len(arr1)
    print("Maksimum pencuri yang dapat ditangkap adalah: {}". format(tangkapPencuri(arr1, n, k)))