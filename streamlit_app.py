import streamlit as st
import pandas as pd




st.header("🍽️ :orange[Percepción Estudiantil] sobre el Comedor Universitario de la :green[UNALM]", 
          divider = "orange", 
          help = "¡Tu opinión cuenta! 🗣️")

tabs = st.tabs(["Home", "Model"])

with tabs[0]:
    st.markdown("**Trabajo para el curso de Ciencia de Datos I - Estadistica Informática**")
    st.text("Hola")
    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)
    
with tabs[1]:
    df = pd.read_csv("df_final.csv")
    st.bar_chart(df, x="V23", y="V24", color="target", horizontal=True)
    st.area_chart(df, x="V23", y="V24", color="target")
    st.line_chart(df)

    st.scatter_chart(
    df,
    x="V23",
    y="V24",
    color="target",
)