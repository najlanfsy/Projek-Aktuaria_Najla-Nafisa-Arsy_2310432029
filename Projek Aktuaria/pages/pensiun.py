# ============================================================
# 👴 PERHITUNGAN DANA PENSIUN PAGE
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
    page_title="Dana Pensiun - Actuarial DSS",
    page_icon="👴",
    layout="wide"
)

# ============================================================
# CSS CUSTOM (Pink Minimalist & Print Support)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap');

/* Style Latar Belakang */
.stApp {
    background-color: #fff7fa;
}

/* Header Container */
.pension-container {
    background: linear-gradient(135deg, #ffb3c7, #ffc2d1, #ffd6e0);
    padding: 35px;
    border-radius: 35px;
    margin-bottom: 25px;
    box-shadow: 0px 12px 35px rgba(255,105,135,0.18);
    text-align: center;
}

.pension-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    color: white;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.pension-subtitle {
    font-family: 'Poppins', sans-serif;
    color: white;
    font-size: 16px;
    font-weight: 300;
}

/* Box Hasil */
.result-box {
    background: white;
    padding: 35px;
    border-radius: 30px;
    margin-top: 25px;
    margin-bottom: 25px;
    box-shadow: 0px 10px 30px rgba(255,105,135,0.15);
}

.result-title {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    color: #ff4d88;
    text-align: center;
    margin-bottom: 25px;
}

/* Card Perhitungan */
.res-card {
    background: linear-gradient(135deg, #ffb3c7, #ffd6e0);
    padding: 25px;
    border-radius: 25px;
    text-align: center;
    color: white;
    box-shadow: 0px 6px 18px rgba(255,105,135,0.15);
}

.card-label {
    font-family: 'Poppins';
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 8px;
}

.card-val {
    font-family: 'Poppins';
    font-size: 22px;
    font-weight: 700;
}

/* Status Box */
.status-banner {
    margin-top: 25px;
    padding: 20px;
    border-radius: 20px;
    text-align: center;
    font-family: 'Poppins';
    font-size: 18px;
    font-weight: 600;
    color: white;
}

/* CSS KHUSUS PRINT LAPORAN */
@media print {
    [data-testid="stSidebar"], 
    .stButton, 
    [data-testid="stForm"],
    .no-print,
    [data-testid="stHeader"],
    .stDownloadButton {
        display: none !important;
    }
    .stApp {
        background: white !important;
    }
    .result-box {
        box-shadow: none !important;
        border: 1px solid #eee !important;
    }
    .res-card {
        color: black !important;
        background: #fdf2f4 !important;
        border: 1px solid #ffcad4 !important;
    }
}
</style>

<div class="pension-container">
    <div class="pension-title">DANA PENSIUN</div>
    <div class="pension-subtitle">Simulasi Perencanaan Dana Masa Tua Strategis</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# INPUT DATA USER
# ============================================================
st.subheader("⌨️ Input Parameter Pensiun")

col_in1, col_in2 = st.columns(2)

with col_in1:
    nama = st.text_input("👤 Nama Pengguna", value=st.session_state.get('nama_user', 'Najla Nafisa Arsy'))
    umur_sekarang = st.number_input("🎂 Umur Sekarang (Tahun)", min_value=15, max_value=80, value=25)
    umur_pensiun = st.number_input("👴 Rencana Umur Pensiun", min_value=umur_sekarang+1, max_value=100, value=55)

with col_in2:
    investasi_bulanan = st.number_input("💵 Investasi Bulanan (Rp)", min_value=0.0, value=1000000.0, step=100000.0, format="%.0f")
    bunga_tahunan = st.number_input("📈 Bunga Investasi Tahunan (%)", min_value=0.0, max_value=100.0, value=8.0, step=0.1) / 100
    target_dana = st.number_input("🎯 Target Dana Pensiun (Rp)", min_value=0.0, value=1000000000.0, step=10000000.0, format="%.0f")

# ============================================================
# LOGIKA PERHITUNGAN AKTUARIA
# ============================================================
lama_investasi = umur_pensiun - umur_sekarang
total_bulan = lama_investasi * 12
bunga_bulanan = bunga_tahunan / 12

# Hitung Future Value (FV) Annuity Due/Ordinary
if bunga_bulanan > 0:
    future_value = investasi_bulanan * (((1 + bunga_bulanan)**total_bulan - 1) / bunga_bulanan)
else:
    future_value = investasi_bulanan * total_bulan

# Status Pencapaian
if future_value >= target_dana:
    status_msg = "🎯 Target Dana Pensiun Tercapai"
    banner_color = "#4CAF50" # Hijau
    rekom_bg = "#f1fff5"
    rekom_title_color = "#28a745"
    rekom_text = "Selamat! Strategi investasi Anda saat ini diperkirakan sudah cukup untuk mencapai kemandirian finansial di masa tua sesuai target."
else:
    status_msg = "⚠️ Target Dana Pensiun Belum Tercapai"
    banner_color = "#ff4d6d" # Merah Muda Tua
    rekom_bg = "#fff0f4"
    rekom_title_color = "#ff4d88"
    kekurangan = target_dana - future_value
    tambahan_bulanan = kekurangan / (((1 + bunga_bulanan)**total_bulan - 1) / bunga_bulanan) if bunga_bulanan > 0 else kekurangan / total_bulan
    rekom_text = f"Dana pensiun Anda diproyeksikan masih kurang. Disarankan untuk menambah investasi bulanan sebesar **Rp {tambahan_bulanan:,.0f}** agar target Anda tercapai."

# ============================================================
# OUTPUT HASIL UI
# ============================================================
st.markdown('<div class="result-box">', unsafe_allow_html=True)
st.markdown('<div class="result-title">Hasil Simulasi Dana Pensiun</div>', unsafe_allow_html=True)

col_res1, col_res2, col_res3 = st.columns(3)

with col_res1:
    st.markdown(f'<div class="res-card"><div class="card-label">Nama Pengguna</div><div class="card-val">{nama}</div></div>', unsafe_allow_html=True)

with col_res2:
    st.markdown(f'<div class="res-card"><div class="card-label">Masa Investasi</div><div class="card-val">{lama_investasi} Tahun</div></div>', unsafe_allow_html=True)

with col_res3:
    st.markdown(f'<div class="res-card"><div class="card-label">Estimasi Dana Akhir</div><div class="card-val">Rp {future_value:,.0f}</div></div>', unsafe_allow_html=True)

st.markdown(f'<div class="status-banner" style="background:{banner_color};">{status_msg}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================
# GRAFIK & TABEL PERTUMBUHAN
# ============================================================
col_viz, col_data = st.columns([3, 2])

# Simulasi data untuk grafik
usia_list = []
dana_list = []
saldo_temp = 0
for u in range(umur_sekarang, umur_pensiun + 1):
    usia_list.append(u)
    dana_list.append(saldo_temp)
    # Akumulasi 12 bulan per tahun
    for _ in range(12):
        saldo_temp = saldo_temp * (1 + bunga_bulanan) + investasi_bulanan

with col_viz:
    st.write("📊 **Proyeksi Pertumbuhan Dana Pensiun**")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(usia_list, dana_list, color='#ff4d88', linewidth=3, marker='o', markersize=4)
    ax.fill_between(usia_list, dana_list, color='#ff4d88', alpha=0.1)
    ax.set_xlabel("Usia (Tahun)")
    ax.set_ylabel("Total Dana (Rp)")
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)

with col_data:
    st.write("📋 **Tabel Akumulasi Tahunan**")
    df_pensiun = pd.DataFrame({
        "Usia": usia_list,
        "Estimasi Dana (Rp)": [f"Rp {x:,.0f}" for x in dana_list]
    })
    st.dataframe(df_pensiun, use_container_width=True, hide_index=True)

# ============================================================
# REKOMENDASI SISTEM
# ============================================================
st.markdown(f"""
<div style="background:{rekom_bg}; padding:25px; border-radius:25px; margin-top:20px; box-shadow:0px 5px 15px rgba(0,0,0,0.05); border-left: 5px solid {rekom_title_color};">
    <h3 style="color:{rekom_title_color}; margin-top:0; font-family:'Poppins';">💡 Rekomendasi Sistem</h3>
    <p style="font-family:'Poppins'; color:#444; line-height:1.8;">{rekom_text}</p>
</div>
""", unsafe_allow_html=True)

# ============================================================
# NAVIGASI FOOTER (CETAK & KEMBALI)
# ============================================================
st.markdown("---")
col_f1, col_f2, col_f3 = st.columns([2, 2, 2])

with col_f1:
    if st.button("🖨️ Cetak Laporan PDF", use_container_width=True):
        st.markdown("<script>window.print();</script>", unsafe_allow_html=True)

with col_f3:
    if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
        st.switch_page("pages/menu.py")

# Footer Branding
st.markdown("""
<div class="no-print" style="text-align: center; color: #aaa; margin-top: 30px; font-size: 12px; font-family: 'Poppins';">
    &lt;/&gt; Actuarial Decision Support System — Retirement Simulation Module. Dibuat oleh Najla Nafisa Arsy
</div>
""", unsafe_allow_html=True)