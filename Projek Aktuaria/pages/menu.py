# ============================================================
# 🌸 MAIN MENU DASHBOARD — LUXURY & CUTE PINK EDITION
# Actuarial Decision Support System
# Fully Native Streamlit Web Implementation
# ============================================================

import streamlit as st
import json
import os

# ============================================================
# PROTECTIONS: LOGIN CHECK & AMBIL NAMA PENGGUNA DINAMIS
# ============================================================
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Silakan login terlebih dahulu untuk mengakses halaman ini.")
    st.switch_page("app.py")
    st.stop()

# Mengambil nama dari session_state secara dinamis
nama_display = st.session_state.get("nama_user", None)

# Jika tidak ada di session_state, coba tarik dari akun_pengguna.json berdasarkan username login
if not nama_display and "username" in st.session_state:
    username_login = st.session_state.username
    if os.path.exists("akun_pengguna.json"):
        try:
            with open("akun_pengguna.json", "r") as f:
                data_akun = json.load(f)
                # Mencari nama yang cocok dengan username di database JSON
                if username_login in data_akun:
                    nama_display = data_akun[username_login].get("nama", username_login)
                elif isinstance(data_akun, list): # Antisipasi jika struktur JSON berbentuk list
                    for akun in data_akun:
                        if akun.get("username") == username_login:
                            nama_display = akun.get("nama")
                            break
        except Exception:
            pass

# Fallback terakhir jika nama tetap tidak ditemukan
if not nama_display:
    nama_display = "Pengguna Actuarial DSS"

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="Dashboard — Actuarial DSS",
    page_icon="🌸",
    layout="wide"
)

# ============================================================
# SURGICAL CSS INJECTION: 3D GLAMOUR PINK STYLE
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Poppins:wght=300;400;500;600;700&display=swap');

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

/* Modifikasi Container Selamat Datang */
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

/* Font Judul Utama */
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

/* Sembunyikan tombol native Streamlit sepenuhnya agar tidak merusak visual */
div.stButton > button {
    display: none !important;
}

