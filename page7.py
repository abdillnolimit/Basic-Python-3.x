#Import Statement (TITLE)
"""
Pernyataan import dalam Python digunakan untuk mengimpor modul atau 
pustaka eksternal ke dalam program Anda. Modul adalah file Python yang 
berisi definisi fungsi, kelas, dan variabel yang dapat Anda gunakan dalam 
kode Anda. Dengan menggunakan pernyataan import, Anda dapat mengakses 
fungsionalitas yang disediakan oleh modul tersebut.

Dengan menggunakan pernyataan import, Anda dapat memanfaatkan pustaka-pustaka 
eksternal yang telah dikembangkan oleh komunitas Python atau yang Anda buat 
sendiri untuk memperluas fungsionalitas program Anda.

"""


#1. menyambungkan program dengan external
import time
t_awal = time.time()
import orang1 #tanpa penggunaan data/variabel, bisa langsung running di terminal

#2. import menggunakan namespace
import datacecep # jika seperti ini saja, maka blm tampil, cuma berhasil import ke main program
print(f"nama panjang Cecep : {datacecep.nama_panjang}")
print(f"Usia Cecep Surecep : {datacecep.umur} tahun")


#3. Import dengan fungsi 
import matematika #harus dideklarasikan import dulu yaa ingat!
hasil = matematika.tambah_aja(2,3)
print(f"berapakah 2 + 3 = {hasil}")



import matematika #masih harus menggunakan namespace

hasil_tambah = matematika.tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = matematika.kali(1,2,3,4,5)
print(f"hasil tambah = {hasil_kali}")

pangkat_3_dari = matematika.eksponen(3)
print(f"hasil pangkat 3 dari 5 = {pangkat_3_dari(5)}")



from matematika import tambah,kali,eksponen #gaperlu pakai namespace lagi
print(f"\n=====Tanpa namespace=====\n")
hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil tambah = {hasil_kali}")

pangkat_3_dari = eksponen(3)
print(f"hasil pangkat 3 dari 5 = {pangkat_3_dari(5)}\n")



#alias
print(f"=====Menggunakan Alias======\n")

from matematika import tambah as add
from matematika import kali as times
from matematika import eksponen as pangkat


hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil tambah = {hasil_kali}")

pangkat_3_dari = eksponen(3)
print(f"hasil pangkat 3 dari 5 = {pangkat_3_dari(5)}\n")



#import semua isi file eksternal 
print(f"\nimport semua isi file eksternal=====\n")

from matematika import * #ini artinya semua data yang ada di file matematika bisa langsung diimport, tanpa namespace lagi
hasil_tambah = tambah(1,2,3,4,5)
print(f"hasil tambah = {hasil_tambah}")

hasil_kali = kali(1,2,3,4,5)
print(f"hasil tambah = {hasil_kali}")

pangkat_3_dari = eksponen(3)
print(f"hasil pangkat 3 dari 5 = {pangkat_3_dari(5)}\n")

t_akhir = time.time()
waktu_running_program = (t_akhir - t_awal)
print(f"Lamanya waktu untuk running program di atas adalah = \n{waktu_running_program} detik \n")
"""Setiap kita melakukan import statement, maka pasti python secara otomatis
membuat compiled file.

Perlu diingat bahwa library time untuk mengukur waktu lamanya running program
itu juga ditentukan oleh prosesor komputer yang kita gunakan saat itu juga.
"""



#Membuat Package dan __init__.py (TITLE)
(f"\n\n=====Membuat Package dan __init__.py=====\n")
"""Package sangat dibutuhkan ketika kita memiliki banyak program external,
tetapi kita ingin file main program tetap rapih dan tidak terlalu panjang.
"""

# mengambil program dari sebuah folder yang sejajar

import sciences
print(f"\n=====menghitung besar gaya yang diperlukan=====\n")
besar_massa_benda       = float(input("Besar massa benda(kg)\t= "))
besar_percepatan_benda  = float(input("Besar percepatan benda(m.s^-2)\t= "))
besar_gaya = sciences.physics.hukum_2_newton(besar_massa_benda,besar_percepatan_benda)
print(f"besar gaya = {besar_gaya} Newton")

print(f"\n=====menghitung besar usaha=====")
besar_gaya_untuk_usaha = float(input("besar gaya(N)\t= "))
besar_perpindahan      = float(input("besar perpindahan benda(meter)\t= "))
besar_usaha            = sciences.work(besar_gaya_untuk_usaha,besar_perpindahan)
print(f"besar usaha benda = {besar_usaha} Joule")

