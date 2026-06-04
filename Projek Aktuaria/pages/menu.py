# ============================================================
# 🌸 MAIN MENU DASHBOARD — LUXURY & CUTE PINK EDITION
# Actuarial Decision Support System
# Fully Native Streamlit Web Implementation
# ============================================================

import streamlit as st

# ============================================================
# PROTECTIONS: LOGIN CHECK
# ============================================================
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Silakan login terlebih dahulu untuk mengakses halaman ini.")
    st.switch_page("app.py")
    st.stop()

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="Dashboard — Actuarial DSS",
    page_icon="🌸",
    layout="wide"
)

# ============================================================
# SURGICAL CSS INJECTION: GLAMOUR PINK STYLE & INTERACTIVE ANIMATION
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Poppins:wght@300;400;500;600;700&display=swap');

/* Latar Belakang Aplikasi Lembut Pastel */
.stApp {
    background: #fff5f8;
}

/* 🎀 JANGKAR STYLE UNTUK CONTAINER EMBEDDED STREAMLIT 🎀 */
.welcome-anchor {
    display: none;
}

/* Efek Animasi Mengambang untuk Header Utama */
@keyframes floatHeader {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
    100% { transform: translateY(0px); }
}

/* Modifikasi Container Selamat Datang (Native Wrapper Trick) */
div[data-testid="stVerticalBlock"] > div:has(div.welcome-anchor) {
    background: linear-gradient(135deg, #ffb6c1, #ffc2d1, #ffe3ec) !important;
    padding: 50px 40px !important;
    border-radius: 40px !important;
    box-shadow: 0px 15px 40px rgba(255, 105, 135, 0.25) !important;
    border: 3px solid rgba(255, 255, 255, 0.7) !important;
    text-align: center !important;
    margin-bottom: 25px !important;
    animation: floatHeader 5s ease-in-out infinite;
}

/* Font Gabungan Aesthetic untuk Judul Utama */
.aesthetic-title {
    font-family: 'Playfair Display', serif;
    font-size: 46px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 2px;
    margin-bottom: 5px;
    text-shadow: 3px 3px 15px rgba(214, 51, 132, 0.3);
}

.aesthetic-subtitle {
    font-family: 'Playfair Display', Georgia, serif;
    font-style: italic;
    font-size: 20px;
    color: #fff0f3;
    font-weight: 400;
    margin-bottom: 25px;
    opacity: 0.95;
}

/* Pembatas Elemen Lucu */
.cute-divider {
    width: 80px;
    height: 4px;
    background: white;
    border-radius: 10px;
    margin: 0 auto 25px auto;
    opacity: 0.8;
}

/* Tipografi Cantik Teks Selamat Datang */
.aesthetic-welcome-title {
    font-family: 'Poppins', sans-serif;
    font-size: 28px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
}

.aesthetic-welcome-desc {
    font-family: 'Poppins', sans-serif;
    font-size: 14.5px;
    font-weight: 300;
    color: #ffffff;
    line-height: 1.9;
    max-width: 900px;
    margin: 0 auto;
    opacity: 0.95;
}

/* Label Pembagian Kelompok Menu */
.section-pink-title {
    font-family: 'Poppins', sans-serif;
    color: #ff4d88;
    font-size: 24px;
    font-weight: 700;
    margin-top: 45px;
    margin-bottom: 25px;
    border-left: 6px solid #ff4d88;
    padding-left: 15px;
    letter-spacing: 0.5px;
}

/* 🌸 KUSTOMISASI TOMBOL MENJADI KOTAK MENU LEBIH BESAR, CANTIK, & ANIMATIF 🌸 */
div.stButton > button {
    background: linear-gradient(135deg, #ffffff, #fff0f3) !important;
    border: 2px solid #ffe3ec !important;
    border-radius: 35px !important; /* Membuat sudut lebih melengkung lembut */
    padding: 40px 30px !important;  /* Diperbesar ukurannya */
    width: 100% !important;
    min-height: 240px !important;   /* Menambah tinggi tombol agar lebih luxury */
    box-shadow: 0px 12px 30px rgba(255, 105, 135, 0.08) !important;
    transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    color: #63414d !important;
    font-family: 'Poppins', sans-serif !important;
    text-align: center !important;
    line-height: 1.5 !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
}

/* 🌟 ANIMASI KETIKA KURSOR DIARAHKAN (HOVER EFFECT) 🌟 */
div.stButton > button:hover {
    transform: translateY(-15px) scale(1.03) !important; /* Efek mengangkat lebih tinggi */
    background: linear-gradient(135deg, #ff4d88, #ff758f) !important;
    color: #ffffff !important;
    border-color: #ff4d88 !important;
    box-shadow: 0px 25px 40px rgba(255, 77, 136, 0.35) !important;
}

/* Mengubah warna teks deskripsi di dalam tombol saat di-hover agar putih bersih */
div.stButton > button:hover p {
    color: #ffe3ec !important;
}

/* Style khusus untuk teks di dalam tombol */
.btn-icon {
    font-size: 42px; /* Ukuran emoji diperbesar */
    margin-bottom: 12px;
}
.btn-title {
    font-size: 20px; /* Ukuran judul menu */
    font-weight: 700;
    display: block;
    margin-bottom: 8px;
}
.btn-desc {
    font-size: 13px; /* Ukuran deskripsi menu kecil di bawahnya */
    font-weight: 400;
    opacity: 0.85;
    line-height: 1.4;
    display: block;
}

/* Footer Copyright Style */
.aesthetic-footer {
    text-align: center;
    color: #b58da0;
    font-family: 'Poppins', sans-serif;
    font-size: 13.5px;
    margin-top: 80px;
    padding-bottom: 30px;
    line-height: 1.8;
    letter-spacing: 0.5px;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# HEADER & WELCOME CARD (ONE HIGH-END NATIVE WRAPPER)
# ============================================================
with st.container():
    # Pemicu style CSS kustom agar menyatu ke dalam satu card pink besar
    st.markdown('<div class="welcome-anchor"></div>', unsafe_allow_html=True)
    
    # Render Tipografi Judul Gabungan Elegan
    st.markdown('<div class="aesthetic-title">ACTUARIAL DECISION SUPPORT SYSTEM</div>', unsafe_allow_html=True)
    st.markdown('<div class="aesthetic-subtitle">Smart Financial & Actuarial Analysis Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="cute-divider"></div>', unsafe_allow_html=True)
    
    # Render Konten Selamat Datang
    st.markdown('<div class="aesthetic-welcome-title">👋 Selamat Datang, Najla Nafisa Arsy</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="aesthetic-welcome-desc">'
        'Sistem pintar ini siap mendampingi Anda dalam melakukan eksekusi formula matematika aktuaria, '
        'proyeksi finansial komprehensif, analisis instrumen investasi, kalkulasi dana pensiun, hingga '
        'pemodelan kurva mortalitas secara akurat, interaktif, dan modern.'
        '</div>', 
        unsafe_allow_html=True
    )

# ============================================================
# KELOMPOK MENU: PERHITUNGAN AKTUARIA & FINANSIAL
# ============================================================
st.markdown('<div class="section-pink-title">✨ Menu Perhitungan Aktuaria & Finansial</div>', unsafe_allow_html=True)

# Grid Layout 3 Kolom Responsif
col1, col2, col3 = st.columns(3)

with col1:
    if st.button(
        "💰\nTime Value of Money\nBunga tunggal, majemuk, & nilai waktu uang", 
        key="btn_tvm", 
        help="Akses perhitungan bunga tunggal, majemuk, dan nilai waktu dari uang."
    ):
        st.switch_page("pages/tvm.py")

with col2:
    if st.button(
        "📈\nInvestasi & Anuitas\nSimulasi investasi berkala & tabungan", 
        key="btn_investasi", 
        help="Akses simulasi investasi berkala, tabungan berjangka, dan nilai anuitas."
    ):
        st.switch_page("pages/investasi.py")

with col3:
    if st.button(
        "🏦\nSimulasi Kredit\nKalkulasi angsuran amortisasi pinjaman", 
        key="btn_kredit", 
        help="Akses perhitungan angsuran bulanan amortisasi kredit pinjaman."
    ):
        st.switch_page("pages/kredit.py")

# Jarak Baris Kedua
st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)

with col4:
    if st.button(
        "🛡️\nPremi Asuransi Jiwa\nEstimasi nilai premi murni tunggal & berkala", 
        key="btn_premi", 
        help="Akses estimasi perhitungan nilai premi murni tunggal maupun berkala."
    ):
        st.switch_page("pages/premi.py")

with col5:
    if st.button(
        "👴\nDana Pensiun\nPerencanaan akumulasi dana hari tua", 
        key="btn_pensiun", 
        help="Akses perencanaan akumulasi dana hari tua dan simulasi alokasi investasi."
    ):
        st.switch_page("pages/pensiun.py")

with col6:
    if st.button(
        "📊\nMortalitas & Survival\nAnalisis peluang hidup tabel mortalitas", 
        key="btn_mortalitas", 
        help="Akses analisis peluang bertahan hidup berdasarkan tabel hukum mortalitas."
    ):
        st.switch_page("pages/mortalitas.py")

# Jarak Baris Ketiga
st.markdown('<div style="margin-top: 25px;"></div>', unsafe_allow_html=True)
col7, _, _ = st.columns(3)


# ============================================================
# FOOTER UTAMA INTERFACE
# ============================================================
st.markdown("""
<div class="aesthetic-footer">
    Aplikasi ini membantu pengguna melakukan perhitungan matematika aktuaria dan memberikan rekomendasi finansial secara interaktif, modern, dan mudah digunakan.<br>
    <b>🌸 Actuarial Decision Support System — Luxury Rose Gold v4.0 (Stable)</b>
</div>
""", unsafe_allow_html=True)
