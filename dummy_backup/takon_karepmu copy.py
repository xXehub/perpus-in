# from karepmu import*
# mengimport semua function yang ada di " karepmu.py "
import program.karepmu as karepmu
import program.nyilek_karepmu as nyilek
import sys
import os

def clear_screen():  # clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
# from run_karepmu import*
# ---- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---  bagian takonan ------ --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---  --- --- --- 
def mbalek_menu():
    print("\n")
    input('''[note] tekan enter untuk kembali...''')
    karepmu.menu_siperpus()

def takon():  # mendefinisikan variable takon
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''       [!] ingin mengulang aplikasi lagi? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        karepmu.awalan()  # kembali ke awalan
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        print('''
    [x] -- exit / anda keluar !''')
        sys.exit()  # metu lurr
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')

def salah():  # mendefinisikan variable takon
    # global option
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''           [!] login ulang ? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        karepmu.access(karepmu.option)  # kembali ke awalan
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        print('''
    [x] -- exit / anda keluar !''')
        sys.exit()  # metu lurr
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')
def tambah_pastikan():  # menanyai tambah ulang apa ora
    # clear_screen()
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''       [!] apakah data diatas sudah benar ? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        #karepmu.tambah_data()  # kembali ke pinjam buku
        sys.get_coroutine_origin_tracking_depth
        
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        print('''
    [x] -- exit / anda keluar !''')
        karepmu.tambah_data()
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')

def tambah_data_ulang():  # menanyai tambah ulang apa ora
    clear_screen()
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''       [!] tambah buku lagi ? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        karepmu.tambah_data()  # kembali ke pinjam buku
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        print('''
    [x] -- exit / anda keluar !''')
        karepmu.menu_siperpus()
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')

def pinjam_buku_ulang():  # menanyai tambah ulang apa ora
    clear_screen()
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''       [!] tambah pinjaman ? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        nyilek.pinjam_buku()  # kembali ke pinjam buku
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        print('''
    [x] -- exit / anda keluar !''')
        karepmu.menu_siperpus()
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')

def cari_list_ulang():  # untuk cari_list
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''       [!] cari ulang ? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        karepmu.cari_list()  # kembali ke awalan
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        print('''
    [x] -- exit / anda keluar !''')
        karepmu.menu_siperpus()
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')

def pinjam_ulang():  # untuk cari_list
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''       [!] cari ulang ? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        nyilek.pinjam_buku()  # kembali ke pinjam buku
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        print('''
    [x] -- exit / anda keluar !''')
        karepmu.menu_siperpus()
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')

def takon_regis():  # mendefinisikan variable takon
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''       [!] ingin melakukan registrasi sekarang ? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        karepmu.awalan()  # kembali ke awalan
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        print('''
    [x] -- exit / anda keluar !''')
        sys.exit()  # metu lurr
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')

def yakin_metu():  # mendefinisikan variable takon
    print('''    ╔════════════════════════════════════════════╗''')
    takon_karepmu = input('''       [!] anda yakin ingin keluar ? [y/t]
    ╔════════════════════════════════════════════╝
    [-] input : ''')
    # print("")
    if takon_karepmu == "y":  # kalo user menginputkan " y "
        print('''
    [x] -- exit / anda keluar !''')
        sys.exit()  # metu lurr
    elif takon_karepmu == "t":  # kalo user menginputkan " t "
        karepmu.menu_siperpus()  # kembali ke awalan
    else:
        print('''
        ╔═════════════╗ input kamu tIDak diketahui
        ║ input salah ║ coba lagi, jalankan ulang
        ╚═════════════╝ program dan cek kembali ^ ^!
        ''')