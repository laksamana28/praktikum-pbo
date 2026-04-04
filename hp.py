class HP:
    def __init__(self, merk, harga, stok):
        self.merk = merk
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"HP {self.merk} | Harga: Rp {self.harga} | Stok: {self.stok}")

    def beli(self, jumlah):
        if jumlah <= self.stok:
            total = self.harga * jumlah
            self.stok -= jumlah
            print(f"Berhasil membeli {jumlah} unit {self.merk}")
            print(f"Total bayar: Rp {total}")
        else:
            print("Stok tidak mencukupi")