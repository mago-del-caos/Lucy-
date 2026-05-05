import streamlit as st
from openai import OpenAI
import streamlit.components.v1 as components

# CONFIGURACIÓN DE PÁGINA
st.set_page_config(
    page_title="⭐ Lucy | Tu apoyo con estilo ⭐",
    page_icon="🛹",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={'Get Help': None, 'Report a bug': None, 'About': None}
)

# CSS CON FONDO DE ESTRELLAS Y ESTILO ESPACIAL
css_lucy = """
<style>
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    [data-testid="stDecoration"] {display: none;}
    .stApp {max-width: 100%; padding: 0;}
    .stDeployButton {display: none;}
    [data-testid="stToolbar"] {display: none;}
    [data-testid="stStatusWidget"] {display: none;}
    
    /* Fondo de estrellas animado */
    .stApp {
        background: linear-gradient(135deg, #0a0a2a 0%, #1a1a3a 50%, #0d0d2b 100%);
        position: relative;
        overflow: hidden;
    }
    
    /* Estrellas animadas */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20px 30px, white, rgba(0,0,0,0)),
            radial-gradient(3px 3px at 80px 150px, #FFE484, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 160px 80px, white, rgba(0,0,0,0)),
            radial-gradient(4px 4px at 300px 200px, #FFD700, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 450px 350px, white, rgba(0,0,0,0)),
            radial-gradient(3px 3px at 600px 100px, #FFE484, rgba(0,0,0,0)),
            radial-gradient(1px 1px at 750px 400px, white, rgba(0,0,0,0)),
            radial-gradient(2px 2px at 900px 250px, #FFD700, rgba(0,0,0,0)),
            radial-gradient(4px 4px at 1050px 500px, white, rgba(0,0,0,0));
        background-repeat: no-repeat;
        background-size: 200px 200px;
        opacity: 0.8;
        pointer-events: none;
        animation: twinkle 3s infinite;
    }
    
    @keyframes twinkle {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 1; }
    }
    
    /* Estilo de los mensajes */
    [data-testid="stChatMessage"] {
        background-color: rgba(25, 25, 45, 0.95);
        border-radius: 20px;
        padding: 15px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 215, 0, 0.3);
    }
    
    /* Título personalizado */
    .custom-title {
        text-align: center;
        color: #FFE484;
        font-size: 3em;
        font-weight: bold;
        text-shadow: 0 0 10px #FFD700, 0 0 20px #FFA500;
        margin-bottom: 0;
    }
    
    .custom-subtitle {
        text-align: center;
        color: #FFD700;
        font-size: 1.1em;
        margin-top: -10px;
        margin-bottom: 20px;
        text-shadow: 0 0 5px #FFA500;
    }
    
    /* Botón de audio */
    .stButton button {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        color: #1a1a3a;
        font-weight: bold;
        border-radius: 30px;
        border: none;
        transition: transform 0.2s;
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.5);
    }
    
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.8);
    }
    
    /* Input */
    [data-testid="stChatInput"] input {
        border-radius: 30px;
        border: 2px solid #FFD700;
        background-color: rgba(25, 25, 45, 0.9);
        color: white;
    }
    
    [data-testid="stChatInput"] input::placeholder {
        color: rgba(255, 215, 0, 0.7);
    }
    
    /* Mensaje del asistente */
    [data-testid="stChatMessage"][data-testid*="assistant"] {
        background: linear-gradient(135deg, rgba(30, 30, 60, 0.95) 0%, rgba(20, 20, 50, 0.95) 100%);
        border-left: 10px solid #FFD700;
    }
    
    /* Mensaje del usuario */
    [data-testid="stChatMessage"][data-testid*="user"] {
        background: linear-gradient(135deg, rgba(50, 50, 90, 0.95) 0%, rgba(40, 40, 80, 0.95) 100%);
        border-right: 10px solid #4CAF50;
    }
    
    /* Texto */
    .stMarkdown {
        color: #f0f0f0;
    }
</style>
"""
st.markdown(css_lucy, unsafe_allow_html=True)

