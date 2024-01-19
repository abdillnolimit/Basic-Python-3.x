#OPERASI ARITMATIKA (TITLE)
print("OPERASI ARITMATIKA")

"""
Tingkatan prioritas operasi matematika
-dalam kurung ()
-eksponen **
-perkalian *, pembagian *, modulus %, floor division //
-pertambahan +, pengurangan -
"""

#Operasi Tambah +
print("=====Operasi Penjumlahan=====")
a = 10
b = 3
c = 5.5
hasil_tambah_a_dan_b = a + b
hasil_tambah_a_dan_c = a + c
hasil_tambah_a_dan_minb = a + (-b)
print("a + b =", hasil_tambah_a_dan_b, "bertipe :", type(hasil_tambah_a_dan_b))

print("a + c =", hasil_tambah_a_dan_c, "bertipe :", type(hasil_tambah_a_dan_c))

print("a+(-b) =", hasil_tambah_a_dan_minb, "bertipe :", type(hasil_tambah_a_dan_minb))

#Operasi Pengurangan -
print("=====Operasi Pengurangan=====")
hasil_pengurangan_a_dan_b     = a - b
hasil_pengurangan_a_dan_c     = a - c
hasil_pengurangan_a_dan_minb = a - (-b)
print("a - b =", hasil_pengurangan_a_dan_b,"bertipe :", type(hasil_pengurangan_a_dan_b))

print("a - c =", hasil_pengurangan_a_dan_c,"bertipe :",type(hasil_pengurangan_a_dan_c))

print("a - (-b)",hasil_pengurangan_a_dan_minb,"bertipe :", type(hasil_pengurangan_a_dan_minb))

#Operasi Perkalian *
print("=====Operasi Perkalian=====")
hasil_perkalian_a_dan_b = a * b
hasil_perkalian_a_dan_c = a * c
hasil_perkalian_a_dan_minb = a * (-b)
print("a x b =", hasil_perkalian_a_dan_b,"bertipe :", type(hasil_perkalian_a_dan_b))
print("a x b =", hasil_perkalian_a_dan_c,"bertipe :", type(hasil_perkalian_a_dan_c))
print("a x b =", hasil_perkalian_a_dan_minb,"bertipe :", type(hasil_perkalian_a_dan_minb))

#Operasi Pembagian /
print("=====Operasi Pembagian=====")
hasil_pembagian_a_dan_b    = a / b
hasil_pembagian_a_dan_c    = a / c
hasil_pembagian_a_dan_minb = a / (-b)
print("a / b =", hasil_pembagian_a_dan_b,"bertipe :", type(hasil_pembagian_a_dan_b))
print("a / b =", hasil_pembagian_a_dan_c,"bertipe :", type(hasil_pembagian_a_dan_c))
print("a / b =", hasil_pembagian_a_dan_minb,"bertipe :", type(hasil_perkalian_a_dan_minb))

#Operasi Eksponen **
print("=====Operasi Eksponen=====")
hasil_eksponen_a_dan_b    = a ** b
hasil_eksponen_a_dan_c    = a ** c
hasil_eksponen_a_dan_minb = a ** (-b)
print("a^b =", hasil_eksponen_a_dan_b,"bertipe :", type(hasil_eksponen_a_dan_b))
print("a^c =", hasil_eksponen_a_dan_c,"bertipe :", type(hasil_eksponen_a_dan_c))
print("a^-b =", hasil_eksponen_a_dan_minb,"bertipe :", type(hasil_eksponen_a_dan_minb))

#Operasi Modulus %
print("=====Operasi Modulus=====")
"Operasi Modulus adalah operasi yang menghitung sisa pembagian."
hasil_modulus_a_dan_b    = a % b
hasil_modulus_a_dan_c    = a % c
hasil_modulus_a_dan_minb = a % (-b)
hasil_modulus_b_dan_a    = b % a

print("a%b =", hasil_modulus_a_dan_b,"bertipe :", type(hasil_modulus_a_dan_b))
print("a%c =", hasil_modulus_a_dan_c,"bertipe :", type(hasil_modulus_a_dan_c))
print("a%-b =", hasil_modulus_a_dan_minb,"bertipe :", type(hasil_modulus_a_dan_minb))
print("b % a =", hasil_modulus_b_dan_a, "bertipe :", type(hasil_modulus_b_dan_a))

"""
misalkan,
11 dibagi 3, maka
11 = 3 x 3 + 2
maka modulusnya adalah 2, floor nya adalah 3.

3 dibagi 10, maka
3 = 10 x 0 + 3
maka modulusnya adalahh 3, floor nya adalah 0.
"""

