# import program.karepmu as awalan 
import csv
import sys
import os
from prettytable import from_csv
# from program.takon_karepmu import*
# import program.karepmu as karepmu
import program.takon_karepmu as takon
import datetime

# menyimpan lokasi direktori file csv kedalam variable
nyilek_csv = 'database/nyilek_sakkarepmu.csv'
perpus_csv = 'database/buku_sakkarepmu.csv'

waktu_saiki = datetime.date.today() # variable waktu yang berisi library date time / waktu
def clear_screen():  # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

# csv_pinjaman = 'database/nyilek_sakkarepmu.csv'
def daftar_peminjam():
    clear_screen()
    print(''' 
 \t\t\t _    _    _     ___           _       _            
  \t\t\t| |  (_)__| |_  | _ \___ _ __ (_)_ _  (_)__ _ _ __  
  \t\t\t| |__| (_-<  _| |  _/ -_) '  \| | ' \ | / _` | '  \ 
 \t\t\t|____|_/__/\__| |_| \___|_|_|_|_|_||_|/ \__,_|_|_|_|
  \t\t\t                                    |__/            ''')
    with open(nyilek_csv, "r") as fp: 
        x = from_csv(fp)
    print(x)
    takon.mbalek_menu()

# def pinjam_buku():
#     clear_screen()
#     buku_sakkarepmu = []
#     with open('database/buku_sakkarepmu.csv', mode="r") as csv_file:
#         csv_file = csv.DictReader(csv_file)
#         # csv_file = csv.reader(csv_file, delimiter='\t')
#         for row in csv_file:
#             buku_sakkarepmu.append(row)
#     # csv_file.close()

#     ketemu = []
#     print(''' 
#     ╔═══════════════╗ [-] kode terdiri dari huruf dan angka
#     ║  pinjam buku  ║ [-] contoh : g-001
#     ╚═══════════════╝ [-] "g" diambil dari huruf terdepan buku dan "001" dari urutan ''')
#     nama_peminjam = input("[-] nama peminjam    : ")
#     nik = input('''[-] masukan nik  : ''')
#     kode_buku = input("[-] kode buku    :  ")
#     # mencari buku_sakkarepmu
#     indeks = 0
    
#     for data in buku_sakkarepmu:
#         if (data['Kode Buku'] == kode_buku):
#             ketemu = buku_sakkarepmu[indeks]
#         indeks = indeks + 1
    
#     if len(ketemu) > 0:
        
#         waktu_saiki = datetime.date.today()
#         # print('''
#         # \t\t\t\t _____           _          _      ___      _        
#         # \t\t\t\t|_   _|_ _ _ __ | |__  __ _| |_   | _ )_  _| |___  _ 
#         # \t\t\t\t  | |/ _` | '  \| '_ \/ _` | ' \  | _ \ || | / / || |
#         # \t\t\t\t  |_|\__,_|_|_|_|_.__/\__,_|_||_| |___/\_,_|_\_\\_,_|''')
#         # with open(perpus_csv, "r") as fp:
#         #     x = from_csv(fp)
#         # print(x)
#         with open('database/nyilek_sakkarepmu.csv', mode='a', newline='') as csv_tod:
#             fieldnames = ['No','Nama Peminjam', 'NIK', 'Kode Buku', 'Judul Buku', 'Tanggal Pinjam', 'Tanggal Pengembalian']
#             writer = csv.DictWriter(csv_tod, fieldnames=fieldnames)
#             print(csv_tod.closed)  # 👉️ False
#         buku_sakkarepmu = []
#         with open('database/nyilek_sakkarepmu.csv', mode="r", newline='') as csv_tod:
#             csv_reader = csv.DictReader(csv_tod)
#             for row in csv_reader:
#                 buku_sakkarepmu.append(row)
#         row_count = sum(1 for row in buku_sakkarepmu) # membaca total row yang ada di csv
#         nomer = row_count + 1 # total row diatas ditambah dengan angka 1 
#         judul_buku = (f'''{ketemu['Judul Buku']}''')
#         print(f'''    [-] pengarang       : {ketemu['Pengarang']}''')
#         print(f'''    [-] penerbit        : {ketemu['Penerbit']}''')
#         print(f'''    [-] jumlah halaman  : {ketemu['Jumlah Halaman']} Halaman''')
#         print(f'''    [-] tahun terbit    : {ketemu['Tahun Terbit']}''')
        
