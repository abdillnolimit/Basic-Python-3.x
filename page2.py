#Pengenalan String (TITLE)
"""
Sebelumnya kita telah menggunakan tipe data string, tetapi tidak secara menyeluruh.
Pada pembahasan sebelumnya, cakupan materi python berupa numbers, dan sekarang
kita akan masuk ke pembelajaran karakter/string.
Pada serial kali ini, kita akan mempelajari string secara menyeluruh.
"""
print("-----------------Cara menuliskan string--------------------")
data_string = "Ini adalah data string, tidak hanya karakter, tetapi juga termasuk spasi."
data_string_kedua = 'Ini juga data string, dengan menggunakan single quote.'
print("Contoh---------------------\ndata string pertama :", data_string, type(data_string),"\ndata string kedua :",data_string_kedua,type(data_string_kedua))

#Cara membuat string
"""
    1. Dengan menggunakan single quote '...'
    2. Dengan menggunakan double quote "..."

"""

print("Ini juga string");print("'ini juga string'");print('"Ini juga string"')
print("-------------------------space----------------------------")

print("ini adalah hari jum'at.")
"Jika ada penggunaan single quote di dalamnya, wajib menggunakan double quote sebagai string printer nya."


#Menggunakan tanda backslash \

"Membuat tanda ' menjadi string."
print('Mari sholat jum\'at')
print('g\'day,isn\'t it?')

print("-----------------space-----------------")

'''
misal kita ingin membuat penulisan yang melibatkan penggunaan backslash juga di dalamnya.'''

print('alamat file ini : C:\\Users\\USER\\OneDrive')

#Raw string r
"atau bisa juga sebagai berikut, dengan menggunakan raw string"
print(r'C:\Users\USER\OneDrive')

#Tab \t
print('alex\tsteve, jadi jauhan deh')

#newline \n
print('ini atas \nini bawah')

print('atas\nbawah') #LF : line Feed, biasanya digunakan pada unix, linux, macos
print("-----------space------------")
print('atas\rbawah') #CR : Carriage Return, biasanya digunakan pada commodore, accorn, lisp
print("------------space-----------")
print('atas\r\nbawah') #CRLF : Carriage Return Line Feed, biasanya digunakan pada windows

#backspace \b
print('alex \bsteve')

#Multiline Literal String
print("""
Nama   : Mohamad Jesus
Status : Belum kawin
""")



#Multiline Literal String dan Raw
print("""
Nama    : Mohamad Jesus
Status  : Belum Kawin
website : MohamadJ.com/newID
""")


#Operasi dan Manipulasi String (TITLE)
"""
Pada kali ini kita akan mempelajari operator-operator yang ada untuk tipe data string,
dan memanipulasi data string. 
"""

#Menyambung String (Concatenate)
nama_pertama = "ucup"
nama_tengah  = "D"
nama_akhir   = "Fame"
nama_lengkap = nama_pertama + nama_tengah + nama_akhir 
print(nama_lengkap)
"agar tidak rapat-rapat, maka"
nama_lengkap = nama_pertama +" "+ nama_tengah +"'"+ nama_akhir 
print("Nama Lengkap : ",nama_lengkap)

"""
Penulisan dengan menyambung string menggunakan tanda + sebenarnya sama aja
dengan kita menggunakan tanda spasi di dalam tanda kutib string.
"""

#Menghitung Panjang string
"Kita dapat menggunakan operator length sebagai helper function."
panjang = len(nama_lengkap) #len termasuk sebagai helper function
print("Panjang nama lengkap ucup :", panjang)
"Jangan lupa, apabila diperlukannya data string, maka"
print("Panjang nama lengkap si ucup :", str(panjang), "tipe data : string",)


