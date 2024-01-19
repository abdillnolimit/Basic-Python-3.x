# Pendahuluan List (TITLE)
"""
List adalah salah satu jenis struktur data yang paling sering digunakan pada python.
Selain assignment, list merupakan struktur data yang sangat fleksibel dan kuat 
dalam Python, dan menjadi salah satu pilihan utama untuk mengelola data dalam 
program Python.

Definisi List :
List merupakan kumpulan elemen berupa nilai atau data yang diurutkan dalam urutan tertentu, 
dan setiap elemennya dapat memiliki tipe data yang berbeda.

List dalam Python ditandai dengan tanda kurung siku [ ] dan elemennya 
dipisahkan dengan koma.

"""

# List --------------------------
"List dengan data numbers."
print("=====List dengan data numbers=====\n")
list_data_numbers = [-1,-2,0,1,2,3]
print("List data numbers =", list_data_numbers,"\n")

"List dengan data string."
print("=====List dengan data string=====\n")
list_data_string = ['Abdill', 'Faiz', 'Ayu']
print("list data string =", list_data_string,"\n")

"List dengan data boolean."
print("=====List dengan data boolean=====\n")
list_data_boolean = [True,False,True]
print("List data boolean =",list_data_boolean,"\n")

"List dengan data campuran."
print("=====List dengan data campuran=====\n")
list_data_campuran = [1,'Abdill', True,2,'Otong',False]
print("List data campuran =", list_data_campuran,'\n')

#Cara alternatif membuat list 

"menggunakan range"
print('=====List menggunakan for loop=====') #list comperhension
data_range = range(-5,3) #range ngeprint data dari -5 sampai 2.
list_datarange = list(data_range)
print("list data range =",list_datarange,"\n")

data_range_kedua = range(0,10,3) # range(start, stop, step)
list_data_range_kedua = list(data_range_kedua)
print("List data range kedua=", list_data_range_kedua,"\n")

"menggunakan for loop"
print("=====List menggunakan for loop=====")
list_pakai_for = [i for i in range(-2,5)]
print("List menggunakan for loop =",list_pakai_for,"\n")
list_pakai_for = [i**3 for i in range(-2,5)] #hanya berlaku di python wkwk.
print("List pakai for jika dikubikkan menjadi =", list_pakai_for,"\n")

"menggunakan for if"
print("=====list using for if=====")
list_pakai_for_if = [i for i in range(0,10) if i !=5 ] #buat list tanpa 5
print("List pakai for if tanpa print data 5=",list_pakai_for_if)

list_pakai_for_if = [i for i in range(0,10) if i%2 ==0] #list genap
print("List genap =", list_pakai_for_if)

list_pakai_for_if = [i for i in range(0,10) if i%2 !=0] #list ganjil
print("List ganjil=", list_pakai_for_if) 

list_pakai_for_if = [i**2 for i in range(0,10) if i%2 !=0]
print("list ganjil yang dikuadratkan=", list_pakai_for_if)




# Operasi Manipulasi List (TITLE)
"Melakukan operasi manipulasi pada data list."

absensi = ["Ucup", "Otong", "Dudung"]
print(f"data pertama : {absensi} \n")
"""
Pada list, urutan/indeks elemen dari kiri/depan ke kanan dimulai dari 0 sampai n.
Jika dimulai dari kanan/belakang maka berindeks -1 sampai dengan -n.

Dengan indeks, kita dapat melakukan pengambilan atau pemanggilan elemen tertentu
yang ada di sebuah data list.
"""


#memanggil/mengambil elemen dari sebuah data list
data_0 = absensi[0]
print(f"siapakah orang yang pertama berdasarkan absensi? {data_0}. \n")

data_terakhir = absensi[-1] #indeks -1 memudahkan kita menemukan elemen terakhir jika data list berelemen banyak.
print(f"siapakah orang terakhir pada absensi? {data_terakhir}. \n")

#mengambil informasi jumlah elemen yang ada pada data list / panjang data
panjang_data = len(absensi)
print(f"berapa orang yang tertera pada absensi? {panjang_data}. \n")

"Perlu dipahami bahwa jika kita memiliki data list, maka pasti kita dapat mencari tahu indeks dan panjangnya data."

#menambahkan item pada data list
print(f"data sebelum update : {absensi}")
absensi.insert(2, "ucok")
print(f"absensi revisi pertama : {absensi}.\n")

#menambah item di akhir list
absensi.append("Jajang")
print(f"absensi revisi kedua :{absensi}.\n")

#menggabungkan/menambahkan list dengan list
siswa_baru = ['dadang', 'usep']
absensi.extend(siswa_baru)
print(f"absensi revisi ketiga : {absensi}.\n")
"dengan cara ini, data baru akan ditambahkan di posisi akhir elemen."

