import streamlit as st
import matplotlib.pyplot as plt
import time

# Konfigurasi halaman
st.set_page_config(page_title="💧 Kalkulator Kebutuhan Air Lucu", layout="centered")

# Tambahkan latar belakang bergambar air minum
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('https://images.unsplash.com/photo-1589467235304-46069d5a3a4a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1650&q=80');
        background-size: cover;
        background-attachment: fixed;
    }}
    .block-container {{
        background-color: rgba(255, 255, 255, 0.90);
        padding: 2rem;
        border-radius: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown("""
    <h1 style='text-align: center; color: #00BFFF;'>💧🐧 Kalkulator Kebutuhan Air Harian Lucu 🥤🍉</h1>
    <p style='text-align: center;'>Yuk hitung berapa banyak kamu harus minum biar nggak jadi kaktus! 🌵➡💦</p>
""", unsafe_allow_html=True)

# Penjelasan awal
st.markdown("""
Kalkulator ini membantu kamu memperkirakan kebutuhan air harian berdasarkan:
- 🎂 *Umur*
- 🚻 *Jenis kelamin*
- ⚖ *Berat badan*
- 🤸 *Aktivitas fisik*
- ☀ *Iklim tempat tinggal*
""")

# Form input
with st.form("form_air"):
    umur = st.number_input("🎂 Umur (tahun)", min_value=0, max_value=120, value=25)
    jenis_kelamin = st.selectbox("🚻 Jenis Kelamin", ["👦 Laki-laki", "👧 Perempuan"])
    berat_badan = st.number_input("⚖ Berat Badan (kg)", min_value=1.0, max_value=200.0, value=60.0)

    aktivitas = st.selectbox("🤸 Tingkat Aktivitas Fisik", [
        "Ringan (pekerjaan ringan, sedikit olahraga)",
        "Sedang (olahraga 3–5 kali/minggu)",
        "Berat (olahraga intens atau pekerjaan berat)"
    ])

    iklim = st.selectbox("☀ Iklim Tempat Tinggal", [
        "Sedang/Dingin",
        "Panas (tropis, kering, atau sangat lembap)"
    ])

    submitted = st.form_submit_button("🚰 Hitung Kebutuhan Air!")

# Proses perhitungan
if submitted:
    with st.spinner("⏳ Menghitung kebutuhan air harian kamu..."):
        time.sleep(1.5)

        # Dasar
        kebutuhan_dasar_min = 30 * berat_badan / 1000
        kebutuhan_dasar_max = 40 * berat_badan / 1000

        # Aktivitas
        faktor_aktivitas = 1.1 if aktivitas.startswith("Ringan") else 1.25 if aktivitas.startswith("Sedang") else 1.35

        # Iklim
        faktor_iklim = 1.1 if iklim.startswith("Panas") else 1.0

        # Total
        kebutuhan_total_min = kebutuhan_dasar_min * faktor_aktivitas * faktor_iklim
        kebutuhan_total_max = kebutuhan_dasar_max * faktor_aktivitas * faktor_iklim

        # Output
        st.success("🎉 Perhitungan selesai!")
        st.subheader("💡 Hasil Perkiraan Kamu:")
        st.write(f"- 💧 Kebutuhan dasar: *{kebutuhan_dasar_min:.2f} - {kebutuhan_dasar_max:.2f} L/hari*")
        st.write(f"- 🔄 Setelah penyesuaian: *{kebutuhan_total_min:.2f} - {kebutuhan_total_max:.2f} L/hari*")

        # Catatan tambahan
        st.markdown("""
        <div style='background-color:#e6f7ff; padding:10px; border-left:5px solid #00BFFF;'>
            📌 <strong>Catatan:</strong><br>
            Nilai ini merupakan estimasi kebutuhan air harian. Kebutuhan sebenarnya bisa bervariasi tergantung kondisi kesehatan, konsumsi makanan dan minuman lain, serta cuaca harian. Konsultasikan dengan ahli gizi atau tenaga medis untuk kebutuhan spesifik.
        </div>
        """, unsafe_allow_html=True)

        # Grafik
        st.subheader("📊 Visualisasi Kebutuhan Air")
        fig, ax = plt.subplots()
        kategori = ['Min (Dasar)', 'Max (Dasar)', 'Min (Total)', 'Max (Total)']
        nilai = [kebutuhan_dasar_min, kebutuhan_dasar_max, kebutuhan_total_min, kebutuhan_total_max]
        warna = ['skyblue', 'dodgerblue', 'lightgreen', 'green']
        ax.bar(kategori, nilai, color=warna)
        ax.set_ylabel('Liter per Hari')
        ax.set_title('💦 Kebutuhan Air Harian')
        st.pyplot(fig)

        # Tips lucu
        st.info("🧊 Tips: Minumlah air secara bertahap sepanjang hari, jangan sekaligus kayak minum sirup waktu buka puasa! 😆")

# Watermark stylist
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 16px; color: grey;'>
    🐬 Dibuat oleh <strong>LPK 7</strong> dengan cinta 💙:<br>
    <b>Daviona ✨, Ifta 🧋, Nadila 🎀, Vania 🌸, Sulthan 🎩</b><br>
    <i>Tim paling segar di antara deadline! 🍹</i>
    </p>
""", unsafe_allow_html=True)
