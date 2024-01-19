"""Modul operasi matematika sederhana"""
def add(*args)  :
    print(f"Operasi pertambahan 2 bilangan secara sederhana")
    a = float(input("masukkan angka pertama = "))
    angka = float(input("masukkan angka kedua = "))
    angka+a
    print(f"Hasil {a} + {angka} = {angka+a} ")

def times(x,y)->float :
    return x*y