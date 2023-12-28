import pandas as pd

# Memuat data dari CSV
file_path = "DatasetDRB_peta.csv"
df = pd.read_csv(file_path)

# Pilih kolom-kolom yang relevan
kolom_populasi = df[['Gempa', 'Longsor']]  # Memilih kolom Gempa dan Longsor

# Hitung populasi terbaru (tahun 2022)
populasi_terbaru = kolom_populasi.mean(axis=1)  # Menggunakan rata-rata dari kolom Gempa dan Longsor

# Hitung kuartil
Q1 = populasi_terbaru.quantile(0.25)
Q2 = populasi_terbaru.quantile(0.5)
Q3 = populasi_terbaru.quantile(0.75)

# Fungsi untuk menentukan kategori kerawanan
def tentukan_kategori_kerawanan(populasi):
    if populasi <= Q1:
        return 'Tidak Rawan'
    elif Q1 < populasi <= Q2:
        return 'Rawan'
    else:
        return 'Sangat Rawan'

# Tambahkan kolom kategori kerawanan ke DataFrame
df['Kategori Kerawanan'] = populasi_terbaru.apply(tentukan_kategori_kerawanan)

# Hitung jumlah desa untuk setiap kategori kerawanan
jumlah_tidak_rawan = df[df['Kategori Kerawanan'] == 'Tidak Rawan'].shape[0]
jumlah_rawan = df[df['Kategori Kerawanan'] == 'Rawan'].shape[0]
jumlah_sangat_rawan = df[df['Kategori Kerawanan'] == 'Sangat Rawan'].shape[0]

# Tampilkan hasil
print(f"Jumlah Tidak Rawan: {jumlah_tidak_rawan}")
print(f"Jumlah Rawan: {jumlah_rawan}")
print(f"Jumlah Sangat Rawan: {jumlah_sangat_rawan}")

# Tampilkan rata-rata populasi untuk setiap kategori kerawanan
print(f"Rata-rata Populasi Tidak Rawan: {Q1:.2f} jiwa")
print(f"Rata-rata Populasi Rawan: {Q2:.2f} jiwa")
print(f"Rata-rata Populasi Sangat Rawan: {Q3:.2f} jiwa")
