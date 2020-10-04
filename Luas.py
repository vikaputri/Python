def menu():
    print "Menu"
    print "1. Keliling"
    print "2. Luas"
    print "3. Volume"
    pil = input("Masukkan Pilihan Anda : ")
    print
    if pil == 1:
        keliling()
    elif pil == 2:
        luas()
    elif pil == 3:
        volume()
    else:
        ulang()
def luas():
    l = 6*(s**2)
    print "Luas Kubus adalah ",l
def volume():
    v = s**3
    print "Volume Kubus adalah ",v
def keliling():
    k = s * 12
    print "Keliling Kubus adalah ",k
def ulang():
    print
    print "Mau ulang lagi [Y/N]?"
    mau = raw_input("Masukkan Pilihan Anda : ")
    if mau == "Y":
        menu()
    else:
        exit()


print 'Program Keliling, Luas, dan Volume Kubus'
print
s = input("Masukkan Panjang Sisi Kubus : ")
print
menu()


        
