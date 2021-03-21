import sys
import numpy as np
import emoji

anggota_kelompok = [["1","MARIA TESSA KARTINI SIRAIT","50420702","1IA07","PEREMPUAN"]
                    ,["2","MOCHAMMAD HUSNI THAMRIN","50420725","1IA07","LAKI-LAKI"]
                    ,["3","MOCHAMMAD YUSUF SIREGAR","50420730","1IA07","LAKI-LAKI"]
                    ,["4","MUHAMMAD ABDUH TRI DIRNA","50420775","1IA07","LAKI-LAKI"]
                    ,["5","MUHAMMAD FADHLAN AQILA","50420816","1IA07","LAKI-LAKI"]
                    ,["6","MUHAMMAD HAFIDZ NURROHMAN","50420844","1IA07","LAKI-LAKI"]
                       ,["7","MUHAMMAD IKBAR ADANI","50420852","1IA07","LAKI-LAKI"]]


def caridata():
    a = True
    while(a):
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("   SELAMAT DATANG DI DATALIST MAHASISWA   ")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("    ")
        print("    1. MARIA TESSA")
        print("    2. THAMRIN")
        print("    3. YUSUF")
        print("    4. ABDUH")
        print("    5. FADHLAN")
        print("    6. HAFIDZ")
        print("    7. IKBAR")
        print("    8. BACK ")
        print()
        print("  Jika ingin mengetahui data lebih detail anda bisa mencari tau dengan mengetik nomor 1-7 \n")
        azz = True
        while (azz):
            input1 = input("  Masukkan nomor urutan nama anggota yang ingin anda cari : ")
            a = int(input1) - 1
            if (a == 0 or a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6 ):
                print()
                print("  Nomor Absen   : " + anggota_kelompok[a][0])
                print("  Nama          : " + anggota_kelompok[a][1])
                print("  NPM           : " + anggota_kelompok[a][2])
                print("  Kelas         : " + anggota_kelompok[a][3])
                print("  Jenis-Kelamin : " + anggota_kelompok[a][4])
                azz = False
            elif (a == 7):
                home()
                azz = False
            else:
                print("Masukkan Inputan yang benar")


        print()
        print(" Jika ingin exit program ketik ya, jika ingin mencari data lagi ketik tidak")
        input2 = input(" Ingin exit program (ya/tidak)? ")
        if (input2 == 'ya' or input2 == 'YA' or input2 == 'iya'):
            sys.exit(0)
        else:
            a = True


def hapusdata():
    b = True
    while (b):
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("   SELAMAT DATANG DI DATALIST MAHASISWA   ")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("    ")
        print("    1. MARIA TESSA")
        print("    2. THAMRIN")
        print("    3. YUSUF")
        print("    4. ABDUH")
        print("    5. FADHLAN")
        print("    6. HAFIDZ")
        print("    7. IKBAR")
        print("    8. BACK")
        print()
        print("  Jika ingin menghapus data pilih data dari salah satu nomor 1-7 ")
        input1 = input("  Masukkan nomor urutan nama anggota yang ingin anda hapus : ")
        a = int(input1) - 1
        print()

        if (a == 0 or a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6):
            del anggota_kelompok[a]

            for i in anggota_kelompok:
                for z in i:
                    print("  "+z,end= " ")
                print()
        elif (a == 7):
            home()
        else:
            b = True
        print()
        print(" Jika ingin exit program ketik ya, jika ingin mencari data lagi ketik tidak")
        input2 = input(" Ingin exit program (ya/tidak)? ")

        if (input2 == 'ya' or input2 == 'YA' or input2 == 'IYA'):
            sys.exit(0)
        else:
            b = True

def tambahdata():
    b = True
    while (b):
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("   SELAMAT DATANG DI DATALIST MAHASISWA   ")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("    DATA TERSEDIA ")
        print("    1. MARIA TESSA")
        print("    2. THAMRIN")
        print("    3. YUSUF")
        print("    4. ABDUH")
        print("    5. FADHLAN")
        print("    6. HAFIDZ")
        print("    7. IKBAR")
        print("  ========================================")
        print("  Jika ingin menambah data ketik ya, Jika tidak ingin meambah data ketik tidak nanti kembali ke home")
        input1 = input("  Ingin menambah data (ya/tidak)? ")
        if (input1 == "ya" or input1 == 'YA'):
            print("  Format isi data NO , NAMA , NPM , KELAS , JENIS KELAMIN ")
            nomorulang = True
            while (nomorulang):
                inputno = input("  Masuk Nomor Urut : ")
                if (inputno > "7"):
                    inputnama = input("  Masukkan Nama  : ")
                    inputnpm = input("  Masukkan NPM : ")
                    inputkelas = input("  Masukkan Kelas : ")
                    inputjk = input("  Masukkan Jenis Kelamin (LAKI - LAKI/PEREMPUAN) : ")
                    anggota_kelompok.append([inputno,inputnama,inputnpm,inputkelas,inputjk])
                    print(" LIST DATA TERBARU")
                    print(np.matrix(anggota_kelompok))
                    nomorulang = False
                else :
                    print( "  Nomor urut sudah terisi silahkan cek list data !! ")
        elif (input1 == 'tidak' or input1 == 'TIDAK'):
            home()
        else :
            print()
            print("Inputan tidak diketahui silahkan ulang lagi")
            tambahdata()

        print()
        print(" Jika ingin exit program ketik ya, jika ingin mencari data lagi ketik tidak")
        input2 = input(" Ingin exit program (ya/tidak)? ")

        if (input2 == 'ya' or input2 == 'YA' or input2 == 'IYA'):
            sys.exit(0)
        else:
            b = True