# FUNCIÓN PARA MOSTRAR LOGO DE LUCY (Patineta + Star Wars)
def mostrar_logo():
    logo_svg = """
    <div style="text-align: center; margin-bottom: 20px;">
        <svg width="220" height="200" viewBox="0 0 220 200" xmlns="http://www.w3.org/2000/svg">
            <!-- Patineta -->
            <rect x="40" y="140" width="140" height="12" rx="6" fill="#FF4444"/>
            <rect x="60" y="132" width="20" height="8" rx="2" fill="#CC3333"/>
            <rect x="140" y="132" width="20" height="8" rx="2" fill="#CC3333"/>
            <!-- Ruedas -->
            <circle cx="65" cy="155" r="8" fill="#333"/>
            <circle cx="155" cy="155" r="8" fill="#333"/>
            <!-- Sable de luz (como personalidad Star Wars) -->
            <rect x="100" y="60" width="4" height="70" fill="#00FF00"/>
            <rect x="95" y="55" width="14" height="10" rx="2" fill="#888"/>
            <circle cx="102" cy="60" r="8" fill="#00FF00" opacity="0.6"/>
            <!-- Efecto de brillo del sable -->
            <ellipse cx="102" cy="130" rx="3" ry="15" fill="#00FF00" opacity="0.4"/>
            <!-- Casco de Stormtrooper (mini) -->
            <ellipse cx="120" cy="50" rx="15" ry="18" fill="white"/>
            <circle cx="114" cy="47" r="4" fill="#333"/>
            <circle cx="126" cy="47" r="4" fill="#333"/>
            <path d="M 112 55 Q 120 62 128 55" stroke="#333" stroke-width="2" fill="none"/>
        </svg>
        <h1 class="custom-title">⭐ Lucy ⭐</h1>
        <p class="custom-subtitle">🛹 ¡Tu apoyo con estilo, joven padawan! ✨</p>
        <p class="custom-subtitle" style="font-size: 0.9em;">💫 Patinetas · Fuerza · Aprendizaje 💫</p>
    </div>
    """
    st.markdown(logo_svg, unsafe_allow_html=True)

# PERSONALIDAD DE LUCY - APOYO PARA TDAH, DISLEXIA, PATINETAS Y STAR WARS
SYSTEM_PROMPT = """Eres LUCY, una chica súper cool que ama las patinetas y es FANÁTICA de Star Wars. Ayudas a estudiantes con TDAH y dislexia.

**TU PERSONALIDAD:**
- Hablas como si estuvieras en el universo de Star Wars: "¡Que la Fuerza te acompañe!", "¡Bien hecho, joven padawan!", "¡Poderoso eres!"
- Usas vocabulario de patinetas: "¡Qué trucazo!", "¡Eso fue un ollie mental!", "¡Le estás dando kickflip a las matemáticas!"
- Eres super enérgica y positiva
- Usas muchos emojis: ⭐🛹✨🚀📚💫

**CÓMO APOYAS (especial para TDAH y dislexia):**
1. **Información en bloques pequeños**: Divides todo en pasos de 2 o 3 ideas máximo
2. **Pausas activas**: Cada 5 minutos sugieres "¡Hagamos un truco mental de 10 segundos!"
3. **Letra amigable para dislexia**: Sugieres usar colores, tamaños grandes o separar palabras
4. **Recordatorios suaves**: Si el estudiante se distrae, dices "¡La Fuerza te llama de vuelta!"
5. **Refuerzos inmediatos**: Después de cada respuesta, un "¡Boom! ¡Qué nivel!"

**ESTRATEGIAS ESPECIALES:**
- Para concentración: "Imagina que este problema es un nivel del juego de Star Wars"
- Para organización: "Hagamos una tabla como el tablero de una patineta: arriba lo más importante"
- Para lectura: "Usa un señalador como si fuera un sable de luz"
- Para memoria: "Creemos un truco con la patineta para recordar esto"

**REGLAS IMPORTANTES:**
- Si ves frustración, dices: "¡Tómate un respiro como entre trucos de patineta!"
- Usa ejemplos con patinetas, Star Wars, naves espaciales, droides
- Cada logro, por pequeño que sea, se celebra como si ganaras un campeonato
- Si el estudiante se equivoca: "¡Buena intentona! Como cuando te caes de la patineta... ¡te levantas y lo intentas mejor!"

**EJEMPLO:**
Estudiante: "No puedo concentrarme para leer"
Tú: "¡Que la Fuerza te acompañe! ⭐ Vamos a leer como si fuera un mapa de una misión secreta. Usa tu dedo como sable de luz ✨ y lee SOLO 2 oraciones. ¿Puedes intentarlo? ¡Tú puedes, joven padawan! 🛹"

Eres paciente, divertida y siempre recuerdas: cada estudiante aprende a su ritmo, como cada patineta tiene su estilo único.
"""

# Mostrar logo de Lucy
mostrar_logo()

# CONEXIÓN CON GROQ USANDO SECRETS
try:
    client = OpenAI(
        base_url="https://api.groq.com/openai/v1",
        api_key=st.secrets["GROQ_API_KEY"]
    )
except Exception as e:
    st.error("⭐ ¡Oh no! Lucy necesita conexión. Por favor configura la API key en los Secrets de Streamlit.")
    st.info("📌 Ve a Settings → Secrets y agrega: GROQ_API_KEY = 'tu_api_key'")
    st.stop()