#Operasi Floor Division (//)
print("=====Operasi Floor Division=====")
hasil_floor_a_dan_b    = a // b
hasil_floor_a_dan_c    = a // c
hasil_floor_a_dan_minb = a // (-b)
hasil_floor_b_dan_a    = b // a
"Operasi Floor Division merupakan kebalikan dari Modulus."

print("a//b =", hasil_floor_a_dan_b,"bertipe :", type(hasil_floor_a_dan_b))
print("a//c =", hasil_floor_a_dan_c,"bertipe :", type(hasil_floor_a_dan_c))
print("a//-b =", hasil_floor_a_dan_minb,"bertipe :", type(hasil_floor_a_dan_minb))
print("b // a =", hasil_floor_b_dan_a, "bertipe :", type(hasil_floor_b_dan_a))

print("=====Latihan=====")
x = 3 ; y = 2 ; z = 4 ;
hasil_operasi = x ** y * z + x / y - y % z // x 
print("x ** y * z + x / y - y % z // x =", hasil_operasi, "bertipe :", type(hasil_operasi))

hasil_operasi_kedua = x ** y * (z + x) / y - y % z // x 
print("x ** y * (z + x) / y - y % z // x =", hasil_operasi_kedua, "bertipe :", type(hasil_operasi_kedua))


#Latihan konversi satuan temperatur C, R, F, K
"""
C = 0-100   : 100 : 5
R = 0-80    : 80  : 4
F = 32-212  : 90  : 9
K = 273-373 : 100 : 5

->C dengan R F K
C =5/4(R)
R =4/5(C)

C = 5/9(F-32)
F = 9/5(C) + 32

C = 5/5(K-273)   = K - 273
K = 5/5(C) + 273 = C + 273

->R dengan F dan K
R = 4/9(F-32)
F = 9/4(R) + 32

R = 4/5(K-273)
K = 5/4(R) + 273

->K dengan F 
(K-273) = 5/9(F-32)
maka K  = 5/9(F-32) + 273

(F-32)  = 9/5(K-273)
maka F  = 9/5(K-273) + 32

"""
print("=====Latihan Konversi Suhu=====")
C = 50
"Tentukan berapa derajat pada termometer satuan R, F, K"
C_ke_R = 4 / 5 * (C)
C_ke_F = 9 / 5 * (C) + 32
C_ke_K = 5 / 5 * (C) + 273
print("===== C dikonversi ke R, F, K =====")
print("C ke R diperoleh :", C_ke_R, "bertipe :", type(C_ke_R))
print("C ke F diperoleh :", C_ke_F, "bertipe :", type(C_ke_F))
print("C ke K diperoleh :", C_ke_K, "bertipe :", type(C_ke_K))

"Setelah memperoleh R,F,dan K, verifikasi bahwa F dan K benar dengan menggunakan data F dan K."
print("===== memverifikasi nilai F dan K =====")
K = 323.0
K_ke_F = 9 / 5 * (K-273) + 32
print("K ke F =", K_ke_F, "bertipe :",type(K_ke_F))
F = K_ke_F #Terbukti benar

F = 122.0
F_ke_K = 5/9 *(F - 32) + 273
print("F ke K =", F_ke_K, "bertipe :",type(F_ke_K))
K = F_ke_K #Terbukti benar


# OPERASI KOMPARASI (TITLE)
"Setiap hasil dari operasi komparasi adalah boolean."

" > , < , == , != , >= , <= , is, is not "

print("=====Latihan Operasi Komparasi=====")
a = 4
b = 2
# Lebih besar serta kurang dari dari > dan <
a_lebihbesar_b = a > b
print("apakah a > b ?", a_lebihbesar_b,"bertipe :", type(a_lebihbesar_b))

a_lebihkecil_b = a < b
print("apakah a < b ?", a_lebihkecil_b, "bertipe :", type(a_lebihkecil_b))

a_lebihbesar_4 = a > 4
print("apakah a > 4 ?", a_lebihbesar_4 , "bertipe :", type(a_lebihbesar_4))

# lebih besar sama dengan serta kurang dari sama dengan >= dan <=
a_lebihbesarsamadengan_4 = a >= 4
print("apakah a lebih besar sama dengan 4 ?", a_lebihbesarsamadengan_4, "bertipe :", type(a_lebihbesarsamadengan_4))