#Memeriksa apakah ada komponen char atau string di string
"kita dapat menggunakan operator in, not in, untuk memeriksa komponennya."
d = "d"
status = d in nama_lengkap
print( d, "ada di " + nama_lengkap + " = " + str(status))
"False, karena d nya lowercase, sedangkan di nama lengkap karakter d nya uppercase (D)."
D = "D"
status_D = D in nama_lengkap 
print("Apakah D ada di " + nama_lengkap + " ? " + str(status_D))

status_d = d not in nama_lengkap
print("Apakah d tidak ada di " + nama_lengkap + "?" + str(status_d))

#Mengulang string 

wkwk = "wkwkk"
print("Banyaknya wkwkk adalah = ", wkwk * 10)
print(wkwk*100)

#indexing
"adalah tindakan mengambil data dari assignment string."
print("Index ke-0 :", nama_lengkap[0])
"""Pada python, indeks pertama justru dianggap ke-0"""

print("Index ke-3 :", nama_lengkap[3])
print("Index ke-(-1) :", nama_lengkap[-1])
print("Index ke-(-5) :", nama_lengkap[-5])

"Apabila indeks berupa rentang, maka menjadi"
print("Index [0,7] :", nama_lengkap[0:7])
"apabila dibuat rentang, python justru menganggap komponen paling akhir tidak diikutsertakan."
print("Index [-1, 7] :", nama_lengkap[-1:7])

"Bagaimana jika berupa pola barisan?"
print("Index ke-(0,3,6,9) :", nama_lengkap[0:10:3])
"Dibaca, urutkan nama lengkap dari index  nol sampai 10 berupa barisan dengan pola kelipatan 3."

#Item paling kecil
print("item paling kecil : ", min(nama_lengkap))

#Item paling besar
print("item paling besar : ", max(nama_lengkap))

"Mengapa u paling besar dan spasi paling kecil?"
"""
karena dalam abjad, u memanglah paling besar jika kita mengacu pada 
assignment string nama lengkap ucup, dan 
spasi merupakan item paling kecil dalam abjad jika kita mengacu pada
assignment string nama lengkap ucup.
karena data berupa string, maka
untuk memeriksa dan membuktikan item string ke ascii code(kode ascii), 
kita dapat menggunakan operator ord().

Untuk memeriksa dan membuktikan data berupa number(ascii code) ke item string,
kita dapat menggunakan operator char, yaitu chr().
Dengan kata lain, kita dapat melakukannya invertible.

simpan ini,  karena suatu waktu akan berguna hehe!
"""

kode_ascii_untuk_z = ord("z")
print("kode ascii untuk z berapa :", kode_ascii_untuk_z)
print("kode ascii untuk huruf z berapa :", str(kode_ascii_untuk_z))

data_random = 117
print("data random di atas merupakan item :", chr(data_random))
print("data random di atas adalah :", str(chr(data_random)))
"Jangan lupa casting jika perlu."

#Operator dalam bentuk method
"""
Jika kita perhatikan sebelumnya, string itu tidak memiliki method default,
karena string sendiri merupakan class. 
String sendiri sebenanrnya memiliki method.
Kegunaannya ialah memanipulasi data string.
Method sendiri bercirikan dengan dituliskannya dekat/nempel dengan data variabel.
"""
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada data assignment string adalah :", str(jumlah))
"""
keterangan :
data merupakan objek,
count merupakan method.
Kita akan sering menjumpai bentuk method pada OOP.
"""



#Methods Operator/Operator Dalam Bentuk Methods (TITLE) / Operasi dan Manipulasi String Part 2
"""
Method adalah  fungsi yang terkait dengan objek tertentu. Dalam konteks objek, 
metode adalah tindakan yang dapat dilakukan oleh objek tersebut. 
Metode digunakan untuk memanipulasi objek atau menghasilkan output yang 
berkaitan dengan objek tersebut. Metode selalu terkait dengan suatu objek 
dan diakses melalui sintaks "objek.nama_metode()".

Perbedannya dengan operator secara ringkas :
operator digunakan untuk melakukan operasi pada nilai atau 
objek, sedangkan metode adalah fungsi yang terkait dengan objek dan digunakan 
untuk memanipulasi objek atau menghasilkan output yang berkaitan 
dengan objek tersebut.
"""