#         tanggal_pengembalian = "belum dikembalikan"
#         tanggal_nyilek = waktu_saiki
        
#         print('''    ╔ [-] tanggal masuk     : ''', tanggal_nyilek.strftime("%d-%m-%Y"))
#         # nyilek_csv.close()  # menutup file
#         csv_tod.close()
#         print(csv_tod.closed)  # 👉️ True
#         writer.writerow(
#             # No,Nama Peminjam,NIK,Kode Buku,Judul Buku,Tanggal Pinjam,Tanggal Pengembalian
#             {'No': nomer, 'Nama Peminjam': nama_peminjam, 'NIK': nik, 'Kode Buku': kode_buku,  'Judul Buku': judul_buku,'Tanggal Pinjam': tanggal_nyilek.strftime("%d-%m-%Y"), 'Tanggal Pengembalian': tanggal_pengembalian})
#         # csv_file.close()
#         print("    ╚ [#] data berhasil ditambahkan!")
#         # nyilek_csv.close()  # menutup file
#     else:
#         print(''' 
#     ╔═════════════╗ input kamu tidak diketahui
#     ║ input salah ║ coba lagi, jalankan ulang
#     ╚═════════════╝ program dan cek kembali ^ ^! ''')
#         takon.pinjam_ulang()
#     takon.mbalek_menu()
    
