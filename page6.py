#Pendahuluan Fungsi (TITLE)
"""
Nama lain fungsi/function pada pemrograman ialah method, subrutin/rutin.

Jika kita perhatikan pada pemrograman sebelum ini, setiap program yang kita buat
terhitung panjang dan kompleks. Dengan mempelajari fungsi, kita dapat membuat
program yang sama, tetapi bisa lebih ringkas.

Secara sederhana, Di Python, 
fungsi adalah blok kode yang dapat dipanggil untuk melaksanakan tugas tertentu. 
Fungsi digunakan untuk mengelompokkan serangkaian pernyataan agar dapat digunakan 
kembali dan dijalankan dengan mudah dari berbagai bagian program. Fungsi membantu 
dalam membuat kode lebih terstruktur, lebih mudah dibaca, dan memungkinkan pemrogram 
untuk memecah program menjadi bagian-bagian yang lebih kecil dan lebih terkelola.

Fungsi pada Python dapat digunakan untuk melaksanakan berbagai tugas, 
mulai dari perhitungan matematika hingga memanipulasi data atau berkomunikasi 
dengan sumber eksternal, dan mempermudah struktur program dengan mengelompokkan 
logika tertentu ke dalam blok yang dapat digunakan kembali.
"""

#struktur fungsi
# def nama_fungsi(parameter1,parameter2, dst...) :
#     blok kode 
#     pernyataan-pernyataan untuk melakukan tugas tertentu (print atau kode program)
#     dst...
#     return
# pemanggilanfungsi(berdasarkanparameter yang diinginkan)

"Jika sebelumnya kita membuat program seperti berikut"
"""
b = 1
c = 2
a = b + c
print("b + c = a =", a)

e = 5
f = 7
d = e + f
print("e + f = d = ", d)
terlihat program atas dan bawah memiliki operasi yang sama. Tentu ini menjadi
suatu hal yang boros. Selain itu, pada pemrograman terdapat paradigma, yaitu
'do not repeat ur code, just do it once'.

Dengan adanya fungsi, kita dapat terbantu untuk melakukan
program sebanyak jumlah tak terhingga dengan input yang dapat kita ubah-ubah
sesuai keinginan users.

"""
#membuat fungsi sederhana
def hello_world():
    'Fungsi Menampilkan kalimat hello world'
    print("hello world")
    print("selamat siang wahai manusia beriman!")

hello_world() #running/pemanggilan pertama
hello_world() #running/pemanggilan dua kali
hello_world() #running/pemanggilan tiga kali, dst...

"""info tambahan

karena python adalah bahasa pemrograman interpreted, kita harus membuatnya secara
berurutan/memperhatikan urutan, kode program->print/pemanggilan.

Berbeda dengan C++ sebagai bahasa compiled, tidak perlu memperhatikan urutan,
karena pada C++ terdapat linkers.
"""


#fungsi dengan input/parameter/argumen (TITLE)
"setiap input, akan diprogram oleh fungsi dan menghasilkan output sesuai keinginan."

def fungsi(nama) :
    print(f"Selamat datang wahai {nama}!")

fungsi("ucup")


def tambah(angka1, angka2) :
    "Operasi matematika sederhana"
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(int(input("angka 1 =")),int(input("angka 2 =")))


def say_hi(list_peserta) :
    data_peserta = list_peserta.copy() #copy agar tidak mengubah variabel anggota_boyband
    for peserta in data_peserta :
        print(f"Yth {peserta}")
    print(f"Selamat datang di acara konser hari ini!")

anggota_boyband = ["Ucup", "Otong", "Dudung"]

say_hi(anggota_boyband)


#Fungsi dengan Return/kembalian (TITLE)

''' Fungsi dengan kembalian'''

