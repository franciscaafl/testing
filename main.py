import streamlit as st
from dotenv import load_dotenv

load_dotenv()
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Configurar el cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configurar la página de Streamlit
st.set_page_config(page_title="Chat interactivo sobre Ciberseguridad", page_icon="💡", layout="wide")

# Forzar scroll al tope al cargar
st.markdown("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)

st.title("💬 Chat interactivo sobre Ciberseguridad")


texto = """
Aprende sobre phishing, malware y ataques DDoS a través de explicaciones paso a paso. Haz preguntas y el sistema ajustará el contenido según tus respuestas para ayudarte a entender mejor estos riesgos digitales.
"""


# Columna con el texto
st.markdown(texto)

# Columna con el chat
# Inicializar historial
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """Quiero que actúes como un sistema de enseñanza adaptativa estilo chatbot. 
        El tema a enseñar es: Phishing, Malware y Ataques DDoS.

        Tu objetivo es:
        - Enseñar el contenido paso a paso, dividiendo cada subtema.
        - Hacer preguntas entre cada paso para verificar comprensión.
        - Adaptar el contenido según las respuestas del usuario: si acierta, continúa; si se equivoca, explica con más detalle.
        - No muestres todo el contenido de golpe, simula una conversación fluida.
        - Usa lenguaje claro, evita términos técnicos sin explicación.""",
        },
        {
            "role": "assistant",
            "content": "¡Hola! 👋",
        },
    ]

# Mostrar mensajes
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Mostrar el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta del asistente
    with st.chat_message("assistant"):
        with st.spinner("Escribiendo..."):
            response = client.chat.completions.create(
                model="gpt-4",
                messages=st.session_state.messages,
                temperature=0.7,
            )
            reply = response.choices[0].message.content

    # Guardar respuesta
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
