from model import Transaksi

import database


class AnggaranHarian:

    def tambah_transaksi(self, transaksi):

        sql = """
        INSERT INTO transaksi
        (deskripsi, jumlah, kategori, tanggal)
        VALUES (?, ?, ?, ?)
        """

        params = (
            transaksi.deskripsi,
            transaksi.jumlah,
            transaksi.kategori,
            transaksi.tanggal.strftime("%Y-%m-%d")
        )

        result = database.execute_query(sql, params)

        return result is not None


    def get_dataframe_transaksi(self):

        sql = """
        SELECT
            id,
            tanggal,
            kategori,
            deskripsi,
            jumlah
        FROM transaksi
        ORDER BY id DESC
        """

        return database.get_dataframe(sql)


    def hitung_total_pengeluaran(self):

        sql = "SELECT SUM(jumlah) FROM transaksi"

        rows = database.fetch_query(sql)

        if rows[0][0] is None:
            return 0

        return rows[0][0]


    def get_pengeluaran_per_kategori(self):

        sql = """
        SELECT kategori, SUM(jumlah)
        FROM transaksi
        GROUP BY kategori
        """

        rows = database.fetch_query(sql)

        hasil = {}

        for row in rows:
            hasil[row[0]] = row[1]

        return hasil


    def hapus_transaksi(self, id_transaksi):

        sql = "DELETE FROM transaksi WHERE id = ?"

        result = database.execute_query(
            sql,
            (id_transaksi,)
        )

        return result is not None