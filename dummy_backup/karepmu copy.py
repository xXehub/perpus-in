# mengimport module dari takon_karepmu
import program.takon_karepmu as takon 
import program.nyilek_karepmu as nyilek
# mengimport library datetime
import datetime
# import library sys gawe exit
import sys
import csv
import os
import string    
import random # define the random module  
import uuid # library gawe generate random id 
# from getpass import getpass # untuk menutupi password
from prettytable import from_csv
from pwinput import pwinput # merubah inputan menjadi * ngawe library iki

# x = PrettyTable()
# password = getpass()

def login(username, password):  # pendefinisian function login
    # melbu = false sebagai default ( karena username dan password masih belum ditemukan )
    melbu = False
    # membuka file txt dengan function r ( hanya read / membaca )
    # " r " membuka dan membaca file txt
    file = open("database/login_db_sakkarepmu.txt", "r")
    # perulangann untuk menata user pw cok
    for i in file:
        #  i.split(",") ini untukambil ID dan pass di file logindatabase.txt, lalu , (koma) adalah pemisah antara ID dan pass nya
        # digunakan untuk memberi tanda pemisah antara username dan password dengan mengguankan " : "
        a, b = i.split(" : ")
        b = b.strip()
        # variable a digunakan untuk menyimpan username | variable b digunakan untuk menyimpan password
        if (a == username and b == password):
            melbu = True  # jika username dan password sesuai persyaratan maka melbu = true / berhasil dan break
            break
        elif (a == username or b == password):  # jika username / password user salah chuakssss
            clear_screen()
            print('''
    [x] username / password anda salah !''')
            takon.salah()

    file.close()  # menutup file
    if (melbu):  # jika masuk / sudah sesuai persyaratan
        # memanggil library date time
        # membuat variable " waktu_saiki " isinya pakek library date time
        waktu_saiki = datetime.date.today()
        print('''    [!] selamat datang : ''' + a +
              ''' \n    [#] masuk pada : ''', waktu_saiki)  # nyeluk waktu variable waktu saiki yang berisi datetime
        menu_siperpus()  # default kasir
    else:
        # print(''' [x] anda belum terdaftar, silahkan register !''')
        clear_screen()
        print('''
    [x] anda belum terdaftar, silahkan register !''')
    takon.takon()

def register(username, password):  # function registrasi
    # membuka file txt dengan function a ( mengedit )
    file = open("database/login_db_sakkarepmu.txt", "a")  # " a " membuka file txt
    # mengedit / write ( username dan password ) kedalam file txt
    file.write("\n" + username + " : " + password)

# proses login / registrasi cuk
def access(option):
    clear_screen()
    global username  # gawe set username secara global / dapat diakses dimanapun
    if (option == "1"):  # kalo memilih / menuliskan angka 1 maka akan mengeluarkan output dibawah / login output
        print(''' 
    ╔═════════════╗ selamat datang di aplikasi inventory sederhana kami
    ║    login    ║ pastikan kamu sudah benar dalam memasukan input
    ╚═════════════╝ silahkan cek terlebih dahulu sebelum menginputkan ^ ^!''')
        print('''    ╔════════════════════════════════╗''')
        username = input('''     [-] username : ''')
        password = pwinput('''     [-] password : ''') # input password menggunakan module " getpass " | dadi passwordnya akan invisble anjoy
        print("    ╔════════════════════════════════╝")
        login(username, password)

    else:  # kalo memilih selain angka 1 maka akan menampilkan register output seperti dibawah
        clear_screen()
        print(''' 
    ╔═════════════╗ silahkan membuat username dan password yang baru
    ║  registrasi ║ pastikan kamu sudah benar dalam memasukan input
    ╚═════════════╝ silahkan cek terlebih dahulu sebelum lanjut ^ ^!''')
        print('''    ╔════════════════════════════════╗''')
        username = input('''     [-] username : ''')
        password = pwinput('''     [-] password : ''')
        print("    ╔════════════════════════════════╝")
        register(username, password)
        # print(''' [#] register anda telah berhasil, silahkan login / masuk''')
        clear_screen()
        print('''
    ╔══════════════════════╗ [-] berhasil membuat akun
    ║  registrasi berhasil ║ [-] anda dapat login menggukanan akun yang telah didaftarkan
    ╚══════════════════════╝ [-] selamat datang ^ ^!''')
    takon.takon()

