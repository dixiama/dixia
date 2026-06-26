import streamlit as st
from groq import Groq
import time


# ----------------------------
# CONFIGURACIÓN INICIAL
# ----------------------------

st.set_page_config(
    page_title="Asistente de Aprendizaje",
    page_icon="🧠",
    layout="wide"
)


# ----------------------------
# ESTILOS MODERNOS
# ----------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Open+Sans:wght@300;400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Open Sans', sans-serif;
}

.main {
    background-color: #0f172a;
    color: white;
}

.stChatMessage {
    background-color: white;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 10px;
    border: 1px solid #334155;
}

[data-testid="stSidebar"] {
    background-color: white;
}

h1, h2, h3, h4, p, label {
    color: black;
}

.stButton button {
    border-radius: 10px;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)


# ----------------------------
# ESTADO DE SESIÓN
# ----------------------------

def inicializar_estado():

    if "mensajes" not in st.session_state:
        st.session_state.mensajes = []

    if "contador_dislexia" not in st.session_state:
        st.session_state.contador_dislexia = 0

    if "contador_tdah" not in st.session_state:
        st.session_state.contador_tdah = 0

    if "contador_discalculia" not in st.session_state:
        st.session_state.contador_discalculia = 0

    if "contador_disgrafia" not in st.session_state:
        st.session_state.contador_disgrafia = 0


# ----------------------------
# MOSTRAR HISTORIAL
# ----------------------------

def mostrar_historial():

    for mensaje in st.session_state.mensajes:

        with st.chat_message(
            mensaje["rol"],
            avatar="🧑" if mensaje["rol"] == "user" else "🧠"
        ):
            st.write(mensaje["contenido"])


# ----------------------------
# APP PRINCIPAL
# ----------------------------

