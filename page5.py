# #Lanjutan Array page 4 !!!




# #Tuple dan Set (TITLE)
# """
# Tuple adalah salah satu dari tipe collection. List juga termasuk.
# Perbedaannya dengan list, elemen-elemen yang ada pada variabel tuple
# tidak bisa diubah-ubah oleh user seperti pada list.
# Tuple banyak digunakan pada machine learning, data sciences, dsb...

# """
# print("\n", "="*5,"Tuple","="*5)
# caramenulis_data_tuple = (1,2,5,3,6,4)
# print(f"menulis data tuple : {caramenulis_data_tuple}")
# print(f"Apakah data tuple dapat memanggil index elemennya? {caramenulis_data_tuple[0]}")
# "Bisa"
# # caramenulis_data_tuple[1] = "bedill"
# # print(f"apakah bisa diubah elemennya? {caramenulis_data_tuple}")
# # "Terbukti bahwa tuple doesn't support it"

# # caramenulis_data_tuple.append("cecep")
# # print(f"apakah bisa menambahkan item pada data tuple? {caramenulis_data_tuple}")
# # "Terbukti bahwa tuple doesn't support it"



# #Set (Himpunan)
# print("\n", "="*5,"Set","="*5)
# "Set bahkan tidak dapat kita gali informasi elemennya sama sekali, berbeda jauh dengan list"
# data_set = {1,2,3,4,5}
# print(f"Data set : {data_set}")
# # print(f"elemen pertama pada data set adalah : {data_set[0]}")
# # "Terbukti tidak bisa."



# #Dictionary (TITLE)
# """Apa itu dictionary?
# dictionary adalah associative array. Pada python, kita perlu memandang dictionary
# secara khusus. Dictionary adalah salah satu collection yang powerfull pada python.

# Dictionary sangat berguna jika kita membicarakan struktur data, dsb...



# Jika pada list kita menggunakan indeks, maka
# pada dictionary kita menggunakan identifier bernama key.

# list -> indeks
# dictionary -> identifier (key , value)
# """


# list_sajah = [1,3,2,4,3]

# #Menulis dictionary
# print("\n\n=====Menulis Dictionary=====")
# caramenulis_dict = {
#     'key 1' : 'value 1',
#     'key 2' : 'value 2',
#     'list sajah' : list_sajah,
# }

# print(f"cara menulis dictionary : {caramenulis_dict}")

# """Pada dictionary, elemen dapat diakses seperti list. 
# sama seperti list juga, pada dictionary kita dapat menginput elemennya
# berupa number, string, boolean, list, dsb... sesuai dengan dimensi yang kita mau.
# """

# #memanggil elemen
# print(f"memanggil value 1 : {caramenulis_dict['key 1']}")
# print(f"memanggil value 2 : {caramenulis_dict['key 2']}")
# print(f"memanggil list sajah ckck : {caramenulis_dict['list sajah']}")


# # Operasi Dictionary (TITLE)
# print("=====Operasi dan Manipulasi Dictionary=====")
# "Operasi pada dictionary sebagian besar mirip dengan List. Apabila menemukan perbedaan, santai sajah.."
# list_operasi = [2,4,5]
# data_dict = {
#     "cp"  : "ucup",
#     "dang": "dadang",
#     "tong": "otong"
    
# } #eror solved : gaboleh ngasih apapun line ini kecuali komen yang menggunakan tanda pagar #
# "penulisan kutib 2 atau 1 pada key dan value harus konsisten"

# "Panjang dictionary"
# print(f"\n=====panjang dictionary=====")
# lendict = len(data_dict) #Jika penamaan variabel menyebabkan konstan, gunakanlah uppercase
# print(f"Panjang data_dict adalah = {lendict}")

# "Memeriksa key exsisting or not"
# print("\n=====checking key exist=====")
# key = 'dang' #menggunakan tanda kutib 1 atau 2 juga bisa
# checkkey = key in data_dict #cara check keberadaan data
# print(f"apakah {key} sebagai key di data_dict ? {checkkey}")

# #Mengakses value(read) dengan get
# print(data_dict['dang']) #menggunakan tanda kutib 1 atau 2 bebas.
# print(data_dict.get('cp')) #cara ini dan atas sama aja.
# print(data_dict.get('anjay')) #key anjay tidak existed di data_dict
# print(data_dict.get('anjay', 'anjay tidak ditemukan')) #cara ini untuk memberi keterangan tambahan


# #mengupdate data
# data_dict["cp"] = "cupu" ; print(data_dict) #mengupdate value

# data_dict.update({'anjay' : 'gurinjay'}) # jika tidak ada di dict, maka otomatis ditambahkan ke posisi paling akhir
# data_dict.update({'tong' : "tongseng"}) #jika ada, akan diubah sesuai perintah paling barunya.
# print(f"\ndata dict setelah di-update : \n{data_dict}\n")

# #meremove data
# del data_dict['anjay']
# print(f"\n data_dict setelah key 'anjay' dihapus : {data_dict}")


# #Looping Dictionary (TITLE)
# teman_teman = {
#     'cup' : "ucup surucup",
#     'tong': "otong surotong",
#     'dung': "dudung surudung",
#     'sep' : "asep si kasyep",
#     'cuy' : "ucuy surucuy"
# }

# #Looping key
# for kawan in teman_teman:
#     print(f"kawan-kawanku : {kawan}") #yang printed hanya key saja
# """
# ini terjadi karena Loop tidak tahu secara spesifik identifier kawan in teman_teman
# apakah collection list, tuple, set. Oleh sebab itu, kita harus menambahkan method terlebih dahulu
# untuk memanggil key ataupun value atau bahkan duaduanya.
# """

