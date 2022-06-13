"""__________________________________________________________________
Permasalahan Policeman Catch Thieves Menggunakan Strategi Brute Force|
Kelompok 8:                                                          |
MUHAMMAD RAFI ANDEO PRAJA (1301200278)                               |
M NAUFAL RIFQI RAMDHANI (1301201572)                                 |
RIZKY FERDIAN PRASETYO (1301204229)                                  |
_____________________________________________________________________|"""
# Program Python untuk menentukan jumlah maksimum pencuri yang dapat ditangkap.

# Function untuk menginisialisasi pencuri dan polisi kedalam array baru
def inisialisasi(arr, n):
    i = 0
    pencuri = []
    polisi = []
 
    # Menginisialisasikan polisi dan pencuri kedalam list
    while i < n:
        if arr[i] == 'P':
            polisi.append(i)
        elif arr[i] == 'T':
            pencuri.append(i)
        i += 1
    return polisi, pencuri

# Function untuk menentukan jumlah maksimum pencuri yang dapat ditangkap
def tangkapPencuri(polisi, pencuri, k):
    # Minimum indeks untuk pencuri : pencuri[x], polisi: polisi[y]
    x = 0
    y = 0
    tertangkap = 0

    while x < len(pencuri) and y < len(polisi):
        # Jika pencuri dapat ditangkap
        if (abs( pencuri[x] - polisi[y] ) <= k):
            tertangkap += 1
            x += 1
            y += 1
             
        # Increment untuk minimum indeks
        elif pencuri[x] < polisi[y]:
            x += 1
        else:
            y += 1
 
    return tertangkap
  
# Main Program
if __name__=='__main__':
    arr1 = ['P', 'T', 'P', 'P', 'T', 'T']
    k = 2
    n = len(arr1)
    polisi, pencuri = inisialisasi(arr1, n)
    print(("Maksimum pencuri yang dapat ditangkap adalah: {}". format(tangkapPencuri(polisi, pencuri, k))))