#Mengubbah Case dari string (Upper->Lower, Lower->Upper)

#upper -> lower case 
"Mengubah semua karakter menjadi lowercase."
"coding : namaobjek.lower() "

alay = "Aku kEce aBiEezzZz"
alay_lowercase = alay.lower()
print("Tipe :", type(alay_lowercase)) #class : string
print("kata si alay : " + alay_lowercase)


#lower -> upper case 
"Mengubah semua karakter menjadi uppercase."
"coding : namaobjek.upper() "

alay_uppercase = alay.upper() #class : string 
print("Tipe data : ", type(alay_uppercase))
print("Kata si alay : " + alay_uppercase)

#Pengecekan dengan method islower() dan isupper 
"Tipe data yang dihasilkan metode isX adalah boolean."
"Jika ingin di-concatenate maka harus di-casting ke string terlebih dahulu."

salam = 'sist'
crosscheck_salam_apakah_lower = salam.islower() ; print("Tipe data :", type(crosscheck_salam_apakah_lower))
crosscheck_salam_apakah_upper = salam.isupper() ; print("Tipe data :", type(crosscheck_salam_apakah_upper))
print("Apakah penulisan salam dalam format lowercase ?" + str(crosscheck_salam_apakah_lower))
print("Apakah penulisan salam dalam format uppercase? ", crosscheck_salam_apakah_upper)

#Pengecekan huruf, numerik, huruf dan numerik, title, spasi, tab, newline, 
"""
isalpha()   -> untuk memeriksa huruf saja
isalnum()   -> untuk memeriksa huruf dan numerik
isdecimal() -> untuk memeriksa numerik saja
isspace()   -> untuk memeriksa spasi, tab, newline,dsb...
istitle()   -> untuk memeriksa semua kata diawali dengan kapital layaknya judul.

"""

judul = 'It Is Okay Not To Be Orkay'
cek_judul = judul.istitle() ; print('Tipe data yang dihasilkan istitle() : ', type(cek_judul))
cek_huruf = judul.isalpha() ; print("Tipe data yang dihasilkan isalpha() : ", type(cek_huruf))
cek_alnum = judul.isalnum() ; print("Tipe data alnum() :", type(cek_alnum))
cek_spasi = judul.isspace() ; print("Tipe data isspace() :", type(cek_spasi))


print("Apakah penulisan judul sudah benar ? " + str(cek_judul))
print("Apakah judul ditulis dengan menggunakan huruf semua ? " + str(cek_huruf))
print("Apakah judul dituliskan dengan menggunakan huruf dan angka ? " + str(cek_alnum))
print("Apakah judul menggunakan spasi ? " + str(cek_spasi))


# #Pengecekan komponen startswith() dan endswith()
# nama = "Mohamad Abdillah"
# cek_startswith = nama.startswith(str(input("cek nama awal : ")))
# cek_endswith   = nama.endswith(str(input("cek nama akhir :")))
# print("Apakah nama awal beliau ? " + str(cek_startswith))
# print("Apakah nama akhiran beliau ? " + str(cek_endswith)) 

# Penggabungan komponen join() split() 
pisah    = ['Aku', 'sayang', 'kamu']
gabungan = ','.join(pisah) #btw ini penulisannya gw ringkas
print("list bertipe : ", type(pisah)) #class 'list'
print("method join bertipe : ", type(gabungan)) #class 'string'

gabungan = " ehm ".join(pisah) ; print(gabungan)

kalimat = "aku ehm sayang ehm kamu" 
convert_menjadi_list = kalimat.split(' ehm ')
print("sekarang, kalimat terkonversi menjadi list : ", convert_menjadi_list)


