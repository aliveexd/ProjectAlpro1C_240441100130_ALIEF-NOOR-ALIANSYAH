murid = []
nis = 1
from datetime import datetime

def cari_murid(nis_murid):
    siswa = next((s for s in murid if s['NIS'] == nis_murid), None)
    if siswa:
        print("\nMurid Ditemukan:")
        print(f"Tahun Ajaran     : {siswa['Tahun Ajaran']}")
        print(f"NIS              : {siswa['NIS']}")
        print(f"Nama             : {siswa['Nama']}")
        print(f"Asal             : {siswa['Asal']}")
        print(f"Status Beasiswa  : {siswa['Status Beasiswa']}")
        print(f"PPDB             : {siswa['PPDB']}")
        print(f"SPP Bulan Dibayar: {siswa['SPP']} Bulan")
        return siswa
    else:
        print("NIS Tidak Ditemukan.")
        return None

def tambah(tahun, nama, asal, beasiswa, ppdb, admin):
    global nis
    pendaftar = {
        'Tahun Ajaran': tahun,
        'NIS': nis,
        'Nama': nama,
        'Asal': asal,
        'Status Beasiswa': beasiswa,
        'PPDB': ppdb,
        'SPP': 0,
        'Penanggung Jawab' : admin
    }
    murid.append(pendaftar)
    print(f"\nMurid Dengan Nama {nama} Berhasil Terdaftar Dengan NIS {nis}.")
    nis += 1

def input_data(tahun, admin):
    while True:
        nama = input("Masukkan Nama Lengkap Murid: ").strip()
        if nama:
            break
        print("Nama Murid Tidak Boleh Kosong, Harap Masukkan Nama.")

    while True:
        asal = input("Masukkan Asal Daerah Murid: ").strip()
        if asal:
            break
        print("Asal Daerah Murid Harus Diisi.")

    while True:
        try:
            nilai = float(input("Masukkan Nilai Rata-Rata Rapot Murid: "))
            if 85 <= nilai <= 100:
                beasiswa = "Mendapatkan Beasiswa"
                print(f"Selamat {nama}, {beasiswa}.")
                break
            elif nilai > 100:
                print("Nilai Tidak Valid, Nilai Tidak Bisa Melebihi 100.")
            elif nilai <= 0:
                print("Nilai Harus Berupa Bilangan Positif.")
            else:
                beasiswa = "Tidak Mendapatkan Beasiswa"
                print(f"Anda {beasiswa}.")
                break
        except ValueError:
            print("Input Harus Berupa Angka.")

    while True:
        try:
            daftar = int(input("Masukkan Uang Untuk Pembayaran PPDB (Rp. 700.000): "))
            if daftar == 700000:
                ppdb = "Lunas"
                print(f"{nama} Telah Terdaftar di SMK Benowo 1.")
                tambah(tahun, nama, asal, beasiswa, ppdb, admin)
                break
            elif daftar > 700000:
                print(f"Kembalian Rp. {daftar - 700000}")
                ppdb = "Lunas"
                print(f"{nama} Telah Terdaftar di SMK Benowo 1.")
                tambah(tahun, nama, asal, beasiswa, ppdb, admin)
                break
            elif daftar < 0:
                print("Uang Yang Diinputkan Tidak Boleh Negatif.")
            else:
                ppdb = "Anda gagal mendaftar SMK Benowo 1, dikarenakan uang anda mendaftar PPDB tidak tercukupi."
                print(ppdb)
                break
        except ValueError:
            print("Input Harus Berupa Bilangan Genap.")

