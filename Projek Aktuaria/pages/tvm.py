# ============================================================
# 📈 TIME VALUE OF MONEY PAGE
# Actuarial Decision Support System
# Streamlit Web Version
# ============================================================

import streamlit as st
import streamlit.components.v1 as components  # Komponen native untuk menangani JavaScript Cetak
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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
    page_title="Time Value of Money - Actuarial DSS",
    page_icon="💰",
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
.tvm-container {
    background: linear-gradient(135deg, #ffb3c7, #ffc2d1, #ffd6e0);
    padding: 35px;
    border-radius: 35px;
    margin-bottom: 25px;
    box-shadow: 0px 12px 35px rgba(255,105,135,0.18);
    text-align: center;
}

.tvm-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    color: white;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.tvm-subtitle {
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
    [data-testid="stSidebar"], 
    [data-testid="stForm"],
    [data-testid="stHeader"],
    .stButton, 
    .no-print,
    iframe {
        display: none !important; /* Sembunyikan elemen navigasi dan tombol saat cetak */
    }
    .stApp {
        background: white !important;
        color: black !important;
    }
}
</style>

<div class="tvm-container">
    <div class="tvm-title">TIME VALUE OF MONEY</div>
    <div class="tvm-subtitle">Analisis Nilai Waktu Uang dan Pertumbuhan Investasi</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# INPUT DATA USER (FORM STREAMLIT)
# ============================================================
st.subheader("⌨️ Input Data Investasi")

col_in1, col_in2 = st.columns(2)

with col_in1:
    modal_awal = st.number_input("💰 Modal Awal (Rp)", min_value=0.0, value=10000000.0, step=500000.0, format="%.0f")
    bunga = st.number_input("📈 Suku Bunga Tahunan (%)", min_value=0.0, max_value=100.0, value=7.5, step=0.1)

with col_in2:
    tahun = st.number_input("📅 Lama Investasi (Tahun)", min_value=1, max_value=100, value=5, step=1)
    tambahan = st.number_input("💵 Investasi Tambahan per Tahun (Rp)", min_value=0.0, value=2000000.0, step=100000.0, format="%.0f")

# ============================================================
# PROSES PERHITUNGAN
# ============================================================
r = bunga / 100
saldo = modal_awal

tahun_list = [0]
saldo_list = [modal_awal]

for t in range(1, int(tahun) + 1):
    saldo = (saldo + tambahan) * (1 + r)
    tahun_list.append(t)
    saldo_list.append(round(saldo, 2))

future_value = saldo

# ============================================================
# OUTPUT HASIL UI
# ============================================================
st.markdown(f"""
<div class="result-box">
    <div class="result-title">Hasil Perhitungan</div>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 15px;">
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 200px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Modal Awal</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">Rp {modal_awal:,.0f}</div>
        </div>
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 200px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Suku Bunga</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">{bunga:.1f}%</div>
        </div>
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 200px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Future Value</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">Rp {future_value:,.0f}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LAYOUT GRAFIK DAN TABEL DATA
# ============================================================
col_graph, col_table = st.columns([3, 2])

with col_graph:
    st.write("📊 **Visualisasi Pertumbuhan Dana**")
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(tahun_list, saldo_list, linewidth=3, marker='o', color='#d63384', label="Saldo Dana")
    ax.set_title("Grafik Pertumbuhan Investasi", fontsize=14, fontname='sans-serif', weight='bold', color='#333333')
    ax.set_xlabel("Tahun", fontsize=11)
    ax.set_ylabel("Saldo Investasi (Rp)", fontsize=11)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    st.pyplot(fig)

with col_table:
    st.write("📋 **Tabel Akumulasi Tahunan**")
    df = pd.DataFrame({
        "Tahun Ke-": tahun_list,
        "Saldo Investasi (Rp)": [f"Rp {x:,.2f}" for x in saldo_list]
    })
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Unduh Data Mentah (.csv)",
        data=csv,
        file_name="laporan_tvm_data.csv",
        mime="text/csv",
        key="download-csv"
    )

# ============================================================
# REKOMENDASI FINANSIAL
# ============================================================
if future_value >= 100000000:
    rekomendasi = "Investasi menunjukkan pertumbuhan yang sangat baik. Target keuangan jangka panjang berpotensi besar tercapai secara optimal."
else:
    rekomendasi = "Pertumbuhan investasi masih dapat ditingkatkan. Sangat disarankan untuk menambah nilai investasi tahunan secara berkala atau memperpanjang masa periode investasi."

st.markdown(f"""
<div class="rekom-box">
    <div class="rekom-title">💡 Rekomendasi Finansial</div>
    <div class="rekom-text">{rekomendasi}</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ACTION BUTTONS & NAVIGASI FOOTER (FITUR CETAK & KEMBALI)
# ============================================================
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])

with col_btn1:
    # Menggunakan HTML Komponen murni (iframe aman) agar browser mengeksekusi print ke window utama
    print_html = """
    <style>
        .luxury-print-btn {
            background: linear-gradient(135deg, #ff4d88, #ff758f);
            color: white !important;
            border: none;
            padding: 10px 20px;
            font-family: 'Poppins', sans-serif;
            font-size: 15px;
            font-weight: 500;
            border-radius: 8px;
            cursor: pointer;
            width: 100%;
            box-shadow: 0px 4px 15px rgba(255, 77, 136, 0.2);
            transition: all 0.3s ease;
            text-align: center;
        }
        .luxury-print-btn:hover {
            background: linear-gradient(135deg, #ff2a70, #ff4d88);
            box-shadow: 0px 6px 20px rgba(255, 77, 136, 0.3);
        }
    </style>
    <button class="luxury-print-btn" onclick="window.parent.parent.print()">🖨️ Cetak Hasil Laporan (PDF/Print)</button>
    """
    components.html(print_html, height=50)

with col_btn3:
    if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
        st.switch_page("pages/menu.py")

# Branding Footer khusus web screen saja
st.markdown("""
<div class="no-print" style="text-align: center; color: #aaa; margin-top: 30px; font-size: 12px; font-family: 'Poppins';">
    &lt;/&gt; Actuarial Decision Support System — Python Core Module. Dibuat oleh Najla Nafisa Arsy
</div>
""", unsafe_allow_html=True)
