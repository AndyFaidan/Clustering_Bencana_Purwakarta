import pickle
import streamlit as st
import pandas as pd
from PIL import Image

##import data
image = Image.open("house3.jpg")
st.image(image, use_column_width=True)
data = pd.read_csv('kc_house_data.csv')
model = pickle.load(open('estimasi_rumah.sav', 'rb'))
st.title('Estimasi Harga Rumah')
st.text('(andy sofyan guspriyanto 191351112)')

#input data
bedrooms = st.number_input('Berapa Banyak Kamar')

bathrooms= st.number_input('Berapa Banyak Kamar Mandi')

sqft_living   = st.number_input('Ukuran Persegi Ruang Tamu')

sqft_lot = st.number_input('Ukuran Persegi Luas Tanah')

floors  = st.number_input('Jumlah Lantai')

waterfront = st.number_input('Apakah Rumah Menghadap Ke Tepi Laut Atau Tidak ')

view = st.number_input('Indeks Seberapa Bagus Tampilan rumah')

condition = st.number_input('Indeks Kondisi Rumah')

grade = st.number_input('Indeks Tingkat Kontruksi Dan Desain Yang Tinggi')

sqft_above = st.number_input('luas interior tingkat atas')

sqft_basement = st.number_input('luas interior tingkat bawah')

yr_built = st.number_input('Tahun Pertama Kali Rumah Di Bangun')

yr_renovated = st.number_input('Tahun Terakhir Rumah Di Renovasi')

lat = st.number_input('latitudinal')

long = st.number_input('longitudinal')

sqft_living15 = st.number_input('luas hunian interior untuk 15 tetangga terdekat')

sqft_lot15 = st.number_input  ('luas lahan untuk 15 tetangga terdekat')          




predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, lat, long, sqft_living15, sqft_lot15]]
    )
    st.write ('Estimasi harga  rumah dalam Ponds : ', predict)
    st.write ('Estimasi harga  rumah dalam IDR (Juta) :', predict*19000)




