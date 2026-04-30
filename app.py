import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# CONFIGURAÇÃO DA PÁGINA

st.set_page_config(page_title="CardioAI", page_icon="🫀", layout="wide")


# CARREGAMENTO

modelo = joblib.load('modelo_random_forest.pkl')
df = pd.read_csv('heart.csv')


# TÍTULO

st.title("🫀 CardioAI - Classificador de Risco Cardíaco")
st.markdown("Previsão de risco de doença cardíaca com base em dados clínicos do paciente.")


# FUNÇÃO DE ENCODE

def encode_inputs(sex, chest_pain_type, resting_ecg, exercise_angina, st_slope):
    sex_dict = {'M': 1, 'F': 0}
    chest_pain_dict = {'ASY': 0, 'ATA': 1, 'NAP': 2, 'TA': 3}
    resting_ecg_dict = {'LVH': 0, 'Normal': 1, 'ST': 2}
    exercise_angina_dict = {'N': 0, 'Y': 1}
    st_slope_dict = {'Down': 0, 'Flat': 1, 'Up': 2}

    return [
        sex_dict.get(sex, 0),
        chest_pain_dict.get(chest_pain_type, 0),
        resting_ecg_dict.get(resting_ecg, 0),
        exercise_angina_dict.get(exercise_angina, 0),
        st_slope_dict.get(st_slope, 0)
    ]


# SIDEBAR

st.sidebar.header("🧾 Dados do Paciente")

age = st.sidebar.number_input('Idade', 0, 120, 40)
sex = st.sidebar.selectbox('Sexo', ['M', 'F'])
chest_pain_type = st.sidebar.selectbox('Dor no Peito', ['ASY', 'ATA', 'NAP', 'TA'])
resting_bp = st.sidebar.number_input('Pressão (mmHg)', 0, 200, 140)
cholesterol = st.sidebar.number_input('Colesterol', 0, 600, 289)
fasting_bs = st.sidebar.selectbox('Glicose em Jejum', [0, 1], format_func=lambda x: 'Normal' if x == 0 else 'Alterada')
resting_ecg = st.sidebar.selectbox('ECG', ['Normal', 'ST', 'LVH'])
max_hr = st.sidebar.number_input('Frequência Máxima', 0, 220, 150)
exercise_angina = st.sidebar.selectbox('Angina Exercício', ['N', 'Y'])
oldpeak = st.sidebar.number_input('Oldpeak', 0.0, 10.0, 0.0)
st_slope = st.sidebar.selectbox('Inclinação ST', ['Up', 'Flat', 'Down'])


# INPUT

encoded = encode_inputs(sex, chest_pain_type, resting_ecg, exercise_angina, st_slope)

input_data = np.array([
    age,
    encoded[0],
    encoded[1],
    resting_bp,
    cholesterol,
    fasting_bs,
    encoded[2],
    max_hr,
    encoded[3],
    oldpeak,
    encoded[4]
])


# BOTÃO CENTRAL

st.divider()

if st.button("🔍 Fazer Previsão"):
    prediction = modelo.predict([input_data])[0]

    st.subheader("Resultado da Análise")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Idade", age)
    with col2:
        st.metric("Colesterol", cholesterol)
    with col3:
        st.metric("Pressão", resting_bp)

    st.divider()

    if prediction == 1:
        st.error("⚠️ Alto risco de doença cardíaca")
    else:
        st.success("✅ Baixo risco de doença cardíaca")


# GRÁFICOS

st.divider()
st.subheader("📊 Análises do Modelo")

if st.checkbox("Importância das Variáveis"):
    features = df.drop(columns=['HeartDisease']).columns
    importances = modelo.feature_importances_

    df_imp = pd.DataFrame({
        'Feature': features,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=df_imp, ax=ax)
    ax.set_title("Importância das Variáveis")

    st.pyplot(fig)

if st.checkbox("Matriz de Correlação"):
    corr = df.corr(numeric_only=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)

    st.pyplot(fig)