def tampilkan(tahun_ajaran=None):
    if not murid:
        print("\nBelum Ada Murid yang Terdaftar.")
        return

    if tahun_ajaran is None:
        print("\nDaftar Semua Murid:")
        daftar_murid = murid
    else:
        daftar_murid = [siswa for siswa in murid if siswa['Tahun Ajaran'] == tahun_ajaran]
        if not daftar_murid:
            print(f"\nTidak Ada Murid yang Terdaftar di Tahun Ajaran {tahun_ajaran}.")
            return
        print(f"\nDaftar Murid Tahun Ajaran {tahun_ajaran}:")

    for i, siswa in enumerate(daftar_murid, start=1):
        print(f"\nMurid ke-{i}:")
        print(f"Tahun Ajaran     : {siswa['Tahun Ajaran']}")
        print(f"NIS              : {siswa['NIS']}")
        print(f"Nama             : {siswa['Nama']}")
        print(f"Asal             : {siswa['Asal']}")
        print(f"Status Beasiswa  : {siswa['Status Beasiswa']}")
        print(f"PPDB             : {siswa['PPDB']}")
        print(f"SPP Bulan Dibayar: {siswa['SPP']} Bulan")
        print(f"Penanggung Jawab : {siswa['Penanggung Jawab']}")

        if 'Tanggal Pembayaran' in siswa and siswa['Tanggal Pembayaran']:
            tanggal_terbaru = siswa['Tanggal Pembayaran'][-1]
            print(f"Pembayaran SPP Terbaru: {tanggal_terbaru}")


def bayar_spp():
    if not murid:
        print("\nBelum Ada Murid yang Terdaftar.")
        return
    while True:
        try:
            nis_spp = int(input("\nMasukkan NIS Untuk Pembayaran SPP: "))
            siswa = cari_murid(nis_spp)
            if siswa:
                if siswa['Status Beasiswa'] == "Mendapatkan Beasiswa":
                    print("Anda Tidak Perlu Membayar SPP Karena Anda Mendapatkan Beasiswa.")
                elif siswa['SPP'] >= 12:
                    print("SPP Anda Untuk 12 Bulan Sudah Lunas.")
                else:
                    print(f"\nSPP Saat Ini Sudah Dibayar Untuk {siswa['SPP']} Bulan.")
                    while True:
                        bayar = input("Apakah Anda Ingin Membayar 1 Bulan SPP Sebesar Rp. 300.000 (ketik 1 jika lanjut ke pembayaran): ").strip()
                        if bayar == '1':
                            while True:
                                try:
                                    nominal = int(input("Masukkan Jumlah Uang Untuk Membayar SPP: "))
                                    if nominal == 300000:
                                        siswa['SPP'] += 1
                                        tanggal_pembayaran = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                        print(f"SPP berhasil dibayar untuk bulan ke-{siswa['SPP']} pada {tanggal_pembayaran}.")
                                        if 'Tanggal Pembayaran' not in siswa:
                                            siswa['Tanggal Pembayaran'] = []
                                        siswa['Tanggal Pembayaran'].append(tanggal_pembayaran)
                                        return
                                    elif nominal > 300000:
                                        print(f"Kembalian Anda: {nominal - 300000}")
                                        siswa['SPP'] += 1
                                        tanggal_pembayaran = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                        print(f"SPP berhasil dibayar untuk bulan ke-{siswa['SPP']} pada {tanggal_pembayaran}.")
                                        if 'Tanggal Pembayaran' not in siswa:
                                            siswa['Tanggal Pembayaran'] = []
                                        siswa['Tanggal Pembayaran'].append(tanggal_pembayaran)
                                        return
                                    else:
                                        print("Maaf Uang Anda Tidak Cukup.")
                                except ValueError:
                                    print("Nominal Uang Tidak Valid.")
                        else:
                            print("Pembayaran SPP dibatalkan.")
                            return
        except ValueError:
            print("Input tidak valid. Silakan masukkan NIS yang benar.")


def hapus():
    if not murid:
        print("\nBelum Ada Murid Yang Terdaftar.")
        return
    while True:
        try:
            nis_hapus = int(input("Masukkan NIS Murid Yang Ingin Dihapus: "))
            siswa = cari_murid(nis_hapus)
            if siswa:
                delete = input("Apakah Anda Yakin Menghapus Data Dari Murid Tersebut (ketik 1 untuk menghapus): ").strip()
                if delete == "1":
                    murid.remove(siswa)
                    print("Data Murid Telah Dihapus.")
                    break
                else:
                    print("Data Murid Tidak Jadi Dihapus.")
                    break
        except ValueError:
            print("NIS Harus Berupa Angka.")

