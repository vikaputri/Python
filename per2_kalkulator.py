def tambah(x, y):
   return x + y

def kurang(x, y):
   return x - y

def kali(x, y):
   return x * y

def bagi(x, y):
   return x / y

print("PROGRAM KALKULATOR SEDERHANA")
print("")
print("Pilih Operasi")
print("1.Jumlah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")

print("")
pil = input("Masukkan pilihan(1/2/3/4): ")
print("")
num1 = int(input("Masukkan bilangan pertama : "))
num2 = int(input("Masukkan bilangan kedua   : "))

if pil== '1':
   print(num1,"+",num2,"=", tambah(num1,num2))

elif pil == '2':
   print(num1,"-",num2,"=", kurang(num1,num2))

elif pil == '3':
   print(num1,"*",num2,"=", kali(num1,num2))

elif pil == '4':
   print(num1,"/",num2,"=", bagi(num1,num2))
else:
   print("Pilihan Tidak Ada")