def pinjam_buku():  # menambahkan data ke csv
    clear_screen()
    # membuat variable " waktu_saiki " isinya pakek library date time
    waktu_saiki = datetime.date.today()
    print('''
  \t\t\t ___ _                              _    _    _     ___      _        
  \t\t\t/ __(_)_ __  ___ _ _ _ __ _  _ ___ | |  (_)__| |_  | _ )_  _| |___  _ 
  \t\t\t\__ \ | '_ \/ -_) '_| '_ \ || (_-< | |__| (_-<  _| | _ \ || | / / || |
  \t\t\t|___/_| .__/\___|_| | .__/\_,_/__/ |____|_/__/\__| |___/\_,_|_\_\\_,_|
 \t\t\t      |_|           |_|                                               ''')
    with open(perpus_csv, "r") as fp: 
        x = from_csv(fp)
    print(x)
    with open(nyilek_csv, mode='a', newline='') as csv_file:
        fieldnames = ['No','Nama Peminjam', 'NIK', 'Kode Buku', 'Judul Buku', 'Tanggal Pinjam', 'Tanggal Pengembalian']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print(''' 
    ╔═══════════════╗ [-] kode terdiri dari huruf dan angka
    ║  tambah buku  ║ [-] contoh : g-001
    ╚═══════════════╝ [-] "g" diambil dari huruf terdepan buku dan "001" dari urutan ''')
        print('''    ╔═══════════════════════════════════╗''')
 # --------------- ini untuk fungsi auto memberi number ------------------------
        buku_sakkarepmu = []
        with open(nyilek_csv, mode="r", newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                buku_sakkarepmu.append(row)
        row_count = sum(1 for row in buku_sakkarepmu) # membaca total row yang ada di csv
        ketemu = []
        buku_sakkarepmu = []

        with open(perpus_csv, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                buku_sakkarepmu.append(row)
        kode_buku = input('''[-] kode buku     : ''')
        ketemu = []
        # mencari buku_sakkarepmu
        indeks = 0
        for data in buku_sakkarepmu:
            if (data['Kode Buku'] == kode_buku):
                ketemu = buku_sakkarepmu[indeks]
            indeks = indeks + 1
        if len(ketemu) > 0:
            nomer = row_count + 1 # total row diatas ditambah dengan angka 1 
            print('''[#] nomor peminjam              : ''', nomer)
            nik = input('''[-] nik  :''')
            nama_peminjam = input('''[-] nama peminjam     : ''')
            
            judul_buku = (f'''{ketemu['Judul Buku']}''')
            tanggal_nyilek = waktu_saiki
            print('''[-] tanggal pinjam     : ''', tanggal_nyilek.strftime("%d-%m-%Y"))
            tanggal_pengembalian = "belum dikembalikan"
            print("    ╠═══════════════════════════════════")
            writer.writerow(
                {'No': nomer, 'Nama Peminjam': nama_peminjam, 'NIK': nik, 'Kode Buku': kode_buku, 'Judul Buku': judul_buku, 'Tanggal Pinjam': tanggal_nyilek.strftime("%d-%m-%Y"), 'Tanggal Pengembalian': tanggal_pengembalian})
            clear_screen()    
            print("[#] data berhasil ditambahkan!")
            #takon.pinjam_buku_ulang()
    takon.mbalek_menu()

# def kembalikan_buku():
#     clear_screen()
#     buku_sakkarepmu = []

#     with open(nyilek_csv, mode="r") as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             buku_sakkarepmu.append(row)
#     nik = input("[-] masukan NIK    : ")
#     ketemu = []
#     with open(nyilek_csv, mode='a', newline='') as csv_file:
#         fieldnames = ['No','Nama Peminjam', 'NIK', 'Kode Buku', 'Judul Buku', 'Tanggal Pinjam', 'Tanggal Pengembalian']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     with open(nyilek_csv, mode="r", newline='') as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             buku_sakkarepmu.append(row)
#     row_count = sum(1 for row in buku_sakkarepmu) # membaca total row yang ada di csv
#     # mencari buku_sakkarepmu
#     indeks = 0
#     for data in buku_sakkarepmu:
#         if (data['NIK'] == nik):
#             ketemu = buku_sakkarepmu[indeks]
#         indeks = indeks + 1
#     if len(ketemu) > 0:
#         print(''' 
#     ╔════════════════╗
#     ║ data ditemukan ║ 
#     ╚════════════════╝ ''')
#         nomer = row_count + 1 # total row diatas ditambah dengan angka 1 
#         nama_peminjam = {ketemu['Kode Buku']}
#         # kode_buku = {ketemu['Kode Buk']}
#         tanggal_nyilek = {ketemu['Tanggal Pinjam']}
#         # print(f'''[-] kode buku      : {ketemu['Kode Buk']}''')
#         judul_buku = {ketemu['Judul Buku']}
#         print(f'''    [-] nomor buku      : {ketemu['Nama Peminjam']}''')
#         print(f'''    [-] nomor buku      : {ketemu['Kode Buku']}''')
#         print(f'''    [-] nomor buku      : {ketemu['Judul Buku']}''')
#         print(f'''    [-] nomor buku      : {ketemu['Tanggal Pinjam']}''')
#         print(f'''    [-] nomor buku      : {ketemu['Tanggal Pengembalian']}''')

#         tanggal_pengembalian = waktu_saiki
#         print('''''')
#         writer.writerow(
#             {'No': nomer, 'Nama Peminjam': nama_peminjam, 'NIK': nik, 'Kode Buku': nik,  'Judul Buku': judul_buku,'Tanggal Pinjam': tanggal_nyilek, 'Tanggal Pengembalian': tanggal_pengembalian.strftime("%d-%m-%Y")})
#     else:
#         print(''' 
#     ╔═════════════╗ input kamu tidak diketahui
#     ║ input salah ║ coba lagi, jalankan ulang
#     ╚═════════════╝ program dan cek kembali ^ ^! ''')
#         takon.cari_list_ulang()
#     takon.mbalek_menu()
    
def kembalikan_buku():
    clear_screen()
    # membuat variable " waktu_saiki " isinya pakek library date time
    waktu_saiki = datetime.date.today()
    with open("database/buku_sakkarepmu.csv", "r") as fp: 
         x = from_csv(fp)
    # print(x)
    with open(nyilek_csv, mode='a', newline='') as csv_file:
        fieldnames = ['No','Nama Peminjam', 'NIK', 'Kode Buku', 'Judul Buku', 'Tanggal Pinjam', 'Tanggal Pengembalian']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        print(''' 
    ╔═══════════════════╗ [-] pastikan anda menginputkan NIK sesuai kepemilikan anda
    ║  kembalikan buku  ║ [-] setelah menginputkan NIK status peminjaman akan berubah
    ╚═══════════════════╝ [-] selamat ulang tahun xixixi''')
        print('''    ╔═══════════════════════════════════╗''')
 # --------------- ini untuk fungsi auto memberi number ------------------------
        buku_sakkarepmu = []
        with open(nyilek_csv, mode="r", newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                buku_sakkarepmu.append(row)
        row_count = sum(1 for row in buku_sakkarepmu) # membaca total row yang ada di csv
        ketemu = []
        buku_sakkarepmu = []

        with open(nyilek_csv, mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                buku_sakkarepmu.append(row)
        nik = input('''[-] masukan NIK  : ''')
        ketemu = []
        indeks = 0
        for data in buku_sakkarepmu:
            if (data['NIK'] == nik):
                ketemu = buku_sakkarepmu[indeks]
            indeks = indeks + 1
        if len(ketemu) > 0:
            # printisasi data
            nomer = row_count # mendapat nomer togel dari row xixixi, becanda lur
            # nama_peminjam = {ketemu['Nama Peminjam']}
            # kode_buku = {ketemu['Kode Buku']}
            # tanggal_nyilek = f"{ketemu['Tanggal Pinjam']}"
            # judul_buku = f"{ketemu['Judul Buku']}"
            tanggal_pengembalian = waktu_saiki
            print(f'''[-] nama peminjam     : {ketemu['Nama Peminjam']}''')
            print(f'''[-] kode buku     : {ketemu['Kode Buku']}''')
            print(f'''[-] judul buku    : {ketemu['Judul Buku']}''')
            print(f'''[-] tanggal pinjam    : {ketemu['Tanggal Pinjam']}''')
            print(f'''[-] tanggal pengembalian  : ''', tanggal_pengembalian.strftime("%d-%m-%Y"))
            # mencari buku_sakkarepmu
        indeks = 0
        for data in buku_sakkarepmu:
            if (data['NIK'] == nik):  # search dari index kode buku di csv
                tanggal_pengembalian = waktu_saiki

                # variabeling biar rapih
                # nama_peminjam = 
                buku_sakkarepmu[indeks]['No'] = nomer
                buku_sakkarepmu[indeks]['Nama Peminjam'] = ketemu['Nama Peminjam']
                buku_sakkarepmu[indeks]['NIK'] = ketemu['NIK']
                buku_sakkarepmu[indeks]['Kode Buku'] = ketemu['Kode Buku']
                buku_sakkarepmu[indeks]['Judul Buku'] = ketemu['Judul Buku']
                buku_sakkarepmu[indeks]['Tanggal Pinjam'] = ketemu['Tanggal Pinjam']
                buku_sakkarepmu[indeks]['Tanggal Pengembalian'] = tanggal_pengembalian.strftime("%d-%m-%Y")
            indeks = indeks + 1
        # Menulis data baru ke file CSV (tulis ulang)
        with open(nyilek_csv, mode="w",  newline='') as csv_file:
            fieldnames = ['No', 'Nama Peminjam', 'NIK', 'Kode Buku', 'Judul Buku', 'Tanggal Pinjam', 'Tanggal Pengembalian']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in buku_sakkarepmu:
                writer.writerow({'No': new_data['No'], 'NIK': new_data['NIK'], 'Nama Peminjam': new_data['Nama Peminjam'], 'Kode Buku': new_data['Kode Buku'],
                                'Judul Buku': new_data['Judul Buku'], 'Tanggal Pinjam': new_data['Tanggal Pinjam'], 'Tanggal Pengembalian': new_data['Tanggal Pengembalian']})
    # clear_screen()    
        print("[#] data berhasil diubah!")
            # takon.pinjam_buku_ulang()
    takon.mbalek_menu()
    
# def kembalikan_buku():
#     clear_screen()
#     # membuat variable " waktu_saiki " isinya pakek library date time
#     waktu_saiki = datetime.date.today()
#     with open("database/buku_sakkarepmu.csv", "r") as fp: 
#          x = from_csv(fp)
#     # print(x)
#     with open(nyilek_csv, mode='a', newline='') as csv_file:
#         fieldnames = ['No','Nama Peminjam', 'NIK', 'Kode Buku', 'Judul Buku', 'Tanggal Pinjam', 'Tanggal Pengembalian']
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         print(''' 
#     ╔═══════════════════╗ [-] kode terdiri dari huruf dan angka
#     ║  kembalikan buku  ║ [-] contoh : g-001
#     ╚═══════════════════╝ [-] "g" diambil dari huruf terdepan buku dan "001" dari urutan ''')
#         print('''    ╔═══════════════════════════════════╗''')
#  # --------------- ini untuk fungsi auto memberi number ------------------------
#         buku_sakkarepmu = []
#         with open(nyilek_csv, mode="r", newline='') as csv_file:
#             csv_reader = csv.DictReader(csv_file)
#             for row in csv_reader:
#                 buku_sakkarepmu.append(row)
#         row_count = sum(1 for row in buku_sakkarepmu) # membaca total row yang ada di csv
#         ketemu = []
#         buku_sakkarepmu = []

#         with open(nyilek_csv, mode="r") as csv_file:
#             csv_reader = csv.DictReader(csv_file)
#             for row in csv_reader:
#                 buku_sakkarepmu.append(row)
#         nik = input('''[-] masukan NIK     : ''')
#         ketemu = []
#         # mencari buku_sakkarepmu
#         indeks = 0
#         for data in buku_sakkarepmu:
#             if (data['NIK'] == nik):
#                 ketemu = buku_sakkarepmu[indeks]
#             indeks = indeks + 1
#         if len(ketemu) > 0:
#             nomer = row_count + 1 # total row diatas ditambah dengan angka 1 
#             nama_peminjam = {ketemu['Nama Peminjam']}
#             # kode_buku = {ketemu['Kode Buk']}
#             tanggal_nyilek = {ketemu['Tanggal Pinjam']}
#             # print(f'''[-] kode buku      : {ketemu['Kode Buk']}''')
#             judul_buku = {ketemu['Judul Buku']}
#             tanggal_pengembalian = waktu_saiki
#             print(f'''    [-] nomor buku      : {ketemu['Nama Peminjam']}''')
#             print(f'''    [-] nomor buku      : {ketemu['Kode Buku']}''')
#             print(f'''    [-] nomor buku      : {ketemu['Judul Buku']}''')
#             print(f'''    [-] nomor buku      : {ketemu['Tanggal Pinjam']}''')
#             print(f'''    [-] nomor buku      : ''', tanggal_pengembalian)

#             writer.writerow(
#                 {'No': nomer, 'Nama Peminjam': nama_peminjam, 'NIK': nik, 'Kode Buku': nik,  'Judul Buku': judul_buku,'Tanggal Pinjam': tanggal_nyilek, 'Tanggal Pengembalian': tanggal_pengembalian.strftime("%d-%m-%Y")})
#         # clear_screen()    
#         print("[#] data berhasil diubah!")
#             # takon.pinjam_buku_ulang()
#     takon.mbalek_menu()