"""Apa itu return pada fungsi?
Dalam Python, return adalah pernyataan khusus yang digunakan dalam fungsi 
untuk mengembalikan nilai dari fungsi tersebut. Saat Anda mendefinisikan 
sebuah fungsi, Anda dapat menggunakan return untuk mengirimkan hasil dari 
fungsi ke pemanggil. Setelah return dieksekusi dalam sebuah fungsi, eksekusi 
fungsi akan berakhir, dan nilai yang dikembalikan akan menjadi hasil dari 
pemanggilan fungsi tersebut.

Penting untuk diingat bahwa fungsi tidak selalu harus mengandung pernyataan return. 
Jika fungsi tidak memiliki pernyataan return, secara default, fungsi akan mengembalikan 
None. Jadi, ketika Anda memanggil fungsi yang tidak memiliki return, pastikan untuk 
menangani nilai kembalian yang mungkin adalah None.

note : 
Di Python, None adalah nilai khusus yang menunjukkan ketiadaan nilai atau 
nilai yang tidak ada. None sering digunakan sebagai nilai kembalian default 
dari fungsi yang tidak memiliki pernyataan return, atau sebagai nilai yang 
diinisialisasi ke dalam variabel ketika belum ada nilai yang tersedia.
Jadi, Ketika sebuah fungsi tidak memiliki pernyataan return, secara otomatis 
nilai kembalian fungsi akan menjadi None. Jika Anda memanggil fungsi seperti 
ini dan mencoba menyimpan hasilnya ke dalam variabel, variabel tersebut akan berisi None.
pernyataan 'none' ini sama seperti ketika kita membuat assignment dari sebuah
variabel tetapi tidak memiliki value. 
variabel = 
maka secara default ketika dirunning, menjadi none.

Note :
Perlu diingat bahwa None adalah objek khusus dalam Python, dan tidak sama 
dengan False, 0, atau string kosong (""). Kita dapat membuktikannya dengan if else statement
bahwa sebuah variabel adalah none.
"""

# template fungsi dengan kembalian
# def nama_fungsi(argument):
#       badan fungsi
#       return output

# fungsi kuadrat    

def kuadrat(input_angka):
    '''Fungsi kuadrat'''
    output_kuadrat = input_angka**2
    return output_kuadrat

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# fungsi tambah

def fungsi_tambah(angka_1,angka_2):
    '''fungsi return dengan multi input'''
    return angka_1 + angka_2

a = fungsi_tambah(10,8)
print(a)

# fungsi dengan return banyak

def operasi_matematika(angka_1,angka_2):
    tambah = angka_1 + angka_2
    kurang = angka_1 - angka_2
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2

    return tambah,kurang,kali,bagi

k,l,m,n = operasi_matematika(9,5)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")




# Default Argumen (TITLE)
"""Argumen yang memiliki default
membantu kita meminimalisir keadaan eror bila kita tidak memberikan input fungsi.
Apabila kita tidak atau lupa memberikan input fungsi, maka fungsi yang memiliki
default pada argumennya akan otomatis melampirkan nilai default argumennya.

"""
# #def fungsi(argument):
# #def fungsi(argument = nilai defaultnya):

# contoh 1
def say_hello(nama = "Ganteng"):
    '''fungsi dengan default argument'''
    print(f"Hallo {nama}")


say_hello("Ucup")
say_hello()

#contoh 2
def sapa_dia(nama, pesan = "Apa kabar?"):
    '''fungsi dengan satu input biasa, dan satu default argument'''
    print(f"hai {nama}, {pesan}")

sapa_dia("Dudung","Hai Ganteeeng")
sapa_dia("Otong")

#contoh 3

