import streamlit as st

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

        # Grafik (Placeholder - grafik bisa ditambahkan sesuai kebutuhan dengan matplotlib atau altair)
        st.subheader("📊 Visualisasi Kebutuhan Air")

        # Pengingat Minum Air
        reminder_frequency = st.slider("⏰ Pengingat Minum Air (dalam menit)", min_value=15, max_value=120, value=60, step=15)
        st.warning(f"⏰ Setiap {reminder_frequency} menit, kamu disarankan untuk minum air segelas! 🍶")

        # Rekomendasi Menu
        st.subheader("🍽️ Rekomendasi Menu untuk Hidrasi yang Lebih Baik:")
        st.markdown("""
        - 🍉 **Buah-buahan**: Semangka, melon, dan jeruk kaya akan kandungan air!
        - 🥗 **Sayuran Hijau**: Selada, timun, dan bayam juga membantu tubuh tetap terhidrasi.
        - 🧃 **Minuman Sehat**: Teh herbal atau infused water dengan irisan lemon atau mentimun.
        - 🍶 **Air Kelapa**: Menyegarkan dan penuh elektrolit alami!
        """)

        # Streak Minum Air (Menampilkan streak jika pengguna sudah melakukan beberapa kali)
        streak = st.number_input("🎉 Berapa banyak hari kamu sudah konsisten minum air?", min_value=0, value=0)
        if streak > 0:
            st.success(f"🔥 Kamu sudah minum air selama {streak} hari berturut-turut! Keep going! 🌟💧")

        # Kuis Hidrasi
        st.subheader("💡 Kuis Hidrasi")
        if 'quiz_answer' not in st.session_state:
            st.session_state.quiz_answer = None

        # Check if the quiz has been answered before
        if st.session_state.quiz_answer is None:
            kuis_answer = st.selectbox(
                "Apa manfaat utama dari hidrasi yang cukup?", 
                ["Mengatur suhu tubuh 🧊", "Meningkatkan konsentrasi 🧠", "Mencegah dehidrasi 🏜️"]
            )
            # Store the answer in session state when submitted
            if st.button("🎯 Submit Jawaban"):
                st.session_state.quiz_answer = kuis_answer
                if kuis_answer == "Mencegah dehidrasi 🏜️":
                    st.success("🎉 Jawaban benar! Hidrasi membantu mencegah dehidrasi yang bisa mengganggu kesehatan kamu!")
                else:
                    st.error("❌ Jawaban salah! Hidrasi membantu mencegah dehidrasi yang bisa mengganggu kesehatan kamu.")
        else:
            # Show the result after answering the quiz
            st.success(f"👏 Kamu sudah menyelesaikan kuis! Jawaban kamu: {st.session_state.quiz_answer}")
            st.button("🔄 Ulangi Kuis", on_click=lambda: st.session_state.update({'quiz_answer': None}))

        # Tips lucu
        st.info("🧊 Tips: Minumlah air secara bertahap sepanjang hari, jangan sekaligus kayak minum sirup waktu buka puasa! 😆")

        # Tips dari pakar kesehatan
        st.subheader("🩺 Tips Profesional dari Pakar Kesehatan")
        st.markdown("""
        <div style='background-color:#fff8e1; padding:15px; border-left:5px solid #f4c430; border-radius:10px;'>
            <ul>
                <li>👩‍⚕️ <strong>Dr. Hydrina Segar</strong>: "Minumlah air sebelum merasa haus. Haus adalah tanda tubuh sudah mulai kekurangan cairan."</li>
                <li>🧑‍⚕️ <strong>Dr. Aqua Vita</strong>: "Bawalah botol air sendiri ke mana pun kamu pergi. Ini membantu kamu tetap terhidrasi sepanjang hari."</li>
                <li>👨‍⚕️ <strong>Dr. Sehat Jernih</strong>: "Perhatikan warna urinmu! Jika terlalu gelap, itu tandanya kamu perlu minum lebih banyak."</li>
                <li>👩‍⚕️ <strong>Dr. Minerva Airin</strong>: "Orang dengan penyakit tertentu (seperti ginjal atau jantung) harus berkonsultasi dulu sebelum menaikkan asupan cairan."</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Watermark stylist
st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 16px; color: grey;'>
    🐬 Dibuat oleh <strong>LPK 7</strong> dengan cinta 💙:<br>
    <b>Daviona ✨, Ifta 🧋, Nadila 🎀, Vania 🌸, Sulthan 🎩</b><br>
    <i>Tim paling segar di antara deadline! 🍹</i>
    </p>
""", unsafe_allow_html=True)