from sciences.math.basic import add, times  #gw mau langsung ringkas biar ga repot penulisan
from sciences.math.scientific import exponen as perpangkatan  #sama, yang ini juga
#btw alias gabisa namain lebih dari 1 import langsung dalam 1 statement, seperti import statement add, times .

print(f"\n=====Pertambahan=====")
tambah = add()

print(f"\n=====Perkalian=====")
a = float(input("a = "))
b = float(input("b = "))
perkalian = times(a, b)
print(f"{a} * {b} = {perkalian} \n")

print(f"\n=====Eksponen=====")
eksponen = perpangkatan('basis', 'eksponen')





#Standard Library (TITLE)
"""
Standard library di Python adalah kumpulan modul dan pustaka (libraries) 
yang telah disertakan dalam distribusi resmi Python. Modul dan pustaka 
ini merupakan bagian integral dari bahasa Python dan menyediakan berbagai 
fungsi dan alat yang siap pakai untuk membantu dalam pengembangan perangkat lunak.

Dalam standard library Python, Anda akan menemukan berbagai macam modul yang 
mencakup berbagai fungsi, termasuk manipulasi string, operasi file, 
pengolahan data, jaringan, pengaturan waktu, dan banyak lagi. 
Anda dapat mengimpor modul-modul ini ke dalam program Python Anda untuk 
memanfaatkan fungsionalitas yang telah disediakan.

web library python :
- docs.python.org
atau ketik
- standard library python


Keuntungan menggunakan standard library adalah bahwa Anda tidak perlu 
mengembangkan kode dari awal untuk fungsi-fungsi umum ini. 
Sebagai gantinya, Anda dapat memanfaatkan modul-modul ini untuk menghemat 
waktu dan upaya dalam pengembangan perangkat lunak Anda.

"""

print(f"=====\nTime Module=====\n")
import datetime #kalau mau eksplor library, klik kanan lalu go to definition
"kalau mau liat penggunaan library yang sama dalam satu folder, go to references."

data_waktu = datetime.datetime.now()
print(f"datetime now : {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")


print(f"\n=====collections - counter=====\n")
from collections import Counter

data = ["a","b","c","d","a","d","a"]
data_count = Counter(data)

print(f"data count = {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")

print(f"\n=====library io=====\n")
import io

file = io.open("file_text.txt","r")
print(file.read())






#Pendahuluan PIP (TITLE)
"""
PIP adalah singkatan dari "Pip Installs Packages" atau "Pip Installs Python". 
Ini adalah sistem manajemen paket yang digunakan untuk menginstal dan 
mengelola pustaka atau modul eksternal (sering disebut sebagai "paket") 
di lingkungan Python Anda. PIP memungkinkan Anda dengan mudah mengunduh, 
menginstal, dan mengelola pustaka-pustaka tambahan yang tidak termasuk 
dalam distribusi standar Python.

Dengan menggunakan PIP, Anda dapat:
Menginstal pustaka eksternal,
Menghapus pustaka,
Mengelola versi pustaka,
Mengimpor pustaka dalam kode Anda.

web PIP : pypi.org 

jika ingin menginstall, install dilakukan pada command prompt (windows user).

"""

"note : syntax pip bisa dilihat di cmd melalui command : pip (kalo lupa)"
#syntax general 
"syntax : pip command option"

#memeriksa versi python
"syntax : python --version (windows user)"

#memeriksa detail dan spesifikasi serta syntax penggunaan PIP dari python yang installed
"syntax : pip (windows user)"

#memeriksa detail list PIP/memeriksa package PIP yang terinstall
"syntax : pip list (windows user)"

#install package 
"syntax : pip install namapackage (windows user)"
"syntax : pip install namapackage==versipackage (windows user)"

#upgrade versi package PIP yang installed
"syntax : python -m pip install --upgrade pip (windows user)"

#uninstall package 
"syntax : pip uninstall namapackage (windows user)"


#Numpy Explore Package (TITLE)
import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list_a = {list_a}")
# print(list_a**2) <- ini akan gagal
print(f"vector_a = {vector_a}")
print(f"a pangkat 2 = {vector_a**2}")
print(f"a kali 5 = {vector_a*5}")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b^2 = \n{matrix_b**2}")

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones c = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"jumlah = \n{jumlah}")


































































