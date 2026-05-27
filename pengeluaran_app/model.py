import datetime


class Transaksi:

    def __init__(
        self,
        deskripsi,
        jumlah,
        kategori,
        tanggal,
        id_transaksi=None
    ):

        self.id = id_transaksi

        self.deskripsi = deskripsi

        self.jumlah = jumlah

        self.kategori = kategori

        self.tanggal = tanggal

    def to_dict(self):

        return {
            "deskripsi": self.deskripsi,
            "jumlah": self.jumlah,
            "kategori": self.kategori,
            "tanggal": self.tanggal.strftime("%Y-%m-%d")
        }