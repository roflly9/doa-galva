import streamlit as st
import os

# Nama file untuk menyimpan antrean di server Streamlit
QUEUE_FILE = "antrean_doa_galva.txt"

# Urutan tetap staf Galva Manado
staf_awal = [
    "David", "Endra", "Eric", "Gerald", "Nofri", 
    "Ricky", "Roflly", "Romasta", "Sendhy", "Steven", 
    "Valentine", "Waldy", "Yulisfer"
]

def muat_antrean():
    if not os.path.exists(QUEUE_FILE):
        return staf_awal
    with open(QUEUE_FILE, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def simpan_antrean(daftar):
    with open(QUEUE_FILE, "w") as f:
        for nama in daftar:
            f.write(nama + "\n")

st.set_page_config(page_title="Doa Pagi Galva", page_icon="🙏")
st.title("🙏 Aplikasi Doa Galva Manado")

# Ambil antrean saat ini
antrean = muat_antrean()
petugas_skrg = antrean[0]

st.subheader("Petugas Hari Ini:")
st.info(f"✨ **{petugas_skrg}** ✨")

# --- FORM UTAMA ---
with st.form("doa_form"):
    ayat = st.text_input("Masukkan Ayat Alkitab yang dibaca:")
    submit = st.form_submit_button("Selesai Berdoa & Update Urutan")
    
    if submit:
        if ayat:
            # Pindahkan ke urutan terakhir hanya jika sudah berdoa
            orang_selesai = antrean.pop(0)
            antrean.append(orang_selesai)
            simpan_antrean(antrean)
            st.success(f"Terima kasih {orang_selesai}!")
            st.rerun()
        else:
            st.error("Mohon isi ayat Alkitab terlebih dahulu.")

# --- TOMBOL SKIP (JIKA TERLAMBAT) ---
st.divider()
st.write("⚠️ **Petugas Terlambat?**")
if st.button(f"Lewati {petugas_skrg} (Tetap Bertugas Besok)"):
    if len(antrean) > 1:
        # Tukar posisi 1 dan 2 agar yang terlambat muncul lagi besok
        antrean[0], antrean[1] = antrean[1], antrean[0]
        simpan_antrean(antrean)
        st.warning(f"{petugas_skrg} digeser. Hari ini digantikan oleh {antrean[0]}.")
        st.rerun()

with st.expander("Lihat Antrean Lengkap"):
    for i, nama in enumerate(antrean):
        st.write(f"{i+1}. {nama}")