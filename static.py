import streamlit as st

# Configurar la página de Streamlit
st.set_page_config(page_title="Proyecto Testing", page_icon="💡", layout="wide")

# Forzar scroll al tope al cargar
st.markdown("<script>window.scrollTo(0, 0);</script>", unsafe_allow_html=True)

st.title("🛡️ Principales amenazas de ciberseguridad: Phishing, Malware y Ataques DDoS")

texto = """
Hoy, gran parte de nuestra vida ocurre en línea: enviamos correos, hacemos transferencias bancarias y compartimos datos personales. Pero en ese mismo entorno digital existen **amenazas invisibles** que pueden comprometer nuestra seguridad. Tres de las más comunes son:

- **Phishing**
- **Malware**
- **Ataques DDoS**

---

### 🎣 1. Phishing

El **phishing** es una técnica de engaño en la que un atacante se hace pasar por una entidad confiable (como un banco, una empresa o una red social) para robar información personal como contraseñas, números de tarjetas o códigos de verificación.

### ¿Cómo funciona?

1. El atacante envía un mensaje (correo, SMS, mensaje de WhatsApp, etc.) con un enlace.
2. El enlace lleva a un sitio falso que imita el original.
3. La víctima ingresa sus datos pensando que es real.
4. El atacante guarda esos datos y los usa para acceder a cuentas reales.

### ¿Cómo prevenirlo?

- No hagas clic en enlaces sospechosos.
- Verifica siempre la dirección del sitio web.
- Activa la verificación en dos pasos.

---

### 💻 2. Malware

**Malware** (del inglés "malicious software") es cualquier tipo de programa diseñado para dañar, robar o controlar un dispositivo sin el permiso del usuario. Hay muchos tipos: virus, gusanos, troyanos, ransomware, spyware, etc.

### ¿Cómo se propaga?

1. A través de archivos adjuntos en correos.
2. En descargas de sitios poco confiables.
3. Mediante dispositivos infectados (como pendrives).

### ¿Qué puede hacer?

- Robar tus archivos.
- Cifrar tus datos y pedir rescate (ransomware).
- Registrar lo que escribes (keyloggers).
- Controlar tu cámara o micrófono.

### ¿Cómo prevenirlo?

- Tener un antivirus actualizado.
- No descargar software pirata.
- Actualizar tu sistema operativo.

---

### 🌐 3. Ataques DDoS

Un **ataque DDoS** (Distributed Denial of Service) ocurre cuando muchos dispositivos envían tráfico falso a un servidor o página para **colapsarlo** y dejarlo fuera de servicio.

### ¿Cómo funciona?

1. El atacante infecta miles de dispositivos (una “botnet”).
2. Todos esos dispositivos atacan un servidor al mismo tiempo.
3. El servidor se satura y deja de funcionar.

### ¿A quién afecta?

- Empresas con sitios web.
- Servicios en línea (streaming, videojuegos).
- Plataformas gubernamentales o educativas.

### ¿Cómo protegerse?

- Usar sistemas de detección y mitigación de DDoS.
- Tener servidores escalables y protección en la nube.
"""

# Mostrar contenido
st.markdown(texto)
