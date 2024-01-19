print("Hello Faizasyah") #cuma nge-test aja kok hehe
print("selamat datang di tutorial python"); 'nge-test juga kok hehe'
print('ini adalah rekam jejak belajar python-ku')


# 03-Cara Kerja Program dan Bytecode (TITLE)
"Setelah melakukan set up text editor, extension, dan path, mari kita lanjutkan belajar python kita."

#Syarat menjalankan program pada python
"""Pada python, jika kita ingin running terminal/menjalankan program,
kita harus download ekstensi python terlebih dahulu.
"""
#Cara menjalankan program python
"""cara menjalankan program python paling mudah ialah dengan mengklik tombol run terminal pada vscode.
Hasil yang muncul ialah berupa detail spesifikasi folder dan file program, dan isi program yang disusun
dalam bentuk absolut.

Selain itu, terdapat cara manual dalam menjalankan program serta memeriksa detail folder dan file python,
yaitu sebagai berikut.
->cara memeriksa detail, folder, dan file apa saja pada program:
tulis dir pada terminal(untuk pengguna windows) atau tulis ls (untuk pengguna Mac dan Linux).
->Cara memeriksa versi python yang digunakan:
tulis python --version (untuk pengguna windows) atau tulis python3 --version (untuk pengguna Mac dan Linux).
->menjalankan program pada file
tulis python namafile.py (bagi pengguna windows) atau python3 namafile.py (bagi pengguna Mac dan Linux).

Apabila ada folder atau file yang tidak ingin dideteksi atau dijalankan pada terminal,
dapat di-hide pada explorer VSCode."""

'Note: tulisan python3 yang dimaksud ialah versi python 3'

#Alur Pemrograman python
'Perlu diketahui bahwa python adalah bahasa pemrograman interpreted.'
"""Maksudnya interpreted apa?Maksud Interpreted di sini ialah semua source code pada file yang ada akan langsung
diterjemahkan oleh python itu sendiri baris per baris ke terminal.
Alur nya ialah sebagai berikut:

Source Code(File)-> Interpreter(Python)->Terminal

Setiap baris kode yang ada di source code(file) secara langsung dieksekusi oleh python.
Hal inilah yang membuat banyak orang menganggap python ialah bahasa pemrograman yang mudah dimengerti.

Program python akan mengeksekusi source code dengan berdasarkan urutan code.


Lain seperti bahasa pemrograman lain, misalnya C/C++. Bahasa ini bukan interpreted, melainkan adalah compiled.
alur C/C++ ialah :
Source Code -> Compiler -> .exe(Executable) -> Terminal
Performa menerjemahkan antara python dengan C/C++ berbeda, yang pasti
C/C++ (Compiled Language) lebih cepat dibanding python(interpreted language)

"""

#Contoh penulisan assignment dan operator
a = 5 #ini tidak dijalankan pada terminal, cuma disimpan di dalam memori
print("a") #bukan seperti ini untuk menjalankan operator a 
print(a) #tapi seperti ini hehe
"""Note : Python menjalankan program berdasarkan urutan pada source code.
contoh pada penulisan operator di atas.
Seandainya operator dituliskan setelah print, maka akan terjadi eror.
Ini karena statement print tidak dapat membaca operator yang dimaksud, atau
malah menjalankan operator a yang sama sebelumnya.
"""

#APAKAH PYTHON BISA DIJADIKAN MENJADI BAHASA COMPILED SEPERTI C/C++?
'BISA DONG!'
"""
Alurnya menjadi Source Code->bytecode->compiler->Executable->Terminal"""

"""caranya ialah pilih file python mana yang ingin dicompile, lalu tuliskan coding an compile-nya pada terminal,
coding compile untuk python :
python -m py_compile namafile.py (bagi pengguna windows)
atau
python3 -m py_compile namafile.py (bagi pengguna MAC/Linux)

lalu run pada terminal.
Maka VSCode akan membuat folder baru bernama __pychache__ yang berisikan file yang ter-compile
yang bernama namafile.cpython-versipython.pyc
c yang tertera pada nama file mengindikasikan bahwa file python yang ter-compile
telah dihubungkan dengan program C/C++.

Untuk pindah turun lokasi pemrograman antar folder dapat dituliskan coding pada terminal
sebagai berikut :

cd __namafolder__

cd di sini maksudnya adalah change directory. Anda telah masuk pada folder yang dituju.
Anda dapat merunning terminal untuk folder tersebut.
Selain itu, kita juga dapat berpindah folder ke folder tepat 1 di bawah folder yang sedang dirunning.
Coding pindah folder ke atasnya:
cd ..

NOTE!apabila kita membuat perubahan pada source code, baik source code interpreted atau compiled,
agar file compiled nya terbarukan, maka kita harus me-compile ulang file yang diubah tersebut
pada terminal. Lalu masuk ke masing-masing folder/file nya untuk dirunning.

untuk mengetahui perbedaan nilai kecepatan running-nya, gunakan library time measurer
coding library time measurer:

import time
start_time= time.time()

lalu tulis coding untuk hasil akhirnya

print(time.time() - start_time, "Detik")

"""
import time 
start_time= time.time() 
a = 10
print(a)
print(time.time() - start_time, "detik") 


