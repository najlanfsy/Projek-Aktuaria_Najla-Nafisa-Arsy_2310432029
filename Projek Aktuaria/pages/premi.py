# ============================================================
# 🛡️ PREMI ASURANSI JIWA PAGE
# Actuarial Decision Support System
# Streamlit Web Version
# ============================================================

import streamlit as st
import streamlit.components.v1 as components  # Komponen native untuk JavaScript Cetak
import matplotlib.pyplot as plt

# ============================================================
# PROTEKSI LOGIN (Wajib Lewat app.py)
# ============================================================
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.warning("Silakan login terlebih dahulu untuk mengakses halaman ini.")
    st.switch_page("app.py")
    st.stop()

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================
st.set_page_config(
    page_title="Premi Asuransi Jiwa - Actuarial DSS",
    page_icon="🛡️",
    layout="wide"
)

# ============================================================
# CSS CUSTOM (Pink Professional & Cetak Pendukung)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap');

/* Style Latar Belakang */
.stApp {
    background-color: #fff7fa;
}

/* Header Container */
.premium-container {
    background: linear-gradient(135deg, #ffb3c7, #ffc2d1, #ffd6e0);
    padding: 35px;
    border-radius: 35px;
    margin-bottom: 25px;
    box-shadow: 0px 12px 35px rgba(255,105,135,0.18);
    text-align: center;
}

.premium-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    color: white;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.premium-subtitle {
    font-family: 'Poppins', sans-serif;
    color: white;
    font-size: 16px;
    font-weight: 300;
}

/* Box Hasil */
.result-box {
    background: linear-gradient(135deg, #ffc2d1, #ffd6e0, #ffe5ec);
    padding: 35px;
    border-radius: 28px;
    margin-top: 25px;
    margin-bottom: 25px;
    box-shadow: 0px 10px 25px rgba(255,105,135,0.18);
}

.result-title {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

/* Card di dalam Grid Hasil */
.grid-card {
    background: rgba(255, 255, 255, 0.35);
    border-radius: 22px;
    padding: 22px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
    border: 1px solid rgba(255,255,255,0.4);
    text-align: center;
}

.card-label {
    font-family: 'Poppins', sans-serif;
    color: #63414d;
    font-size: 14px;
    margin-bottom: 8px;
    font-weight: 500;
}

.card-val {
    font-family: 'Poppins', sans-serif;
    color: #d63384;
    font-size: 22px;
    font-weight: 700;
}

/* Box Rekomendasi */
.rekom-box {
    background: white;
    padding: 28px;
    border-radius: 25px;
    margin-top: 25px;
    margin-bottom: 25px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.06);
    border-left: 5px solid #d63384;
}

.rekom-title {
    font-family: 'Poppins', sans-serif;
    color: #d63384;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 12px;
}

.rekom-text {
    font-family: 'Poppins', sans-serif;
    color: #555;
    font-size: 15px;
    line-height: 1.8;
}

/* CSS KHUSUS PRINT LAPORAN */
@media print {
    [data-testid="stSidebar"], 
    .stButton, 
    [data-testid="stForm"],
    .no-print,
    [data-testid="stHeader"],
    iframe {
        display: none !important;
    }
    .stApp {
        background: white !important;
        color: black !important;
    }
    .grid-card {
        background: #f8f9fa !important;
        border: 1px solid #ddd !important;
    }
    .card-val {
        color: black !important;
    }
}
</style>

<div class="premium-container">
    <div class="premium-title">PREMI ASURANSI JIWA</div>
    <div class="premium-subtitle">Simulasi Perhitungan Premi Menggunakan Konsep Matematika Aktuaria</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# INPUT DATA USER (WIDGET WEB INTERAKTIF)
# ============================================================
st.subheader("⌨️ Input Data Asuransi")

col_in1, col_in2 = st.columns(2)

with col_in1:
    nama = st.text_input("👤 Nama Tertanggung", value="Najla Nafisa Arsy")
    umur = st.number_input("🎂 Umur Tertanggung (Tahun)", min_value=1, max_value=100, value=21, step=1)
    uang_pertanggungan = st.number_input("💰 Uang Pertanggungan (Rp)", min_value=0.0, value=100000000.0, step=5000000.0, format="%.0f")

with col_in2:
    lama_kontrak = st.number_input("📅 Lama Kontrak / Tenor Asuransi (Tahun)", min_value=1, max_value=50, value=10, step=1)
    bunga = st.number_input("📈 Tingkat Suku Bunga (%)", min_value=0.0, max_value=100.0, value=6.0, step=0.1) / 100

# ============================================================
# LOGIKA PERHITUNGAN MATEMATIKA AKTUARIA
# ============================================================
# Faktor mortalitas sederhana (mengikuti formula bawaan kamu)
qx = 0.0005 * umur

# Nilai diskonto keuangan
v = 1 / (1 + bunga)

# Present Value dari Benefit (Manfaat) Asuransi
pv_benefit = uang_pertanggungan * qx * (v ** lama_kontrak)

# Perhitungan Premi Tahunan & Bulanan
premi_tahunan = pv_benefit / lama_kontrak
premi_bulanan = premi_tahunan / 12

# Probabilitas Kelangsungan Hidup (Survival Probability)
survival = ((1 - qx) ** lama_kontrak) * 100

# ============================================================
# LAYOUT OUTPUT HASIL (SINKRONISASI UI GRID)
# ============================================================
st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.markdown('<div class="result-title">Hasil Perhitungan Aktuaria</div>', unsafe_allow_html=True)

col_g1, col_g2, col_g3, col_g4 = st.columns(4)

with col_g1:
    st.markdown(f"""
    <div class="grid-card">
        <div class="card-label">Nama Tertanggung</div>
        <div class="card-val">{nama}</div>
    </div>
    """, unsafe_allow_html=True)

with col_g2:
    st.markdown(f"""
    <div class="grid-card">
        <div class="card-label">Premi Tahunan</div>
        <div class="card-val">Rp {premi_tahunan:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col_g3:
    st.markdown(f"""
    <div class="grid-card">
        <div class="card-label">Premi Bulanan</div>
        <div class="card-val">Rp {premi_bulanan:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with col_g4:
    st.markdown(f"""
    <div class="grid-card">
        <div class="card-label">Probabilitas Survival</div>
        <div class="card-val">{survival:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# GRAFIK ANALISIS PROPORSI KOMPONEN ASURANSI
# ============================================================
st.write("📊 **Grafik Analisis Risiko & Nilai Pertanggungan**")
col_chart, col_empty = st.columns([2, 1])

with col_chart:
    fig, ax = plt.subplots(figsize=(6, 2.5))
    labels = ['Uang Pertanggungan', 'Total Estimasi Premi']
    sizes = [uang_pertanggungan, premi_tahunan * lama_kontrak]
    colors = ['#ffcad4', '#d63384']
    
    ax.barh(labels, sizes, color=colors, height=0.5)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(axis='x', linestyle='--', alpha=0.5)
    st.pyplot(fig)

# ============================================================
# REKOMENDASI SISTEM
# ============================================================
st.markdown(f"""
<div class="rekom-box">
    <div class="rekom-title">💡 Rekomendasi Sistem</div>
    <div class="rekom-text">
        Premi asuransi jiwa ini dipengaruhi secara linier oleh faktor umur tertanggung (<b>{umur} tahun</b>), 
        skala uang pertanggungan, serta tingkat kapitalisasi suku bunga pasar. 
        Mengingat peluang hidup tertanggung hingga akhir masa kontrak diproyeksikan sebesar <b>{survival:.2f}%</b>, 
        struktur alokasi premi tahunan senilai <b>Rp {premi_tahunan:,.0f}</b> dinilai proporsional dan ideal 
        untuk mengover risiko mortalitas masa datang.
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ACTION BUTTONS & NAVIGASI FOOTER (SINKRON DENGAN TVM.PY)
# ============================================================
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])

with col_btn1:
    # Menggunakan HTML Komponen murni dengan penyesuaian tinggi (height=70) agar teks dua baris tidak terpotong
    print_html = """
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background: transparent; overflow: hidden; }
        .luxury-print-btn {
            background: linear-gradient(135deg, #ff4d88, #ff758f);
            color: white !important;
            border: none;
            padding: 12px 20px;
            font-family: 'Poppins', sans-serif;
            font-size: 15px;
            font-weight: 500;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            display: block;
            box-shadow: 0px 4px 15px rgba(255, 77, 136, 0.2);
            transition: all 0.3s ease;
            text-align: center;
            line-height: 1.3;
        }
        .luxury-print-btn:hover {
            background: linear-gradient(135deg, #ff2a70, #ff4d88);
            box-shadow: 0px 6px 20px rgba(255, 77, 136, 0.3);
        }
    </style>
    <button class="luxury-print-btn" onclick="window.parent.parent.print()">🖨️ Cetak Hasil Laporan (PDF/Print)</button>
    """
    components.html(print_html, height=70)

with col_btn3:
    # Mengembalikan rute halaman ke dashboard utama (menu.py)
    if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
        st.switch_page("pages/menu.py")

# Hak Cipta Elemen Footer Aktuaria
st.markdown("""
<div class="no-print" style="text-align: center; color: #aaa; margin-top: 30px; font-size: 12px; font-family: 'Poppins';">
    &lt;/&gt; Actuarial Decision Support System — Python Core Module. Dibuat oleh Najla Nafisa Arsy
</div>
""", unsafe_allow_html=True)
