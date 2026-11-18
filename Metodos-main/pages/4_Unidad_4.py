import streamlit as st
import pandas as pd
from estilos import cargar_estilos_y_navbar, imagen_a_base64
from nucleo4 import EJEMPLO_LU_A, EJEMPLO_LU_B, factorizacion_doolittle, factorizacion_crout

st.set_page_config(page_title="Unidad 4: Factorización LU", layout="wide")
cargar_estilos_y_navbar()

img_lu_gen = imagen_a_base64("imagenes/lu_general.png")
img_doolittle = imagen_a_base64("imagenes/doolittle.png")
img_crout = imagen_a_base64("imagenes/crout.png")

st.markdown("""
<style>
    .unidad-tag { color: #B484A0; font-size: 20px; font-weight: 800; margin-bottom: 2px; }
    .unidad-titulo { color: #1A1A1A; font-size: 32px; font-weight: 800; margin-top: 0px; margin-bottom: 18px; line-height: 1.2; }
    .pendiente-tag {
        display: inline-block; background-color: #FCEEF5; color: #C96B9D;
        border: 1.5px dashed #E082B4; font-family: 'Courier New', Courier, monospace;
        font-size: 12px; font-weight: 800; letter-spacing: 1px;
        padding: 4px 10px; border-radius: 6px; margin-bottom: 10px; text-transform: uppercase;
    }
    .intro-center-box { text-align: center; max-width: 720px; margin: 12px auto; }
    .intro-lorem { color: #555555; font-size: 14.5px; font-style: italic; line-height: 1.6; margin-bottom: 0; }
    .diagrama-box { text-align: center; margin: 18px 0px; }
    .diagrama-box img { max-width: 440px; width: 100%; border-radius: 8px; }
    .unit-card {
        background-color: #FFFFFF; padding: 26px 30px; border-radius: 16px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.04); margin-top: 10px; margin-bottom: 20px;
    }
    .theory-text { color: #777777; font-size: 14.5px; font-style: italic; line-height: 1.65; text-align: justify; margin-bottom: 16px; }
    button[data-baseweb="tab"]:nth-child(1) p { color: #2B6CB0 !important; font-weight: 700 !important; font-size: 15px !important; }
    button[data-baseweb="tab"]:nth-child(2) p { color: #D97706 !important; font-weight: 700 !important; font-size: 15px !important; }
    .st-key-btn_calc_doo div.stButton > button { background-color: #2B6CB0 !important; box-shadow: 0 4px 10px rgba(43, 108, 176, 0.3) !important; }
    .st-key-btn_calc_doo div.stButton > button:hover { background-color: #2C5282 !important; }
    .st-key-btn_calc_cro div.stButton > button { background-color: #D97706 !important; box-shadow: 0 4px 10px rgba(217, 119, 6, 0.3) !important; }
    .st-key-btn_calc_cro div.stButton > button:hover { background-color: #B45309 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="unidad-tag">Unidad 4.</div>
<div class="unidad-titulo">Factorización LU</div>
<div class="intro-center-box">
    <p class="intro">Si tenemos una matriz A entonces esta matriz se puede representar de la siguiente manera. A= LU, donde L es una matriz triangular inferior y U una matriz triangular superior.
    <p>
    <div class="diagrama-box"><img src ="{img_lu_gen}" alt= "Diagrama Factorización A=L*U"></div>
<p class="unidad-intro" style="margin-bottom: 28px;"> 
    Entonces el sistema de ecuaciones lineales Ax=b se puede resolver en dos fases:
    </p>
    < div class ="into-center-box>
<p class="unidad-intro" style="margin-bottom: 28px;">
    a) Lv=b.
<p class="unidad-intro" style="margin-bottom: 28px;">    
    b) Ux=v
</div>
<div class="intro-center-box" style="margin-bottom: 28px;">
<p class="unidad-intro" style="margin-bottom: 28px;">
 <p class="intro">Resolvemos primero la ecuación a) y despues la ecuación b).</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<h3 style='font-size: 18px; font-weight: 800; color: #1A1A1A; margin-bottom: 10px;'>Selecciona un método para ver su fundamento:</h3>", unsafe_allow_html=True)
tab_doo, tab_cro = st.tabs(["🔹 Método de Doolittle", "🔸 Método de Crout"])
with tab_doo:
    st.markdown(f"""
    <div class="unit-card" style="border-left: 5px solid #3182CE;">
        <h3 style="color: #2B6CB0; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 10px;">Doolittle</h3>
        <div class="pendiente-tag">[ VARIANTE DOOLITTLE: L tiene diagonal de 1]</div>
        <p class="theory-text">Define las matrices L y U tal que U es triangular inferior y L una matriz triangular superior con elementos unitarios en la diagonal principal..</p>
        <div class="diagrama-box" style="margin-bottom: 0;"><img src="{img_doolittle}" alt="Diagrama Doolittle"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='color: #2B6CB0; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Doolittle</h4>", unsafe_allow_html=True)
    col_dim_doo, col_info_doo = st.columns([1, 2.5])
    n_doo = col_dim_doo.number_input("Tamaño (n × n):", min_value=2, max_value=8, value=3, step=1, key="doo_n")
    col_info_doo.info("Edita **A** y **b** en la tabla (precargada con el ejercicio de clase 3×3).")

    datos_doo = [EJEMPLO_LU_A[i] + [EJEMPLO_LU_B[i]] for i in range(3)] if n_doo == 3 else [[4.0 if i == j else 1.0 for j in range(n_doo)] + [5.0] for i in range(n_doo)]
    df_doo = st.data_editor(pd.DataFrame(datos_doo, columns=[f"x{j+1}" for j in range(n_doo)] + ["b"], index=[f"Ec. {i+1}" for i in range(n_doo)]), use_container_width=True, key="editor_doo")

    if st.button("Resolver por Doolittle", key="btn_calc_doo"):
        try:
            mat = df_doo.to_numpy(dtype=float)
            L, U, x_sol, pasos = factorizacion_doolittle(mat[:, :-1].tolist(), mat[:, -1].tolist())
            st.markdown("**Vector Solución Obtenido:**")
            cols_s = st.columns(len(x_sol))
            for idx, val in enumerate(x_sol):
                cols_s[idx].metric(f"x{idx+1}", f"{val:.6f}")
            cl, cu = st.columns(2)
            cl.markdown("**Matriz L**")
            cl.dataframe(pd.DataFrame(L, columns=[f"c{j+1}" for j in range(len(L))]), use_container_width=True)
            cu.markdown("**Matriz U**")
            cu.dataframe(pd.DataFrame(U, columns=[f"c{j+1}" for j in range(len(U))]), use_container_width=True)
            with st.expander("Ver desarrollo paso a paso"):
                st.code("\n".join(pasos), language="text")
        except Exception as e:
            st.error(f"Error en Doolittle: {e}")

with tab_cro:
    st.markdown(f"""
    <div class="unit-card" style="border-left: 5px solid #D97706;">
        <h3 style="color: #D97706; font-size: 21px; font-weight: 800; margin-top: 0; margin-bottom: 10px;">Crout</h3>
        <div class="pendiente-tag">[ VARIANTE DE CROUT: U tiene diagonal de 1 ]</div>
        <p class="theory-text">La matriz L es triangular inferior y la matriz U es triangular superior con elementos unitarios en la diagonal principal.</p>
        <div class="diagrama-box" style="margin-bottom: 0;"><img src="{img_crout}" alt="Diagrama Crout"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h4 style='color: #D97706; font-weight: 800; margin-top: 10px;'>Calculadora Interactiva — Crout</h4>", unsafe_allow_html=True)
    col_dim_cro, col_info_cro = st.columns([1, 2.5])
    n_cro = col_dim_cro.number_input("Tamaño (n × n):", min_value=2, max_value=8, value=3, step=1, key="cro_n")
    col_info_cro.info("Edita **A** y **b** en la tabla (precargada con el ejercicio de clase 3×3).")

    datos_cro = [EJEMPLO_LU_A[i] + [EJEMPLO_LU_B[i]] for i in range(3)] if n_cro == 3 else [[4.0 if i == j else 1.0 for j in range(n_cro)] + [5.0] for i in range(n_cro)]
    df_cro = st.data_editor(pd.DataFrame(datos_cro, columns=[f"x{j+1}" for j in range(n_cro)] + ["b"], index=[f"Ec. {i+1}" for i in range(n_cro)]), use_container_width=True, key="editor_cro")

    if st.button("Resolver por Crout", key="btn_calc_cro"):
        try:
            mat = df_cro.to_numpy(dtype=float)
            L, U, x_sol, pasos = factorizacion_crout(mat[:, :-1].tolist(), mat[:, -1].tolist())
            st.markdown("**Vector Solución Obtenido:**")
            cols_s = st.columns(len(x_sol))
            for idx, val in enumerate(x_sol):
                cols_s[idx].metric(f"x{idx+1}", f"{val:.6f}")
            cl, cu = st.columns(2)
            cl.markdown("**Matriz L**")
            cl.dataframe(pd.DataFrame(L, columns=[f"c{j+1}" for j in range(len(L))]), use_container_width=True)
            cu.markdown("**Matriz U**")
            cu.dataframe(pd.DataFrame(U, columns=[f"c{j+1}" for j in range(len(U))]), use_container_width=True)
            with st.expander("Ver desarrollo paso a paso"):
                st.code("\n".join(pasos), language="text")
        except Exception as e:
            st.error(f"Error en Crout: {e}")

# 3. BOTONES DE NAVEGACIÓN ENTRE UNIDADES
st.write("")
col_prev, col_space, col_next = st.columns([1, 2, 1])
with col_prev:
    st.markdown('<a href="/Unidad_3" target="_self" class="btn-comenzar">Volver a Unidad 3</a>', unsafe_allow_html=True)
with col_next:
    st.markdown('<div style="text-align: right;"><a href="/Unidad_5" target="_self" class="btn-comenzar">Ir a Unidad 5</a></div>', unsafe_allow_html=True)
