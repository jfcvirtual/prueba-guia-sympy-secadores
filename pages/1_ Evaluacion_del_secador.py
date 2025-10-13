import streamlit as st
import sympy as sp
import pandas as pd
from utils.thermo_helpers import L_v, kJ_to_J, symbols_safe, sensitivity_table, validar_positivo, validar_temperatura

st.title("Evaluación del desempeño del secador solar")
st.markdown("""
Calcula la eficiencia de secado (η_d) y pick-up (η_p) según el Apéndice 7 del PDF.
""")

# Entradas del usuario
with st.form("form_secador"):
    masa_fresca = st.number_input("Masa fresca (kg)", min_value=0.0, value=10.0)
    humedad_inicial = st.number_input("Humedad inicial (% b.h.)", min_value=0.0, max_value=100.0, value=80.0)
    humedad_final = st.number_input("Humedad final objetivo (% b.h.)", min_value=0.0, max_value=100.0, value=20.0)
    area_colector = st.number_input("Área de colector (m²)", min_value=0.0, value=4.0)
    insolacion_diaria = st.number_input("Insolación diaria (kJ/m²·día)", min_value=0.0, value=18000.0)
    dias = st.number_input("Días de secado", min_value=0.0, value=2.0)
    caudal_v = st.number_input("Caudal volumétrico (m³/s)", min_value=0.0, value=0.4)
    densidad_aire = st.number_input("Densidad aire (kg/m³)", min_value=0.0, value=1.2)
    tiempo_total = st.number_input("Tiempo total (h)", min_value=0.0, value=48.0)
    T_amb = st.number_input("T ambiente (°C)", value=25.0)
    RH_amb = st.number_input("Humedad relativa ambiente (%)", value=60.0)
    T_entrada = st.number_input("T entrada secador (°C)", value=40.0)
    submitted = st.form_submit_button("Calcular")

if submitted:
    # Conversión de humedades a base seca
    X_i = humedad_inicial / (100 - humedad_inicial)
    X_f = humedad_final / (100 - humedad_final)
    masa_seca = masa_fresca / (1 + X_i)
    W = masa_seca * (X_i - X_f)  # masa evaporada
    I_t = insolacion_diaria * dias  # kJ/m²
    eta_d = (W * L_v) / (area_colector * kJ_to_J(I_t))
    # Estimación psicrométrica simplificada
    h_i = 0.01 * humedad_inicial  # valor aproximado
    h_as = 0.01 * humedad_final   # valor aproximado
    eta_p = W / (caudal_v * densidad_aire * tiempo_total * (h_as - h_i))
    st.latex(r"\eta_d = \frac{W \cdot L_v}{A_c \cdot I_t}")
    st.latex(r"\eta_p = \frac{W}{v \cdot \rho \cdot t \cdot (h_{as} - h_i)}")
    st.write(f"Eficiencia de secado η_d: **{eta_d:.2%}**")
    st.write(f"Pick-up efficiency η_p: **{eta_p:.2%}**")
    # Sensibilidad
    df_sens = sensitivity_table(sp.Symbol('I_t') * area_colector, sp.Symbol('I_t'), I_t)
    st.line_chart(df_sens.set_index(str(sp.Symbol('I_t'))))
    st.write("Ejemplo del PDF: valores por defecto replican el caso ilustrativo (~20% eficiencia)")
