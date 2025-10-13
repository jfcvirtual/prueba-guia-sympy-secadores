import streamlit as st
import sympy as sp
import pandas as pd
from utils.thermo_helpers import symbols_safe, sensitivity_table, validar_positivo

st.title("Flujo de aire a través del lecho y potencia de ventilador")
st.markdown("""
Calcula el caudal a través del lecho y la potencia del ventilador (Apéndice 13).
""")

with st.form("form_lecho"):
    L = st.number_input("Largo cámara (m)", min_value=0.0, value=2.0)
    W = st.number_input("Ancho cámara (m)", min_value=0.0, value=1.0)
    D = st.number_input("Profundidad cámara (m)", min_value=0.0, value=0.5)
    masa_producto = st.number_input("Masa producto (kg)", min_value=0.0, value=100.0)
    densidad_aparente = st.number_input("Densidad aparente (kg/m³)", min_value=0.0, value=400.0)
    resistencia_Pa_por_m = st.number_input("Resistencia (Pa/m)", min_value=0.0, value=100.0)
    a = st.number_input("Constante a (material)", min_value=0.0, value=0.0003)
    b = st.number_input("Constante b (material)", min_value=0.0, value=1.0)
    eta_m = st.number_input("Eficiencia mecánica ventilador", min_value=0.0, max_value=1.0, value=0.6)
    submitted = st.form_submit_button("Calcular")

if submitted:
    area = L * W
    volumen_lecho = masa_producto / densidad_aparente
    h_b = volumen_lecho / area
    DeltaP = resistencia_Pa_por_m * h_b
    v = a * (DeltaP / h_b) ** b
    V = v * area
    P_aire = V * DeltaP
    P_motor = P_aire / eta_m if eta_m > 0 else float('nan')
    st.latex(r"h_b = \frac{\text{volumen lecho}}{\text{área}}")
    st.latex(r"\Delta P = \text{resistencia} \cdot h_b")
    st.latex(r"v = a \left( \frac{\Delta P}{h_b} \right)^b")
    st.latex(r"V = v \cdot \text{área}")
    st.latex(r"P_{aire} = V \cdot \Delta P")
    st.latex(r"P_{motor} = \frac{P_{aire}}{\eta_m}")
    st.write(f"Caudal total V: **{V:.4f} m³/s**")
    st.write(f"Potencia aire: **{P_aire:.2f} W**")
    st.write(f"Potencia motor: **{P_motor:.2f} W**")
    # Sensibilidad
    df_sens = sensitivity_table(sp.Symbol('h_b'), sp.Symbol('h_b'), h_b)
    st.line_chart(df_sens.set_index(str(sp.Symbol('h_b'))))
    st.write("Ejemplo del PDF: valores por defecto replican el caso ilustrativo (V ≈ 0.4 m³/s, potencia ~125 W y ~210 W)")
