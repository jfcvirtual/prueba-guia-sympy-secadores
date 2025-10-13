import streamlit as st
import sympy as sp
import pandas as pd
from utils.thermo_helpers import symbols_safe, sensitivity_table, validar_positivo, validar_temperatura

st.title("Convección natural y caudales de aire")
st.markdown("""
Calcula el caudal por convección natural y la altura de chimenea requerida (Apéndice 12).
""")

with st.form("form_conveccion"):
    T_amb = st.number_input("T ambiente (°C)", value=25.0)
    RH_amb = st.number_input("Humedad relativa ambiente (%)", value=60.0)
    T_secador = st.number_input("T secador (°C)", value=40.0)
    H1 = st.number_input("Altura H₁ (m)", min_value=0.0, value=2.0)
    H2 = st.number_input("Altura H₂ (m)", min_value=0.0, value=1.0)
    H3 = st.number_input("Altura chimenea H₃ (m)", min_value=0.0, value=2.0)
    h_b = st.number_input("Espesor de lecho h_b (m)", min_value=0.0, value=0.2)
    a = st.number_input("Constante a (material)", min_value=0.0, value=0.0008)
    b = st.number_input("Constante b (material)", min_value=0.0, value=0.87)
    g = st.number_input("Gravedad g (m/s²)", min_value=0.0, value=9.81)
    area = st.number_input("Área transversal (m²)", min_value=0.0, value=1.0)
    submitted = st.form_submit_button("Calcular")

if submitted:
    DeltaT = T_secador - T_amb
    H = H1 + H2 + H3
    DeltaP = 0.00308 * DeltaT * g * H
    v = a * (DeltaP / h_b) ** b
    V = v * area
    st.latex(r"\Delta P = 0.00308 \cdot \Delta T \cdot g \cdot H")
    st.latex(r"v = a \left( \frac{\Delta P}{h_b} \right)^b")
    st.write(f"Caudal volumétrico v: **{v:.4f} m³/s**")
    st.write(f"Caudal total V: **{V:.4f} m³/s**")
    # Sensibilidad
    df_sens = sensitivity_table(sp.Symbol('H'), sp.Symbol('H'), H)
    st.line_chart(df_sens.set_index(str(sp.Symbol('H'))))
    st.write("Ejemplo del PDF: valores por defecto replican el caso ilustrativo (arroz, v ≈ 0.4 m³/s)")