def main():

    # ----------------------------
    # SIDEBAR
    # ----------------------------

    st.sidebar.title("⚙️ Configuración")

    MODELOS = [
        "Llama 3.1 8B",
        "Llama 3.1 70B",
        "Mixtral 8x7B",
    ]

    modelo_seleccionado = st.sidebar.selectbox(
        "Selecciona un modelo de IA",
        MODELOS
    )

    modelos_groq = {
        "Llama 3.1 8B": "llama-3.1-8b-instant",
        "Llama 3.1 70B": "llama-3.3-70b-versatile",
        "Mixtral 8x7B": "mixtral-8x7b-32768",
    }

    modelo_real = modelos_groq[modelo_seleccionado]

    # ----------------------------
    # MODO DE USUARIO
    # ----------------------------

    modo_usuario = st.sidebar.selectbox(
        "👤 ¿Quién sos?",
        ["Estudiante", "Docente", "Familia"]
    )

    # ----------------------------
    # MODO INFANTIL
    # ----------------------------

    modo_infantil = st.sidebar.checkbox(
        "👶 Explicar para niños"
    )

    # ----------------------------
    # TÍTULO
    # ----------------------------

    st.title("🧠 Asistente sobre Dificultades del Aprendizaje")

    st.write(
        "Preguntá sobre dislexia, disgrafía, discalculia, TDAH y estrategias de estudio."
    )

    st.warning(
        "Esta IA brinda orientación educativa y no reemplaza una evaluación profesional."
    )

    st.write(f"### Modelo seleccionado: {modelo_seleccionado}")

    # ----------------------------
    # API KEY
    # ----------------------------

    api_key = st.secrets.get("CLAVE_API")

    if api_key:
        st.success("✅ Conectado a Groq")
        cliente = Groq(api_key=api_key)
    else:
        st.error("❌ No se encontró la API key")
        st.stop()

    # ----------------------------
    # BOTONES RÁPIDOS
    # ----------------------------

    st.subheader("💡 Preguntas rápidas")

    col1, col2, col3 = st.columns(3)

    pregunta_rapida = None

    with col1:
        if st.button("¿Qué es la dislexia?"):
            pregunta_rapida = "¿Qué es la dislexia?"

    with col2:
        if st.button("¿Cómo ayudar con la discalculia?"):
            pregunta_rapida = "¿Cómo ayudar con la discalculia?"

    with col3:
        if st.button("Consejos para estudiar con TDAH"):
            pregunta_rapida = "Dame consejos para estudiar con TDAH"

    # ----------------------------
    # MOSTRAR HISTORIAL
    # ----------------------------

    mostrar_historial()

    # ----------------------------
    # INPUT USUARIO
    # ----------------------------

    mensaje_usuario = st.chat_input("Escribí tu pregunta...")

    if pregunta_rapida:
        mensaje_usuario = pregunta_rapida

    # ----------------------------
    # PROCESAR MENSAJE
    # ----------------------------

    if mensaje_usuario and mensaje_usuario.strip():

        mensaje_lower = mensaje_usuario.lower()

        # ----------------------------
        # CONTADORES
        # ----------------------------

        if "dislexia" in mensaje_lower:
            st.session_state.contador_dislexia += 1

        if "tdah" in mensaje_lower:
            st.session_state.contador_tdah += 1

        if "discalculia" in mensaje_lower:
            st.session_state.contador_discalculia += 1

        if "disgrafia" in mensaje_lower or "disgrafía" in mensaje_lower:
            st.session_state.contador_disgrafia += 1

        # ----------------------------
        # GUARDAR MENSAJE
        # ----------------------------

        st.session_state.mensajes.append({
            "rol": "user",
            "contenido": mensaje_usuario
        })

        # ----------------------------
        # MOSTRAR MENSAJE
        # ----------------------------

        with st.chat_message("user", avatar="🧑"):
            st.write(mensaje_usuario)

        # ----------------------------
        # MODO INFANTIL
        # ----------------------------

        if modo_infantil:
            prompt_extra = """
            Explicá de forma muy simple,
            como para un niño pequeño.
            """
        else:
            prompt_extra = ""

        # ----------------------------
        # PROMPT DEL SISTEMA
        # ----------------------------

        prompt_sistema = f"""
        Sos un asistente educativo especializado en:

        - dislexia
        - disgrafía
        - discalculia
        - TDAH
        - dificultades del aprendizaje

        El usuario es: {modo_usuario}

        Adaptá tus respuestas según el perfil:

        - Si es estudiante: explicá simple y motivá.
        - Si es docente: sugerí adaptaciones escolares.
        - Si es familia: explicá cómo acompañar desde casa.

        {prompt_extra}

        Reglas importantes:
        - Explicá de forma clara y sencilla
        - Usá lenguaje amigable
        - Nunca des diagnósticos médicos
        - Nunca afirmes que alguien tiene una condición
        - Recomendá consultar profesionales
        - Da estrategias educativas y consejos útiles
        - Sé empático y positivo
        """

        # ----------------------------
        # CONTEXTO IA
        # ----------------------------

        mensajes_para_ia = [
            {
                "role": "system",
                "content": prompt_sistema
            }
        ]

        for mensaje in st.session_state.mensajes:
            mensajes_para_ia.append({
                "role": mensaje["rol"],
                "content": mensaje["contenido"]
            })

        # ----------------------------
        # RESPUESTA IA
        # ----------------------------

        with st.chat_message("assistant", avatar="🧠"):

            with st.spinner("Pensando..."):

                respuesta = cliente.chat.completions.create(
                    model=modelo_real,
                    messages=mensajes_para_ia,
                    temperature=0.7,
                    max_tokens=1024
                )

                texto_respuesta = respuesta.choices[0].message.content

                # ----------------------------
                # EFECTO ESCRITURA
                # ----------------------------

                respuesta_placeholder = st.empty()

                texto_parcial = ""

                for palabra in texto_respuesta.split():

                    texto_parcial += palabra + " "

                    respuesta_placeholder.markdown(
                        texto_parcial
                    )

                    time.sleep(0.02)

        # ----------------------------
        # GUARDAR RESPUESTA
        # ----------------------------

        st.session_state.mensajes.append({
            "rol": "assistant",
            "contenido": texto_respuesta
        })

        # ----------------------------
        # RECURSOS AUTOMÁTICOS
        # ----------------------------

        st.subheader("📚 Recursos recomendados")

        if "dislexia" in mensaje_lower:

            st.info(
                "📄 Te recomendamos descargar la guía de lectura para dislexia."
            )

        if "tdah" in mensaje_lower:

            st.info(
                "📄 Probá nuestra técnica Pomodoro para concentración."
            )

        if "discalculia" in mensaje_lower:

            st.info(
                "📄 Mirá los ejercicios visuales de matemática."
            )

        if "disgrafia" in mensaje_lower or "disgrafía" in mensaje_lower:

            st.info(
                "📄 Te recomendamos las actividades de motricidad fina."
            )

# ----------------------------
# EJECUCIÓN
# ----------------------------

inicializar_estado()
main()