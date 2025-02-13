import streamlit as st

st.title("HOLA SKIBIDI TOILET")
st.write("Tu historia comienza aquí...")

opcion = st.radio("¿Qué querés hacer primero?", ["Explorar el bosque", "Entrar a la cabaña"])

if opcion == "Explorar el bosque":
    st.write("Te adentras en el bosque y escuchas un sonido misterioso... ¿Qué será?")
elif opcion == "Entrar a la cabaña":
    st.write("Empujas la puerta y encuentras una nota sobre la mesa... ¿La lees?")