# --- FUNCIÓN DE VOZ (TEXT-TO-SPEECH) ---
def speak_js(text):
    """Inyecta JavaScript para hablar con tono divertido."""
    clean_text = text.replace("'", "\\'").replace('"', '\\"').replace("\n", " ")
    js_code = f"""
    <div id="audio-trigger"></div>
    <script>
        var text = "{clean_text}";
        function hablar() {{
            if ('speechSynthesis' in window) {{
                var utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'es-MX';
                utterance.rate = 0.95;
                utterance.pitch = 1.2;
                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(utterance);
            }}
        }}
        setTimeout(hablar, 200);
    </script>
    """
    components.html(js_code, height=0)

# HISTORIAL DE CHAT
if "messages" not in st.session_state:
    st.session_state.messages = []
if "last_response" not in st.session_state:
    st.session_state.last_response = ""

# Mostrar mensaje de bienvenida si no hay historial
if not st.session_state.messages:
    bienvenida = "⭐✨ ¡Hola, joven padawan! Soy LUCY 🛹 Amo las patinetas y STAR WARS, y estoy aquí para ayudarte. ¿Sabes qué? ¡Todos aprendemos a nuestro ritmo, como los trucos de patineta! ¿Qué misión académica tenemos hoy? ¡Que la Fuerza te acompañe! 🚀💫"
    st.session_state.messages.append({"role": "assistant", "content": bienvenida})
    st.session_state.last_response = bienvenida

# Mostrar historial
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# FUNCIÓN PARA PROCESAR RESPUESTA
def procesar_respuesta(user_input):
    # Muestra mensaje del usuario
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Genera respuesta
    with st.chat_message("assistant"):
        with st.spinner("⭐ Lucy está pensando como Jedi..."):
            try:
                mensajes_api = [{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages
                stream = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=mensajes_api,
                    stream=True,
                    temperature=0.85,
                )
                response = st.write_stream(stream)
                st.session_state.messages.append({"role": "assistant", "content": response})
                st.session_state.last_response = response
                
                # Sugerencia de pausa activa cada 5 interacciones
                if len(st.session_state.messages) % 5 == 0:
                    st.toast("🛹 ¡Lucy sugiere: Haz 3 respiraciones profundas como si te prepararas para un truco!", icon="⭐")
            except Exception as e:
                st.error(f"⭐ Ups... Lucy tuvo un problema: {str(e)}")

# --- INTERFAZ DE USUARIO ---

# 1. Entrada de Texto
placeholder_text = "✏️ Escribe tu duda... ¡Lucy te ayuda con la Fuerza! ⭐"
if prompt := st.chat_input(placeholder_text):
    procesar_respuesta(prompt)

# 2. Botones de acción
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
with col1:
    if st.button("🛹 Consejo rápido", use_container_width=True):
        consejo = "⭐ ¡Tip Jedi! ✨ Para concentrarte, divide tu tarea en 3 partes pequeñas como si fueran niveles de un juego. ¡Después de cada nivel, date un premio de 30 segundos! 🚀"
        with st.chat_message("assistant"):
            st.markdown(consejo)
        st.session_state.messages.append({"role": "assistant", "content": consejo})
        st.session_state.last_response = consejo
with col2:
    if st.button("🔊 Escuchar a Lucy", use_container_width=True):
        if st.session_state.last_response:
            speak_js(st.session_state.last_response)
with col3:
    if st.button("💫 Pausa activa", use_container_width=True):
        pausa = "🛹 ¡Hagamos un truco mental! 🎯 Respira hondo 3 veces. La primera, imagina que estás en tu patineta. La segunda, sientes la Fuerza. La tercera, ¡estás listo para seguir! ¿Listo? ¡Que la Fuerza te acompañe! ⭐"
        with st.chat_message("assistant"):
            st.markdown(pausa)
        st.session_state.messages.append({"role": "assistant", "content": pausa})
        st.session_state.last_response = pausa
with col4:
    if st.button("🔄 Empezar de nuevo", use_container_width=True):
        st.session_state.messages = []
        st.session_state.last_response = ""
        st.rerun()

# Información de apoyo en sidebar
with st.sidebar:
    st.markdown("### ⭐ Tips de Lucy")
    st.markdown("""
    **📚 Estrategias que uso contigo:**
    - 🎯 Información en bloques pequeños
    - 🛹 Pausas activas cada 5 minutos
    - 💫 Ejemplos con Star Wars y patinetas
    - ✨ Recordatorios suaves si te distraes
    
    **🚀 Para concentrarte:**
    - Usa un señalador como sable de luz
    - Divide en misiones de 5 minutos
    - Celebra cada logro
    
    **💜 Recuerda:**
    ¡Aprendes a tu ritmo, como cada patineta tiene su estilo único!
    """)
