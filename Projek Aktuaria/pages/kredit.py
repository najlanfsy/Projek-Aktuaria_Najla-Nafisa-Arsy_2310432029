# ============================================================
# 🏦 SIMULASI KREDIT PAGE
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
    page_title="Simulasi Kredit - Actuarial DSS",
    page_icon="🏦",
    layout="wide"
)

# ============================================================
# CSS CUSTOM (Mendukung Tampilan Web & Sembunyikan Tombol Saat Print)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;700&family=Playfair+Display:wght@700&display=swap');

/* Style Latar Belakang Utama */
.stApp {
    background-color: #fff7fa;
}

/* Container Utama Header */
.loan-container {
    background: linear-gradient(135deg, #ffb3c7, #ffc2d1, #ffd6e0);
    padding: 35px;
    border-radius: 35px;
    margin-bottom: 25px;
    box-shadow: 0px 12px 35px rgba(255,105,135,0.18);
    text-align: center;
}

.loan-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    color: white;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.loan-subtitle {
    font-family: 'Poppins', sans-serif;
    color: white;
    font-size: 16px;
    font-weight: 300;
}

/* Kotak Hasil */
.result-box {
    background: linear-gradient(135deg, #ffcad4, #ffe5ec);
    padding: 30px;
    border-radius: 30px;
    margin-top: 25px;
    margin-bottom: 25px;
    box-shadow: 0px 8px 25px rgba(255,105,135,0.15);
}

.result-title {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    color: #d63384;
    text-align: center;
    margin-bottom: 25px;
}

/* Kotak Rekomendasi */
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
    margin-bottom: 15px;
}

.rekom-text {
    font-family: 'Poppins', sans-serif;
    color: #555;
    font-size: 15px;
    line-height: 1.9;
}

/* CSS KHUSUS SAAT CETAK LAPORAN (PRINT/PDF) */
@media print {
    /* Sembunyikan sidebar, tombol navigasi, komponen input, dan footer */
    [data-testid="stSidebar"], 
    .stButton, 
    [data-testid="stForm"],
    .no-print,
    [data-testid="stHeader"] {
        display: none !important;
    }
    /* Sesuaikan ukuran halaman cetak */
    .stApp {
        background: white !important;
        color: black !important;
    }
}
</style>

<div class="loan-container">
    <div class="loan-title">SIMULASI KREDIT</div>
    <div class="loan-subtitle">Analisis Cicilan, Bunga, dan Tabel Amortisasi Kredit</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# INPUT DATA USER (FORM STREAMLIT)
# ============================================================
st.subheader("⌨️ Input Data Kredit")

col_in1, col_in2 = st.columns(2)

with col_in1:
    pinjaman = st.number_input("💰 Jumlah Pinjaman (Rp)", min_value=0.0, value=50000000.0, step=1000000.0, format="%.0f")
    bunga_tahunan = st.number_input("📈 Bunga Tahunan (%)", min_value=0.0, max_value=100.0, value=10.0, step=0.1)

with col_in2:
    tenor = st.number_input("📅 Tenor Pinjaman (Tahun)", min_value=1, max_value=50, value=3, step=1)

# ============================================================
# PROSES PERHITUNGAN KREDIT
# ============================================================
r = (bunga_tahunan / 100) / 12
n = int(tenor * 12)

# Mengantisipasi jika bunga diinput 0% agar tidak pembagian nol (ZeroDivisionError)
if r > 0:
    cicilan = (pinjaman * r * (1 + r)**n) / ((1 + r)**n - 1)
else:
    cicilan = pinjaman / n

total_pembayaran = cicilan * n
total_bunga = total_pembayaran - pinjaman

# ============================================================
# GENERATE TABEL AMORTISASI
# ============================================================
saldo = pinjaman
bulan_data = []
cicilan_data = []
pokok_data = []
bunga_data = []
sisa_data = []

for bulan in range(1, n + 1):
    bunga_bayar = saldo * r
    pokok = cicilan - bunga_bayar
    saldo -= pokok
    
    # Pengaman jika ada nilai sisa minus sekecil pembulatan floating point
    if saldo < 0:
        saldo = 0
        
    bulan_data.append(bulan)
    cicilan_data.append(round(cicilan, 2))
    pokok_data.append(round(pokok, 2))
    bunga_data.append(round(bunga_bayar, 2))
    sisa_data.append(round(saldo, 2))

# ============================================================
# OUTPUT HASIL UI
# ============================================================
st.markdown(f"""
<div class="result-box">
    <div class="result-title">Hasil Simulasi Kredit</div>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 15px;">
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 220px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Cicilan per Bulan</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">Rp {cicilan:,.0f}</div>
        </div>
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 220px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Total Pembayaran</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">Rp {total_pembayaran:,.0f}</div>
        </div>
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 220px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Total Bunga</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">Rp {total_bunga:,.0f}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LAYOUT GRAFIK DAN TABEL DATA AMORTISASI
# ============================================================
col_graph, col_table = st.columns([3, 2])

with col_graph:
    st.write("📊 **Grafik Sisa Pokok Pinjaman**")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(bulan_data, sisa_data, linewidth=3, color='#d63384', label="Sisa Kredit")
    ax.set_title("Grafik Pelunasan Pinjaman", fontsize=14, fontname='sans-serif', weight='bold', color='#333333')
    ax.set_xlabel("Bulan", fontsize=11)
    ax.set_ylabel("Sisa Pinjaman (Rp)", fontsize=11)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    st.pyplot(fig)

with col_table:
    st.write("📋 **Tabel Amortisasi Lengkap**")
    df = pd.DataFrame({
        "Bulan": bulan_data,
        "Cicilan (Rp)": [f"Rp {x:,.2f}" for x in cicilan_data],
        "Pokok (Rp)": [f"Rp {x:,.2f}" for x in pokok_data],
        "Bunga (Rp)": [f"Rp {x:,.2f}" for x in bunga_data],
        "Sisa Pinjaman (Rp)": [f"Rp {x:,.2f}" for x in sisa_data]
    })
    
    # Menampilkan DataFrame interaktif berekstensi penuh
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Tombol export CSV data amortisasi
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Unduh Tabel Amortisasi (.csv)",
        data=csv,
        file_name="tabel_amortisasi_kredit.csv",
        mime="text/csv",
        key="download-csv"
    )

# ============================================================
# REKOMENDASI SISTEM
# ============================================================
if total_bunga > (0.5 * pinjaman):
    rekomendasi = "⚠️ **Total beban bunga akumulatif cukup besar.** Disarankan untuk mempertimbangkan pengambilan masa tenor yang lebih pendek atau meningkatkan jumlah setoran uang muka awal guna menekan akumulasi margin bunga."
else:
    rekomendasi = "✅ **Struktur kredit terpantau cukup baik.** Komposisi bunga tahunan masih berada dalam batas aman dan rasio pinjaman dinilai ideal untuk dilanjutkan sesuai dengan tenor yang dipilih."

st.markdown(f"""
<div class="rekom-box">
    <div class="rekom-title">💡 Rekomendasi Sistem</div>
    <div class="rekom-text">{rekomendasi}</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ACTION BUTTONS & NAVIGASI FOOTER (SAMA DENGAN TVM.PY)
# ============================================================
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])

with col_btn1:
    # Memicu pemanggilan fungsi print bawaan sistem operasi komputer
    if st.button("🖨️ Cetak Hasil Laporan (PDF/Print)", use_container_width=True):
        st.markdown("""
            <script>
                window.print();
            </script>
        """, unsafe_allow_html=True)

with col_btn3:
    # Melompat kembali ke panel dashboard menu secara terproteksi
    if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
        st.switch_page("pages/menu.py")

# Branding Footer khusus layar monitor saja
st.markdown("""
<div class="no-print" style="text-align: center; color: #aaa; margin-top: 30px; font-size: 12px; font-family: 'Poppins';">
    &lt;/&gt; Actuarial Decision Support System — Python Core Module. Dibuat oleh Najla Nafisa Arsy
</div>
""", unsafe_allow_html=True)