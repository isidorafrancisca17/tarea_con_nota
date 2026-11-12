import streamlit as st

st.title("Mi primera aplicacion de Streamlit")
st.subheader("¡Hola, Streamlit!")


# Inicio de la barra lateral
st.sidebar.title("Mi primera barra lateral de Streamlit")
st.sidebar.text("¡hola, barra lateral!")

#  Area Principal
st.text("Esta es una aplicacion simple")
st.image("https://researchers.uss.cl/skin/footerIcon/", width=250)

#Boton de area principal 
if st.butto("haz click"):
  st.write("¡Boton presionado!")

#Campo de texto del area principal
nombre_texto = st.text_input("Escribe algo:")
st.write(f"Escribiste: {nombre_texto}")


# Barra lateral 
st.sidebear.text("Esto es una barra lateral")
st.sidebear.image("https://researchers.uss.cl/skin/footerIcon/", width=200)

#Boton de la barra lateral 
if st.sedebear.button("Haz click pero en la barra lateral"):
  st.sidebear.write("¡Boton de la barra presionado!")

#Campo de texto de la barra lateral 
texto_barra = st.sidebear.text_input("Escribe algo de la barra:")
st.sidebear.write(f"Escribiste en la barra: {texto_barra}")

