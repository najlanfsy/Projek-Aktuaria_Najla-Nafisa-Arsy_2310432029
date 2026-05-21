# ============================================================
# HALAMAN AWAL - LOGIN & REGISTER
# ACTUARIAL DECISION SUPPORT SYSTEM
# Streamlit Version
# ============================================================

import json
import os
import streamlit as st
import time # Ditambahkan untuk jeda transisi ke halaman menu

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="Actuarial Decision Support System",
    page_icon="📊",
    layout="centered"
)

# ============================================================
# DATABASE FILE
# ============================================================

DB_FILE = "data/akun_pengguna.json"

os.makedirs("data", exist_ok=True)

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({}, f)

# ============================================================
# LOAD & SAVE DATABASE
# ============================================================

def load_users():
    with open(DB_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(DB_FILE, "w") as f:
        json.dump(users, f)

# ============================================================
# INISIALISASI SESSION STATE
# ============================================================

if "halaman" not in st.session_state:
    st.session_state.halaman = "awal"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "nama_user" not in st.session_state:
    st.session_state.nama_user = ""

# ============================================================
# CSS GLOBAL STYLE
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;0,700;1,600&family=DM+Sans:wght@300;400;500;600&display=swap');

/* ── Background ── */
.stApp {
    background: linear-gradient(160deg, #fff0f5 0%, #ffe4ef 50%, #ffd6e7 100%);
    min-height: 100vh;
    position: relative;
    overflow-x: hidden;
}

/* ── Floating bubbles ── */
.bubble-wrap {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.bubble {
    position: absolute;
    border-radius: 50%;
    animation: floatUp linear infinite;
}

.b1  { width:55px;  height:55px;  background:rgba(255,143,171,0.22); left:4%;   animation-duration:10s; animation-delay:0s;   bottom:-80px; }
.b2  { width:30px;  height:30px;  background:rgba(255,182,210,0.28); left:14%;  animation-duration:13s; animation-delay:2s;   bottom:-80px; }
.b3  { width:75px;  height:75px;  background:rgba(255,194,209,0.18); left:27%;  animation-duration:11s; animation-delay:1s;   bottom:-80px; }
.b4  { width:40px;  height:40px;  background:rgba(255,143,171,0.20); left:41%;  animation-duration:15s; animation-delay:4s;   bottom:-80px; }
.b5  { width:22px;  height:22px;  background:rgba(255,204,213,0.30); left:57%;  animation-duration:9s;   animation-delay:0.5s; bottom:-80px; }
.b6  { width:65px;  height:65px;  background:rgba(255,182,210,0.20); left:69%;  animation-duration:12s; animation-delay:3s;   bottom:-80px; }
.b7  { width:38px;  height:38px;  background:rgba(255,143,171,0.22); left:81%;  animation-duration:14s; animation-delay:1.5s; bottom:-80px; }
.b8  { width:50px;  height:50px;  background:rgba(255,214,224,0.25); left:91%;  animation-duration:10s; animation-delay:5.5s; bottom:-80px; }
.b9  { width:28px;  height:28px;  background:rgba(255,204,213,0.22); left:34%;  animation-duration:16s; animation-delay:2.5s; bottom:-80px; }
.b10 { width:48px;  height:48px;  background:rgba(255,143,171,0.18); left:63%;  animation-duration:11s; animation-delay:6.5s; bottom:-80px; }
.b11 { width:20px;  height:20px;  background:rgba(255,182,210,0.28); left:50%;  animation-duration:8s;   animation-delay:3.5s; bottom:-80px; }
.b12 { width:60px;  height:60px;  background:rgba(255,194,209,0.15); left:75%;  animation-duration:17s; animation-delay:1s;   bottom:-80px; }

@keyframes floatUp {
    0%   { transform: translateY(0)      scale(0.85) rotate(0deg);   opacity: 0;    }
    8%   { opacity: 1; }
    92%  { opacity: 1; }
    100% { transform: translateY(-105vh) scale(1.12) rotate(25deg);  opacity: 0;    }
}

/* ── Sparkle / bintang ── */
.sparkle-wrap {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
}

.sparkle {
    position: absolute;
    border-radius: 50%;
    animation: twinkle ease-in-out infinite;
    opacity: 0;
}

.s1  { width:7px;  height:7px;  background:#ffb3c6; top:8%;  left:7%;  animation-duration:2.5s; animation-delay:0s;   }
.s2  { width:5px;  height:5px;  background:#ff8fab; top:18%; left:88%; animation-duration:3s;   animation-delay:0.8s; }
.s3  { width:8px;  height:8px;  background:#ffc2d1; top:33%; left:48%; animation-duration:2s;   animation-delay:1.5s; }
.s4  { width:5px;  height:5px;  background:#ffb3c6; top:52%; left:18%; animation-duration:3.5s; animation-delay:0.3s; }
.s5  { width:9px;  height:9px;  background:#ff8fab; top:68%; left:73%; animation-duration:2.2s; animation-delay:2.2s; }
.s6  { width:6px;  height:6px;  background:#ffd6e0; top:82%; left:38%; animation-duration:2.8s; animation-delay:1s;   }
.s7  { width:7px;  height:7px;  background:#ffb3c6; top:4%;  left:58%; animation-duration:3.2s; animation-delay:0.6s; }
.s8  { width:5px;  height:5px;  background:#ff8fab; top:42%; left:93%; animation-duration:2.4s; animation-delay:1.8s; }
.s9  { width:8px;  height:8px;  background:#ffc2d1; top:25%; left:30%; animation-duration:2.7s; animation-delay:0.4s; }
.s10 { width:6px;  height:6px;  background:#ffb3c6; top:75%; left:55%; animation-duration:3.1s; animation-delay:2.5s; }

@keyframes twinkle {
    0%,100% { opacity: 0;    transform: scale(0.4) rotate(0deg);   }
    50%      { opacity: 0.9;  transform: scale(1.5) rotate(180deg); }
}

/* ── Ornamen sudut ── */
.corner-deco {
    position: fixed;
    pointer-events: none;
    z-index: 0;
    font-size: 80px;
    opacity: 0.06;
    animation: cornerSpin 20s linear infinite;
}
.corner-tl { top: -20px;  left: -20px;  }
.corner-br { bottom: -20px; right: -20px; transform: rotate(180deg); }

@keyframes cornerSpin {
    from { transform: rotate(0deg); }
    to   { transform: rotate(360deg); }
}
.corner-br { animation-direction: reverse; }

/* ── Main card ── */
.main-box {
    position: relative;
    z-index: 2;
    background: linear-gradient(145deg, #ff6b8a 0%, #ff8fab 35%, #ffb3c6 70%, #ffd6e0 100%);
    border-radius: 32px;
    padding: 44px 42px 38px;
    box-shadow:
        0 25px 70px rgba(255, 80, 120, 0.28),
        0 6px 24px rgba(255, 143, 171, 0.20),
        inset 0 1px 0 rgba(255, 255, 255, 0.45),
        inset 0 -1px 0 rgba(200, 50, 90, 0.10);
    margin-bottom: 28px;
    overflow: hidden;
    text-align: center;
}

/* shimmer sweep di main card */
.main-box::before {
    content: '';
    position: absolute;
    top: 0; left: -70%;
    width: 45%; height: 100%;
    background: linear-gradient(100deg, transparent 0%, rgba(255,255,255,0.28) 50%, transparent 100%);
    animation: shimmerCard 5s ease-in-out infinite;
    pointer-events: none;
}

@keyframes shimmerCard {
    0%   { left: -70%; }
    55%  { left: 130%; }
    100% { left: 130%; }
}

/* ── Ikon dekorasi animasi ── */
.deco-icon {
    font-size: 56px;
    margin-bottom: 12px;
    display: block;
    animation: iconFloat 3.5s ease-in-out infinite;
    filter: drop-shadow(0 4px 12px rgba(200,50,90,0.25));
}

@keyframes iconFloat {
    0%,100% { transform: translateY(0px)    rotate(-3deg); }
    50%      { transform: translateY(-10px) rotate(3deg);  }
}

/* ── Judul ── */
.main-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 28px;
    font-weight: 700;
    color: white;
    letter-spacing: 1.8px;
    margin-bottom: 8px;
    text-shadow: 0 2px 14px rgba(180, 40, 80, 0.22);
    line-height: 1.3;
}

/* ── Subtitle ── */
.subtitle {
    font-family: 'DM Sans', sans-serif;
    color: rgba(255, 255, 255, 0.95);
    font-size: 14.5px;
    margin-bottom: 6px;
    font-weight: 400;
}

/* ── Kreator ── */
.creator {
    font-family: 'Cormorant Garamond', serif;
    font-style: italic;
    color: rgba(255, 255, 255, 0.90);
    font-size: 14px;
    margin-bottom: 4px;
    letter-spacing: 0.5px;
}

/* ── Divider dots ── */
.pink-divider {
    font-size: 16px;
    letter-spacing: 8px;
    color: rgba(255, 255, 255, 0.55);
    margin: 6px 0 0;
    animation: dotFade 2s ease-in-out infinite;
}

@keyframes dotFade {
    0%,100% { opacity: 0.55; }
    50%      { opacity: 1;    }
}

/* ── Form card ── */
.form-card {
    background: rgba(255, 255, 255, 0.82);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 22px;
    padding: 28px 30px 20px;
    box-shadow:
        0 8px 32px rgba(255, 100, 140, 0.12),
        0 2px 8px rgba(255, 143, 171, 0.10),
        inset 0 1px 0 rgba(255, 255, 255, 0.9);
    margin-bottom: 18px;
    border: 1.5px solid rgba(255, 182, 210, 0.35);
}

/* ── Tombol ── */
div.stButton > button {
    background: linear-gradient(135deg, #ff6b8a, #ff8fab) !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    height: 48px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14.5px !important;
    letter-spacing: 0.4px !important;
    transition: all 0.3s ease !important;
    width: 100% !important;
    box-shadow: 0 5px 20px rgba(255, 80, 120, 0.30) !important;
}

div.stButton > button:hover {
    background: linear-gradient(135deg, #e85c7a, #ff6b8a) !important;
    transform: translateY(-3px) !important;
    box-shadow: 0 10px 28px rgba(255, 80, 120, 0.40) !important;
}

div.stButton > button:active {
    transform: translateY(-1px) !important;
}

/* ── Input fields ── */
.stTextInput label {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    color: #c0506a !important;
    font-size: 13.5px !important;
}

.stTextInput > div > div > input {
    border-radius: 14px !important;
    border: 1.8px solid rgba(255, 182, 210, 0.55) !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 14px !important;
    padding: 10px 16px !important;
    background: rgba(255, 255, 255, 0.95) !important;
    transition: border-color 0.25s ease, box-shadow 0.25s ease !important;
    color: #5a2535 !important;
}

.stTextInput > div > div > input:focus {
    border-color: #ff8fab !important;
    box-shadow: 0 0 0 3px rgba(255, 143, 171, 0.18) !important;
    outline: none !important;
}

.stTextInput > div > div > input::placeholder {
    color: rgba(180, 100, 130, 0.5) !important;
}

/* ── Notifikasi custom ── */
.notif-success {
    background: linear-gradient(135deg, #d4edda, #c3e6cb);
    border-left: 4px solid #28a745;
    border-radius: 14px;
    padding: 14px 18px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: #155724;
    font-weight: 500;
    box-shadow: 0 4px 16px rgba(40,167,69,0.15);
    margin: 10px 0;
    animation: slideDown 0.4s ease;
}

.notif-warning {
    background: linear-gradient(135deg, #fff3cd, #ffeeba);
    border-left: 4px solid #ffc107;
    border-radius: 14px;
    padding: 14px 18px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: #856404;
    font-weight: 500;
    box-shadow: 0 4px 16px rgba(255,193,7,0.15);
    margin: 10px 0;
    animation: slideDown 0.4s ease;
}

.notif-error {
    background: linear-gradient(135deg, #f8d7da, #f5c6cb);
    border-left: 4px solid #dc3545;
    border-radius: 14px;
    padding: 14px 18px;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    color: #721c24;
    font-weight: 500;
    box-shadow: 0 4px 16px rgba(220,53,69,0.15);
    margin: 10px 0;
    animation: slideDown 0.4s ease;
}

@keyframes slideDown {
    from { opacity: 0; transform: translateY(-10px); }
    to   { opacity: 1; transform: translateY(0);     }
}

/* ── Footer ── */
.footer-wrap {
    position: relative;
    z-index: 2;
    text-align: center;
    font-family: 'DM Sans', sans-serif;
    margin-top: 24px;
    padding-bottom: 24px;
}

.footer-tag {
    font-size: 12.5px;
    color: #c0607a;
    opacity: 0.85;
    margin-bottom: 8px;
    letter-spacing: 0.5px;
}

.footer-desc {
    font-size: 12.5px;
    color: #b05060;
    opacity: 0.72;
    line-height: 1.9;
    max-width: 360px;
    margin: auto;
}

.pulse-code {
    display: inline-block;
    font-family: 'Cormorant Garamond', serif;
    font-size: 14px;
    font-weight: 700;
    font-style: italic;
    color: #e05578;
    margin-top: 12px;
    animation: pulse 2s ease-in-out infinite;
    letter-spacing: 0.8px;
}

@keyframes pulse {
    0%,100% { opacity: 1;   transform: scale(1);    }
    50%      { opacity: 0.4; transform: scale(0.97); }
}

/* ── Sembunyikan default Streamlit notif & menu ── */
.stAlert           { display: none !important; }
#MainMenu          { visibility: hidden; }
footer             { visibility: hidden; }
.block-container   { padding-top: 2rem !important; }

</style>
""", unsafe_allow_html=True)

# ── Injeksi animasi latar (bubbles + sparkles + ornamen) ──
st.markdown("""
<div class="bubble-wrap">
  <div class="bubble b1"></div>  <div class="bubble b2"></div>
  <div class="bubble b3"></div>  <div class="bubble b4"></div>
  <div class="bubble b5"></div>  <div class="bubble b6"></div>
  <div class="bubble b7"></div>  <div class="bubble b8"></div>
  <div class="bubble b9"></div>  <div class="bubble b10"></div>
  <div class="bubble b11"></div> <div class="bubble b12"></div>
</div>

<div class="sparkle-wrap">
  <div class="sparkle s1"></div>  <div class="sparkle s2"></div>
  <div class="sparkle s3"></div>  <div class="sparkle s4"></div>
  <div class="sparkle s5"></div>  <div class="sparkle s6"></div>
  <div class="sparkle s7"></div>  <div class="sparkle s8"></div>
  <div class="sparkle s9"></div>  <div class="sparkle s10"></div>
</div>

<div class="corner-deco corner-tl">✿</div>
<div class="corner-deco corner-br">✿</div>
""", unsafe_allow_html=True)

# ============================================================
# HELPER NOTIFIKASI
# ============================================================

def notif_success(msg):
    st.markdown(f'<div class="notif-success">✅ &nbsp; {msg}</div>', unsafe_allow_html=True)

def notif_warning(msg):
    st.markdown(f'<div class="notif-warning">⚠️ &nbsp; {msg}</div>', unsafe_allow_html=True)

def notif_error(msg):
    st.markdown(f'<div class="notif-error">❌ &nbsp; {msg}</div>', unsafe_allow_html=True)

# ============================================================
# HALAMAN AWAL
# ============================================================

def halaman_awal():

    st.markdown("""
    <div class="main-box">
        <span class="deco-icon">📊</span>
        <div class="main-title">ACTUARIAL DECISION SUPPORT SYSTEM</div>
        <div class="subtitle">Smart Financial &amp; Actuarial Analysis Platform</div>
        <div class="creator">Created by Najla Nafisa Arsy &nbsp;·&nbsp; 2310432029</div>
        <div class="pink-divider">· · ·</div>
    </div>
    """, unsafe_allow_html=True)

    _, col1, col2, _ = st.columns([1, 2, 2, 1])

    with col1:
        if st.button("Login"):
            st.session_state.halaman = "login"
            st.rerun()

    with col2:
        if st.button("Daftar"):
            st.session_state.halaman = "daftar"
            st.rerun()

    st.markdown("""
    <div class="footer-wrap">
        <div class="footer-desc">
            Aplikasi ini membantu pengguna melakukan perhitungan
            matematika aktuaria dan memberikan rekomendasi finansial
            secara interaktif.
        </div>
        <div class="pulse-code">✦ Actuarial Mathematics System ✦</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# HALAMAN DAFTAR
# ============================================================

def halaman_daftar():

    st.markdown("""
    <div class="main-box">
        <span class="deco-icon"></span>
        <div class="main-title">BUAT AKUN BARU</div>
        <div class="subtitle">Isi data diri kamu di bawah ini</div>
    </div>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([0.3, 3, 0.3])

    with col:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        nama     = st.text_input("Nama Lengkap", placeholder="Masukkan nama lengkap kamu")
        email    = st.text_input("Email",         placeholder="Masukkan alamat email kamu")
        password = st.text_input("Password",      placeholder="Buat password kamu", type="password")
        st.markdown("</div>", unsafe_allow_html=True)

        notif_area = st.empty()

        _, c1, c2, _ = st.columns([0.3, 2, 2, 0.3])

        with c1:
            klik_daftar = st.button("Daftar Sekarang")
        with c2:
            klik_kembali = st.button("Kembali")

        if klik_daftar:
            if not nama or not email or not password:
                with notif_area:
                    notif_warning("Semua kolom wajib diisi terlebih dahulu.")
            else:
                users = load_users()
                if email in users:
                    with notif_area:
                        notif_warning("Email ini sudah terdaftar. Coba gunakan email lain.")
                else:
                    users[email] = {"nama": nama, "password": password}
                    save_users(users)
                    with notif_area:
                        notif_success("Akun berhasil dibuat! Silakan login sekarang.")

        if klik_kembali:
            st.session_state.halaman = "awal"
            st.rerun()

# ============================================================
# HALAMAN LOGIN
# ============================================================

def halaman_login():

    st.markdown("""
    <div class="main-box">
        <span class="deco-icon"></span>
        <div class="main-title">SELAMAT DATANG KEMBALI</div>
        <div class="subtitle">Masuk ke akun kamu untuk melanjutkan</div>
    </div>
    """, unsafe_allow_html=True)

    _, col, _ = st.columns([0.3, 3, 0.3])

    with col:
        st.markdown('<div class="form-card">', unsafe_allow_html=True)
        email    = st.text_input("Email",     placeholder="Masukkan email kamu")
        password = st.text_input("Password", placeholder="Masukkan password kamu", type="password")
        st.markdown("</div>", unsafe_allow_html=True)

        notif_area = st.empty()

        _, c1, c2, _ = st.columns([0.3, 2, 2, 0.3])

        with c1:
            klik_login = st.button("Login")
        with c2:
            klik_daftar = st.button("Daftar")

        _, c3, _ = st.columns([1, 2, 1])
        with c3:
            klik_kembali = st.button("Kembali ke Beranda")

        if klik_login:
            if not email or not password:
                with notif_area:
                    notif_warning("Email dan password wajib diisi.")
            else:
                users = load_users()
                if email not in users:
                    with notif_area:
                        notif_warning("Akun tidak ditemukan. Silakan daftar terlebih dahulu.")
                elif users[email]["password"] != password:
                    with notif_area:
                        notif_error("Email atau password yang kamu masukkan salah.")
                else:
                    # SIMPAN STATUS LOGIN KE SESSION STATE
                    st.session_state.logged_in = True
                    st.session_state.nama_user = users[email]["nama"]
                    
                    with notif_area:
                        notif_success("Login berhasil! Mengalihkan ke halaman menu...")
                    
                    # Berikan sedikit waktu tunda (1.5 detik) agar animasi sukses terbaca
                    time.sleep(1.5)
                    
                    # REDIRECT KE HALAMAN MENU UTAMA KAMU
                    st.switch_page("pages/menu.py")

        if klik_daftar:
            st.session_state.halaman = "daftar"
            st.rerun()

        if klik_kembali:
            st.session_state.halaman = "awal"
            st.rerun()

# ============================================================
# ROUTING HALAMAN
# ============================================================

if st.session_state.halaman == "awal":
    halaman_awal()

elif st.session_state.halaman == "login":
    halaman_login()

elif st.session_state.halaman == "daftar":
    halaman_daftar()