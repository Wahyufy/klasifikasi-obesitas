import joblib
import streamlit as st

# Load the model from the file
model = joblib.load('model_logistic_regression.pkl')

# Function to predict obesity level
def predict_obesity_level(jenis_kelamin, tinggi_badan, berat_badan):
    input_data = [[jenis_kelamin, tinggi_badan, berat_badan]]
    prediction = model.predict(input_data)
    return prediction[0]

# Function to calculate BMI
def hitung_bmi(tinggi_badan, berat_badan):
    tinggi_meter = tinggi_badan / 100
    bmi = berat_badan / (tinggi_meter ** 2)
    return bmi

# Function to provide healthy lifestyle suggestions
def saran_gaya_hidup(bmi, aktivitas_fisik, asupan_buah_sayur):
    saran = ""
    if bmi < 18.5:
        saran += "Anda kekurangan berat badan. Disarankan untuk menambah asupan makanan bergizi dan melakukan aktivitas fisik ringan.\n"
    elif bmi >= 25:
        saran += "Anda kelebihan berat badan. Disarankan untuk mengurangi asupan kalori dan meningkatkan aktivitas fisik.\n"

    if aktivitas_fisik < 150:
        saran += "Anda perlu meningkatkan aktivitas fisik minimal 150 menit per minggu.\n"

    if asupan_buah_sayur < 5:
        saran += "Anda perlu meningkatkan asupan buah dan sayur minimal 5 porsi per hari.\n"

    return saran

# Function to label the prediction
def label_prediction(prediction):
    labels = {
        0: "Sangat Lemah",
        1: "Lemah",
        2: "Normal",
        3: "Kelebihan Berat Badan",
        4: "Obesitas",
        5: "Obesitas Ekstrim"
    }
    return labels.get(prediction, "Unknown")

# Streamlit app
st.title("Obesity Level and Healthy Lifestyle Suggestions")

st.write("This app predicts the obesity level based on gender, height, and weight, and provides healthy lifestyle suggestions.")

# Input widgets
jenis_kelamin = st.radio("Jenis Kelamin:", [0, 1], format_func=lambda x: "Laki-laki" if x == 0 else "Perempuan")
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=50, max_value=250, value=160)
berat_badan = st.number_input("Berat Badan (kg):", min_value=20, max_value=200, value=70)
aktivitas_fisik = st.number_input("Durasi Aktivitas Fisik per Minggu (menit):", min_value=0, value=0)
asupan_buah_sayur = st.number_input("Jumlah Porsi Buah dan Sayur per Hari (kalori) :", min_value=0, value=0)

# Prediction and suggestions
if st.button("Predict and Get Suggestions"):
    hasil_prediksi = predict_obesity_level(jenis_kelamin, tinggi_badan, berat_badan)
    prediksi_label = label_prediction(hasil_prediksi)
    bmi = hitung_bmi(tinggi_badan, berat_badan)
    saran = saran_gaya_hidup(bmi, aktivitas_fisik, asupan_buah_sayur)
    
    st.write(f"Kategori anda berada pada level: {prediksi_label}")
    st.write(f"Indeks Massa Tubuh (BMI): {bmi:.2f}")
    st.write("Saran Gaya Hidup Sehat:")
    st.write(saran)
