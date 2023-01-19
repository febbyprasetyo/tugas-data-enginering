i = 0
while True:
    print("====== ROGRAM ENTRY MATAKULIAH =====")
    print("====================================")
    matkul = input("Masukkan Nama Matakuliah Anda : ")
    tugas  = int(input("Masukkan Nilai Tugas Anda : "))
    uts    = int(input("Masukkan Nilai UTS Anda   : "))
    uas    = int(input("Masukkan Nilai UAS Anda   : "))
    
    print("====================================")
    print("====== NILAI AKHIR MAHASISWA ======)")
    angka = float(tugas * 30) / 100 + float(uts * 30) / 100 + float(uas * 40) / 100
    print("Nama Matakuliah : " + str(matkul))
    print("Nilai Tugas     : " + str(tugas))
    print("Nilai UTS       : " + str(uts))
    print("Nilai UAS       : " + str(uas))
    print("Nilai Angka     : " + str(angka))
    if angka >= 80:
        print("Nilai Huruf A")
    else:
        if angka >= 60:
            print("Nilai Huruf B")
        else:
            if angka >= 40:
                print("Nilai Huruf C")
            else:
                if angka <= 20:
                    print("Nilai Huruf D")
                else:
                    print("Nilai Huruf E")

    lagi = ""
    while lagi != 'y' and lagi != 't':
        lagi = input("Apakah Entry Lagi [y/t] : ")
    i += 1
    if lagi =='t':
        break


