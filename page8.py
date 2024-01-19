# __main__ (TITLE)

""" Apa itu __main__ ? apa kegunaannya ?

__main__ adalah sebuah istilah dalam bahasa pemrograman Python yang digunakan 
untuk mengidentifikasi apakah suatu script dieksekusi secara langsung sebagai 
program utama atau jika script tersebut diimpor sebagai modul dalam script lain
(file eksternal). 
Ketika sebuah script Python dieksekusi, interpreter Python mengatur variabel 
__name__ pada level modul saat ini. Jika script tersebut adalah script utama 
yang dieksekusi secara langsung, nilai __name__ akan menjadi "__main__". 
Jika script tersebut diimpor sebagai modul dalam script lain, nilai __name__ 
akan menjadi nama modul tersebut.

Dengan menggunakan if __name__ == "__main__":, Anda dapat mengatur bagian 
kode yang hanya akan dieksekusi ketika script tersebut dieksekusi sebagai 
program utama, dan bagian tersebut tidak akan dieksekusi ketika script 
tersebut diimpor sebagai modul. Ini dapat membantu dalam mengatur alur 
eksekusi dan menjaga kerapihan dalam kode Anda.

"""

#__main__ adalah top level code environment
print(__name__)
print(f"nilai __name__ pada page8.py = {__name__}")


# impor modul berisikan __main__ pada file eksternal
import latihan_mainfungsi 


# contoh penggunaan __main__

# deklarasi
def fungsi_tambah(a:int,b:int)->int:
    return a+b

# fungsi utama
if __name__ == "__main__":
    angka1 = 5
    angka2 = 10
    hasil = fungsi_tambah(angka1,angka2)
    print(f"hasil tambah = {hasil}")


## import package
import package #setiap skrip __name__,dsb pada package menjadi __main__ pada program utama karenna sudah diimport



# open & with read external file (TITLE)

"""
Di Python, kata kunci "open" digunakan untuk membuka file, sementara "with" 
digunakan untuk mengelola konteks eksekusi dengan pengelolaan sumber daya 
yang lebih baik, seperti menutup file secara otomatis setelah selesai.

Menggunakan "with" direkomendasikan karena lebih aman dan lebih efisien 
dalam mengelola sumber daya, seperti file, karena memastikan bahwa sumber daya
 tersebut akan ditutup dengan benar setelah digunakan.
"""

## Tutorial membaca file eksternal

print(3*"=", " Membaca file txt ", 3*"=")
file = open("data.txt",mode="r")
"Penulisan salah :"
# file = ("data.txt", mode="r")
# file.open()

print(f"status read : {file.readable()}")
print(f"status write : {file.writable()}")

## baca seluruh file
print(file.read())

## baca per baris
# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris kedua

## baca semua baris sebagai list
# print(file.readlines())

print(f"apakah file sudah diclose : {file.closed}")
file.close() #jika pakai open, harus diclose secara manual.
print(f"apakah file sudah diclose : {file.closed}")


## salah satu teknik membuka file di python

print("\n",3*"=", " Membaca file txt dengan with", 3*"=")

with open("data.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose : {file.closed}")

print(f"apakah file sudah diclose : {file.closed}")





#write external file (TITLE)


# 1. mode write (menimpa)

# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isinya

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("jon si jhonny")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("ucup surucup")

with open("data_1.txt",'w',encoding="utf-8") as file:
    file.write("overwriteee")

