class Barang:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

class ItemKeranjang:
    def __init__(self, barang, jumlah):
        self.barang = barang
        self.jumlah = jumlah
        self.subtotal = barang.harga * jumlah

class Keranjang:
    def __init__(self):
        self.items = []
        
    def tambah_barang(self, barang, jumlah):
        item = ItemKeranjang(barang, jumlah)
        self.items.append(item)
        print(f"\nBerhasil menambahkan {jumlah} {barang.nama} ke keranjang")
        
    def hitung_total(self):
        total = sum(item.subtotal for item in self.items)
        print(f"\nTotal belanja: Rp {total:,}")
        return total
    
    def tampilkan_daftar(self):
        if not self.items:
            print("\nKeranjang masih kosong!")
            return
            
        print("\nDaftar Belanja:")
        print("=" * 50)
        print("Kode\tNama\t\tHarga\tJumlah\tSubtotal")
        print("-" * 50)
        for item in self.items:
            print(f"{item.barang.kode}\t{item.barang.nama}\t\t{item.barang.harga}\t{item.jumlah}\t{item.subtotal}")
        print("-" * 50)
        print(f"Total: Rp {self.hitung_total():,}")
        
    def cetak_struk(self):
        if not self.items:
            print("\nKeranjang masih kosong!")
            return
            
        print("\n" + "="*50)
        print("\tSTRUK BELANJA")
        print("="*50)
        print("Kode\tNama\t\tHarga\tJumlah\tSubtotal")
        print("-"*50)
        for item in self.items:
            print(f"{item.barang.kode}\t{item.barang.nama}\t\t{item.barang.harga}\t{item.jumlah}\t{item.subtotal}")
        print("-"*50)
        print(f"Total Pembayaran: Rp {self.hitung_total():,}")
        print("="*50)
        print("Terima kasih telah berbelanja!")
        print("="*50)

def tampilkan_menu():
    print("\nMENU PROGRAM KASIR")
    print("1. Tambah Barang ke Keranjang")
    print("2. Tampilkan Daftar Barang")
    print("3. Hitung Total Harga")
    print("4. Cetak Struk")
    print("5. Keluar")
    return input("Pilih menu (1-5): ")

def main():
    # Inisialisasi daftar barang yang tersedia
    daftar_barang = [
        Barang("B01", "parfum", 20000),
        Barang("B02", "air mineral", 5000),
        Barang("B03", "sabun wajah   ", 15000),
        Barang("B04", "Sabun mandi    ", 6000),
        Barang("B05", "suncreen   ", 25000),
    ]
    
    # Buat keranjang baru
    keranjang = Keranjang()
    
    while True:
        pilihan = tampilkan_menu()
        
        if pilihan == "1":
            # Tampilkan barang yang tersedia
            print("\nDaftar Barang Tersedia:")
            print("Kode\tNama\t\t        Harga")
            for barang in daftar_barang:
                print(f"{barang.kode}\t{barang.nama}\t\t{barang.harga}")
            
            # Input dari user
            kode = input("Masukkan kode barang: ")
            jumlah = int(input("Masukkan jumlah: "))
            
            # Cari barang berdasarkan kode
            barang = next((b for b in daftar_barang if b.kode == kode), None)
            if barang:
                keranjang.tambah_barang(barang, jumlah)
            else:
                print("\nBarang tidak ditemukan!")
                
        elif pilihan == "2":
            keranjang.tampilkan_daftar()
            
        elif pilihan == "3":
            keranjang.hitung_total()
            
        elif pilihan == "4":
            keranjang.cetak_struk()
            
        elif pilihan == "5":
            print("\nTerima kasih telah menggunakan program kasir!")
            break
            
        else:
            print("\nPilihan tidak valid!")

if __name__ == "__main__":
    main()