print("Berikut cara membuat komentar dan string di python")
judul = "Penulisan komentar dan string"
nama = 'ini nama'
awikwok = """WKKWKWK"""
#penulisan judul, nama, dan awikwok di atas adalah contoh penulisan string.

#ini komentar one line atau single comment line

"""ini 
multiline 
comment"""

'Ini tanda petik tunggal. bisa juga seperti ini, tapi single line juga'

"Ini tanda petik ganda. Seperti ini juga bisa dijadikan komentar, tapi juga single line"

"""tanda petik tunggal dan ganda hanya digunakan sebagai
komentar dengan single line. Berbeda dengan triple tanda kutib.
Selain itu, tanda petik tunggal dan ganda juga digunakan untuk
menuliskan string(teks atau kumpulan karakter) dan komentar."""


#VARIABEL (TITLE)
"Sebelum mengenal variabel, perlu kita ketahui fitur python, salah satunya adalah interaktif python/Interaktif Shell"
#Coding Interaktif Shell : python atau python3 (run into terminal), tanda >>> artinya python siap menerima perintah.
#coding keluar dari mode interaktif : exit() (run into terminal)
"Apa itu variabel pada python?"
""" Jika sudah masuk variabel, maka kita membahas mengenai data.
Variabel pada python sebenarnya sama dengan variabel pada matematika.
Variabel pada python adalah tempat menyimpan data.
misal x = 5
x disebut sebagai variabel, 5 disebut sebagai value, = disebut sebagai operator.
x = 5 dapat diartikan sebagai 5 kita simpan sebagai x (assignment).
Atau kita juga dapat artikan sebagai x adalah variabel yang bernilai 5.
"""
#Pemanggilan data pada variabel
a = 19
print(a)
print("Nilai a =",a)
#Penulisan variabel
"""
Selain menggunakan satu huruf, variabel sebenarnya dapat ditulis dengan gabungan huruf,
atau bahkan angka, dan simbol lainnya. Namun, harus memenuhi kaidah penulisannya.

x = 5
panjang = 100000

10ribu = 10000 (ini tidak boleh, tidak boleh ada angka di depan)
ribu10 = 10000 (ini boleh)

nilai x = 3 (salah, jika menggunakan spasi, harus dipisah dengan underscore)
nilai_x = 3 (Benar)
atau
nilaix = 3 (benar)
penggunaan underscore pada source code, jika di run di terminal, akan menjadi spasi.

"""

c = 23
print("Nilai C =", c)
#Bagaimana jika ada c lagi di bawahnya?
c = 33
print("Nilai c =", c)
#Tetap bisa. Karena statement yang dipilih oleh python adalah statement paling baru.
nilai_x = 99
print("Nilai x =", nilai_x)

b = c #Jenis penamaan indirect assignment
print("Nilai b =", b)

#TIPE DATA (TITLE)
"""
Tipe data adalah macam-macam data yang dapat kita pakai di python, yang dapat
kita input ke variabel.
Pada kali ini, kita bahas jenis-jenis tipe data.
"""

#int (Integer)
"""
Integer adalah salah satu jenis data dengan nilai nondesimal. Dengan kata lain,
integer berupa bilangan bulat (bilangan negatif, nol, positif)
"""
awikwok = 25
print(awikwok)
print("awikwok bertipe :", type(awikwok))
#terbukti bahwa 25 termasuk tipe data integer.

#float (Desimal)
"""
Float adalah salah satu jenis data dengan nilai desimal.
"""
abdill = 2.5
print(abdill)
print("abdill bertipe :", type(abdill))
"""
Perhatikan bahwa tanda koma yang digunakan adalah . bukan ,
jika menggunakan tanda . maka jenis data berupa tuple."""

