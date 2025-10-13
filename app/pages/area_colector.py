import streamlit as st
import sympy as sp

st.title("Área de Colector Solar")

st.markdown("""
Calcula el área necesaria del colector solar según los parámetros del sistema.
""")


# Parámetros de entrada
Q = st.number_input("Energía requerida (Q) [kJ]", min_value=0.0, value=1000.0)
I = st.number_input("Irradiancia solar (I) [W/m²]", min_value=0.0, value=800.0)
eta = st.number_input("Eficiencia del colector (η)", min_value=0.0, max_value=1.0, value=0.6)
t = st.number_input("Tiempo de operación (t) [h]", min_value=0.0, value=6.0)

# Conversión de Q a Joules
Q_J = Q * 1000

# Cálculo simbólico
t_s = sp.Symbol('t')
A = sp.Symbol('A')
Q_s = sp.Symbol('Q')
I_s = sp.Symbol('I')
eta_s = sp.Symbol('eta')


# Fórmula: Q = A * I * η * t * 3600
A_expr = sp.Eq(Q_s, A * I_s * eta_s * t_s * 3600)
A_sol = sp.solve(A_expr.subs({Q_s: Q_J, I_s: I, eta_s: eta, t_s: t}), A)[0]

st.latex(r"Q = A \cdot I \cdot \eta \cdot t \cdot 3600")
st.write(f"Área necesaria del colector: **{A_sol:.2f} m²**")