def editdata():
    b = True
    while (b):
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("   SELAMAT DATANG DI DATALIST MAHASISWA   ")
        print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
        print("    DATA TERSEDIA ")
        print("    1. MARIA TESSA")
        print("    2. THAMRIN")
        print("    3. YUSUF")
        print("    4. ABDUH")
        print("    5. FADHLAN")
        print("    6. HAFIDZ")
        print("    7. IKBAR")
        print("    8. BACK")
        print("  ========================================")
        print("  Jika ingin mengedit data pilih data dari salah satu nomor 1-7 \n")
        input1 = int(input("  Masukkan nomor urutan nama anggota yang ingin anda edit : "))
        a = int(input1) - 1
        if (a == 0 or a == 1 or a == 2 or a == 3 or a == 4 or a == 5 or a == 6):
            print("  Nomor Urut    : " + anggota_kelompok[a][0])
            print("  Nama          : " + anggota_kelompok[a][1])
            print("  NPM           : " + anggota_kelompok[a][2])
            print("  Kelas         : " + anggota_kelompok[a][3])
            print("  Jenis-Kelamin : " + anggota_kelompok[a][4])
            print()

            yakinnorut = input("  Edit Nomor urut (ya/tidak) ? ")
            if (yakinnorut == 'ya'or yakinnorut == 'YA'):
                inputnorut = input("  Masukkan nomor urut yang terbaru : ")
                anggota_kelompok[a][0] = inputnorut
            yakinnama = input("  Edit Nama (ya/tidak) ? ")
            if (yakinnama == 'ya' or yakinnama == 'YA'):
                inputnama = input("  Masukkan nama yang terbaru : ")
                anggota_kelompok[a][1] = inputnama
            yakinnpm = input("  Edit NPM (ya/tidak) ? ")
            if (yakinnpm == 'ya'or yakinnpm == 'YA'):
                inputnpm = input("  Masukkan NPM yang terbaru : ")
                anggota_kelompok[a][2] = inputnpm
            yakinkelas = input("  Edit Kelas (ya/tidak) ? ")
            if (yakinkelas == 'ya' or yakinkelas == 'YA'):
                inputkelas = input("  Masukkan Kelas yang terbaru : ")
                anggota_kelompok[a][3] = inputkelas
            yakinkelamin = input("  Edit Jenis Kelamin (ya/tidak) ? ")
            if (yakinkelamin == 'ya' or yakinkelamin == 'YA'):
                inputkelamin = input("  Masukkan Jenis Kelamin terbaru : ")
                anggota_kelompok[a][4] = inputkelamin
            print()
            print("  Data Terupdate ! ")
            print()
            print("  Nomor Urut    : " + anggota_kelompok[a][0])
            print("  Nama          : " + anggota_kelompok[a][1])
            print("  NPM           : " + anggota_kelompok[a][2])
            print("  Kelas         : " + anggota_kelompok[a][3])
            print("  Jenis-Kelamin : " + anggota_kelompok[a][4])
            print()

            print(" Jika ingin exit program ketik ya, jika ingin mencari data lagi ketik tidak")
            input2 = input(" Ingin exit program (ya/tidak)? ")

            if (input2 == 'ya' or input2 == 'YA' or input2 == 'IYA'):
                sys.exit(0)
            else:
                b = True

        elif (a == 7):
            home()
        else:
            print("Input kamu salah !!!! Silahkan Coba lagi")
            b = True



def home():
    print("""$$\   $$\ $$$$$$$$\ $$\       $$$$$$\  $$\      $$\ $$$$$$$\   $$$$$$\  $$\   $$\       $$\   $$\ 
$$ | $$  |$$  _____|$$ |     $$  __$$\ $$$\    $$$ |$$  __$$\ $$  __$$\ $$ | $$  |      $$ |  $$ |
$$ |$$  / $$ |      $$ |     $$ /  $$ |$$$$\  $$$$ |$$ |  $$ |$$ /  $$ |$$ |$$  /       $$ |  $$ |
$$$$$  /  $$$$$\    $$ |     $$ |  $$ |$$\$$\$$ $$ |$$$$$$$  |$$ |  $$ |$$$$$  /        $$$$$$$$ |
$$  $$<   $$  __|   $$ |     $$ |  $$ |$$ \$$$  $$ |$$  ____/ $$ |  $$ |$$  $$<         \_____$$ |
$$ |\$$\  $$ |      $$ |     $$ |  $$ |$$ |\$  /$$ |$$ |      $$ |  $$ |$$ |\$$\              $$ |
$$ | \$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$  |$$ | \_/ $$ |$$ |       $$$$$$  |$$ | \$$\             $$ |
\__|  \__|\________|\________|\______/ \__|     \__|\__|       \______/ \__|  \__|            \__|
                                                                                                  """)

    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("   SELAMAT DATANG DI DATALIST MAHASISWA   ")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ")
    print("   ~ Urutan Tools Data ")
    print("    1. CARI DATA")
    print("    2. HAPUS DATA")
    print("    3. TAMBAH DATA")
    print("    4. EDIT DATA")
    print("    5. EXIT PROGRAM")

    print("  Cari dengan mengetik nomor 1-5 \n")
    x = True
    while (x):
        input1 = int(input("  Masukkan nomor urutan yang ingin anda cari : "))
        if input1 == 1:
            caridata()
            x = False
        elif input1 == 2:
            hapusdata()
            x = False
        elif input1 == 3:
            tambahdata()
            x = False
        elif input1 == 4:
            editdata()
            x = False
        elif input1 == 5:
            print()
            print(emoji.emojize('  Sampai Jumpa Kembali :smiling_face_with_smiling_eyes:'))
            sys.exit(0)
        else:
            print("  Pilihan kamu tidak diketahui !! Silahkan Coba Lagi")




if __name__ == '__main__':
    home()