#str (string : kumpulan satu atau lebih karakter)
"""
String adalah salah satu jenis data dengan nilai desimal.
"""
Faiz = "epic1abadi"
print(Faiz)
print("Faiz bertipe :", type(Faiz))

#bool (boolean : Biner/ True or False)
"""
Boolean adalah salah satu jenis data dengan nilai 0 atau 1 (bilangan biner).
Value lain yang biasa digunakan adalah true, false.
False dinyatakan sebagai nilai 0, sedangkan bilangan selain 0 
dinyatakan sebagai boolean.
"""
data_boolean = True
print(data_boolean)
print("data boolean bertipe :", type(data_boolean))

"Tipe-tipe data yang dibahas barusan ialah tipe data dasar pada pemrograman, termasuk python."
"selain tipe data dasar, disebut tipe data khusus."

#complex (bilangan kompleks)
"""
complex adalah salah satu jenis data dengan nilai yang mencakup bilangan real dan imajiner.
"""
data_bilangan_kompleks = complex(5,7)
print(data_bilangan_kompleks)
print("data bilangan kompleks bertipe :", type(data_bilangan_kompleks))
"""
Pelajari juga cara penulisan operasi bilangan matematika pada pemrograman,
seperti + - : x bila ditulis ke dalam bahasa pemrograman seperti apa.
"""

#tipe data dari bahasa C
"""
mengingat bahwa bahasa python dibuat sebagiannya dengan menggunakan bahasa C,
maka python dapat menggunakan bahasa C dengan cara mengimpornya terlebih dahulu.
coding import :
from ctypes import namajenistipedata
"""

#c_double (bilangan desimal dengan nilai yang lebih banyak)
"""
tipe data double sebenarnya tidak ada di python, hanya saja kita mengimpornya sendiri
dari bahasa C dengan kebutuhan tertentu.
"""
from ctypes import c_double 
data_cdouble = c_double(10.5)
print(data_cdouble)
print("data c_double bertipe:", type(data_cdouble))

#c_char


#c_long


#Casting Tipe Data (TITLE)
"""
Casting Tipe Data adalah pengubahan tipe data ke jenis tipe data yang lain.
"""

print("===integer===")
data_integer = 55
data_float   = float(data_integer)
data_string  = str(data_integer)
data_boolean = bool(data_integer)
print("data ", data_float,"berjenis : ", type(data_float))
print("data ", data_string, "berjenis : ", type(data_string))
print("data ", data_boolean,"berjenis : ", type(data_boolean))

print("===float===")
data_float = 0.5
data_integer   = int(data_float) #int membulatkan bilangan desimal ke bawah
data_string    = str(data_float)
data_boolean   = bool(data_float)
print("data", data_integer,"berjenis :", type(data_integer))
print("data", data_string,"berjenis :", type(data_string))
print("data", data_boolean,"berjenis :", type(data_boolean))

print("===string===")
data_string   = -3 
data_integer  = int(data_string)
data_float    = float(data_string)
data_boolean  = bool(data_string)
print("data", data_integer,"berjenis :", type(data_integer))
print("data", data_float,"berjenis :", type(data_float))
print("data", data_boolean,"berjenis :", type(data_boolean))

print("===boolean===")
data_boolean   = 1
data_integer   = int(data_boolean)
data_float     = float(data_boolean)
data_string    = str(data_boolean)
print("data", data_integer,"berjenis :", type(data_integer))
print("data", data_float,"berjenis :", type(data_float))
print("data", data_string,"berjenis :", type(data_string))


print("data", data_integer,"berjenis :", type(data_integer))
print("data", data_float,"berjenis :", type(data_float))
print("data", data_string,"berjenis :", type(data_string))


# Mengambil input dari User (TITLE)
"""
Mengambil input dari user maksudnya adalah kita dapat menginput value data dari variabel
secara langsung pada terminal melalui sintaks casting tipe data yang sudah dibuat.
"""
data = input("masukan input :")
print(data,"bertipe",type(data))
"""
Semua data yang diinput pada casting input, menghasilkan tipe data string.
"""

input_data = int(input("input untuk menghasilkan integer:"))
print(input_data,"bertipe",type(input_data))
"Input dan output berupa integer"

input_float = float(input("input float :"))
print(input_float,"bertipe",type(input_float))
"input harus integer dan output berupa float"

input_boolean = bool(int(input("masukan angka biner:")))
print(input_boolean,"bertipe:", type(input_boolean))
"""
note : harus dicasting dulu dari input ke int atau float supaya tidak eror
yang selalu menghasilkan type true. 
"""