# sama dengan serta tidak sama dengan = dan !=
a_samadengan_4 = a == 4
a_samadengan_b = a == b
a_tidaksamadengan_4 = a != 4 
a_tidaksamadengan_b = a != b
print("apakah a sama dengan 4? ", a_lebihbesar_4, "bertipe :", type(a_lebihbesar_4))
print("apakah a sama dengan b? ", a_samadengan_b, "bertipe :", type(a_samadengan_b))
print("apakah a tidak sama dengan 4 ?", a_tidaksamadengan_4, "bertipe :", type(a_tidaksamadengan_4))
print("apakah a tidak sama dengan b ?", a_tidaksamadengan_b, "bertipe :", type(a_tidaksamadengan_b))

# is dan is not
"""Perlu diketahui sebelumnya bahwa
jika kita menyatakan 
a = 4, kemudian kita menyatakan
a == 4, maka
a ada nilainya, sedangkan 4 adalah literal(tidak memiliki variabel dan tidak tersimpan pada memori).
a memakan memori komputer kita, sedangkan 4 tidak.

apa itu operasi komparasi is?
is adalah operasi komparasi yang membandingkan antara nilai yang memakan memori
atau dengan kata lain is membandingkan memori/objek.
Kita baru akan paham dan sering menggunakan is dan is not ketika kita sedang
belajar menggunakan OOP(Object Orioented Programming)

contoh sederhana pennggunaan operasi komparasi is dan is not
misal kita nyatakan
a = 4
b = 2
c = 4
maka
a is 4 (invalid/salah)
a is C (Valid/benar)
a is not b (valid/benar)

Fun Fact : is dan is not sebelumnya pada python versi di bawah 3.5 
dapat digunakan untuk mengomparasi literal, tetapi sekarang python 
menetapkan is dan is not untuk komparasi objek.
"""

"is dan is not adalah operasi komparasi dan juga bisa digunakan untuk object identity."
x = 5 #ingat sebelumnya bahwa adalah ini bentuk assignment

"""
informasi tambahan,
apabila kita buat bentuk assignment di mode interaktif shell,
misal a = 10,
kita dapat memeriksa address memori id a dengan
id(a)
kita juga dapat memeriksa address memori hex a dengan
hex(id(a))
lalu run di terminal.
Ini merupakan cara yang digunakan pada bahasa C dan C++,
tetapi kita juga dapat melakukannya pada python.
"""
a = 11
b = 11
print("nilai a =",a, "id :", hex(id(a)), ", a bertipe :", type(a))
print("nilai b =",b, "id :", hex(id(b)),", b bertipe :", type(b))
"""
Terbukti bahwa alamat memori a dan b sama.
Pada python, apabila terdapat objek yang sama, maka alamat memori objeknya dijadikan sama.
Oleh karena itu, python menjadi efisien.
Berbeda dengan C/C++, Java, dsb...

"""
hasil = a is b
print("apakah a is b ?", hasil, ",hasil bertipe :", type(hasil))

"Lalu apa yang akan terjadi jika kita bandingkan objek dengan literal?"
result = a is 11
print("apakah a is 1 ?", result, ",result bertipe :", type(result))
"hasilnya ada, tetapi terdapat syntax warning pada terminal."

"""
operasi komparasi == dan != digunakan untuk perangkaan,
sedangkan is dan is not untuk object identity.

operasi komparasi is dan is not akan sangat menyenangkan digunakan
ketika kita sedang melakukan OOP dan juga membuat project OOP hehe."""



#Operasi Logika / Operasi Boolean (TITLE)
"not, or, and, XOR."
"""
Operasi Logika mencakup kaidah-kaidah logika matematika pada umumnya.
Contohnya logika matematika mengenai konjungsi, disjungsi, negasi,
silogisme, beserta konsep diagram venn - nya.
"""

#not (pengeculian/komplemen)
"jumlah input minimal 1."
print("=====Not=====")
q = bool(input("masukan data boolean :")) #input true atau false yaa
b = not q
print("output a :", b)
x = True ; c = not x 
b = False; y = not b
print("komplemen a :", c)
print("komplemen b :", y)

#or (Gabungan)
"Jumlah input minimal 2."
print("=====or=====")
x = True
y = False 
z = x or y 
print("Gabungan a dan b :", z)
x = True
y = True
z = x or y 
print("Gabungan a dan b :", z)
x = False
y = False 
z = x or y 
print("Gabungan a dan b :", z)

#and
print("=====and=====")
x = True
y = False 
z = x and y 
print("Gabungan a dan b :", z)
x = True
y = True
z = x and y 
print("Gabungan a dan b :", z)
x = False
y = False 
z = x and y 
print("Gabungan a dan b :", z)

