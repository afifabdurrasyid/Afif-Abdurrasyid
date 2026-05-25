KomikList = {
    'id': ['K001', 'K002', 'K003', 'K004', 'K005'],
    'judul': ['Grand Blue', 'Kaguya-sama', 'Demon Slayer', 'Tokyo Ghoul', 'Frieren'],
    'genre': ['Comedy', 'Romance', 'Action', 'Horror', 'Fantasy'],
    'rating': [8.8, 8.9, 8.7, 8.5, 9.3],
    'author': ['Kenji Inoue', 'Aka Akasaka', 'Koyoharu Gotouge', 'Sui Ishida', 'Kanehito Yamada']
}


def headerKomik():

    print()
    print("ID\t| Judul\t\t| Genre\t\t| Rating | Author")
    print("-" * 75)


def printKomik(i):

    print(
        KomikList['id'][i], "\t|",
        KomikList['judul'][i], "\t |",
        KomikList['genre'][i], "\t|",
        KomikList['rating'][i], "\t |",
        KomikList['author'][i]
    )


def showKomik():

    while True:

        menuShowKomik = int(input("""
1. Tampilkan Semua Komik
2. Cari Komik
3. Kembali

Pilih Menu : 
"""))

        if menuShowKomik == 1:

            headerKomik()

            for i in range(len(KomikList['id'])):

                printKomik(i)

        elif menuShowKomik == 2:

            find = input("Masukkan Judul Komik : ").lower()

            ditemukan = False

            headerKomik()

            for i in range(len(KomikList['id'])):

                if find in KomikList['judul'][i].lower():

                    printKomik(i)

                    ditemukan = True

            if not ditemukan:

                print("Komik tidak ditemukan!")

        elif menuShowKomik == 3:

            break

        else:

            print("Menu tidak tersedia!")


def addKomik():

    while True:

        menuAddKomik = int(input("""
1. Tambah Komik
2. Kembali

Pilih Menu : 
"""))

        if menuAddKomik == 1:

            idKomik = input("Masukkan ID Komik : ").upper()

            if idKomik in KomikList['id']:

                print("ID sudah tersedia!")

            else:

                judulKomik = input("Masukkan Judul Komik : ")
                genreKomik = input("Masukkan Genre Komik : ")
                ratingKomik = float(input("Masukkan Rating Komik : "))
                authorKomik = input("Masukkan Author Komik : ")

                save = input("""
Apakah data ingin disimpan? (Y/N) : 
""").upper()

                if save == 'Y':

                    KomikList['id'].append(idKomik)
                    KomikList['judul'].append(judulKomik)
                    KomikList['genre'].append(genreKomik)
                    KomikList['rating'].append(ratingKomik)
                    KomikList['author'].append(authorKomik)

                    print("\nKomik berhasil ditambahkan!")
                    
                    headerKomik()

                    for i in range(len(KomikList['id'])):

                        printKomik(i)

                elif save == 'N':

                    print("\nData batal disimpan!")

                else:

                    print("\nMenu tidak tersedia!")

        elif menuAddKomik == 2:

            break

        else:

            print("Menu tidak tersedia!")

def updateKomik():

    while True:

        menuUpdateKomik = int(input("""
1. Update Komik
2. Kembali

Pilih Menu : 
"""))

        if menuUpdateKomik == 1:

            headerKomik()

            for i in range(len(KomikList['id'])):

                printKomik(i)

            idKomik = input("\nMasukkan ID Komik : ").upper()

            ditemukan = False

            for i in range(len(KomikList['id'])):

                if idKomik == KomikList['id'][i]:

                    ditemukan = True

                    print("\nData Komik")
                    print("-" * 75)

                    printKomik(i)

                    lanjut = input("""
Lanjut update data? (Y/N) : 
""").upper()

                    if lanjut == 'Y':

                        judulKomik = input("Masukkan Judul Baru : ")
                        genreKomik = input("Masukkan Genre Baru : ")
                        ratingKomik = float(input("Masukkan Rating Baru : "))
                        authorKomik = input("Masukkan Author Baru : ")

                        save = input("""
Apakah data ingin diupdate? (Y/N) : 
""").upper()

                        if save == 'Y':

                            KomikList['judul'][i] = judulKomik
                            KomikList['genre'][i] = genreKomik
                            KomikList['rating'][i] = ratingKomik
                            KomikList['author'][i] = authorKomik

                            print("\nKomik berhasil diupdate!")

                            headerKomik()

                            for i in range(len(KomikList['id'])):

                                printKomik(i)

                        elif save == 'N':

                            print("\nData batal diupdate!")

                        else:

                            print("\nMenu tidak tersedia!")

                    elif lanjut == 'N':

                        print("\nUpdate dibatalkan!")

                    else:

                        print("\nMenu tidak tersedia!")

            if not ditemukan:

                print("ID tidak ditemukan!")

        elif menuUpdateKomik == 2:

            break

        else:

            print("Menu tidak tersedia!")

def deleteKomik():

    while True:

        menuDeleteKomik = int(input("""
1. Hapus Komik
2. Kembali

Pilih Menu : 
"""))

        if menuDeleteKomik == 1:

            headerKomik()

            for i in range(len(KomikList['id'])):

                printKomik(i)

            idKomik = input("\nMasukkan ID Komik : ").upper()

            ditemukan = False

            for i in range(len(KomikList['id'])):

                if idKomik == KomikList['id'][i]:

                    ditemukan = True

                    print("\nData Komik")
                    print("-" * 75)

                    printKomik(i)

                    delete = input("""
Apakah data ingin dihapus? (Y/N) : 
""").upper()

                    if delete == 'Y':

                        del KomikList['id'][i]
                        del KomikList['judul'][i]
                        del KomikList['genre'][i]
                        del KomikList['rating'][i]
                        del KomikList['author'][i]

                        print("\nKomik berhasil dihapus!")

                        headerKomik()

                        for i in range(len(KomikList['id'])):

                            printKomik(i)

                    elif delete == 'N':

                        print("\nData batal dihapus!")

                    else:

                        print("\nMenu tidak tersedia!")

            if not ditemukan:

                print("ID tidak ditemukan!")

        elif menuDeleteKomik == 2:

            break

        else:

            print("Menu tidak tersedia!")            

def listMenu():

    while True:

        menu = int(input("""
===== MENU UTAMA =====

1. Menu Komik
2. Tambah Komik
3. Update Komik
4. Hapus Komik
5. Keluar

Pilih Menu : 
"""))

        if menu == 1:

            showKomik()

        elif menu == 2:

            addKomik()

        elif menu == 3:

            updateKomik()

        elif menu == 4:

            deleteKomik()

        elif menu == 5:

            print("Terima kasih!")
            break

        else:

            print("Menu tidak tersedia!")


listMenu()