import streamlit as st
from groq import Groq
import time


# ---------------------------------------------------
# CONFIGURACIÓN
# ---------------------------------------------------

st.set_page_config(
    page_title="DIXIA",
    page_icon="🧠",
    layout="wide"
)


# ---------------------------------------------------
# ESTILOS
# ---------------------------------------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
@import url('https://fonts.cdnfonts.com/css/opendyslexic');

html, body, [class*="css"]{
    font-family:'Inter',sans-serif;
}

.stApp{
    background:
    radial-gradient(circle at top left,#dbeafe 0%,#eff6ff 25%,#f8fafc 60%,#ffffff 100%);
}

section[data-testid="stSidebar"]{
    background:rgba(255,255,255,.75);
    backdrop-filter:blur(25px);
    border-right:1px solid rgba(0,0,0,.05);
}

section[data-testid="stSidebar"] *{
    color:#0f172a !important;
}

.main .block-container{
    padding-top:2rem;
    max-width:1400px;
}

h1{
    font-size:4rem !important;
    font-weight:800 !important;
    letter-spacing:-2px;
    color:#0f172a;
}

h2,h3{
    color:#0f172a;
    font-weight:700;
}

.stChatMessage{
    border-radius:24px !important;
    padding:20px !important;
    margin-bottom:15px !important;
    border:1px solid rgba(0,0,0,.05);
    background:rgba(255,255,255,.8);
    backdrop-filter:blur(20px);
    box-shadow:
    0 10px 30px rgba(0,0,0,.05);
}

[data-testid="chatAvatarIcon-user"]{
    background:#2563eb;
}

.stButton button{
    width:100%;
    border:none;
    border-radius:16px;
    height:50px;
    font-weight:600;
    background:linear-gradient(
    135deg,
    #2563eb,
    #3b82f6
    );
    color:white;
    transition:.3s;
}

.stButton button:hover{
    transform:translateY(-2px);
    box-shadow:
    0 10px 25px rgba(37,99,235,.35);
}

.stTextInput input,
.stTextArea textarea{
    border-radius:16px !important;
    border:1px solid #dbeafe !important;
}

.stSelectbox div[data-baseweb="select"]{
    border-radius:14px;
}

.hero{
    background:rgba(255,255,255,.75);
    backdrop-filter:blur(20px);
    padding:50px;
    border-radius:30px;
    margin-bottom:30px;
    border:1px solid rgba(255,255,255,.5);
    box-shadow:
    0 20px 40px rgba(0,0,0,.05);
}

.metric-card{
    background:white;
    border-radius:24px;
    padding:20px;
    text-align:center;
    box-shadow:
    0 10px 25px rgba(0,0,0,.05);
}

.feature-card{
    background:white;
    padding:25px;
    border-radius:24px;
    box-shadow:
    0 10px 30px rgba(0,0,0,.05);
    transition:.3s;
}

.feature-card:hover{
    transform:translateY(-6px);
}

.dyslexia-font{
    font-family:'OpenDyslexic',sans-serif;
    font-size:20px;
    line-height:2.1;
    background:white;
    border-radius:24px;
    padding:25px;
    box-shadow:
    0 10px 25px rgba(0,0,0,.05);
}

@keyframes fadeUp{
    from{
        opacity:0;
        transform:translateY(20px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}

.hero,
.feature-card,
.metric-card,
.stChatMessage{
    animation:fadeUp .5s ease;
}

/* =========================
   RESPONSIVE MOBILE
========================= */

@media (max-width: 768px){

    h1{
        font-size:2.4rem !important;
        text-align:center;
    }

    h2{
        font-size:1.6rem !important;
    }

    h3{
        font-size:1.2rem !important;
    }

    .hero{
        padding:25px;
        border-radius:20px;
    }

    .hero p{
        font-size:15px !important;
    }

    .stChatMessage{
        padding:12px !important;
        border-radius:18px !important;
    }

    .feature-card{
        padding:18px;
        margin-bottom:15px;
    }

    .metric-card{
        padding:15px;
    }

    .stButton button{
        height:55px;
        font-size:15px;
    }

    .main .block-container{
        padding-left:1rem;
        padding-right:1rem;
    }

}

/* =========================
   CELULARES PEQUEÑOS
========================= */

@media (max-width: 480px){

    h1{
        font-size:2rem !important;
    }

    .hero{
        padding:20px;
    }

    .hero p{
        font-size:14px !important;
    }

    .stButton button{
        height:50px;
        font-size:14px;
    }

}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# ESTADO
# ---------------------------------------------------

if "mensajes" not in st.session_state:
    st.session_state.mensajes = []


# ---------------------------------------------------
# API
# ---------------------------------------------------

api_key = st.secrets.get("CLAVE_API")

if not api_key:
    st.error("❌ No se encontró la API KEY")
    st.stop()

cliente = Groq(api_key=api_key)


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

seccion = st.sidebar.radio(
    "📚 Secciones",
    [
        "Chatbot IA",
        "Adaptador de Texto",
        "Tests Orientativos"
    ]
)

modo_usuario = st.sidebar.selectbox(
    "👤 Usuario",
    [
        "Estudiante",
        "Docente",
        "Familia"
    ]
)

modo_infantil = st.sidebar.checkbox(
    "👶 Explicar para niños"
)


# ---------------------------------------------------
# CHATBOT IA
# ---------------------------------------------------

if seccion == "Chatbot IA":

    st.title("🧠 DIXIA")
    st.subheader("Asistente Educativo Inclusivo")

    st.warning(
        """
        Esta IA brinda orientación educativa y NO realiza diagnósticos.
        """
    )

    # ---------------------------------------------------
    # PREGUNTAS RÁPIDAS
    # ---------------------------------------------------

    st.subheader("💡 Preguntas frecuentes")

    col1, col2, col3 = st.columns(3)

    pregunta_rapida = None

    with col1:
        if st.button("¿Qué es la dislexia?"):
            pregunta_rapida = "¿Qué es la dislexia?"

    with col2:
        if st.button("¿Cómo ayudar con discalculia?"):
            pregunta_rapida = "¿Cómo ayudar con discalculia?"

    with col3:
        if st.button("Consejos de estudio"):
            pregunta_rapida = "Dame consejos de estudio"

    # ---------------------------------------------------
    # HISTORIAL
    # ---------------------------------------------------

    for mensaje in st.session_state.mensajes:

        with st.chat_message(
            mensaje["role"],
            avatar="🧑" if mensaje["role"] == "user" else "🧠"
        ):
            st.write(mensaje["content"])

    # ---------------------------------------------------
    # INPUT
    # ---------------------------------------------------

    mensaje_usuario = st.chat_input(
        "Escribí tu pregunta..."
    )

    if pregunta_rapida:
        mensaje_usuario = pregunta_rapida

    # ---------------------------------------------------
    # RESPUESTA IA
    # ---------------------------------------------------

    if mensaje_usuario:

        st.session_state.mensajes.append({
            "role": "user",
            "content": mensaje_usuario
        })

        with st.chat_message("user", avatar="🧑"):
            st.write(mensaje_usuario)

        if modo_infantil:
            prompt_extra = """
            Explicá de forma simple y amigable,
            como para un niño pequeño.
            """
        else:
            prompt_extra = ""

        prompt_sistema = f"""
        Sos DIXIA, un asistente educativo especializado en:

        - dislexia
        - disgrafía
        - discalculia
        - inclusión educativa
        - dificultades del aprendizaje

        Tus respuestas deben basarse principalmente en información educativa proveniente de:

        - International Dyslexia Association
        - Learning Disabilities Association of America
        - Disfam
        - Dislexia y Dispraxia Argentina
        - Orientación Andújar
        - OIDEA
        - ASDICAN
        - Discalculia Madrid

        Tu función es:
        - responder dudas
        - explicar conceptos
        - recomendar estrategias
        - sugerir actividades
        - recomendar contenidos educativos
        - orientar a familias y docentes

        Usuario actual: {modo_usuario}

        {prompt_extra}

        Reglas:
        - Nunca diagnostiques
        - Nunca afirmes que alguien tiene una condición
        - Recomendá consultar profesionales
        - Sé empático
        - Respondé de forma clara
        """

        mensajes_ia = [
            {
                "role": "system",
                "content": prompt_sistema
            }
        ]

        for mensaje in st.session_state.mensajes:
            mensajes_ia.append(mensaje)

        with st.chat_message("assistant", avatar="🧠"):

            with st.spinner("Pensando..."):

                respuesta = cliente.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=mensajes_ia,
                    temperature=0.7,
                    max_tokens=1200
                )

                texto = respuesta.choices[0].message.content

                placeholder = st.empty()

                parcial = ""

                for palabra in texto.split():

                    parcial += palabra + " "

                    placeholder.markdown(parcial)

                    time.sleep(0.02)

        st.session_state.mensajes.append({
            "role": "assistant",
            "content": texto
        })

        # ---------------------------------------------------
        # RECURSOS
        # ---------------------------------------------------

        st.divider()

        st.subheader("📚 Recursos recomendados")

        if "dislexia" in mensaje_usuario.lower():

            st.info(
                "📄 Guía de lectura accesible para dislexia."
            )

            st.info(
                "🎮 Juegos de reconocimiento de letras."
            )

        if "discalculia" in mensaje_usuario.lower():

            st.info(
                "🔢 Actividades visuales de matemática."
            )

        if "disgrafia" in mensaje_usuario.lower() or "disgrafía" in mensaje_usuario.lower():

            st.info(
                "✍️ Ejercicios de motricidad fina."
            )


# ---------------------------------------------------
# ADAPTADOR DE TEXTO
# ---------------------------------------------------

elif seccion == "Adaptador de Texto":

    st.title("✨ Adaptador de Texto")

    st.write(
        """
        Transformá contenidos escolares
        en formatos más accesibles.
        """
    )

    tipo_adaptacion = st.selectbox(
        "Seleccioná adaptación",
        [
            "Dislexia",
            "Discalculia",
            "Disgrafía"
        ]
    )

    texto_original = st.text_area(
        "📄 Pegá el texto o actividad",
        height=300
    )

    adaptar = st.button("✨ Adaptar contenido")

    if adaptar and texto_original.strip():

        with st.spinner("Adaptando contenido..."):

            if tipo_adaptacion == "Dislexia":

                prompt = f"""
                Adaptá este texto para personas con dislexia.

                Objetivos:
                - simplificar lectura
                - dividir ideas
                - usar frases cortas
                - destacar conceptos importantes
                - usar listas
                - mejorar comprensión

                Texto:
                {texto_original}
                """

            elif tipo_adaptacion == "Discalculia":

                prompt = f"""
                Adaptá este contenido para estudiantes con discalculia.

                Objetivos:
                - explicar paso a paso
                - simplificar operaciones
                - usar ejemplos sencillos
                - facilitar comprensión matemática

                Texto:
                {texto_original}
                """

            else:

                prompt = f"""
                Adaptá este contenido para estudiantes con disgrafía.

                Objetivos:
                - reducir escritura
                - organizar ideas
                - usar listas
                - facilitar expresión

                Texto:
                {texto_original}
                """

            respuesta = cliente.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "system",
                        "content": """
                        Sos especialista en adaptación pedagógica.
                        """
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.5,
                max_tokens=1500
            )

            texto_adaptado = respuesta.choices[0].message.content

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("📄 Original")

                st.text_area(
                    "",
                    value=texto_original,
                    height=400,
                    disabled=True
                )

            with col2:

                st.subheader("✨ Adaptado")

                if tipo_adaptacion == "Dislexia":

                    st.markdown(
                        f"""
                        <div class="dyslexia-font">
                        {texto_adaptado}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            st.success(
                "✅ Contenido adaptado correctamente."
            )


# ---------------------------------------------------
# TESTS
# ---------------------------------------------------

# ---------------------------------------------------
# TESTS ORIENTATIVOS
# ---------------------------------------------------

elif seccion == "Tests Orientativos":

    st.title("🧪 Tests Orientativos")

    st.warning(
        """
        ⚠️ IMPORTANTE:

        Estos tests NO realizan diagnósticos médicos.

        Solo identifican posibles señales asociadas
        a dificultades de aprendizaje.

        Ante cualquier duda, recomendamos consultar
        profesionales especializados.
        """
    )

    tipo_test = st.selectbox(
        "Seleccioná un test",
        [
            "Dislexia",
            "Discalculia",
            "Disgrafía"
        ]
    )

    puntaje = 0

    # ---------------------------------------------------
    # DISLEXIA
    # ---------------------------------------------------

    if tipo_test == "Dislexia":

        st.subheader("📖 Test orientativo de Dislexia")

        preguntas = [
            "¿Leés lentamente?",
            "¿Tuviste dificultades para aprender a leer en la escuela?",
            "¿Necesitás leer algo varias veces para comprenderlo?",
            "¿Te incomoda leer en voz alta?",
            "¿Omitís, cambiás o agregás letras al leer o escribir?",
            "¿Seguís teniendo errores ortográficos incluso usando corrector?",
            "¿Te cuesta pronunciar palabras largas o poco comunes?",
            "¿Preferís artículos cortos antes que libros largos?",
            "¿Te resultó muy difícil aprender otro idioma?",
            "¿Evitás actividades que requieren mucha lectura?"
        ]

        for i, pregunta in enumerate(preguntas):

            respuesta = st.radio(
                pregunta,
                ["Nunca", "A veces", "Frecuentemente"],
                key=f"dislexia_{i}"
            )

            if respuesta == "A veces":
                puntaje += 1

            elif respuesta == "Frecuentemente":
                puntaje += 2

        if st.button("📊 Ver resultado Dislexia"):

            st.subheader("Resultado")

            if puntaje >= 14:

                st.error(
                    """
                    Existen varias señales asociadas
                    a dificultades de lectura compatibles
                    con dislexia.
                    """
                )

            elif puntaje >= 8:

                st.warning(
                    """
                    Existen algunas señales asociadas
                    a dificultades de lectura.
                    """
                )

            else:

                st.success(
                    """
                    No aparecen muchas señales asociadas.
                    """
                )

            st.info(
                """
                ⚠️ Este resultado NO constituye un diagnóstico.

                Recomendamos consultar profesionales
                especializados para una evaluación adecuada.
                """
            )

    # ---------------------------------------------------
    # DISCALCULIA
    # ---------------------------------------------------

    elif tipo_test == "Discalculia":

        st.subheader("🔢 Test orientativo de Discalculia")

        preguntas = [
            "¿Confundís símbolos matemáticos como +, -, ÷ o x?",
            "¿Te cuesta seguir procedimientos matemáticos paso a paso?",
            "¿Tenés dificultad para comprender sumas, restas o multiplicaciones?",
            "¿Te cuesta memorizar las tablas?",
            "¿Te resulta difícil hacer cálculos mentales?",
            "¿Tenés dificultades usando calculadora?",
            "¿Confundís o invertís números?",
            "¿Te cuesta comprender el paso del tiempo?",
            "¿Tenés dificultades con dinero o cuentas simples?",
            "¿Te cuesta llevar puntajes en juegos?",
            "¿Tenés dificultades con presupuestos o planificación financiera?",
            "¿Te cuesta recordar fórmulas matemáticas?",
            "¿Tenés mala orientación espacial o direccional?",
            "¿Te cuesta calcular distancias o medidas?",
            "¿Sentís ansiedad al hacer matemáticas?",
            "¿Te cuesta imaginar números en orden?",
            "¿Tenés dificultades contando con los dedos?",
            "¿Te cuesta comprender relaciones numéricas simples?"
        ]

        opciones = [
            "Nunca",
            "Rara vez",
            "A veces",
            "Siempre"
        ]

        for i, pregunta in enumerate(preguntas):

            respuesta = st.radio(
                pregunta,
                opciones,
                key=f"discalculia_{i}"
            )

            if respuesta == "Rara vez":
                puntaje += 1

            elif respuesta == "A veces":
                puntaje += 2

            elif respuesta == "Siempre":
                puntaje += 3

        if st.button("📊 Ver resultado Discalculia"):

            st.subheader("Resultado")

            if puntaje >= 35:

                st.error(
                    """
                    Existen múltiples señales asociadas
                    a dificultades matemáticas compatibles
                    con discalculia.
                    """
                )

            elif puntaje >= 20:

                st.warning(
                    """
                    Existen algunas señales asociadas
                    a dificultades en el procesamiento numérico.
                    """
                )

            else:

                st.success(
                    """
                    No aparecen muchas señales asociadas.
                    """
                )

            st.info(
                """
                ⚠️ Este test NO realiza diagnósticos.

                Ante dudas, recomendamos consultar
                profesionales especializados.
                """
            )

        st.caption(
            "Fuente de referencia: DyscalculiaTest.com"
        )

    # ---------------------------------------------------
    # DISGRAFÍA
    # ---------------------------------------------------

    elif tipo_test == "Disgrafía":

        st.subheader("✍️ Test orientativo de Disgrafía")

        st.write(
            """
            La disgrafía es una dificultad relacionada
            con la escritura y la organización escrita.
            """
        )

        preguntas = [
            "¿Tenés dificultad para escribir de forma clara?",
            "¿Tu letra suele ser difícil de entender?",
            "¿Evitás escribir textos largos?",
            "¿Te cansás rápidamente al escribir?",
            "¿Te cuesta organizar ideas por escrito?",
            "¿Tenés problemas respetando espacios entre palabras?",
            "¿Te cuesta sostener correctamente el lápiz?",
            "¿Cometés errores frecuentes de puntuación o gramática?",
            "¿Escribís muy lentamente?",
            "¿Preferís responder oralmente antes que escribir?"
        ]

        for i, pregunta in enumerate(preguntas):

            respuesta = st.radio(
                pregunta,
                [
                    "Nunca",
                    "A veces",
                    "Frecuentemente"
                ],
                key=f"disgrafia_{i}"
            )

            if respuesta == "A veces":
                puntaje += 1

            elif respuesta == "Frecuentemente":
                puntaje += 2

        if st.button("📊 Ver resultado Disgrafía"):

            st.subheader("Resultado")

            if puntaje >= 14:

                st.error(
                    """
                    Existen varias señales asociadas
                    a dificultades de escritura compatibles
                    con disgrafía.
                    """
                )

            elif puntaje >= 8:

                st.warning(
                    """
                    Existen algunas señales asociadas
                    a dificultades de escritura.
                    """
                )

            else:

                st.success(
                    """
                    No aparecen muchas señales asociadas.
                    """
                )

            st.info(
                """
                ⚠️ Este resultado NO constituye un diagnóstico.

                Recomendamos consultar profesionales
                especializados para una evaluación completa.
                """
            )

        with st.expander("📚 Más información sobre Disgrafía"):

            st.write(
                """
                La disgrafía puede afectar:

                - escritura
                - ortografía
                - motricidad fina
                - organización de ideas
                - velocidad de escritura

                Muchas personas con disgrafía
                tienen más facilidad para expresarse
                oralmente que por escrito.
                """
            )