# def kasir_lur():  # kasir disini soon
#     print()
#     print('''    [x] durung su, alur kasir soon !  ''')
#     if __name__ == "__main__":
#         while True:
#             menu_siperpus()

def awalan():  # awalan ini untuk menu awal
    clear_screen()
    global option
#     print('''
#   _                                   _
#  | |_ _  _ __ _ __ _ ___  __ _ ___ __| |___ _ _
#  |  _| || / _` / _` (_-< / _` / -_) _` / -_) ' \
#   \__|\_,_\__, \__,_/__/ \__, \___\__,_\___|_||_|
#           |___/          |___/satukan unesa untuk membangun telkom surabaya !''')
    option = input('''
    ╔════════════════════════════════╗
    ║             welcome            ║
    ╠════════════════════════════════╣
    ║   [1] login                    ║
    ║   [2] registrasi               ║
    ║   [3] keluar                   ║
    ║   [99] author                  ║
    ╚════════════════════════════════╝   
    [-] pilih menu selection diatas [1/2/3/99] 
        input : ''')  # menggunakan select menu untuk berinteraksi dengan user / user dapat memilih sesuai dengan angka yang tertera dan yang diinputkan
    # if (option == "1" and option == "2"):
    if (option == "1"):  # jika user menginputkan angka 1 maka :
        access(option)  # menampilkan definisi akses
    elif (option == "2"):  # jika user menginputkan angka 2 maka :
        access(option)  # menampilkan definisi akses
    elif (option == "99"):
        print(''' 
            _   _            
  __ _ _  _| |_| |_  ___ _ _    [-] -- auditya fariz hermansyah | 120422001
 / _` | || |  _| ' \/ _ \ '_|   [-] -- fajri | 120422001
 \__,_|\_,_|\__|_||_\___/_|     [-] -- muhammad deru | 120422001
                                [-] -- muhammad izzul haq syihabuddin sanni | 120422001
                                [-] -- rey septian fariz hermansyah | 120422001
        ''')
    elif (option == "3"):  # jika user menginputkan angka 3 maka :
        print('''
    [x] -- exit / anda keluar !''')
        sys.exit()
    else:
        clear_screen()
        print('''
    ╔═════════════╗ input kamu tIDak diketahui
    ║ input salah ║ coba lagi, jalankan ulang
    ╚═════════════╝ program dan cek kembali ^ ^!
    ''')
    takon.takon()

# ----- bagian CSV -----
# menyimpan nama csv file kedalam sebuah variable
perpus_csv = 'database/buku_sakkarepmu.csv'

