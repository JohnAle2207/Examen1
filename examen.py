import streamlit as st
from transformers import pipeline

st.title('Examen Final Desarrollo')
texto = st.text_area('Ingrese el texto a clasificar')
#Clasificacion del texto
candidate_labels = ['Deportes', 'Politica', 'Relilgion', 'Cine', 'No encontrado' ]
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

if st.button("Clasificar"):
    resultado = classifier(texto, candidate_labels)
    
    st.write(f'{resultado}')