def hitung_pangkat(angka, pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# contoh 4


def fungsi(input1=1,input2=2,input3=3,input4=4):
    hasil = input1 + input2 + input3 + input4
    return hasil

print(fungsi())
print(fungsi(input3=10))
print(fungsi(input1= 3, input2= 10, input3 = 9, input4 = 5))


# Latihan Fungsi (TITLE)

'''Latihan Fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# # Membuat header program
# os.system("clear")
# # os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input("Masukan nilai lebar: "))
# PANJANG = int(input("Masukan nilai panjang: "))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi Header'''
    os.system("clear")
    # os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # Mengambil input user
    lebar = int(input("Masukan nilai lebar: "))
    panjang = int(input("Masukan nilai panjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''
    print(f"hasil perhitungan {message} = {value}")


# Program utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)

    display("luas", LUAS)
    display("keliling", KELILING)

    isContinue = input("apakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("Program selesai, terima kasih")



#Type hints pada fungsi (TITLE)
''' Type hints untuk fungsi '''

# bentuk standar fungsi yang udah kita pelajari

'''
studi kasus
def fungsi(parameter):
    hasil = parameter**2
    print(hasil)

fungsi(1)
fungsi("Ucup")
fungsi(True)

Jangan pernah lagi membuat fungsi seperti ini, riskan eror. 
Ini karena kita tidak melakukan spesifikasi pada tipe data dari 
argumen/parameternya.

'''

# penggunaan type hints

import string

def sepuluh_pangkat(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10**argument
    return output

HASIL = sepuluh_pangkat(4)
print(HASIL)

def display(argument:string):
    print(argument)

display("Ucup")




# *args pada fungsi (TITLE)
'''*args'''

# memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",170,40)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["otong",100,120])

# kenalan dengan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung",120,120)

# studi kasus

def tambah(*data):
    # data tipenya adalah tuple, dia bisa diiterasi
    output = 0
    for angka in data:
        output += angka
    
    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"hasil = {hasil}")




# Anonymous Function & Lambda Function

def f_kuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

"""Apa itu fungsi lambda ?
Lambda function dalam bahasa pemrograman Python adalah fungsi anonim atau 
tanpa nama yang dapat didefinisikan dalam satu baris kode. Lambda function 
sering digunakan untuk membuat fungsi sederhana yang hanya memiliki satu 
ekspresi/satu baris. Mereka umumnya digunakan ketika Anda memerlukan 
fungsi singkat untuk operasi-operasi sederhana, seperti pemetaan (mapping) 
atau penyaringan (filtering) elemen dalam koleksi data, operasi aritmatika,
operasi logika, dsb...

"""

# kita coba dengan lambda
# lambda function syntax : output = lambda argument: expression
kuadrat = lambda angka : angka**2
print(f"hasil lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"hasil lambda pangkat = {pangkat(4,2)}")

## kegunaan apa bang?

# sorting untuk list biasa
data_list = ["Otong","Ucup","Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting dia pakai panjang
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama) #sintaks baru menggunakan key hehehe, gws hapalin
print(f"sorted list by panjang = {data_list}")

# sorting pakai lambda
data_list = ["Otong","Ucup","Dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

def kurang_dari_lima(angka):
    return angka < 5

data_angka_baru = list(filter(kurang_dari_lima,data_angka)) #sintaks baru hehe, gws hapalin
data_angka_baru = list(filter(lambda x:x<7,data_angka)) #menggunakan lambda
print(data_angka_baru)

# kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_angka))
print(data_genap)

# kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print(data_ganjil)

# kelipatan 3
data_3 = list(filter(lambda x:(x%3==0),data_angka))
print(f"kelipatan 3 : {data_3}")

# Menggunakan lambda function dalam fungsi built-in seperti map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"squared numbers : {squared_numbers}")  # Output: [1, 4, 9, 16, 25]

# anonymous function
# currying <- Haskell Curry 

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan currying menjadi

def pangkat(n):
    return lambda angka:angka**n
"Bentuk fungsi anonymous ialah fungsi lambda(termasuk anonymous) di dalam fungsi anonymous juga."
pangkat2 = pangkat(2)
print(f"pangkat2 = {pangkat2(5)}")
pangkat3 = pangkat(3)
print(f"pangkat3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}") #bentuk langsung, tanpa assignment pangkat n dulu.

"""REMINDING!!!
Namun, penting untuk diingat bahwa lambda function memiliki keterbatasan. 
Mereka hanya cocok untuk fungsi-fungsi sederhana dan tidak dapat mengandung 
pernyataan-pernyataan kompleks atau multi-baris. Jika Anda membutuhkan fungsi 
yang lebih rumit, lebih disarankan untuk menggunakan pendekatan fungsi biasa 
dengan pernyataan def.
"""




#Global and Local Scope
"""Apa perbedaannya ? Apa urgensi mempelajari Scope?

Dalam pemrograman Python, konsep "scope" (lingkup) merujuk pada wilayah di 
dalam kode di mana suatu variabel dapat diakses dan digunakan. 
Ada dua jenis scope utama dalam Python: global scope dan local scope.

"""

"""Global Scope

Global scope (lingkup global) adalah lingkup yang mencakup seluruh program 
atau modul. Variabel yang didefinisikan di dalam global scope dapat diakses 
dari seluruh bagian kode dalam program atau modul tersebut.

"""

global_variable = 10  # Variabel global didefinisikan di luar semua fungsi

def print_global():
    print(global_variable)  # Variabel global dapat diakses dari dalam fungsi

print_global()  # Output: 10


nama_global = "otong" 

# akses variabel global dalam loop
for i in range(0,5):
    print(f"loop {i} - {nama_global}")

# percabangan
if True:
    print(f"if menampilkan {nama_global}")



"""Local Scope
Local scope (lingkup lokal) adalah lingkup yang terbatas pada suatu fungsi 
atau blok kode tertentu. Variabel yang didefinisikan di dalam local scope 
hanya dapat diakses dari dalam fungsi atau blok kode tersebut.
"""
def example_function():
    local_variable = 20  # Variabel lokal didefinisikan di dalam fungsi
    print(local_variable)

example_function()  # Output: 20

# print(local_variable)  # Ini akan menyebabkan error karena variabel lokal tidak dapat diakses di luar fungsi

# Contoh 1: penggunaan akses variabel
def say_otong():
    print(f"Hello {nama}")

nama = "Otong" #variabel berada di bawah fungsi, tetap bisa diakses fungsi.
say_otong() #asalkan pemanggilan/fungsi akses berada di bawah variabelnya.

# contoh 2: mengubah variabel global menggunakan fungsi, apakah bisa?
angka = 0
name = "Ucup"

def ubah(nilai_baru, nama_baru):
    global angka # fungsi ini mendapat akses mengubah angka
    global name
    angka = nilai_baru
    name = nama_baru

print(f"Sebelum {angka,name}")

ubah(10,"Otong")
print(f"Sesudah {angka,name}")



# contoh 3 : mengubah variabel global dengan perulangan / percabangan
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(f"mengubah angka menjadi : {angka}")
print(f"ini adalah local scope angka dummy : {angka_dummy}")

if True:
    angka = 5
    angka_dummy = 10

print(angka)
print(angka_dummy)

"Mengubah variabel global dengan perulangan/percabangan tidak perlu menginput modul global seperti pada fungsi."

"tidak perlu menginput modul global untuk mengub"
"""
Variabel yang didefinisikan di dalam suatu fungsi hanya dapat diakses di 
dalam fungsi tersebut. Jika Anda mencoba mengakses variabel lokal di luar 
fungsi, akan terjadi error.

Penting untuk memahami perbedaan antara global scope dan local scope, 
karena pemahaman ini sangat penting dalam mengelola variabel dan memastikan 
kode berjalan sesuai harapan. Jika Anda ingin variabel dapat diakses di 
seluruh program, Anda harus mendefinisikannya di dalam global scope. 
Jika Anda ingin variabel hanya dapat diakses di dalam fungsi tertentu, 
Anda harus mendefinisikannya di dalam local scope.
"""