def clear_screen():  # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_siperpus():
    clear_screen()
    buku_sakkarepmu = []
    with open(perpus_csv, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            buku_sakkarepmu.append(row)
    row_count = sum(1 for row in buku_sakkarepmu)
    # membuat variable " waktu_saiki " isinya pakek library date time
    waktu_saiki = datetime.date.today()
    print('''    
  ___ _                            
 / __(_)_ __  ___ _ _ _ __ _  _ ___
 \__ \ | '_ \/ -_) '_| '_ \ || (_-<
 |___/_| .__/\___|_| | .__/\_,_/__/
       |_|           |_| ketik "gusur" untuk mengambil alih unesa, salam telkom                    
    * INFO statistic      
    [⛑ ] username        :  ''' , username ,
          ''' \n    [🛡 ] masuk pada      : ''', waktu_saiki, ''' \n    [🛠 ] total buku      : ''', row_count)  # nyeluk waktu variable waktu saiki yang berisi datetime
    raimu = input(''' 
    ╔════════════════════════════════╗
    ║              MENU              ║
    ╠════════════════════════════════╣
    ║   [1] daftar buku              ║
    ║   [2] tambah buku              ║
    ║   [3] edit buku                ║
    ║   [4] hapus buku               ║
    ║   [5] cari buku                ║
    ║   [6] daftar pinjam buku       ║
    ║   [7] pinjam buku              ║
    ║   [8] kembalikan buku          ║
    ║   [0] keluar                   ║
    ╚════════════════════════════════╝  
    [-] pilih menu selection diatas [1/2/3/4/5//6/7/8/0] 
        input : ''')
    if (raimu == "1"):
        daftar_buku()
    elif (raimu == "2"):
        tambah_buku()
    elif (raimu == "3"):
        edit_list()
    elif (raimu == "4"):
        delete_buku()
    elif (raimu == "5"):
        cari_list()
    elif (raimu == "6"):
# -------- ngambil dari file " nyilek_karepmu.py " -----------
        nyilek.daftar_peminjam()
    elif (raimu == "7"):
        nyilek.pinjam_buku()
    elif (raimu == "8"):
        nyilek.kembalikan_buku()
        sys.exit()
    elif (raimu == "0"):
        clear_screen()
        takon.yakin_metu() # module takon dari file takon
    else:
        print(''' 
    ╔═════════════╗ input kamu tIDak diketahui
    ║ input salah ║ coba lagi, jalankan ulang
    ╚═════════════╝ program dan cek kembali ^ ^!
        ''')
        takon.mbalek_menu()

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- CRUD --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- 
def daftar_buku():
    clear_screen()
    print(''' 
\t\t\t\t    ___        __ _              ___      _        
\t\t\t\t   |   \ __ _ / _| |_ __ _ _ _  | _ )_  _| |___  _ 
\t\t\t\t   | |) / _` |  _|  _/ _` | '_| | _ \ || | / / || |
\t\t\t\t   |___/\__,_|_|  \__\__,_|_|   |___/\_,_|_\_\\_,_|''')
    with open(perpus_csv, "r") as fp: 
        x = from_csv(fp)
    print(x)
    # cf = open("database/buku_sakkarepmu.csv", "r")
    # for rows in cf:
    #     pt = from_csv(rows)
    # print(pt)
    # fp.close()

    # cf = open("database/buku_sakkarepmu.csv", "r")
    # for fname in cf:
    #     fname = fname.rstrip()
    #     fname = fname.replace("'", "")
    #     if len(fname) == 0:  # have an empty line in the file list
    #         continue        
    #     f = open("database/buku_sakkarepmu.csv", "r")
    #     pt = from_csv(f)
    #     f.close()
    #     print(pt)    
    #     w = open('database/buku_sakkarepmu.csv','w')
    #     w.write(pt.get_string())
    # w.close()
    # cf.close()
#     buku_sakkarepmu = []
# # buka file CSV dengan mode R / Baca
#     with open(perpus_csv, mode="r") as csv_file:
#         csv_reader = csv.DictReader(csv_file)
#         for row in csv_reader:
#             buku_sakkarepmu.append(row)

#     row_count = sum(1 for row in buku_sakkarepmu)

#     print("-" * 160)
#     print("\t\t\t\t\t\t\t\t Daftar Stok buku Toko")
#     print("-" * 160)
#     table_buku = PrettyTable(["Not Kode "," Tanggal Masuk", "Judul Buku ", "Pengarang",  "Penerbit", "Jumlah Halaman", "Tahun Terbit"])
#     # print("No. \t Kode Buku \t Tanggal Masuk \t\t Judul Buku \t\t Pengarang \t\t Penerbit \t\tJumlah Halaman \t Tahun Terbit \t")
#     print("-" * 160)
#     # Looping untuk mengeluarkan datanyna
#     for data in buku_sakkarepmu:
#         table_buku(
#         f"{data['No']}. \t {data['Kode Buku']} \t\t {data['Tanggal Masuk']} \t\t  {data['Judul Buku']} \t\t {data['Pengarang']} \t {data['Penerbit']} \t\t\t {data['Jumlah Halaman']} Halaman \t\t  {data['Tahun Terbit']} \t")
#     print("-" * 55)
#     print("Total Buku: ", row_count)
#     print("-" * 55)
    takon.mbalek_menu()

def tambah_buku():  # menambahkan data ke csv
    clear_screen()
    # membuat variable " waktu_saiki " isinya pakek library date time
    waktu_saiki = datetime.date.today() # generate waktu saiki
    id = uuid.uuid1() # membuat variable untuk generating random id
    print('''
    \t\t\t\t _____           _          _      ___      _        
    \t\t\t\t|_   _|_ _ _ __ | |__  __ _| |_   | _ )_  _| |___  _ 
      \t\t\t\t  | |/ _` | '  \| '_ \/ _` | ' \  | _ \ || | / / || |
      \t\t\t\t  |_|\__,_|_|_|_|_.__/\__,_|_||_| |___/\_,_|_\_\\_,_|''')
    with open(perpus_csv, "r") as fp: 
        x = from_csv(fp)
    print(x)
    with open(perpus_csv, mode='a', newline='') as csv_file:
        fieldnames = ['No', 'Kode Buku', 'Tanggal Masuk', 'Judul Buku',
                      'Pengarang', 'Penerbit', 'Jumlah Halaman', 'Tahun Terbit']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # print("===============================")
        # print("======== Tambah Buku  ========")
        # print("===============================\n")
        print(''' 
    ╔═══════════════╗ [-] kode terdiri dari 10 string
    ║  tambah buku  ║ [-] di generate menggunakan library random, string
    ╚═══════════════╝ [-] kode dapat berguna di menu lain ''')
        print('''╔═══════════════════════════════════╗''')
 # --------------- ini untuk fungsi auto memberi number ------------------------
        buku_sakkarepmu = []
        with open(perpus_csv, mode="r", newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                buku_sakkarepmu.append(row)
        row_count = sum(1 for row in buku_sakkarepmu) # membaca total row yang ada di csv
        nomer = row_count + 1 # total row diatas ditambah dengan angka 1 
        print('''╠ [#] nomor              : ''', nomer)
        print('''╚═══════════════════════════════════╝''')
        huruf = 10  # number of characters in the string.  
        # call random.choices() string module to find the string in Uppercase + numeric data.  
        random_kode = ''.join(random.choices(string.ascii_uppercase + string.digits, k = huruf))    
        kode_buku = str(random_kode)
        print('''[#] kode buku     : ''', kode_buku)
        # kode_buku = input('''    ╔ [-] kode buku     : ''')
        # tanggal_masuk = input('''    ╠ [-] tanggal masuk   : ''')
        tanggal_masuk = waktu_saiki
        print('''[#] tanggal masuk     : ''', tanggal_masuk.strftime("%d-%m-%Y"))
        judul_buku = input('''[-] judul buku    : ''').title()
        pengarang = input('''[-] pengarang    : ''').title()
        penerbit = input('''[-] penerbit    : ''').title()
        jumlah_halaman = input('''[-] jumlah halaman    : ''')
        # jumlah_halaman = jumlah_halaman_input, "halaman"
        tahun_terbit = input('''[-] tahun terbit    : ''')
        print("    ╠═══════════════════════════════════")
        writer.writerow(
            {'No': nomer, 'Kode Buku': kode_buku, 'Tanggal Masuk': tanggal_masuk.strftime("%d-%m-%Y"), 'Judul Buku': judul_buku, 'Pengarang': pengarang, 'Penerbit': penerbit, 
            'Jumlah Halaman': jumlah_halaman + ' halaman', 'Tahun Terbit': tahun_terbit})
        clear_screen()
        print("    [#] data berhasil ditambahkan!")
        # takon.tambah_buku_ulang()
    takon.mbalek_menu()

def cari_list():
    clear_screen()
    buku_sakkarepmu = []

    with open(perpus_csv, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            buku_sakkarepmu.append(row)
    judul_buku = input("[-] cari buku berdasrakan judul     : ").title()
    ketemu = []

    # mencari buku_sakkarepmu
    indeks = 0
    for data in buku_sakkarepmu:
        if (data['Judul Buku'] == judul_buku):
            ketemu = buku_sakkarepmu[indeks]
        indeks = indeks + 1
    if len(ketemu) > 0:
        print(''' 
    ╔════════════════╗
    ║ data ditemukan ║ 
    ╚════════════════╝ ''')
        print(f'''    [-] nomor buku      : {ketemu['No']}''')
        print(f'''    [-] kode buku       : {ketemu['Kode Buku']}''')
        print(f'''    [-] tanggal masuk   : {ketemu['Tanggal Masuk']}''')
        print(f'''    [-] judul buku      : {ketemu['Judul Buku']}''')
        print(f'''    [-] pengarang       : {ketemu['Pengarang']}''')
        print(f'''    [-] penerbit        : {ketemu['Penerbit']}''')
        print(f'''    [-] jumlah halaman  : {ketemu['Jumlah Halaman']} Halaman''')
        print(f'''    [-] tahun terbit    : {ketemu['Tahun Terbit']}''')
    else:
        print(''' 
    ╔═════════════╗ input kamu tidak diketahui
    ║ input salah ║ coba lagi, jalankan ulang
    ╚═════════════╝ program dan cek kembali ^ ^! ''')
        takon.cari_list_ulang()
    takon.mbalek_menu()

def edit_list():  # definisi fungsi edit data / buku
    clear_screen()
    buku_sakkarepmu = []
    with open(perpus_csv, mode="r", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            buku_sakkarepmu.append(row)
    row_count = sum(1 for row in buku_sakkarepmu)
    with open(perpus_csv, "r") as fp: 
        x = from_csv(fp)
    print(x)
    # print("-" * 150)
    # print("\t\t  Daftar Stok buku")
    # print("-" * 150)
    # print("No. \t Kode Buku \t Tanggal Masuk \t\t Judul Buku \t\t Pengarang \t\t Penerbit \t\t\t Jumlah Halaman \t Tahun Terbit \t")
    # print("-" * 150)
    for data in buku_sakkarepmu:
    #     print(
    #         f"{data['No']}. \t {data['Kode Buku']} \t\t {data['Tanggal Masuk']} \t\t  {data['Judul Buku']} \t\t {data['Pengarang']} \t {data['Penerbit']} \t\t\t {data['Jumlah Halaman']} Halaman \t\t  {data['Tahun Terbit']} \t")

        # print("-" * 55)
        # print("total data :", row_count)
        # print("-" * 55)
        kode_buku = input("[-] input kode buku     : ")
        # nomer = buku_sakkarepmu[indeks]['No']
        print('''[-] buku nomor      : ''' +
        f"{data['No']}")  # memanggil nomor buku dari tabel
        tanggal_masuk = input("[-] tanggal masuk         : ")
        judul_buku = input("[-] judul buku     : ")
        pengarang = input("[-] pengarang   : ")
        penerbit = input("[-] penerbit   : ")
        jumlah_halaman = input("[-] jumlah halaman   : ")
        tahun_terbit = input("[-] tahun terbit   : ")
        # mencari buku_sakkarepmu dan mengubah datanya
        # dengan data yang baru
        indeks = 0
        for data in buku_sakkarepmu:
            if (data['Kode Buku'] == kode_buku):  # search dari index kode buku di csv
                buku_sakkarepmu[indeks]['Tanggal Masuk'] = tanggal_masuk
                buku_sakkarepmu[indeks]['Judul Buku'] = judul_buku
                buku_sakkarepmu[indeks]['Pengarang'] = pengarang
                buku_sakkarepmu[indeks]['Penerbit'] = penerbit
                buku_sakkarepmu[indeks]['Jumlah Halaman'] = jumlah_halaman
                buku_sakkarepmu[indeks]['Tahun Tebit'] = tahun_terbit
            indeks = indeks + 1
        # Menulis data baru ke file CSV (tulis ulang)
        with open(perpus_csv, mode="w",  newline='') as csv_file:
            fieldnames = ['No', 'Kode Buku', 'Tanggal Masuk', 'Judul Buku',
                        'Pengarang', 'Penerbit', 'Jumlah Halaman', 'Tahun Terbit']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for new_data in buku_sakkarepmu:
                writer.writerow({'No': new_data['No'], 'Kode Buku': new_data['Kode Buku'], 'Tanggal Masuk': new_data['Tanggal Masuk'],
                                'Judul Buku': new_data['Judul Buku'], 'Pengarang': new_data['Pengarang'], 'Penerbit': new_data['Penerbit'], 
                                'Jumlah Halaman': new_data['Jumlah Halaman'], 'Tahun Terbit': new_data['Tahun Terbit']})
            clear_screen()
            print('''[#] data berhasil diubah!''')
        takon.mbalek_menu()

def delete_buku():
    clear_screen()
    buku_sakkarepmu = []
    with open(perpus_csv, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            buku_sakkarepmu.append(row)

    with open(perpus_csv, "r") as fp: 
        x = from_csv(fp)
    print(x)
    # print("ID \t Nama \t Jumlah \t Harga")
    # print("-" * 55)

    # for data in buku_sakkarepmu:
    #     print(
    #         f"{data['No']}. \t {data['Kode Buku']} \t\t {data['Tanggal Masuk']} \t\t  {data['Judul Buku']} \t\t {data['Pengarang']} \t {data['Penerbit']} \t\t\t {data['Jumlah Halaman']} Halaman \t\t  {data['Tahun Terbit']} \t")

    # print("-----------------------")
    kode_buku = input("[-] hapus buku berdasarkan kode buku : ")
    indeks = 0
    for data in buku_sakkarepmu:
        if (data['Kode Buku'] == kode_buku):
            buku_sakkarepmu.remove(buku_sakkarepmu[indeks])
        indeks = indeks + 1
    # Menulis data baru ke file CSV (tulis ulang)
    with open(perpus_csv, mode="w", newline='') as csv_file:
        fieldnames = ['No', 'Kode Buku', 'Tanggal Masuk', 'Judul Buku', 'Pengarang', 'Penerbit', 'Jumlah Halaman', 'Tahun Terbit']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for new_data in buku_sakkarepmu:
            writer.writerow({'No':new_data['No'], 'Kode Buku':new_data['Kode Buku'], 'Tanggal Masuk':new_data['Tanggal Masuk'], 'Judul Buku':new_data['Judul Buku'], 'Pengarang':new_data['Pengarang'], 'Penerbit':new_data['Penerbit'], 'Jumlah Halaman':new_data['Jumlah Halaman'], 'Tahun Terbit':new_data['Tahun Terbit']})
    print("Data sudah terhapus")
    takon.mbalek_menu()

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- bagian persilihan  --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# csv_pinjaman = 'database/nyilek_sakkarepmu.csv'
# def daftar_peminjam():
#     clear_screen()
#     with open("database/nyilek_sakkarepmu.csv", "r") as fp: 
#         x = from_csv(fp)
#     print(x)

#     takon.mbalek_menu()

# def pinjam_buku():
#     print(''' ''')

# def kembalikan_buku():
#     print(''' ''')
# # ---- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---  bagian takonan ------ --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---  --- --- --- 

# def mbalek_menu():
#     print("\n")
#     input('''[note] tekan enter untuk kembali...''')
#     menu_siperpus()


# def takon():  # mendefinisikan variable takon
#     print('''    ╔════════════════════════════════════════════╗''')
#     takon_karepmu = input('''       [!] ingin mengulang aplikasi lagi? [y/t]
#     ╔════════════════════════════════════════════╝
#     [-] input : ''')
#     # print("")
#     if takon_karepmu == "y":  # kalo user menginputkan " y "
#         awalan()  # kembali ke awalan
#     elif takon_karepmu == "t":  # kalo user menginputkan " t "
#         print('''
#     [x] -- exit / anda keluar !''')
#         sys.exit()  # metu lurr
#     else:
#         print('''
#         ╔═════════════╗ input kamu tIDak diketahui
#         ║ input salah ║ coba lagi, jalankan ulang
#         ╚═════════════╝ program dan cek kembali ^ ^!
#         ''')


# def salah():  # mendefinisikan variable takon
#     print('''    ╔════════════════════════════════════════════╗''')
#     takon_karepmu = input('''           [!] login ulang ? [y/t]
#     ╔════════════════════════════════════════════╝
#     [-] input : ''')
#     # print("")
#     if takon_karepmu == "y":  # kalo user menginputkan " y "
#         access(option)  # kembali ke awalan
#     elif takon_karepmu == "t":  # kalo user menginputkan " t "
#         print('''
#     [x] -- exit / anda keluar !''')
#         sys.exit()  # metu lurr
#     else:
#         print('''
#         ╔═════════════╗ input kamu tIDak diketahui
#         ║ input salah ║ coba lagi, jalankan ulang
#         ╚═════════════╝ program dan cek kembali ^ ^!
#         ''')


# def cari_list_ulang():  # untuk cari_list
#     print('''    ╔════════════════════════════════════════════╗''')
#     takon_karepmu = input('''       [!] cari ulang ? [y/t]
#     ╔════════════════════════════════════════════╝
#     [-] input : ''')
#     # print("")
#     if takon_karepmu == "y":  # kalo user menginputkan " y "
#         cari_list()  # kembali ke awalan
#     elif takon_karepmu == "t":  # kalo user menginputkan " t "
#         print('''
#     [x] -- exit / anda keluar !''')
#         menu_siperpus()
#     else:
#         print('''
#         ╔═════════════╗ input kamu tIDak diketahui
#         ║ input salah ║ coba lagi, jalankan ulang
#         ╚═════════════╝ program dan cek kembali ^ ^!
#         ''')


# def takon_regis():  # mendefinisikan variable takon
#     print('''    ╔════════════════════════════════════════════╗''')
#     takon_karepmu = input('''       [!] ingin melakukan registrasi sekarang ? [y/t]
#     ╔════════════════════════════════════════════╝
#     [-] input : ''')
#     # print("")
#     if takon_karepmu == "y":  # kalo user menginputkan " y "
#         awalan()  # kembali ke awalan
#     elif takon_karepmu == "t":  # kalo user menginputkan " t "
#         print('''
#     [x] -- exit / anda keluar !''')
#         sys.exit()  # metu lurr
#     else:
#         print('''
#         ╔═════════════╗ input kamu tIDak diketahui
#         ║ input salah ║ coba lagi, jalankan ulang
#         ╚═════════════╝ program dan cek kembali ^ ^!
#         ''')


# awalan()

#   $$\                                                                             $$\
#   $$ |                                                                            $$ |
# $$$$$$\   $$\   $$\  $$$$$$\   $$$$$$\   $$$$$$$\        $$$$$$\   $$$$$$\   $$$$$$$ | $$$$$$\  $$$$$$$\
# \_$$  _|  $$ |  $$ |$$  __$$\  \____$$\ $$  _____|      $$  __$$\ $$  __$$\ $$  __$$ |$$  __$$\ $$  __$$\
#   $$ |    $$ |  $$ |$$ /  $$ | $$$$$$$ |\$$$$$$\        $$ /  $$ |$$$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  $$ |
#   $$ |$$\ $$ |  $$ |$$ |  $$ |$$  __$$ | \____$$\       $$ |  $$ |$$   ____|$$ |  $$ |$$   ____|$$ |  $$ |
#   \$$$$  |\$$$$$$  |\$$$$$$$ |\$$$$$$$ |$$$$$$$  |      \$$$$$$$ |\$$$$$$$\ \$$$$$$$ |\$$$$$$$\ $$ |  $$ |
#    \____/  \______/  \____$$ | \_______|\_______/        \____$$ | \_______| \_______| \_______|\__|  \__|
#                     $$\   $$ |                          $$\   $$ |
#                     \$$$$$$  |                          \$$$$$$  |
#                      \______/                            \______/