# 2. mode append (menambahkan data pada indeks selanjutnya)
"baris pertama wajib menggunakan 'w' jika tidak runned lebih dari 1 kali"
with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("jon si jhonny\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("ucup surucup\n")

with open("data_2.txt",'a',encoding="utf-8") as file:
    file.write("tambah lagi dengan append\n")

# 3. mode r+ (memperbarui berdasarkan panjang karakter dan indeks karakter)

with open("data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke 3\n") #data ini overwrite jika elemen berikutnya melebihi jumlah karakter data ini

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("baris-1 \n")
    file.write("baris-2 \n")
    file.write("baris-3 \n")

with open("data_3.txt",'r+',encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("data_3.txt",'r+',encoding="utf-8") as file:
    file.write("tai kucing bau banget") # menimpa isi text sesuai dengan panjang data dan indeks elemen.






#Try & Exception (TITLE)


# exception akan terjadi saat program 
# mengalami error saat runtime

"""

Di dalam bahasa pemrograman Python, "try" dan "except" adalah mekanisme 
yang digunakan untuk menangani kesalahan atau pengecualian (exceptions) 
yang dapat terjadi selama eksekusi program. Ini memungkinkan Anda untuk 
mengatasi situasi yang tidak terduga atau tidak diharapkan tanpa menghentikan 
program secara keseluruhan.

Sintaks dasar dari blok "try" dan "except" adalah sebagai berikut:
try:
    Potensi kode yang dapat memunculkan pengecualian
    ...
except ExceptionType:
    Blok ini akan dijalankan jika pengecualian dari tipe ExceptionType terjadi
    ...


penjelasan blok try dan except sebagai berikut,

Try: Blok ini berisi kode yang mungkin menghasilkan pengecualian. 
Jika suatu pengecualian terjadi saat eksekusi kode di dalam blok "try", 
program tidak akan langsung berhenti atau crash. Sebaliknya, 
Python akan mencari blok "except" yang cocok untuk menangani jenis pengecualian tertentu.

Except: Blok ini adalah tempat di mana Anda menentukan jenis pengecualian 
yang ingin ditangani. Jika pengecualian yang cocok terjadi di dalam 
blok "try", maka blok "except" yang sesuai akan dieksekusi. 
Anda dapat menentukan jenis pengecualian tertentu, seperti "ZeroDivisionError", 
"ValueError", atau "FileNotFoundError", atau Anda bahkan dapat menangkap 
pengecualian umum seperti "Exception" untuk menangani semua jenis pengecualian.
"""

#contoh sederhana
try:
    num = int(input("Masukkan sebuah angka: "))
    result = 10 / num
    print("Hasil pembagian: ", result)
except ZeroDivisionError:
    print("Tidak bisa membagi dengan nol.")
except ValueError:
    print("Masukan harus berupa angka.")
except Exception as e:
    print("Terjadi kesalahan:", e)

"""Penjelasan :
Dalam contoh di atas, program mencoba membagi 10 dengan angka yang dimasukkan
oleh pengguna. Jika angka yang dimasukkan adalah nol, akan terjadi 
ZeroDivisionError, dan blok except ZeroDivisionError akan menangani kasus ini. 
Jika pengguna memasukkan input yang bukan angka, maka ValueError akan 
terjadi dan blok except ValueError akan menanganinya. 
Blok except Exception adalah cadangan untuk menangani pengecualian umum 
yang mungkin tidak ditangkap oleh pengecualian khusus di atasnya.


Dengan menggunakan "try" dan "except", Anda dapat membuat program Python Anda 
lebih tahan terhadap kesalahan dan lebih mudah untuk dikelola ketika terjadi 
pengecualian atau kondisi tidak diharapkan lainnya.
"""



# contoh sederhana untuk menangkap exception

from math import nan

## contoh sederhana
# input_user = int(input("masukan angka: "))
# hasil = nan

# try:
#     hasil = 10/input_user
# except:
#     print("input tidak boleh 0")

# print(f"hasil = {hasil}")



# contoh di aplikasi
print(f"\n=====contoh aplikasi try and except=====\n")

while(True):
    angka = int(input("masukan angka pembagi: "))
    try:
        hasil = 10/angka
        print(f"hasil = {hasil}")
        is_done = input("lanjutkan (y/n)? ")
        if is_done == "n":
            break
    except:
        print("pembagi nol, silahkan masukan input lagi")

print("Akhir dari program 1")

# contoh aplikasi untuk membuat file data.txt 
try:
    with open("data.txt",'r') as file:
        print(file.read())
except:
    print("file data.txt tidak ditemukan, membuat file baru")
    with open("data.txt",'w',encoding='utf-8') as file:
        file.write("file baru")

print("akhir dari program 2")



# contoh membuat exception

from numbers import Number

def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "input harus angka"
    return a+b

print(tambah(5,6))

angka = 0


#memeriksa jenis eror yang berpotensi muncul
try:
    hasil = 10/angka
except Exception as error_message:
    print(error_message)

#cara lain
try:
    hasil = 10/angka
except ZeroDivisionError as error_message:
    print(error_message)