#mengubah elemen dari data list 
absensi[0] = 'Nisrina'
print(f"absensi terbaru : {absensi}.\n")

#meremove elemen dari data list
absensi.remove('usep') #perhatikan kesesuaian penulisan huruf elemen agar tidak eror.
print(f"absensi setelah usep keluar : {absensi}. \n")

#meremove elemen paling akhir dari data list
orang_terakhir_pada_absensi = absensi.pop()
print(f"orang urutan terakhir pada absensi ialah : {orang_terakhir_pada_absensi}. \n{absensi}. \n")


#Operasi List (TITLE)

data_angka = [1,1,5,7,9,3,2,4,1,3,6,5,0]

#Count jumlah elemen yang sama pada sebuah data list
jumlah_elemen_1 = data_angka.count(1) ; print(f"Jumlah angka 1 pada data list = {jumlah_elemen_1} buah.")
jumlah_elemen_3 = data_angka.count(3) ; print(f"Jumlah angka 3 pada data list = {jumlah_elemen_3} buah.")

#ambil posisi/indeks elemen 
absen = ['otong', 'ucup', 'daulah', 'talulah'] ; print(f"\nabsensi : {absen}")
index_otong = absen.index('otong')
print(f"indeks otong : {index_otong}")

absen.index('ucup') ; print(f"indeks ucup : {absen.index('ucup')}")

#sorting/mengurutkan elemen-elemen pada data list
print(f"data list angka sebelum sorting : \n{data_angka}.")
data_angka.sort()
print(f"\ndata angka sorted kecil ke besar : \n{data_angka}.")

absen.sort() ; print(f"\nabsensi sorted : \n{absen}.")

#reverse sorting
absen.reverse() ; print(f"\nabsensi reverse : \n{absen}")
data_angka.reverse() ; print(f"\ndata list angka reverse sorted : \n{data_angka}.")


#Copy/duplikat List (TITLE)
"Terdapat 2 metode."

nama_orang_beriman = ['ucup', 'otong', 'daulah']
print(f"nama orang beriman : {nama_orang_beriman}. \n")

b = nama_orang_beriman #Pass by Reference (adress nya sama)
print(f"data list b : {b}.\n")

b.sort() ; print(f"sorting b : {b}.")
print(f"data nama orang beriman : {nama_orang_beriman}.\n") 
"Perhatikan bahwa jika kita mengubah salah satu variabel, maka variabel lain juga terlibat."
print(f"periksa adress nama orang beriman : {hex(id(nama_orang_beriman))}")
print(f"periksa adress variabel b : {hex(id(b))}")
"terbukti adress nya sama, maka ini akan membuat perubahan pada variabel lain jika dibuat assignment pada keduanya."
"!!!Metode duplikat seperti ini namanya pass by reference. Ini bukan copy list!"

c = nama_orang_beriman.copy() #full duplicate
print(f"\nperiksa address nama orang beriman : {hex(id(nama_orang_beriman))}")
print(f"periksa address variabel b : {hex(id(b))}")
print(f"periksa address variabel c : {hex(id(c))}")
"terbukti adress c berbeda, tetapi c berhasil menduplikat list nama orang beriman."
"inilah yang dinamakan metode copy list!"
print(f"\ndata list c : {c}\n")
"maka jika kita lakukan perubahan pada c, tidak akan menyebabkan perubahan pada variabel lainnya."
c[0] = 'herman'
print(f"\ndata list c menjadi : {c}.\n")
print(f"data list orang beriman : {nama_orang_beriman}")
print(f"data list b : {b}")


#Nested List / List bersarang / List di dalam List (TITLE)
data_1 = [0,1,2] ; data_2 = [2,3] ; data_3 = [3,4,5]
list_2D = [data_1,data_2,data_3, 'ucup', 'otong', 'daulah']
print(f"list 2 dimensi : {list_2D}.\n")

peserta_0 = ['ucup', 17, 'laki-laki']
peserta_1 = ['otong',18,'laki-laki']
peserta_2 = ['daulah',19,'banci']
list_peserta = [peserta_0,peserta_1,peserta_2]
print(f"list peserta lomba :\n{list_peserta}.\n")

for peserta in list_peserta : #enumerated,akan dipelajari di next
    print(f"nama\t: {peserta[0]}")
    print(f"usia\t: {peserta[1]}")
    print(f"jenis kelamin : {peserta[2]}.\n")

"untuk data list 2 dimensi, ada metode list khusus, mari kita pelajari."



#DeepCopy untuk Nested List
"""
Jika pada data list sederhana, kita perlu melakukan copy dengan method
variabel.copy(), maka ini tidak berlaku sepenuhnya jika kita ingin
copy nested list.
"""

