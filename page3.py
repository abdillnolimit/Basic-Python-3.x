# #If dan Else Statement (Title)
# """
# Pada pembelajaran sebelumnya, kita mempelajari pemrograman dengan
# satu alur/satu kondisi(linear). Dengan diagram sebagai berikut,

# Input ->Program -> Stop

# Pada topik kali ini, kita akan belajar pemrograman dengan alur
# lebih dari 1 atau tak terhingga(controlled flow).
# Misal 2 kondisi,

# input -> pengondisian (if statement) -> aksi (true/false) -> Stop

# pada fase pengondisian(if statement) lah yang dinamakan controlled flow atau
# alur yang dikendalikan.

# Mari kita coba buat kasus sederhananya.

# codingan if dan else statement berikut,

# if kondisi: aksi
#     aksi if(jika true)
#     aksi if(jika true)

# else aksi else(jika false)
#     aksi else(jika false)

# Stop(Akhir dari alur program)

# catatan : Indentasi
# Tanda indentasi menyatakan bahwa area input pengondisian. Tanda indentasi
# dapat kita temui ketika kita telah mendeklarasikan if atau else statement
# yang jika kita klik enter, maka akan membuat indentasi di line barunya.
# Untuk keluar dari indentasi/program pengondisian, kita dapat klik backspace.
# """

# #Program if sederhana pertama (inline)
# nama = str(input("Silakan input nama Anda :"))
# if nama=="Abdillah":
#     print("Selamat, kamu adalah orang terpilih,")
#     print("kamu adalah orang paling tampan dan baik di dunia selain Nabi dan Rasulullah.")
    
# print(f"Terima kasih telah berkunjung {nama}!")
# print("Program telah berakhir.")

# """Diagram Program
# input -> pengondisian (if statement) -> Jika true -> Aksi True -> stop.
# input -> pengondisian (if statement) -> Jika false-> Aksi false-> stop.
# """

# # #ElIf Statement
# """
# ElIf statement dapat kita gunakan untuk membuat pengondisian yang sangat banyak
# dengan berbagai macam aksi pada masing-masing kondisinya.
# Pada contoh sebelumnya(inline sederhana), ketika kondisi false, tidak ada aksi false
# atau dengan kata lain program langsung berakhir.
# Pada ElIf statement, jika kondisi false, maka akan dilanjutkan ke kondisi selanjutnya.

# Diagram ElIf Statement :

# input -> kondisi -> true/false -> jika true maka langsung dieksekusi lalu program selesai.

# input -> kondisi -> true/false -> jika false -> kondisi lain -> jika false -> kondisi lain -> 
# ->dst sampai true atau sama sekali tidak memenuhi dan akhirnya program dialihkan ke stop -> stop.

# """

# #Else Statement
# if nama== "Abdillah" :
#     print(f"Fiks, kamu idaman :))) , selamat {nama}!")
# else : 
#     print("Maaf kamu bukan Abdillah, kamu tidak idaman :(")

# print("Program berakhir.")


# #Elif Statement
# "Controlled flow dari Elif statement biasa disebut sebagai percabangan."
# if nama=="Abdillah" :
#     print("=====Fiks Kamu keren=====")
# elif  nama=="Faizasyah" :
#     print("Fiks, kamu adeknya Abdillah, kamu juga keren!")
# elif nama=="ucup" :
#     print("Fiks, kamu gajelas!")

# else : print("Maaf, nama tidak dikenal hehe.")
# print("Program berakhir.")

# "Kita dapat menggunakan elif statement sebanyak apapun."



# #Latihan membuat kalkulator sederhana dengan percabangan (TITLE)

# """
# Misalkan kita memiliki bentuk operasi sebagai
# angka_1 (+ - x /), integral dan turunan belakangan dulu ygy.
# """
# angka_1 = float(input("masukan angka pertama = "))
# operator = input("masukan jenis operator yang digunakan : ")
# angka_2 = float(input("Masukan angka kedua = "))

# print(20*"=") ; print("Latihan Operasi sederhana dengan percabangan")
# print(20*"=")