#alokasi karakter rjust(), ljust(), center()
rata_kanan = "kanan".rjust(10) #ini penulisannya gw ringkas. btw  class : str
print("|",rata_kanan,"|") ; print("\nbedakan dengan : ", "|"+rata_kanan+"|")

rata_kiri = "kiri"
left_just = rata_kiri.ljust(20) #ini penulisannya gw jabarin.
print("|"+left_just+"|")

rata_tengah = "tengah"
center_just = rata_tengah.center(10)
print("|"+center_just+"|")
center_just = rata_tengah.center(20)
print("\nbedakan dengan","|"+center_just+"|")
"Kalau yang rata tengah, value yang diinput akan dibagi dua, kanan dan kiri."
center_just = rata_tengah.center(20, ":") #kita bisa menambahkan argumen untuk mengisi kekosongan.
print(center_just)

print("=========delete==========") # strip()
print("menghapus space  kiri dari rata kanan : ",rata_kanan.strip())
print("menghapus space kanan dari rata kiri  : ",left_just.strip())
print("menghapus space dari rata tengah      : ",center_just.strip(":"))
"""Perhatikan bahwa argumen langsung terhapus semuanya,
sehingga semua method format justifying beserta argumennya terhapus."""


# Format String (TITLE)
"""
Sejauh ini, string yang telah kita pelajari meliputi kaidah penulisan,
operasi string, dan terakhir methods yang ada di string. 
Pada output operator, bahkan methods string sekalipun, menghasilkan output
dengan tipe data selain string. Hal ini tentu saja membuat kita melakukan
langkah berikutnya, yakni casting tipe data menjadi string juga sehingga
dapat di-running secara keseluruhan sebagai class string.

Pada kali ini(Format String), kita akan mempelajari format string untuk
memudahkan penulisan string.
"""
#contoh generic

#string
nama = 'alex'
format_str = f"Hello {nama}" #Tidak perlu casting ke str lagi
print(format_str)

#Boolean
boolean = True
format_bool = f"Boolean : {boolean}"
print(boolean)

#Numerik
angka = 250.5
format_num = f"Hello {angka}" #Tidak perlu casting ke str lagi 
print(format_num)

#int / bilangan bulat
int = 255
format_int = f"Bilangan bulat sebesar : {int:d}" # d untuk penanda bilangan bulat.
print(format_int) #sukses

# angka = 250.5 ; format_angka = f"Nilai : {angka:d}"
# print(format_angka) #Eror, karena inputnya float, harusnya int.

# bilangan bulat berorde (orde ribuan, jutaan, miliyaran, triliun, dst...)
ribuan = 5000
format_ribuan = f"Lima ribu : {ribuan:,}"
print(format_ribuan)

jutaan = 5755000
format_jutaan = f"Berapa juta uangku : {jutaan:,}"
print(format_jutaan)

#Pembatasan jumlah angka di belakang koma
angka_desimal = 575.5757575
format_angka_desimal = f"dua angka penting : {angka_desimal:.2f}"
print(format_angka_desimal)

#Leading Zero
format_angka_leading = f"leading 1 angka   : {angka_desimal:7.2f}"
print(format_angka_leading)
format_angka_leading = f"Leading 1 angka   : {angka_desimal:07.2f}"
print(format_angka_leading) #sukses

#Menampilkan tanda plus + atau minus -
angka_plus  = 10 ; format_plus = f"plus : {angka_plus:+d}" #d untuk int
angka_minus = -10; format_minus= f"minus: {angka_minus:+d}" #d untuk int
print(format_plus)
print(format_minus)

angka_plus  = 10.35789
angka_minus =-10.35789
format_plus = f"plus : {angka_plus:+.2f}";print(format_plus)
format_minus= f"minus: {angka_minus:+.2f}";print(format_minus)

