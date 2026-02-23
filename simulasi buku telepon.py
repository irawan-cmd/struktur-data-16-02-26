def buku_telepon():
    kontak = {}
    
    while True:
        print("\n1. Tambah Kontak")
        print("2. Cari Kontak")
        print("3. Tampilkan Semua")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            nama = input("Nama: ")
            nomor = input("Nomor: ")
            kontak[nama] = nomor
            print("Kontak berhasil ditambahkan.")
            
        elif pilihan == "2":
            nama = input("Nama yang dicari: ")
            if nama in kontak:
                print("Nomor:", kontak[nama])
            else:
                print("Kontak tidak ditemukan.")
                
        elif pilihan == "3":
            if not kontak:
                print("Belum ada kontak.")
            else:
                for nama, nomor in kontak.items():
                    print(nama, ":", nomor)
                    
        elif pilihan == "4":
            print("Program selesai.")
            break
            
        else:
            print("Pilihan tidak valid.")

# Jalankan program
buku_telepon()
