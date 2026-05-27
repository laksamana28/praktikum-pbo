import streamlit as st
import datetime
import pandas as pd

from model import Transaksi
from manajer_anggaran import AnggaranHarian
from konfigurasi import KATEGORI_PENGELUARAN


st.set_page_config(
    page_title="Catatan Pengeluaran",
    layout="wide"
)

anggaran = AnggaranHarian()

st.title("Aplikasi Pengeluaran Harian")

menu = st.sidebar.radio(
    "Pilih Menu",
    ["Tambah", "Riwayat", "Ringkasan"]
)

# ====================================
# MENU TAMBAH
# ====================================

if menu == "Tambah":

    st.header("Tambah Pengeluaran")

    with st.form("form_transaksi"):

        deskripsi = st.text_input("Deskripsi")

        kategori = st.selectbox(
            "Kategori",
            KATEGORI_PENGELUARAN
        )

        jumlah = st.number_input(
            "Jumlah",
            min_value=0.0,
            step=1000.0
        )

        tanggal = st.date_input(
            "Tanggal",
            value=datetime.date.today()
        )

        submit = st.form_submit_button("Simpan")

        if submit:

            transaksi = Transaksi(
                deskripsi,
                jumlah,
                kategori,
                tanggal
            )

            sukses = anggaran.tambah_transaksi(transaksi)

            if sukses:
                st.success("Data berhasil disimpan")
            else:
                st.error("Gagal menyimpan")


# ====================================
# MENU RIWAYAT
# ====================================

elif menu == "Riwayat":

    st.header("Riwayat Pengeluaran")

    df = anggaran.get_dataframe_transaksi()

    st.dataframe(df)

    st.subheader("Hapus Transaksi")

    id_hapus = st.number_input(
        "Masukkan ID",
        min_value=1,
        step=1
    )

    if st.button("Hapus"):

        sukses = anggaran.hapus_transaksi(id_hapus)

        if sukses:
            st.success("Transaksi berhasil dihapus")
            st.rerun()
        else:
            st.error("Gagal menghapus")


# ====================================
# MENU RINGKASAN
# ====================================

elif menu == "Ringkasan":

    st.header("Ringkasan Pengeluaran")

    total = anggaran.hitung_total_pengeluaran()

    st.metric(
        "Total Pengeluaran",
        f"Rp {total:,.0f}"
    )

    kategori = anggaran.get_pengeluaran_per_kategori()

    if kategori:

        df_kategori = pd.DataFrame(
            kategori.items(),
            columns=["Kategori", "Total"]
        )

        st.dataframe(df_kategori)

        st.bar_chart(
            df_kategori.set_index("Kategori")
        )