# if operator=="+" :
#     hasil = angka_1 + angka_2
#     print(f"Hasilnya adalah {hasil}")
# elif operator=="-" :
#     hasil = angka_1 - angka_2
#     print(f"Hasilnya adalah {hasil}")
# elif operator=="x" or operator=="*" : 
#     hasil = angka_1 * angka_2
#     print(f"Hasilnya adalah {hasil}")
# elif operator=="/" :
#     hasil = angka_1 / angka_2 
#     print(f"Hasilnya adalah {hasil}")
# else : 
#     print("Maaf terjadi kesalahan input user.")

# print("Program telah berakhir.")



# #For Loop/Perulangan (TITLE)

# """ Percabangan (Elif) VS Perulangan (Loop)

# Jika pada elif, percabangan adalah program dengan alur menuju ke bawah(aksi->Stop),
# sedangkan pada perulangan, program yang dijalankan akan mengulang dengan diagram
# sebagai berikut,

# Diagram Loop :
# input -> kondisi -> aksi -> kondisi -> aksi -> mengulang sampai n kali -> stop.


# Format coding for Loop sebagai berikut,

# for kondisi : aksi
#     aksi
#     aksi

# Akhir program.

# """

# #For Loop dengan menggunakan list
# himpunan_A = [0,1,2,3,4,5]

# for elemen_himpunan_A_wkwk in himpunan_A :
#     print(f"elemen himpunan A, yaitu = {elemen_himpunan_A_wkwk}")

# print("Program selesai. \n")


# #For Loop dengan menggunakan range
# himpunan_B =  range(10)

# for i in himpunan_B : 
#     print(f"Range himpunan B sampai dengan : {i}")

# print("Program selesai. \n")

# himpunan_C = range(1, 10)
# for c in himpunan_C :
#     print(f"Himpunan C : {c}")

# print("Program telah berakhir. \n")


# #For Loop dengan menggunakan string
# data_str = "gw keceh dari lahir."
# for str in data_str :
#     print(f"{str}")

# print("Program berakhir.")

# """List VS Range VS String (For Loop)
# ->List akan mengulang kondisi dan aksi untuk elemen-elemen di
# dalam list/himpunan.

# ->Range akan mengulang kondisi dan aksi untuk program yang diinput
# sebanyak range yang dibuat.

# -> string akan mengulang kondisi dan aksi ke bawah sesuai urutan
# komponen string yang dibuat.


# """


# #While Loop (TITLE)
# """ For Loop VS While Loop
# Pada  for loop, data akan diulang berdasarkan perintah(list, range, string, dsb...),
# sedangkan pada while loop, data akan diulang berdasarkan kebenaran/validasi.
# Oleh sebab itu while loop melibatkan tipe data boolean.

# while kondisi(boolean) :
#     aksi
#     aksi

# akhir dari program.

# """

# angka = 10

# while angka < 5 :
#     print(f"gw keceh {angka}") # #gak jalan anying, knp y
# #jawaban : karena angka > 5. pernyataan angka < 5 tidak valid.

# print("Akhir dari program. \n")

# while angka > 5 :
#     print(f"gw kecehh parahmeen {angka}")
# #btw buat ngedelete terminalnya pas di run, klik ctrl+C dulu!
# print("akhir program. \n")

# angka = 0
# print("Angka awal adalah = ", angka)

# while angka < 5 :
#     angka += 1
#     print(f"Hasilnya adalah {angka}")
#     print("gw ganteng maximal")

# print("Program berakhir.")
# #ini baru jalan! 
# # berarti yang sblmnya ga jalan karna statement salah, angka 10.

# """ For Loop VS While Loop

# Dalam Python, for loop dan while loop adalah dua jenis perulangan 
# yang digunakan untuk menjalankan blok kode secara berulang. 
# Perbedaan utama antara keduanya adalah cara mereka mengontrol 
# jalannya perulangan.

# For loop digunakan ketika kita ingin menjalankan blok kode 
# secara berulang sejumlah tertentu. Ini adalah jenis perulangan 
# yang paling umum digunakan untuk mengulang melalui elemen-elemen 
# dalam sebuah urutan seperti daftar (list), tuple, atau string.

# While loop digunakan ketika kita ingin menjalankan blok kode 
# secara berulang selama kondisi tertentu terpenuhi. Blok kode 
# dalam while loop akan terus dieksekusi selama kondisi tersebut 
# bernilai True. Kondisi ini diperiksa sebelum setiap iterasi perulangan.

