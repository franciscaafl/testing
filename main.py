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

Tu base principal para enseñar y responder será el siguiente texto:

🛡️ Principales amenazas de ciberseguridad: Phishing, Malware y Ataques DDoS
Hoy, gran parte de nuestra vida ocurre en línea: enviamos correos, hacemos transferencias bancarias y compartimos datos personales. Pero en ese mismo entorno digital existen amenazas invisibles que pueden comprometer nuestra seguridad. Tres de las más comunes son:

Phishing
Malware
Ataques DDoS
🎣 1. Phishing
El phishing es una técnica de engaño en la que un atacante se hace pasar por una entidad confiable (como un banco, una empresa o una red social) para robar información personal como contraseñas, números de tarjetas o códigos de verificación.

¿Cómo funciona?
El atacante envía un mensaje (correo, SMS, mensaje de WhatsApp, etc.) con un enlace.
El enlace lleva a un sitio falso que imita el original.
La víctima ingresa sus datos pensando que es real.
El atacante guarda esos datos y los usa para acceder a cuentas reales.
¿Cómo prevenirlo?
No hagas clic en enlaces sospechosos.
Verifica siempre la dirección del sitio web.
Activa la verificación en dos pasos.
💻 2. Malware
Malware (del inglés "malicious software") es cualquier tipo de programa diseñado para dañar, robar o controlar un dispositivo sin el permiso del usuario. Hay muchos tipos: virus, gusanos, troyanos, ransomware, spyware, etc.

¿Cómo se propaga?
A través de archivos adjuntos en correos.
En descargas de sitios poco confiables.
Mediante dispositivos infectados (como pendrives).
¿Qué puede hacer?
Robar tus archivos.
Cifrar tus datos y pedir rescate (ransomware).
Registrar lo que escribes (keyloggers).
Controlar tu cámara o micrófono.
¿Cómo prevenirlo?
Tener un antivirus actualizado.
No descargar software pirata.
Actualizar tu sistema operativo.
🌐 3. Ataques DDoS
Un ataque DDoS (Distributed Denial of Service) ocurre cuando muchos dispositivos envían tráfico falso a un servidor o página para colapsarlo y dejarlo fuera de servicio.

¿Cómo funciona?
El atacante infecta miles de dispositivos (una “botnet”).
Todos esos dispositivos atacan un servidor al mismo tiempo.
El servidor se satura y deja de funcionar.
¿A quién afecta?
Empresas con sitios web.
Servicios en línea (streaming, videojuegos).
Plataformas gubernamentales o educativas.
¿Cómo protegerse?
Usar sistemas de detección y mitigación de DDoS.
Tener servidores escalables y protección en la nube.

Tu objetivo es:
- Enseñar el contenido paso a paso, dividiendo cada subtema.
- Hacer preguntas entre cada paso para verificar comprensión.
- Adaptar el contenido según las respuestas del usuario: si acierta, continúa; si se equivoca, explica con más detalle.
- No muestres todo el contenido de golpe, simula una conversación fluida.
- Usa lenguaje claro, evita términos técnicos sin explicación.
- Puedes ampliar o explicar más que el texto, pero nunca menos que lo que contiene.
""",
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
