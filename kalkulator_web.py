import streamlit as st
from PIL import Image

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Kalkulator Bobot Sapi",
    page_icon="🐄",
    layout="centered"
)

# --- Logo dan Judul ---
try:
    image = Image.open("unnamed.png")
    st.image(image, width=80)
except FileNotFoundError:
    st.warning("File logo 'unnamed.png' tidak ditemukan.")

st.title("🐄 Kalkulator Bobot Badan Sapi")
st.write("Aplikasi untuk estimasi bobot badan sapi potong.")
st.markdown("---")

# --- Pilihan Rumus ---
pilihan_rumus = st.selectbox(
    "Pilih rumus yang ingin Anda gunakan:",
    ("Rumus Modifikasi Schoorl (LD+18)", "Rumus Winter Indonesia (LD & PB)")
)

# --- Kolom Input Data ---
lingkar_dada = st.number_input("Masukkan Lingkar Dada / LD (cm):", min_value=0.1, step=1.0, format="%.1f")

panjang_badan = 0
if pilihan_rumus == "Rumus Winter Indonesia (LD & PB)":
    panjang_badan = st.number_input("Masukkan Panjang Badan / PB (cm):", min_value=0.1, step=1.0, format="%.1f")

# --- Tombol dan Perhitungan ---
if st.button("Hitung Estimasi Bobot", type="primary"):
    bobot = 0
    input_valid = True

    if pilihan_rumus == "Rumus Modifikasi Schoorl (LD+18)":
        if lingkar_dada > 0:
            bobot = ((lingkar_dada + 18) ** 2) / 100
        else:
            st.error("Masukkan nilai Lingkar Dada yang valid.")
            input_valid = False

    elif pilihan_rumus == "Rumus Winter Indonesia (LD & PB)":
        if lingkar_dada > 0 and panjang_badan > 0:
            bobot = (lingkar_dada ** 2 * panjang_badan) / 10815.15
        else:
            st.error("Masukkan nilai Lingkar Dada dan Panjang Badan yang valid.")
            input_valid = False

    if input_valid:
        st.metric(label="Hasil Estimasi Bobot Badan", value=f"{bobot:.2f} kg")

# --- Footer ---
st.divider()
st.caption("Dibuat oleh: **Alexander Kevin Sandiputra, S.Pt.** (SMK Negeri 2 Sukoharjo)")