# Kesimpulan :
# -For loop cocok untuk situasi di mana kita ingin mengulang melalui urutan elemen.
# -While loop cocok untuk situasi di mana kita tidak tahu berapa kali perulangan 
# akan terjadi dan tergantung pada kondisi yang harus terpenuhi.
# """

# #Continue, pass, break (TITLE)

# #Misal kita melakukan if di dalam while Loop, menjadi
# angka = 5
# while angka < 10 : #dibaca : selama angka dibawah 10, jumlahkan angka dengan 1 dan print gw keceh ketika sampai 7,5 .
#     angka += 0.5
#     if angka== 7.5 : #if di dalam proses/program while
#         print(f"gw keceh ") #program if di dalam while
#     print(angka) #jalankan while
# print("Program telah berakhir. \n")

# "Jika kita ingin mengomposisikan seperti di atas, ingat syntax html."

# #Pass
# "Pass adalah dummy, yang artinya memblok program if else loop sehingga tidak terjalankan."
# print("\n dummy pass")
# angka = 0
# while angka < 5 :
#     angka+=1
#     if angka == 3 :
#         pass # program if tidak akan dieksekusi.
#     print(angka)
# print("program berakhir. \n")

# #continue
# """
# Dummy continue berfungsi untuk mengulang program tanpa menjalankan
# program berikutnya.

# Misalkan terdapat diagram sebagai berikut,

# input -> kondisi 1 ->jika true maka mengulang
# -> jika false, lanjut ke kondisi 2 -> jika true mengulang ke kondisi 2 -> stop.

# """
# print("\ndummy continue")
# angka = 0
# print("angka start ->", angka)
# while angka < 5 :
#     angka += 1
#     print(f"gw keceh ")
    
#     if angka == 3 :
#         print("anjay 3")
#         continue
#     print("mabar") #aksi ini di skip ketika angka = 3
# print("selesai. \n")

# """ TIPS
# Kalau bingung, uraikan program ke skema gambar/diagram blok.
# """

# #break
# """
# Berbeda dengan pass dan continue, break akan mengakhiri proses perulangan
# ketika telah mencapai kondisi tertentu pada kondisi ke-n.

# """


# print("\ndummy break")
# angka = 0
# print(f"angka mulai -> {angka}")

# while angka < 5 :
#     angka+=1
#     print("kalimat pertama")
#     if angka == 3 :
#         print("woy udah 3 kali ngulang, selesai!")
#         break
#     print(f"kalimat kedua")
# print("Program berakhir.\n")


# Latihan Perulangan (Title)


# Dummy Variable

# "Menggunakan for"
# print("\n=====Menggunakan for=====")
# sisi = 5
# count = 0 # Dummy variable
# for i in range(sisi) :
#     count+=1 #hanya sebagai konstanta pengali/dummy variable
#     print("x"*count) # fungsi

# print("Program berakhir.\n")


# "Menggunakan while"
# print("\n=====Menggunakan While=====")
# ke_bawah = 5
# count = 0 #Dummy Variable
# while True:
#     count+=1
#     print('x'*count)
#     if count > ke_bawah :
#         print("Batas.")
#         break

# print("Program berakhir.\n")


"Latihan print genap saja"
print("=====Ganjil=====")
ke_bawah = 10
count = 0
while True:
    if count%2 : #artinya : print jika habis dibagi 2, jika tidak habis maka diteruskan ke else.
        count+=1 #sebagai input ke kondisi if count%2 
        
        print("x"*count)

    else : #karena jika habis dibagi 2 true dan diberikan aksi lalu looping
        count+=1 #Jika tidak habis dibagi 2, maka diberikan aksi oleh else.
        continue #count yang diberi aksi, yaitu 1,3,5,7,9, sedangkan 2,4,6,8 dieksekusi true.

    if count > ke_bawah :
        break

print("Program Berakhir.")



"Latihan membuat segita sama kaki."
jumlah_baris_ke_bawah = 10
spasi = int(jumlah_baris_ke_bawah/2)
count = 1
while True :
    if count == 1:
        print(" "*spasi+"X") #buat nambahin 1 di atasnya yg ketinggalan aowkaowk.


    if (count%2) :
        count+=1
        continue

    else :
        
        count+=1
        spasi-=1
        print(" "*spasi+"X"*count)

    if count>=jumlah_baris_ke_bawah :
        print("Limit")
        break