#format persentase 
angka_persentase = 37.8977
format_angka_persentase = f"persentase nilai : {angka_persentase:.2%}"
print(format_angka_persentase)
angka_persentase_lainnya = 0.75
format_persen_lainnya = f"berapa persen : {angka_persentase_lainnya:.0%}"
print(format_persen_lainnya)

#Melakukan operasi aritmatika di dalam placeholder
harga_persatuan = 5000
ingin_membeli   = 5
format_harga_yang_harus_dibayar = f"harga tagihan =Rp {harga_persatuan*ingin_membeli:,}"
print(format_harga_yang_harus_dibayar)


#format angka lainnya (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal  = f"octal  = {oct(angka)}"
format_hex    = f"hex    = {hex(angka)}"
print(format_binary);print(format_octal);print(format_hex)

"""
Untuk kegunaan format angka sendiri tentunya banyak. 
Misalnya saja format angka hexadecimal digunakan untuk penamaan warna,
selain itu digunakan untuk memprogram pin-pin mikrokontroler seperti
raspbery pi, dan masih banyak lagi.

Btw, untuk rangkuman tutorial kelas terbuka, ada di
GitHub KelasTerbuka .
"""




#Width and Multiline (Title)


data_nama   = "Ucup Surucup"
data_umur   = "17"
data_tinggi = "150.1"
data_sepatu = "44"
print(5*"="+"DATA"+5*"=")
print(f"Data Ucup : {data_nama,data_umur,data_tinggi,data_sepatu}") #string standard
print(f"Data Ucup : {data_nama}, {data_umur}, {data_tinggi},{data_sepatu}") #string standard
print("\n")
print(5*"="+"Multiline"+"="*5)
print(f"Data Ucup : \nnama : {data_nama}, \numur : {data_tinggi}, sepatu : {data_sepatu}") #string multiline 
print("\n")
print(f"""Data Ucup
      nama   : {data_nama}
      umur   : {data_umur}
      tinggi : {data_tinggi}
      sepatu : {data_sepatu}
""") #string multiline

#Perataan kanan atau kiri atau tengah
print(f"""Data Ucup Surucup
      nama   : {data_nama:>12}
      umur   : {data_umur:>12}
      tinggi : {data_tinggi:>12}
      sepatu : {data_sepatu:>12}
      
""")
"pilih data string yang paling banyak karakternya, lalu set perataan kanan/kiri."
"Secara default, data multiline akan menjadi rata kiri."


#Latihan Date and Time (Title)
"Menentukan umur berdasarkan data tanggal kelahiran."

"""Disclaimer
kita bisa menggunakan library sesuai kebutuhan kita di python.org.
Library bisa berupa modul, method, operator, class, atribut, dan lainnya."""
import datetime as dt 

hari_ini  = dt.date.today()
tanggal   = 26
bulan     =  4
tahun     = 2003
kelahiran = dt.date(tahun, bulan, tanggal)
print("birth date Abdill : ", kelahiran,",\n" f"pada hari : {kelahiran:%A}")
print("hari ini          : ", hari_ini,"\n",f"hari : {hari_ini:%A}")

format_umur  = (hari_ini - kelahiran) / 365
print('umur Abdill ;' , format_umur.days, "tahun") #untuk menghilangkan satuan, masukan .satuannya


"Form Umur \nsilakan input data kelahiran Anda di bawah ini."
print(5*"="+"Form Usia"+"="*5)
tanggal_lahir  = int(input("tanggal :"))
bulan_lahir    = int(input("bulan   :"))
tahun_lahir    = int(input("tahun   :"))
data_kelahiran = dt.date(tahun, bulan, tanggal)
print("Anda lahir pada :", data_kelahiran,"\n" f"pada hari : {data_kelahiran:%A}")
print("Usia Anda saat ini adalah :", ((hari_ini-data_kelahiran)/365).days,"tahun")

#Jangan lupa untuk selalu memperhatikan tipe data!




