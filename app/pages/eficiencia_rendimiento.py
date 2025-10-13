import streamlit as st
import sympy as sp

st.title("Eficiencia y Rendimiento")

st.markdown("""
Calcula la eficiencia y el rendimiento del secador solar.
""")

# Parámetros de entrada
Q_util = st.number_input("Energía útil (Q_util) [kJ]", min_value=0.0, value=800.0)
Q_total = st.number_input("Energía total recibida (Q_total) [kJ]", min_value=0.0, value=1000.0)

# Cálculo simbólico
eta = sp.Symbol('eta')
Q_util_s = sp.Symbol('Q_util')
Q_total_s = sp.Symbol('Q_total')

# Fórmula: η = Q_util / Q_total
eta_expr = sp.Eq(eta, Q_util_s / Q_total_s)
eta_sol = sp.solve(eta_expr.subs({Q_util_s: Q_util, Q_total_s: Q_total}), eta)[0]

st.latex(r"\eta = \frac{Q_{util}}{Q_{total}}")
st.write(f"Eficiencia del secador: **{eta_sol:.2f}**")
