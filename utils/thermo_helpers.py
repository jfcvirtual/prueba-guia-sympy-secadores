"""
Funciones de utilidades físicas y simbólicas para Solar Dryers
"""
import sympy as sp
import numpy as np
import pandas as pd

L_v = 2.32e6  # Calor latente de vaporización del agua (J/kg)

def kJ_to_J(kJ):
    """Convierte kJ a J"""
    return kJ * 1000

def horas_a_segundos(h):
    """Convierte horas a segundos"""
    return h * 3600

def segundos_a_horas(s):
    """Convierte segundos a horas"""
    return s / 3600

def symbols_safe(names):
    """Declara símbolos con nombres LaTeX"""
    return sp.symbols(names)

def solve_positive(eq_or_system, vars_target):
    """Resuelve y filtra soluciones reales positivas"""
    sols = sp.solve(eq_or_system, vars_target, dict=True)
    return [sol for sol in sols if all(sp.re(sol[v]) > 0 for v in vars_target)]

def sensitivity_table(expr, var, center, pct_range=0.2, steps=11):
    """Genera tabla de sensibilidad para expr respecto a var"""
    vals = np.linspace(center*(1-pct_range), center*(1+pct_range), steps)
    results = [float(expr.subs(var, v)) for v in vals]
    return pd.DataFrame({str(var): vals, 'Resultado': results})

def validar_positivo(valor, nombre):
    if valor <= 0:
        raise ValueError(f"{nombre} debe ser positivo")
    return valor

def validar_temperatura(temp, nombre):
    if temp < -50 or temp > 100:
        raise ValueError(f"{nombre} fuera de rango físico")
    return temp
