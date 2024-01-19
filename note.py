print("ini catatan belajar python") #mode interaktif python
"""
Fungsi mode interaktif python:
->Uji coba suatu fungsi,
->Eksperimen modul tertentu,
->mencari bantuan tentang fungsi tertentu,
dll
"""
#pada python, kita tidak perlu tanda titik koma untuk mengakhiri code
#Apabila statement dibuat menjadi 1 baris, masing-masing harus dipisahkan dengan ;
print("Hello");print("World");print("mwahh")
#python menjalankan program source code secara berurutan/berdasarkan urutan
#python dapat dijalankan langsung dengan run terminal atau secara manual dengan menuliskan code pada terminal
"""
->memeriksa detail file dan folder pada folder python yang sedang dijalanlan:
dir (for windows user) atau ls (for MAC/Linux user)
->menjalankan sebuah file pada folder :
python namafile.py (Windows User) atau python3 namafile.py(MAC/Linux User)
->memeriksa versi python yang sedang digunakan :
python --version (windows user) atau
python3 --version (MAC/Linux user)
"""
#python adalah bahasa interpreted, untuk menjadi lebih cepat harus dicompile filenya
"""
Alur pemrograman compiled python:
Source Code->bytecode->compiler->Exe->Terminal

coding compiling file python:
python -m py_compile namafile.py (windows user)
python3 -m py_compile namafile.py (MAC/Linux user)

cara turun 1 tahap ke folder di bawah :
cd __namafolder__

naik 1 tahap ke atas folder :
cd ..
(tulis dan running di terminal)

apabila sedang berada di folder lain, kemudian ingin menjalankan file di dalam folder lain,
maka codingannya menjadi :
python __namafolder__/namafile.py
"""
#Compile ulang File apabila telah melakukan perubahan pada source code


#Operator vs assignment
"""
-Operator
adalah operasi yang dapat diberikan pada variabel(objek), value variabel, ataupun literal.
Operator pada python : operator aritmatika, operator logika, operator bitwise, 
Operator assignment, operator string, dsb...

-Assignment
adalah tindakan memberikan value pada variabel sehingga menjadi objek memori.

"""

#Operator vs Method
"""
->Operator
adalah simbol atau tanda khusus yang digunakan untuk melakukan operasi 
pada nilai-nilai atau objek dalam suatu program. 
Dalam Python, operator digunakan untuk melakukan operasi matematika, 
perbandingan, logika, dan operasi pada tipe data lainnya. 
Contoh operator yang umum digunakan adalah + (penjumlahan), - (pengurangan),
* (perkalian), / (pembagian), == (sama dengan), dan lain-lain.


->Method
adalah  fungsi yang terkait dengan objek tertentu. Dalam konteks objek, 
metode adalah tindakan yang dapat dilakukan oleh objek tersebut. 
Metode digunakan untuk memanipulasi objek atau menghasilkan output yang 
berkaitan dengan objek tersebut. Metode selalu terkait dengan suatu objek 
dan diakses melalui sintaks "objek.nama_metode()".

Kesimpulan :
Dalam ringkasan, operator digunakan untuk melakukan operasi pada nilai atau 
objek, sedangkan metode adalah fungsi yang terkait dengan objek dan digunakan 
untuk memanipulasi objek atau menghasilkan output yang berkaitan 
dengan objek tersebut.


"""


sisi = 4 
count = 0
for i in range(sisi) :
    count += 1
    print("x"*count)
print("Program selesai.")

himpunan_B =  range(10)

for i in himpunan_B : 
    print(f"Range himpunan B sampai dengan : {i}")

print("Program selesai. \n")