import streamlit as st
from openai import OpenAI
import os

# Configurar el cliente de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configurar la página de Streamlit
st.set_page_config(page_title="Proyecto Testing", page_icon="💡", layout="wide")

# Forzar scroll al tope al cargar
st.markdown("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)

st.title("💬 Aprende X tema/idioma")


texto = """
Las interfaces usuarias son el punto de contacto entre las personas y los sistemas, en donde las personas, o usuarios del sistema, navegan los contenidos, acceden a las funcionalidades y completan las tareas. El diseño de estos sistemas tiene un gran impacto en la usabilidad, accesibilidad y experiencia del usuario. 

Actualmente, la interacción humano-máquina se enfrenta al desafío de ofrecer experiencias digitales que sean cada vez más inclusivas, eficientes y personalizadas. Debido a la creciente diversidad de usuarios, dispositivos y contextos de uso, los modelos tradicionales como los basados en esquemas estáticos o uniformes, resultan ser insuficientes para satisfacer las demandas actuales. A raíz de esto, surgen las interfaces de usuario adaptativas y personalizadas como una solución para garantizar la usabilidad y la accesibilidad en entornos dinámicos, híbridos y heterogéneos. 

Estas interfaces no solo permiten ajustar el contenido, la disposición y los elementos visuales según las características del usuario como la edad, habilidades y estilo cognitivo, sino que también responde a factores contextuales (entorno físico, el dispositivo que se utiliza o el estado emocional del usuario). La incorporación de tecnologías como la inteligencia artificial simbólica, el aprendizaje de refuerzo, las ontologías semánticas y las interfaces de usuario distribuidas han posibilitado el diseño de sistemas que sean capaces de adaptar la experiencia en tiempo real, de manera autónoma y escalable.
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
            "content": "¡Hola! 👋 Puedes hacerme preguntas sobre el texto que estás revisando.",
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
