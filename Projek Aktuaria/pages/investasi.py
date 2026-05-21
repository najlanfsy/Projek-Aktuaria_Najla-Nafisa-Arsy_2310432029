# ============================================================
# 📈 INVESTASI & ANUITAS PAGE
# Actuarial Decision Support System
# Streamlit Web Version
# ============================================================

import streamlit as st
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
    page_title="Investasi & Anuitas - Actuarial DSS",
    page_icon="📈",
    layout="wide"
)

# ============================================================
# CSS CUSTOM (Mendukung Tampilan Web & Sembunyikan Tombol Saat Print)
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght=300;400;500;700&family=Playfair+Display:wght=700&display=swap');

/* Style Latar Belakang Utama */
.stApp {
    background-color: #fff7fa;
}

/* Container Utama Header */
.inv-container {
    background: linear-gradient(135deg, #ffb3c7, #ffc2d1, #ffd6e0);
    padding: 35px;
    border-radius: 35px;
    margin-bottom: 25px;
    box-shadow: 0px 12px 35px rgba(255,105,135,0.18);
    text-align: center;
}

.inv-title {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    color: white;
    letter-spacing: 2px;
    margin-bottom: 10px;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.12);
}

.inv-subtitle {
    font-family: 'Poppins', sans-serif;
    color: white;
    font-size: 16px;
    font-weight: 300;
}

/* Kotak Hasil Analisis */
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

/* CSS KHUSUS SAAT CETAK LAPORAN (PRINT/PDF) */
@media print {
    [data-testid="stSidebar"], 
    .stButton, 
    [data-testid="stForm"],
    .no-print,
    .stDownloadButton {
        display: none !important;
    }
    .stApp {
        background: white !important;
        color: black !important;
    }
}
</style>

<div class="inv-container">
    <div class="inv-title">INVESTASI & ANUITAS</div>
    <div class="inv-subtitle">Simulasi pertumbuhan investasi dan perhitungan anuitas secara interaktif</div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# INPUT DATA USER (FORM STREAMLIT)
# ============================================================
st.subheader("⌨ nighttime: Input Data Investasi")

col_in1, col_in2 = st.columns(2)

with col_in1:
    modal_awal = st.number_input("💰 Modal Awal (Rp)", min_value=0.0, value=10000000.0, step=500000.0, format="%.0f")
    investasi_bulanan = st.number_input("💵 Investasi Bulanan / Anuitas (Rp)", min_value=0.0, value=500000.0, step=50000.0, format="%.0f")

with col_in2:
    bunga_tahunan = st.number_input("📈 Suku Bunga Tahunan (%)", min_value=0.0, max_value=100.0, value=8.0, step=0.1)
    lama_investasi = st.number_input("📅 Lama Investasi (Tahun)", min_value=1, max_value=100, value=5, step=1)

# ============================================================
# PROSES PERHITUNGAN MATEMATIKA FINANSIAL
# ============================================================
i = bunga_tahunan / 100 / 12  # Bunga per bulan
n = int(lama_investasi * 12)  # Total periode bulan

tahun_list = [0]
saldo_list = [modal_awal]
setoran_kumulatif = [modal_awal]

saldo_berjalan = modal_awal
total_setoran_berjalan = modal_awal

# Menghitung perkembangan dana bulan demi bulan untuk visualisasi grafik & tabel
for bulan in range(1, n + 1):
    saldo_berjalan = (saldo_berjalan * (1 + i)) + investasi_bulanan
    total_setoran_berjalan += investasi_bulanan
    
    # Simpan koordinat data setiap kelipatan 12 bulan (tahunan) untuk grafik/tabel agar rapi
    if bulan % 12 == 0:
        tahun_list.append(bulan // 12)
        saldo_list.append(round(saldo_berjalan, 2))
        setoran_kumulatif.append(total_setoran_berjalan)

future_value = saldo_berjalan
total_setoran = total_setoran_berjalan
keuntungan = future_value - total_setoran

# ============================================================
# OUTPUT HASIL UI
# ============================================================
st.markdown(f"""
<div class="result-box">
    <div class="result-title">Hasil Analisis Investasi</div>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 15px;">
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 250px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Total Setoran</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">Rp {total_setoran:,.0f}</div>
        </div>
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 250px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Nilai Investasi Akhir (FV)</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">Rp {future_value:,.0f}</div>
        </div>
        <div style="background: white; padding: 20px; border-radius: 20px; min-width: 250px; text-align: center; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <div style="color: #888; font-size: 14px; font-family: 'Poppins';">Total Keuntungan (Bunga)</div>
            <div style="color: #d63384; font-size: 22px; font-weight: 700; font-family: 'Poppins';">Rp {keuntungan:,.0f}</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================
# LAYOUT GRAFIK DAN TABEL DATA
# ============================================================
col_graph, col_table = st.columns([3, 2])

with col_graph:
    st.write("📊 **Visualisasi Akumulasi Dana & Anuitas**")
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Membuat grafik perbandingan modal investasi vs hasil akhir majemuk
    ax.plot(tahun_list, saldo_list, linewidth=3, marker='o', color='#d63384', label="Nilai Akhir Dana (FV)")
    ax.fill_between(tahun_list, saldo_list, color='#ffcad4', alpha=0.4)
    ax.plot(tahun_list, setoran_kumulatif, linewidth=2, linestyle='--', color='#888888', label="Total Modal Disetor")
    
    ax.set_title("Grafik Pertumbuhan Investasi", fontsize=14, fontname='sans-serif', weight='bold', color='#333333')
    ax.set_xlabel("Tahun", fontsize=11)
    ax.set_ylabel("Jumlah Dana (Rp)", fontsize=11)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    st.pyplot(fig)

with col_table:
    st.write("📋 **Tabel Akumulasi Tahunan**")
    df = pd.DataFrame({
        "Tahun Ke-": tahun_list,
        "Total Setoran (Rp)": [f"Rp {x:,.0f}" for x in setoran_kumulatif],
        "Saldo Investasi (Rp)": [f"Rp {x:,.2f}" for x in saldo_list]
    })
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Fitur Export berkas spreadsheet .csv
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Unduh Data Mentah (.csv)",
        data=csv,
        file_name="laporan_investasi_anuitas.csv",
        mime="text/csv",
        key="download-csv"
    )

# ============================================================
# ACTION BUTTONS & NAVIGASI FOOTER (SAMA SEPERTI TVM.PY)
# ============================================================
st.markdown("---")
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])

with col_btn1:
    # Trigger jendela cetak otomatis bawaan web browser
    if st.button("🖨️ Cetak Hasil Laporan (PDF/Print)", use_container_width=True):
        st.markdown("""
            <script>
                window.print();
            </script>
        """, unsafe_allow_html=True)

with col_btn3:
    # Tombol balik ke menu utama tanpa merusak token session login
    if st.button("⬅️ Kembali ke Menu Utama", use_container_width=True):
        st.switch_page("pages/menu.py")

# Hak Cipta & Informasi Identitas
st.markdown("""
<div class="no-print" style="text-align: center; color: #aaa; margin-top: 30px; font-size: 12px; font-family: 'Poppins';">
    &lt;/&gt; Actuarial Decision Support System — Python Core Module. Dibuat oleh Najla Nafisa Arsy
</div>
""", unsafe_allow_html=True)