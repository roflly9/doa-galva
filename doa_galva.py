import streamlit as st
import os

# Daftar Nama Staf Galva Manado (Urutan Tetap)
staf = [
    "David", "Endra", "Eric", "Gerald", "Nofri", 
    "Ricky", "Roflly", "Romasta", "Sendhy", "Steven", 
    "Valentine", "Waldy", "Yulisfer"
]

INDEX_FILE = "last_index.txt"

def ambil_index():
    if not os.path.exists(INDEX_FILE):
        return 0
    with open(INDEX_FILE, "r") as f:
        return int(f.read().strip())

def simpan_index(idx):
    with open(INDEX_FILE, "w") as f:
        f.write(str(idx))

st.set_page_config(page_title="Doa Pagi Galva", page_icon="🙏")

st.title("🙏 Aplikasi Doa Galva Manado")

# Ambil urutan saat ini
current_idx = ambil_index()
petugas = staf[current_idx]

# Tampilan utama
st.subheader("Petugas Hari Ini:")
st.info(f"✨ **{petugas}** ✨")

with st.form("doa_form"):
    ayat = st.text_input("Masukkan Ayat Alkitab yang dibaca:")
    submit = st.form_submit_button("Selesai Berdoa & Update Urutan")
    
    if submit:
        if ayat:
            # Hitung urutan berikutnya (jika sudah Yulisfer, balik ke David)
            next_idx = (current_idx + 1) % len(staf)
            simpan_index(next_idx)
            
            st.success(f"Terima kasih {petugas}!")
            st.write(f"Ayat hari ini: *{ayat}*")
            st.write(f"Jadwal berikutnya: **{staf[next_idx]}**")
            
            # Berikan tombol untuk refresh halaman
            if st.button("OK, Lanjutkan"):
                st.rerun()
        else:
            st.error("Mohon isi ayat Alkitab terlebih dahulu.")

# Informasi Urutan (Opsional)
with st.expander("Lihat Antrean Lengkap"):
    st.write(" -> ".join(staf))