himpunan_angka_pertama = [1,2,3]
himpunan_angka_kedua   = [-1,0,2]
nested_list_pertama = [himpunan_angka_pertama, himpunan_angka_kedua,9,10]
print(f"\nnested list pertama = {nested_list_pertama}")
print(f"dengan adress : {hex(id(nested_list_pertama))}")
cara_copy_nestedlist_yangsalah = nested_list_pertama.copy()
print(f"adress copy nested list cara yang salah : {hex(id(cara_copy_nestedlist_yangsalah))}\n")
"adress data list nya memang sudah berbeda, tetapi adress list sebagai elemennya masih sama."
"sehingga itulah yang dapat menjadi masalah."
"mari kita buktikan"
print(f"adress elemen 0 pertama pada nested list : {hex(id(nested_list_pertama[0]))}")
print(f"adress elemen pertama copied nested list : {hex(id(cara_copy_nestedlist_yangsalah[0]))}")
"terbukti sama!"

"berikut cara yang benar untuk copy nested list"
from copy import deepcopy #gunakan modul import ini untuk memanggil deepcopy
cara_copy_nestedlist_yangBENAR = deepcopy(nested_list_pertama) #ini bentuk function yang bukan berformat method
print(f"\n=====Mari kita buktikan=====\n")
print(f"adress elemen 0 pertama pada nested list : {hex(id(nested_list_pertama[0]))}")
print(f"adress elemen pertama copied nested list : {hex(id(cara_copy_nestedlist_yangsalah[0]))}")
print(f"adress elemen pertama dengan deepcopy : {hex(id(cara_copy_nestedlist_yangBENAR[0]))}\n")

print(f"=====Perbedaan adress data list=====")
print(f"data list asal  : {hex(id(nested_list_pertama))}")
print(f"copy\t\t: {hex(id(cara_copy_nestedlist_yangsalah))}")
print(f"deepcopy\t: {hex(id(cara_copy_nestedlist_yangBENAR))}\n")
""" 
Terbukti masing-masing address berbeda, begitupun address masing-masing elemennya.
Cara copy pada nested list berbeda !!!
GUNAKAN function deepcopy(namavariabelyangingindicopy) pada variabel deepcopy yang telah dibuat.
"""


# Looping List & Enumearate (TITLE)

#for
print(f"=====for=====")
kumpulan_angka = [2,1,3,5,4]
for anjay in kumpulan_angka :
    print(f"nilai = {anjay}")
print(f"\n\n")

#for dan range
print(f"=====for dan range=====")
kumpulan_angka = [2,1,3,5,4]
panjang_list = len(kumpulan_angka)
for anjay in range(panjang_list) : #penulisan range langsung, bisa juga dipisah/dibuat variabel assignmentnya sendiri.
    print(f"ini data ke-{anjay} = {kumpulan_angka[anjay]}")

print(f"\n\n")

#while 
print(f"=====while=====")
kumpulan_angka = [2,1,3,5,4]
indeks = 0
while indeks<len(kumpulan_angka) :
    print(f"data ke-{indeks} = {kumpulan_angka[indeks]}")
    indeks+=1 #gw baru tau, operator assignment harus dibawah declarator. awkaowkok maap

print(f"\n\n")

#list comprehension
print(f"=====List Comprehension=====")
kumpulan_angka = [2,1,3,5,4] ; panjang = len(kumpulan_angka)

[print(f"data = {i}") for i in kumpulan_angka]

print(f"\n\n")


#Enumerate 
print(f"=====Enumerate=====")
kumpulan_angka = [2,1,3,5,4]
for anjay in enumerate(kumpulan_angka) :
    print(f"Enumerate indeks dan data = {anjay}") #

print(f"\n\n")

#Eksponen
kumpulan_angka = [2,1,3,5,4]
kuadrat = [anjayy**2 for anjayy in kumpulan_angka]
print(f"kuadrat = {kuadrat}")


#Latihan List (TITLE)
"Membuat program daftar pustaka yg berisikan judul dan penulis buku."

list_buku = []
while True :
    print(f"Masukkan data buku")
    judul = input("judul buku\t:")
    penulis = input("penulis buku\t:")

    buku_baru = [judul,penulis]
    list_buku.append(buku_baru)

    print(f"\n\n","="*10, "Data Buku","="*10)
    for index,buku in enumerate(list_buku) :
        print(f"{index+1} | {buku[0]} | {buku[1]}")

    print("\n\n", "="*20)
    isLanjut = input("Apakah dilanjutkan? (y/n)")

    if isLanjut == "n" :
        break

print("PROGRAM SELESAI")

"""perhatian-perhatian !!!

sebenarnya membuat program ini tidaklah sulit dan kompleks,
kita dapat membuatnya lebih sederhana setelah kita mempelajari function.


"""















