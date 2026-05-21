# ============================================================
# 📊 MORTALITAS & SURVIVAL ANALYSIS PAGE
# Actuarial Decision Support System
# Streamlit Web Version
# ============================================================

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

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
    page_title="Mortalitas & Survival - Actuarial DSS",
    page_icon="📊",
    layout="wide"
)

# ============================================================
# CSS CUSTOM (Pink Professional & Cetak Pendukung)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap');

/* Style Latar Belakang Utama */
.stApp {
    background-color: #fff7fa;
}

/* Container Utama Header */
.mortalitas-container {
    background: linear-gradient(135deg, #ffb3c7, #ffc2d1, #ffd6e0);
    padding: 35px;
    border-radius: 35px;
    margin-bottom: 25px;
    box-shadow: 0px 12px 35px rgba(255,105,135,0.18);
    text-align: center;
}

.mortalitas-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    color: white;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.mortalitas-subtitle {
    font-family: 'Poppins', sans-serif;
    color: white;
    font-size: 16px;
    font-weight: 300;
}

/* Kotak Hasil (Result Cards) */
.result-card {
    background: rgba(255, 255, 255, 0.35);
    border-radius: 22px;
    padding: 22px;
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
    border: 1px solid rgba(255,255,255,0.4);
    text-align: center;
    transition: 0.3s;
}

.result-card:hover {
    transform: translateY(-5px);
    background: rgba(255, 255, 255, 0.5);
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
    font-size: 24px;
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

/* CSS KHUSUS PRINT LAPORAN (PDF) */
@media print {
    [data-testid="stSidebar"], 
    .stButton, 
    [data-testid="stForm"],
    .no-print,
    [data-testid="stHeader"] {
        display: none !important;
    }
    .stApp {
        background: white !important;
        color: black !important;
    }
    .mortalitas-container {
        color: black !important;
        border: 2px solid #ddd !important;
        background: #fdf2f4 !important;
    }
    .result-card {
        background: #f8f9fa !important;
        border: 1px solid #ddd !important;
    }
}
</style>

<div class="mortalitas-container">
    <div class="mortalitas-title">MORTALITAS & SURVIVAL</div>
    <div class="mortalitas-subtitle">Analisis Peluang Hidup dan Mortalitas Berdasarkan Matematika Aktuaria</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# INPUT DATA USER (WIDGET STREAMLIT)
# ============================================================
st.subheader("⌨️ Input Parameter Analisis")

col_in1, col_in2 = st.columns(2)

with col_in1:
    umur = st.number_input("🎂 Umur Saat Ini (Tahun)", min_value=1, max_value=110, value=25, step=1)

with col_in2:
    tahun_analisis = st.number_input("📅 Analisis Sampai Berapa Tahun ke Depan?", min_value=1, max_value=100, value=20, step=1)

# ============================================================
# PROSES PERHITUNGAN MATEMATIKA AKTUARIA
# ============================================================

# Peluang meninggal sederhana (Model Linier Aktuaria)
qx = 0.0005 + (umur / 100000)

# Peluang hidup (px)
px = 1 - qx

# Survival probability dalam n tahun (npx)
survival = px ** tahun_analisis

# Peluang meninggal dalam n tahun (nqx)
death_prob = 1 - survival

# Expected future lifetime sederhana (E[x])
ex = 75 - umur if umur < 75 else 5

# ============================================================
# OUTPUT HASIL UI (RESULT CARDS)
# ============================================================
st.markdown('<div style="margin-top:20px;"></div>', unsafe_allow_html=True)
col_res1, col_res2, col_res3 = st.columns(3)

with col_res1:
    st.markdown(f"""
    <div class="result-card">
        <div class="card-label">Peluang Bertahan Hidup</div>
        <div class="card-val">{survival*100:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col_res2:
    st.markdown(f"""
    <div class="result-card">
        <div class="card-label">Peluang Meninggal</div>
        <div class="card-val">{death_prob*100:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col_res3:
    st.markdown(f"""
    <div class="result-card">
        <div class="card-label">Expected Lifetime</div>
        <div class="card-val">±{ex} Tahun</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================
# GRAFIK SURVIVAL (MATPLOTLIB)
# ============================================================
st.markdown('<div style="margin-top:40px;"></div>', unsafe_allow_html=True)
col_viz, col_tbl = st.columns([3, 2])

# Data untuk grafik
tahun_list = list(range(0, tahun_analisis + 1))
survival_list = [(px ** t) * 100 for t in tahun_list]

with col_viz:
    st.write("📊 **Grafik Proyeksi Peluang Survival**")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(tahun_list, survival_list, color='#d63384', linewidth=3, marker='o', markersize=4, label="Peluang Hidup (%)")
    ax.fill_between(tahun_list, survival_list, color='#ffcad4', alpha=0.3)
    ax.set_xlabel("Tahun ke-n")
    ax.set_ylabel("Peluang Bertahan Hidup (%)")
    ax.set_title("Penurunan Probabilitas Survival Seiring Waktu")
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    st.pyplot(fig)

with col_tbl:
    st.write("📋 **Tabel Proyeksi Tahunan**")
    df = pd.DataFrame({
        "Tahun ke-": tahun_list,
        "Peluang Survival (%)": [f"{round(x,2)}%" for x in survival_list]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)

# ============================================================
# REKOMENDASI SISTEM
# ============================================================
if survival > 0.90:
    rekomendasi = "✅ **Risiko mortalitas relatif rendah.** Fokus utama disarankan pada akumulasi aset jangka panjang, investasi agresif, dan perencanaan dana pensiun dini."
elif survival > 0.75:
    rekomendasi = "⚠️ **Risiko mortalitas sedang.** Disarankan untuk mulai mempertimbangkan proteksi asuransi jiwa (Term Life) guna melindungi tanggungan finansial keluarga."
else:
    rekomendasi = "🚨 **Risiko mortalitas cukup tinggi.** Disarankan untuk segera memperkuat perlindungan finansial, melakukan evaluasi asuransi kesehatan, dan meninjau kembali wasiat atau distribusi aset."

st.markdown(f"""
<div class="rekom-box">
    <div class="rekom-title">💡 Rekomendasi Sistem</div>
    <div class="rekom-text">{rekomendasi}</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ACTION BUTTONS & NAVIGASI FOOTER (SAMA SEPERTI TVM.PY)
# ============================================================
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])

with col_btn1:
    # Trigger cetak browser/simpan PDF
    if st.button("🖨️ Cetak Laporan (PDF/Print)", use_container_width=True):
        st.markdown("""
            <script>
                window.print();
            </script>
        """, unsafe_allow_html=True)

with col_btn3:
    # Navigasi kembali ke menu utama secara aman
    if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
        st.switch_page("pages/menu.py")

# Branding Footer khusus web saja
st.markdown("""
<div class="no-print" style="text-align: center; color: #aaa; margin-top: 30px; font-size: 12px; font-family: 'Poppins';">
    &lt;/&gt; Actuarial Decision Support System — Mortality Analysis Module. Dibuat oleh Najla Nafisa Arsy
</div>
""", unsafe_allow_html=True)