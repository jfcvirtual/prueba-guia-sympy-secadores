import streamlit as st
import sympy as sp

st.title("Masa de Aire y Producto")

st.markdown("""
Calcula la masa de aire y producto involucrados en el proceso de secado solar.
""")

# Parámetros de entrada
m_prod = st.number_input("Masa de producto (kg)", min_value=0.0, value=10.0)
X_i = st.number_input("Humedad inicial (kg agua/kg producto)", min_value=0.0, value=2.0)
X_f = st.number_input("Humedad final (kg agua/kg producto)", min_value=0.0, value=0.2)

# Cálculo simbólico
m_agua = sp.Symbol('m_agua')
m_prod_s = sp.Symbol('m_prod')
X_i_s = sp.Symbol('X_i')
X_f_s = sp.Symbol('X_f')

# Fórmula: m_agua = m_prod * (X_i - X_f)
m_agua_expr = sp.Eq(m_agua, m_prod_s * (X_i_s - X_f_s))
m_agua_sol = sp.solve(m_agua_expr.subs({m_prod_s: m_prod, X_i_s: X_i, X_f_s: X_f}), m_agua)[0]

st.latex(r"m_{agua} = m_{prod} \cdot (X_i - X_f)")
st.write(f"Masa de agua a eliminar: **{m_agua_sol:.2f} kg**")