def ganti_tahun_ajaran():
    while True:
        try:
            tahun_baru = int(input("Masukkan Tahun Ajaran Baru: "))
            print(f"Tahun Ajaran Diubah Menjadi {tahun_baru}.")
            return tahun_baru
        except ValueError:
            print("Input Tidak Valid. Harap Masukkan Angka Tahun yang Benar.")

def tampilkan(tahun_ajaran=None):
    if not murid:
        print("\nBelum Ada Murid yang Terdaftar.")
        return

    if tahun_ajaran is None:
        print("\nDaftar Semua Murid:")
        daftar_murid = murid
    else:
        daftar_murid = [siswa for siswa in murid if siswa['Tahun Ajaran'] == tahun_ajaran]
        if not daftar_murid:
            print(f"\nTidak Ada Murid yang Terdaftar di Tahun Ajaran {tahun_ajaran}.")
            return
        print(f"\nDaftar Murid Tahun Ajaran {tahun_ajaran}:")

    for i, siswa in enumerate(daftar_murid, start=1):
        print(f"\nMurid ke-{i}:")
        print(f"Tahun Ajaran     : {siswa['Tahun Ajaran']}")
        print(f"NIS              : {siswa['NIS']}")
        print(f"Nama             : {siswa['Nama']}")
        print(f"Asal             : {siswa['Asal']}")
        print(f"Status Beasiswa  : {siswa['Status Beasiswa']}")
        print(f"PPDB             : {siswa['PPDB']}")
        print(f"SPP Bulan Dibayar: {siswa['SPP']} Bulan")
        print(f"Penanggung Jawab : {siswa['Penanggung Jawab']}")

        if 'Tanggal Pembayaran' in siswa and siswa['Tanggal Pembayaran']:
            tanggal_terbaru = siswa['Tanggal Pembayaran'][-1]
            print(f"Pembayaran SPP Terbaru: {tanggal_terbaru}")


def menu(admin, tahun):
    while True:
        try:
            print("\n=== MENU APLIKASI ADMINISTRASI SMK BENOWO 1 ===")
            print(f"Admin: {admin}")
            print(f"Tahun Ajaran: {tahun}")
            print("1. Tambah Murid")
            print("2. Tampilkan Semua Murid")
            print("3. Tampilkan Murid Berdasarkan Tahun Ajaran")
            print("4. Update Bayar SPP")
            print("5. Hapus Murid")
            print("6. Ganti Tahun Ajaran")
            print("7. Log Out")
            pilihan = int(input("Pilih Menu (1-7): "))
            if pilihan == 1:
                input_data(tahun, admin)
            elif pilihan == 2:
                tampilkan()
            elif pilihan == 3:
                try:
                    tahun_filter = int(input("Masukkan Tahun Ajaran yang Ingin Ditampilkan: "))
                    tampilkan(tahun_filter)
                except ValueError:
                    print("Tahun Ajaran Harus Berupa Angka.")
            elif pilihan == 4:
                bayar_spp()
            elif pilihan == 5:
                hapus()
            elif pilihan == 6:
                tahun = ganti_tahun_ajaran()
            elif pilihan == 7:
                break
            else:
                print("Harap Masukkan Opsi Yang Tersedia.")
        except ValueError:
            print("Input Tidak Valid. Harap Masukkan Angka.")

print("\n=== SELAMAT DATANG DI APLIKASI ADMINISTRASI SMK BENOWO 1 ===")
while True:
    login = input("Masukkan Username Anda Untuk Log In atau Ketik 1 Untuk Keluar: ").lower().strip()
    if login in ["amin", "alief"]:
        print(f"Selamat Datang {login.capitalize()}")
        tahun = int(input("Masukkan Tahun Ajaran: "))
        menu(login.capitalize(), tahun)
    elif login == "1":
        print("Terima Kasih.")
        break
    else:
        print("Username Tidak Terdaftar.")