/* 🌸 KARTU MENU 3D LUXURY KUSTOM 🌸 */
.menu-card-3d {
    background: linear-gradient(135deg, #ffffff, #fff0f3);
    border-radius: 25px;
    padding: 30px 20px;
    text-align: center;
    cursor: pointer;
    text-decoration: none;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 210px;
    
    /* Efek Timbul 3D (Neumorphism / Isometrik Shadow) */
    border-top: 2px solid #ffffff;
    border-left: 2px solid #ffffff;
    border-right: 2px solid #ffe3ec;
    border-bottom: 5px solid #fca3b7; /* Efek ketebalan bawah tombol */
    
    box-shadow: 0px 10px 20px rgba(255, 105, 135, 0.12), 
                inset 0px 2px 5px rgba(255, 255, 255, 0.8);
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

/* Icon Di Dalam Kartu Menu */
.menu-card-3d .icon {
    font-size: 44px;
    margin-bottom: 12px;
    filter: drop-shadow(0px 5px 5px rgba(255, 105, 135, 0.2));
    transition: transform 0.3s ease;
}

/* Judul Di Dalam Kartu Menu */
.menu-card-3d .title {
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #63414d;
    margin-bottom: 6px;
    line-height: 1.3;
}

/* Deskripsi Di Dalam Kartu Menu */
.menu-card-3d .desc {
    font-family: 'Poppins', sans-serif;
    font-size: 12.5px;
    font-weight: 400;
    color: #8c6b77;
    line-height: 1.4;
    opacity: 0.9;
}

/* 🌟 INTERACTIVE 3D HOVER EFFECT 🌟 */
.menu-card-3d:hover {
    transform: translateY(-8px); /* Mengambang naik */
    background: linear-gradient(135deg, #ff4d88, #ff758f);
    border-top: 2px solid #ff758f;
    border-left: 2px solid #ff758f;
    border-bottom: 5px solid #d6225c; /* Dasar tebal saat aktif */
    box-shadow: 0px 20px 35px rgba(255, 77, 136, 0.35);
}

/* Perubahan teks menjadi putih bersih saat di-hover */
.menu-card-3d:hover .title { color: #ffffff; }
.menu-card-3d:hover .desc { color: #ffe3ec; }
.menu-card-3d:hover .icon {
    transform: scale(1.15) rotate(5deg); /* Efek icon membesar dan sedikit miring */
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
    st.markdown('<div class="welcome-anchor"></div>', unsafe_allow_html=True)
    st.markdown('<div class="aesthetic-title">ACTUARIAL DECISION SUPPORT SYSTEM</div>', unsafe_allow_html=True)
    st.markdown('<div class="aesthetic-subtitle">Smart Financial & Actuarial Analysis Platform</div>', unsafe_allow_html=True)
    st.markdown('<div class="cute-divider"></div>', unsafe_allow_html=True)
    
    # Menampilkan Nama Pengguna secara Dinamis
    st.markdown(f'<div class="aesthetic-welcome-title">👋 Selamat Datang, {nama_display}</div>', unsafe_allow_html=True)
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
    st.markdown("""
    <div class="menu-card-3d">
        <div class="icon">💰</div>
        <div class="title">Time Value of Money</div>
        <div class="desc">Bunga tunggal, majemuk, & nilai waktu dari uang.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Akses TVM", key="btn_tvm", help="Buka Halaman Time Value of Money"):
        st.switch_page("pages/tvm.py")

with col2:
    st.markdown("""
    <div class="menu-card-3d">
        <div class="icon">📈</div>
        <div class="title">Investasi & Anuitas</div>
        <div class="desc">Simulasi investasi berkala, tabungan berjangka, & anuitas.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Akses Investasi", key="btn_investasi", help="Buka Halaman Investasi & Anuitas"):
        st.switch_page("pages/investasi.py")

with col3:
    st.markdown("""
    <div class="menu-card-3d">
        <div class="icon">🏦</div>
        <div class="title">Simulasi Kredit</div>
        <div class="desc">Kalkulasi nilai angsuran bulanan amortisasi kredit pinjaman.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Akses Kredit", key="btn_kredit", help="Buka Halaman Simulasi Kredit"):
        st.switch_page("pages/kredit.py")

# Jarak Baris Kedua
st.markdown('<div style="margin-top: 30px;"></div>', unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="menu-card-3d">
        <div class="icon">🛡️</div>
        <div class="title">Premi Asuransi Jiwa</div>
        <div class="desc">Estimasi perhitungan nilai premi murni tunggal maupun berkala.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Akses Premi", key="btn_premi", help="Buka Halaman Premi Asuransi Jiwa"):
        st.switch_page("pages/premi.py")

with col5:
    st.markdown("""
    <div class="menu-card-3d">
        <div class="icon">👴</div>
        <div class="title">Dana Pensiun</div>
        <div class="desc">Perencanaan akumulasi dana hari tua & simulasi alokasi investasi.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Akses Pensiun", key="btn_pensiun", help="Buka Halaman Dana Pensiun"):
        st.switch_page("pages/pensiun.py")

with col6:
    st.markdown("""
    <div class="menu-card-3d">
        <div class="icon">📊</div>
        <div class="title">Mortalitas & Survival</div>
        <div class="desc">Analisis peluang bertahan hidup berdasarkan tabel hukum mortalitas.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Akses Mortalitas", key="btn_mortalitas", help="Buka Halaman Mortalitas & Survival"):
        st.switch_page("pages/mortalitas.py")

# ============================================================
# FOOTER UTAMA INTERFACE
# ============================================================
st.markdown("""
<div class="aesthetic-footer">
    Aplikasi ini membantu pengguna melakukan perhitungan matematika aktuaria dan memberikan rekomendasi finansial secara interaktif, modern, dan mudah digunakan.<br>
    <b>🌸 Actuarial Decision Support System — Luxury Rose Gold v4.0 (Stable)</b>
</div>
""", unsafe_allow_html=True)