# #Method untuk mengambil item/iterable

# "mengambil key"
# print(f"=====Mengambil key saja=====")
# keys = teman_teman.keys()
# print(f"\n{keys}")
# for key in keys :
#     print("key :", key) #mengambil key saja
#     print("value :", teman_teman.get(key)) #mengambil value saja

# "mengambil value"
# print(f"\n=====mengambil value saja=====")
# value = teman_teman.values()
# print(value)
# for value in teman_teman.values():
#     print(f"value : {value}")
    
# "mengambil item(key dan value)"
# print(f"\n=====mengambil items=====")
# item = teman_teman.items() #method ini terdiri atas identifier key dan value untuk Looping
# print(item)
# for item in teman_teman.items() :
#     print(f"item : {item}")

# print(f"\natau\n")

# for key,value in teman_teman.items() :
#     print(f"key : {key}, value : {value}")




# # Copy Dictionary dan pop dictionary
# print(f"\n=====Copy Dictionary=====")
# """Sama seperti list,

# Pada dictionary, apabila kita ingin menduplikat sebuah variabel data dictionary,
# maka kita harus memisahkan address variabel asal dengan copied variabel dengan
# menggunakan method copy pada variabelnya. Ini bertujuan supaya data dictionary
# variabel awal tidak mengalami perubahan yang sama akibat perubahan pada copied variabel.
# """

# teman_teman = {
#     'cup' : "ucup surucup",
#     'tong': "otong surotong",
#     'dung': "dudung surudung",
#     'sep' : "asep si kasyep",
#     'cuy' : "ucuy surucuy"
# }

# print(f"data dictionary teman-teman awal : \n{teman_teman}\nmemiliki address : {hex(id(teman_teman))}\n")

# friends = teman_teman.copy()
# print(f"\nfriends : {friends}\n memiliki address : {hex(id(friends))}")

# friends['cup'] = "ucup ganteng" ; print(f"\nfriends updated ucup : {friends}")
 
# #method pop (mentransfer sebuah item / meremove sebuah dari ke variabel pop)
# data_asep = friends.pop('sep') ; print(f"\ndata asep : {data_asep}\n")
# print(f"data teman-teman setelah pop 'sep' : {teman_teman}\n")
# print(f"data friends setelah pop 'sep' : {friends}\n")


# #method popitem (mengambil yang terakhir saja)
# "sama seperti pop, pop item mentransfer item paling akhir."
# print(f"\ndata friends saat ini : {friends}\n")
# data_terakhir = friends.popitem()
# print(f"data terakhir : {data_terakhir}\n")
# print(f"data friends setelah di-popitem : {friends}\n")




# # Multikeys & Nesting Dictionary (TITLE)

# import datetime

# mahasiswa1 = {
#     'nama' : 'Ucup Surucup',
#     'nim'  : '19022001',
#     'sks_lulus' : 130,
#     'beasiswa' : False,
#     'lahir' : datetime.datetime(2001,4,10)

# }

# mahasiswa2 = {
#     'nama' : 'Otong Surotong',
#     'nim'  : '19022002',
#     'sks_lulus' : 140,
#     'beasiswa' : True,
#     'lahir' : datetime.datetime(2002,10,10)

# }
# mahasiswa3 = {
#     'nama' : 'Asep Si Kasyep',
#     'nim'  : '19022003',
#     'sks_lulus' : 100,
#     'beasiswa' : False,
#     'lahir' : datetime.datetime(2000,2,29)

# }

# data_mahasiswa = {
#     'MAH001' : mahasiswa1,
#     'MAH002' : mahasiswa2,
#     'MAH003' : mahasiswa3,

# }

# "Misal kita buat database. Dengan melakukan format perataan kiri."

# print(f"{'KEY':<6} {'NAMA':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")

# """Remind
# :< rata kiri
# :> rata kanan
# :^ center/rata tengah"""

# print("-"*50)

# for mahasiswa in data_mahasiswa :
#     KEY = mahasiswa 

#     NAMA = data_mahasiswa[KEY]['nama']
#     NIM  = data_mahasiswa[KEY]['nim']
#     SKS  = data_mahasiswa[KEY]['sks_lulus']
#     BEASISWA = data_mahasiswa[KEY]['beasiswa']
#     LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

#     print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")



#Latihan Dictionary (TITLE)
'ada yang baru : fromkeys'

'''Program data mahasiswa menggunakan dictionary'''
import datetime
import os
import string
import random

# template dict mahasiswa
mahasiswa_template = {
	'nama':'nama',
	'nim':'00000000',
	'sks_lulus':0,
	'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
	# os.system("cls") # untuk windows
	os.system("clear")
	print(f"{'SELAMAT DATANG':^20}")
	print(f"{'DATA MAHASISWA':^20}")
	print("-"*20)

	mahasiswa = dict.fromkeys(mahasiswa_template.keys())
	mahasiswa['nama'] = input("Nama Mahasiswa: ")
	mahasiswa['nim'] = input("NIM Mahasiswa: ")
	mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
	TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
	BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
	TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
	mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

	KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
	data_mahasiswa.update({KEY:mahasiswa})

	# dari tutorial sebelumnya, hilangkan beasiswa
	print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
	print('-'*60)

	for mahasiswa in data_mahasiswa:
		KEY = mahasiswa
		
		NAMA = data_mahasiswa[KEY]['nama']
		NIM = data_mahasiswa[KEY]['nim']
		SKS = data_mahasiswa[KEY]['sks_lulus']
		LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
		
		print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

	print("\n")
	is_done = input("Mau tambah lagi bro (y/n)? ")
	if is_done == "n":
		break

print("\nAkhir dari program, terima kasih")


