#xor ^
"pada operasi xor, true ibaratnya tanda minus, sedangkan false plus."
print("=====xor=====")
x = True
y = False 
z = x ^ y 
print("Gabungan a dan b :", z)
x = True
y = True
z = x ^ y 
print("Gabungan a dan b :", z)
x = False
y = False 
z = x ^ y 
print("Gabungan a dan b :", z)

# Lathihan operasi komparasi dan operasi logika (Title)
"latihan penggabungan nilai beberapa himpunan."
a = float(input("gabungan himpunan x dan y \n dengan \n x himpunan nilai kurang dari 3 \n y himpunan nilai lebih dari 10. \ninput :"))
x = a < 3
print("x kurang dari 3 :", x)
y = a > 10
print("a lebih besar dari 10 :", y)

print("maka, gabungannya menjadi")
gabungan = x or y
print("setelah x dan y digabungkan, angka yang anda input :", gabungan,"," "sebagai hasil gabungan x dan y.")


#PR dari kelas terbuka
""" Nomor 1
Buatlah pernyataan yang valid untuk daerah penyelesaian sebagai berikut
-----0+++++5-----8+++++11-----

Nomor 2
Buatlah pernyataan yang valid untuk daerah penyelesaian sebagai berikut
+++++0-----5+++++8-----11+++++
"""
print("=====Jawaban nomor 2=====")
#misal
himpunan_nomor2 = float(input("input untuk <0 , >5, <8, >11, input :"))
p = himpunan_nomor2 < 0
q = himpunan_nomor2 > 5
r = himpunan_nomor2 < 8
s = himpunan_nomor2 > 11
himpunan_penyelesaian_nomor_2 = (p or q) and (r or s)
print("verifikasi input terhadap himpunan penyelesaian :", himpunan_penyelesaian_nomor_2)


print("=====Jawaban nomor 1=====")
#misal
himpunan_nomor1 = float(input("input untuk >0, <5, >8, <11.\n input :"))
a = himpunan_nomor1 > 0
b = himpunan_nomor1 < 5
c = himpunan_nomor1 > 8
d = himpunan_nomor1 < 11
himpunan_penyelesaian_nomor_1 = (a and b) or (c and d)
print("verifikasi input terhadap himpunan penyelesaian :", himpunan_penyelesaian_nomor_1)


# Operasi Bitwise (TITLE)
"""
Operasi bitwise adalah salah satu operasi pada bilangan biner/binary.
Operasi bitwise bekerja dengan cara mengoperasikan masing-masing bit pada
bilangan bilangan biner dari dua atau lebih assignment.
"""
#Konversi integer ke biner dan sebaliknya
"""
Sebelum mempelajari operasi bitwise, ada baiknya jika kita mengetahui terlebih dahulu
cara konversi antara bilangan bulat(integer) dan bilangan biner.
Misalkan,
->15 = 2.7 + 1
7 = 2.3 + 1
3 = 2.1 + 1
1 = 2.0 + 1
maka 15 jika diinterpretasikan ke bilangan biner menjadi = 1111,
artinya 1111 = 1.2^3 + 1.2^2 + 1.2^1 + 2^0 = 8 + 4 + 2 + 1 = 15.

-> 27 =  2.13 + 1
13 = 2.6 + 1
6 = 2.3 + 0
3 = 2.1 + 1
1 = 2.0 + 1
maka 27 jika diinterpretasikan ke bilangan biner menjadi = 11011,
artinya 11011 = 1.2^4 + 1.2^3 + 0.2^2 + 1.2^1 + 1.2^0 = 16 + 8 + 0 + 2 + 1 = 27. 

"""

""" Cara membuat assignment biner
a = 0bbilanganbiner
contoh x = 0b1111 ; y = 0b11011;

cara menginterpretasikan bilangan interger menjadi biner melalui print
a = 15
print("bilangan biner dari a adalah", format(a, '0bykbitb'))
contoh
print("bilangan biner a adalah", format('a, 08b'))
"""
#Operasi or |
print("=====or=====")
a = 9
b = 5
c = 15
print("Bilangan biner a adalah", format(a,'08b'))
print("Bilangan biner b adalah", format(b, '08b'))
print("Bilangan biner c adalah", format(c,'08b'))
print("---------------space----------------------")
"misalkan kita melakukan operasi bitwise or pada a dan b."
d = a | b 
print("Bilangan biner a adalah", format(a,'08b'))
print("Bilangan biner b adalah", format(b, '08b'))
print("---------------------------------\nd = (a or b) =",d, "\nBilangan biner d adalah",format(d,'08b'))





