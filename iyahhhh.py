import streamlit as st
import random

# Konfigurasi halaman
st.set_page_config(page_title="💧 Kalkulator Kebutuhan Air Harian", layout="centered")

# CSS untuk latar belakang dan font dengan warna yang lebih cerah & menarik
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0.75)),
                    url('https://images.unsplash.com/photo-1532009324734-20a7a5813719?auto=format&fit=crop&w=1400&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: #F5F5F5 !important;
    }

    h1, h3 {
        color: #00FFCC;
    }

    .perhitungan-selesai {
        color: #00FA9A; /* Medium spring green */
    }

    .catatan {
        color: #FF69B4; /* Hot pink */
    }

    .pengingat {
        color: #FFD700; /* Gold */
    }

    .tips {
        color: #7FFFD4; /* Aquamarine */
    }

    .watermark {
        color: #D3D3D3; /* Light grey */
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("""  
    <h1 style='text-align: center;'>💧🐧 Kalkulator Kebutuhan Air Harian 🥤🍉</h1>
    <p style='text-align: center;'>Yuk hitung berapa banyak kamu harus minum biar nggak jadi kaktus! 🌵➡💦</p>
""", unsafe_allow_html=True)

# Penjelasan awal
st.markdown("""  
Kalkulator ini membantu kamu memperkirakan kebutuhan air harian berdasarkan:

- 🎂 *Umur*  
- 🚻 *Jenis kelamin*  
- ⚖️ *Berat badan*  
- 🤸 *Aktivitas fisik*  
- ☀️ *Iklim tempat tinggal*
- 😊 *Kondisi kesehatan*

---
## 📚 Informasi Tentang Air dan Hidrasi 💧

**Kenapa Air Itu Penting?🤷‍♀️🤷‍♂️**  
Air adalah komponen utama tubuh manusia yang mendukung berbagai fungsi vital, seperti mengatur suhu tubuh, mendukung proses pencernaan, serta menjaga keseimbangan elektrolit. Tanpa cukup air, tubuh kita tidak dapat berfungsi dengan optimal.

**Manfaat Minum Air😲**:
1. **Meningkatkan Konsentrasi dan Fokus** 🧠  
2. **Membantu Pencernaan** 💪  
3. **Mengatur Suhu Tubuh** 🌡️  
4. **Mencegah Sakit Kepala** 🤕

""")

# Form input
umur = st.number_input("🎂 Umur (tahun)", min_value=0, max_value=120, value=25)
jenis_kelamin = st.selectbox("🚻 Jenis Kelamin", ["👦 Laki-laki", "👧 Perempuan"])
berat_badan = st.number_input("⚖️ Berat Badan (kg)", min_value=1.0, max_value=200.0, value=60.0)
aktivitas = st.selectbox("🤸 Tingkat Aktivitas Fisik", [
    "Ringan (pekerjaan ringan, hanya kuliah teori) 🐌",
    "Sedang (kuliah sedikit praktik) 🏃‍♂️",
    "Berat (kuliah full praktik, lanjut laprak) 🏋️"
])
iklim = st.selectbox("☀️ Iklim Tempat Tinggal", [
    "Sedang/Dingin 🧣",
    "Panas (tropis, kering, atau sangat lembap) 🏖️"
])

# Kondisi Kesehatan
kondisi_kesehatan = st.selectbox("😊Apakah kamu memiliki kondisi kesehatan yang mempengaruhi kebutuhan air?", 
                                  ["Tidak ada", "Diabetes", "Hipertensi", "Penyakit ginjal"])

# Faktor iklim: memberikan saran minuman berdasarkan suhu tempat tinggal
if iklim == "Sedang/Dingin 🧣":
    saran_minuman = "☕ Teh hangat atau sup bisa menjadi pilihan yang menyegarkan! Jangan lupa tetap minum air putih."
elif iklim == "Panas (tropis, kering, atau sangat lembap) 🏖️":
    saran_minuman = "🥥 Air kelapa, infused water dengan lemon, atau air putih dingin untuk menjaga tubuh tetap terhidrasi!"

# Menampilkan saran minuman berdasarkan iklim
st.markdown(f"💡 Saran minuman berdasarkan iklim tempat tinggalmu: {saran_minuman}")

submitted = st.button("🚰 Hitung Kebutuhan Air!")

# Proses perhitungan
if submitted:
    with st.spinner("⏳ Menghitung kebutuhan air harian kamu... 🕒"):

        kebutuhan_dasar_min = 30 * berat_badan / 1000
        kebutuhan_dasar_max = 40 * berat_badan / 1000

        faktor_aktivitas = 1.1 if aktivitas.startswith("Ringan") else 1.25 if aktivitas.startswith("Sedang") else 1.35
        faktor_iklim = 1.1 if iklim.startswith("Panas") else 1.0

        # Menyesuaikan kebutuhan berdasarkan kondisi kesehatan
        if kondisi_kesehatan == "Diabetes":
            faktor_kesehatan = 1.2  # Tambahkan faktor untuk kondisi diabetes
            st.warning("⚠️ Kondisi Diabetes membutuhkan hidrasi yang lebih tinggi! Pastikan untuk minum cukup air.")
        elif kondisi_kesehatan == "Hipertensi":
            faktor_kesehatan = 1.1  # Tambahkan faktor untuk kondisi hipertensi
            st.warning("⚠️ Hipertensi memerlukan perhatian khusus terhadap hidrasi. Pastikan tidak dehidrasi.")
        elif kondisi_kesehatan == "Penyakit ginjal":
            faktor_kesehatan = 1.3  # Tambahkan faktor untuk kondisi ginjal
            st.warning("⚠️ Penyakit ginjal memerlukan lebih banyak perhatian terhadap hidrasi. Minumlah air secara bertahap.")
        else:
            faktor_kesehatan = 1.0  # Tidak ada faktor khusus jika kondisi kesehatan tidak ada
            
        # Menambahkan faktor suhu minuman dalam perhitungan
        kebutuhan_total_min = kebutuhan_dasar_min * faktor_aktivitas * faktor_iklim * faktor_kesehatan
        kebutuhan_total_max = kebutuhan_dasar_max * faktor_aktivitas * faktor_iklim * faktor_kesehatan

        # Hasil
        st.markdown("<h3 class='perhitungan-selesai'>🎉 Perhitungan selesai! 🎉</h3>", unsafe_allow_html=True)
        st.markdown("<h3>💡 Hasil Perkiraan Kamu: 🥤</h3>", unsafe_allow_html=True)
        st.markdown(f"""
        <div class="perhitungan-selesai">
        - 🔄 Kebutuhan Air Harian kamu adalah: <strong>{kebutuhan_total_min:.2f} - {kebutuhan_total_max:.2f} L/hari</strong>
        </div>
        """, unsafe_allow_html=True)

        # Catatan
        st.markdown("""  
        <div class="catatan">
            📌 <strong>Catatan:</strong><br>
            Nilai ini merupakan estimasi kebutuhan air harian. Kebutuhan sebenarnya bisa bervariasi tergantung kondisi kesehatan, konsumsi makanan dan minuman lain, serta cuaca harian. Konsultasikan dengan ahli gizi atau tenaga medis untuk kebutuhan spesifik.
        </div>
        """, unsafe_allow_html=True)

        # Fitur mode "Emergency Hydration"
        is_emergency = ("🔥 Situasi darurat🫨 (setelah olahraga/di tempat panas)?")
        st.markdown("🚨 **Penting!** Jika kamu baru selesai berolahraga atau berada di suhu yang sangat panas, kamu harus meningkatkan asupan air hingga 2 kali lipat dari kebutuhan normal!")

        # Pengingat
        reminder_frequency = st.slider("⏰ Pengingat Minum Air (dalam menit)", min_value=15, max_value=120, value=60, step=15)
        st.markdown(f"<p class='pengingat'>⏰ Setiap {reminder_frequency} menit, kamu disarankan untuk minum air segelas! 🍶</p>", unsafe_allow_html=True)

        # Menu rekomendasi
        st.subheader("🍽️ Rekomendasi Menu untuk Hidrasi yang Lebih Baik: 🥗🍉")
        st.markdown("""
        - 🍉 **Buah-buahan**: Semangka, melon, dan jeruk kaya akan kandungan air!
        - 🥗 **Sayuran Hijau**: Selada, timun, dan bayam juga membantu tubuh tetap terhidrasi.
        - 🧃 **Minuman Sehat**: Teh herbal atau infused water dengan irisan lemon atau mentimun.
        - 🍶 **Air Kelapa**: Menyegarkan dan penuh elektrolit alami!
        """)

        # Tips
        st.markdown("<p class='tips'>🧊 Tips: Minumlah air secara bertahap sepanjang hari, jangan sekaligus kayak minum sirup waktu buka puasa! 😆</p>", unsafe_allow_html=True)

        # Tips profesional
        st.subheader("🩺 Tips Profesional dari Pakar Kesehatan: 💼")
        st.markdown("""
        <div style='background-color:transparent; padding:15px; border-left:5px solid #f4c430; border-radius:10px;'>
            <ul>
                <li>👩‍⚕️: "Minumlah air sebelum merasa haus. 🌊"</li>
                <li>🧑‍⚕️: "Selalu bawa tumbler air ke mana pun kamu pergi. 🚶‍♂️💧"</li>
                <li>👨‍⚕️: "Perhatikan warna urinmu. Urin gelap = kurang minum. 🔍🚽"</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Fun fact
        st.subheader("💡 Fun Fact tentang Air & Tubuhmu! 🤓")
        fakta_air = [
            "🧠 Otak manusia terdiri dari sekitar 75% air!",
            "💧 Kehilangan hanya 2% cairan tubuh bisa menurunkan fokus dan konsentrasi.",
            "🧃 Air membantu mengangkut nutrisi dan oksigen ke seluruh tubuh.",
            "🚽 Minum cukup air membantu ginjal menyaring limbah dengan lebih efektif.",
            "🔥 Air membantu mengatur suhu tubuh lewat keringat.",
            "😴 Minum cukup air bisa membantu kualitas tidurmu jadi lebih baik!",
            "👶 Bayi memiliki persentase air lebih tinggi daripada orang dewasa, hingga 78% dari berat tubuh!"
        ]
        st.markdown(f"<p class='tips'>🧠 {random.choice(fakta_air)}</p>", unsafe_allow_html=True)

# Watermark
st.markdown("""  
    <hr style="border: 1px solid #00BFFF; margin-top: 40px;">
    <p class="watermark" style="text-align: center; font-size: 16px;">
        🐬 Dibuat oleh <strong>LPK 7</strong>💙<br>
        <b>Ifta 🍄, Daviona ✨, Nadila 🎀, Vania 🌸, Sulthan 🎩</b><br>
    </p>
    <p class="watermark" style="text-align: center; font-size: 13px;">
        <i>Design &amp; Kelompok 7 LPK • 2025</i>
    </p>
""", unsafe_allow_html=True)