#Operasi and &
print("=====and=====")
d = a & b
print("Bilangan biner a adalah", format(a,'08b'))
print("Bilangan biner b adalah", format(b, '08b'))
print("---------------------------------\nd = (a and b) =",d, "\nBilangan biner d adalah",format(d,'08b'))



#Operasi xor ^
print("=====xor=====")
d = a ^ b 
print("Bilangan biner a adalah", format(a,'08b'))
print("Bilangan biner b adalah", format(b, '08b'))
print("---------------------------------\nd = (a xor b) =",d, "\nBilangan biner d adalah",format(d,'08b'))




#Operasi not ~
print("=====not=====")
d = ~a
print("Bilangan biner a adalah", format(a,'08b'))
print("---------------------------------\nd = (not a) =",d, "\nBilangan biner d adalah",format(d,'08b'))
print("dengan nilai a sendiri adalah", a)
"""
Mirroring yang dilakukan oleh operasi not tidak mengikutsertakan bilangan 0,
tetapi dimulai dari bilangan negatif atau positif pertama.
Pembuktian dapat diilustrasikan dengan garis bilangan matematika.
"""

#Jika ingin membuat flip
print("=====Flip=====")
a = 0b00001001
flip_variable  = 0b11111111
setelah_diflip = a ^ flip_variable
print("Bilangan biner a :", format(a,'08b'))
print("Setelah di-flip  :", format(setelah_diflip,'08b'))
"Kegunaanya apa? yaa lihat saja nanti, suatu saat mungkin perlu."

#shifting right >> (Menggeser ke kanan)
print("=====shifting right=====")
x = 0b00010010
flip_x_duakali = x >> 2
flip_x_sekali  = x >> 1
print("------------->>")
print("Bilangan biner variabel x            =", format(x,'08b'))
print("Bilangan biner x shift right 2 kali  =", format(flip_x_duakali,'08b'))
print("jika digeser 1 kali ke kanan menjadi =", format(flip_x_sekali,'08b'))


#Shifting left << (Menggeser ke kiri)
print("=====shift left=====")
flip_x_duakali = x << 2
flip_x_sekali  = x << 1

print("------------->>")

print("Bilangan biner variabel x            =", format(x,'08b'))
print("Bilangan biner x shift right 2 kali  =", format(flip_x_duakali,'08b'))
print("jika digeser 1 kali ke kanan menjadi =", format(flip_x_sekali,'08b'))



#Operator Assignment (Title)
"""
Operator assignment yang dimaksud di sini sebenarnya hanya prosedur penulisan
agar lebih singkat saja, dengan cara langsung menggabungkan dengan assignment.
"""

#tambah +
print("=====Penambahan=====")
a = 9 ; print("a =", a)
b = 5 ; print("b =", b)
a += b
print("a + b =", a)

#kurang -
print("=====pengurangan=====")
a = 9
b = 5
a -= b
print("a - b =", a)

#Perkalian *
print("=====Perkalian=====")
a = 9
b = 5
a *= b
print("a * b =", a)

#Pembagian /
print("=====Pembagian=====")
a = 9
b = 5
a /= b 
print("a / b =", a)

#Eksponen ** 
print("=====Eksponen=====")
a = 9
b = 5
a **= b 
print("a ** b =", a)

#Modulus %
print("=====Modulus=====")
a = 9
b = 5
a %= b 
print("a % b =", a)

#Floor Division //
print("=====Floor Division=====")
a = 9
b = 5
a //= b
print("a // b =", a)

print("==========Operasi Bitwise ===========")

#or |
print("=====or=====")
a = True
a |= False 
print("a or false =", a)

#and &
print("=====and=====")
a = True
a &= False
print("a and false =", a)

#xor ^
print("=====xor=====")
a = True
a ^= False
print("a xor false =", a)

#not ~ (TIDAK ADA !)
print("=====not=====")
a = True
x = ~a
print(" ~a =", x)
"kwkwkwwk ini cuma ngide."

#geser kanan >>
print("=====geser kanan=====")
a = 0b00110011
print("Bilangan biner a =", format(a,'08b'))
a >>= 2 ; print("geser 2 kali =", format(a,'08b'),", dengan nilai =", a)
a = 0b00110011
a >>= 1 ; print("geser 1 kali =", format(a,'08b'), ", dengan nilai =", a)


#geser kiri <<
print("=====geser kiri=====")
a = 0b00110011
print("Bilangan biner a =", format(a,'08b'))
a <<= 2 ; print("geser 2 kali =", format(a,'08b'),", dengan nilai =", a)
a = 0b00110011
a <<= 1 ; print("geser 1 kali =", format(a,'08b'), ", dengan nilai =", a)














