import streamlit as st
import random

st.set_page_config(page_title="Juegos del Corazón 💘", layout="centered")

st.sidebar.title("🎮 Juegos disponibles")
selected_game = st.sidebar.radio("Elige un juego:", ["Cartas del Corazón", "Adivina la Palabra", "Memoria de Amor", "Test del Corazón"])

# ----------------------------
# 🃏 CARTAS DEL CORAZÓN
# ----------------------------
if selected_game == "Cartas del Corazón":
    st.markdown("""
        <style>
        .title {
            font-size: 40px;
            color: #e75480;
            text-align: center;
            font-weight: bold;
        }
        .subtitle {
            font-size: 24px;
            color: #ff69b4;
            text-align: center;
        }
        .poem {
            font-style: italic;
            text-align: center;
            margin: 20px;
        }
        .card {
            border: 2px solid #ff69b4;
            border-radius: 12px;
            padding: 20px;
            margin: 10px auto;
            background: #fff0f5;
            width: 300px;
            text-align: center;
            box-shadow: 0px 0px 15px rgba(231, 84, 128, 0.4);
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🃏 Cartas del Corazón</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Haz clic en una carta... y descubre lo que siento por ti</div>", unsafe_allow_html=True)

    messages = [
        "Tu sonrisa ilumina los días más grises ☀️",
        "Contigo aprendí que el amor no se dice... se siente 💓",
        "Cada latido mío lleva tu nombre ❤️",
        "Tu voz es mi canción favorita 🎶",
        "No hay distancia cuando el corazón está tan cerca 💌",
        "Eres mi pensamiento bonito de cada día 🌸",
        "Tu risa es mi lugar feliz 😊",
        "Si fueras una estrella, serías la que guía mi universo ✨"
    ]

    if 'deck' not in st.session_state:
        st.session_state.deck = random.sample(messages, len(messages))
        st.session_state.revealed = [False] * len(messages)

    cols = st.columns(4)
    for i in range(len(st.session_state.deck)):
        col = cols[i % 4]
        with col:
            if st.session_state.revealed[i]:
                st.markdown(f"<div class='card'>{st.session_state.deck[i]}</div>", unsafe_allow_html=True)
            else:
                if st.button(f"Carta {i+1}", key=f"carta{i}"):
                    st.session_state.revealed[i] = True
                    st.rerun()

    if all(st.session_state.revealed):
        st.balloons()
        st.markdown("## 💖 Has descubierto todas las cartas del corazón")
        st.markdown("Y ahora, un regalo final...")

        st.components.v1.html("""
        <model-viewer src='https://modelviewer.dev/shared-assets/models/rose.glb' alt='Rosa Encantada'
                      auto-rotate camera-controls background-color='#FFFFFF'
                      style='width: 100%; height: 500px;'>
        </model-viewer>
        <script type='module' src='https://unpkg.com/@google/model-viewer/dist/model-viewer.min.js'></script>
        """, height=520)

        st.markdown("""
        <div class='poem'>
        Esta rosa no es solo belleza,<br>
        es la forma en que mi alma florece,<br>
        cada vez que tú estás cerca.<br>
        </div>
        """, unsafe_allow_html=True)

        if st.button("Volver a barajar 💫"):
            del st.session_state.deck
            del st.session_state.revealed
            st.rerun()

# ----------------------------
# 🎲 ADIVINA LA PALABRA
# ----------------------------
elif selected_game == "Adivina la Palabra":
    st.markdown("<h1 style='text-align:center; color:#e75480;'>🎲 Adivina la Palabra Secreta</h1>", unsafe_allow_html=True)
    palabras_secretas = [
        "amor", "ternura", "pasión", "alegría", "complicidad", "abrazo", "caricia", "sueño",
        "mirada", "sonrisa", "magia", "destino", "confianza", "hogar", "esperanza", "paz",
        "cariño", "futuro", "eternidad", "encanto", "locura", "beso", "deseo",
        "misterio", "universo", "belleza", "chispa", "risa", "compañía"
    ]
    if 'secret_word' not in st.session_state:
        st.session_state.secret_word = random.choice(palabras_secretas)
        st.session_state.correct_letters = [False] * len(st.session_state.secret_word)
        st.session_state.guessed_letters = set()
    secret = st.session_state.secret_word
    correct = st.session_state.correct_letters
    display = " ".join([c if correct[i] else '_' for i, c in enumerate(secret)])
    st.markdown(f"### Palabra: {display}")
    letra = st.text_input("Adivina una letra:", max_chars=1).lower()
    if letra:
        if letra in secret:
            for i, c in enumerate(secret):
                if c == letra:
                    correct[i] = True
            st.session_state.guessed_letters.add(letra)
            if all(correct):
                st.success(f"¡Felicidades! La palabra era '{secret.upper()}' 💖")
        else:
            if letra not in st.session_state.guessed_letters:
                st.session_state.guessed_letters.add(letra)
                st.warning(f"La letra '{letra}' no está. ¡Intenta con otra!")
    st.markdown(f"Letras usadas: {', '.join(sorted(st.session_state.guessed_letters))}")
    if st.button("Nueva palabra 🔄"):
        del st.session_state.secret_word
        del st.session_state.correct_letters
        del st.session_state.guessed_letters
        st.rerun()

# ----------------------------
# 🧠 MEMORIA DE AMOR
# ----------------------------
elif selected_game == "Memoria de Amor":
    st.markdown("<h1 style='text-align:center; color:#e75480;'>🧠 Memoria de Amor</h1>", unsafe_allow_html=True)
    palabras = ["Amor", "Amor", "Risa", "Risa", "Abrazo", "Abrazo", "Paz", "Paz"]
    if 'memoria_cartas' not in st.session_state:
        st.session_state.memoria_cartas = random.sample(palabras, len(palabras))
        st.session_state.memoria_mostradas = [False] * len(palabras)
        st.session_state.memoria_seleccion = []
    cols = st.columns(4)
    for i in range(len(st.session_state.memoria_cartas)):
        with cols[i % 4]:
            if st.session_state.memoria_mostradas[i]:
                st.button(st.session_state.memoria_cartas[i], key=f"mem{i}", disabled=True)
            else:
                if st.button("❓", key=f"mem{i}"):
                    st.session_state.memoria_seleccion.append(i)
                    st.session_state.memoria_mostradas[i] = True
    if len(st.session_state.memoria_seleccion) == 2:
        i, j = st.session_state.memoria_seleccion
        if st.session_state.memoria_cartas[i] != st.session_state.memoria_cartas[j]:
            st.session_state.memoria_mostradas[i] = False
            st.session_state.memoria_mostradas[j] = False
        st.session_state.memoria_seleccion = []
    if all(st.session_state.memoria_mostradas):
        st.balloons()
        st.success("¡Encontraste todas las parejas! El amor es memoria compartida 💞")
        if st.button("Jugar de nuevo 🔁"):
            del st.session_state.memoria_cartas
            del st.session_state.memoria_mostradas
            del st.session_state.memoria_seleccion
            st.rerun()

# ----------------------------
# 📝 TEST DEL CORAZÓN
# ----------------------------
elif selected_game == "Test del Corazón":
    st.markdown("""
    <style>
    .title {
        font-size: 36px;
        color: #e75480;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>📝 Test del Corazón</div>", unsafe_allow_html=True)
    st.write("Responde las siguientes preguntas para descubrir qué tan conectados estamos 💖")

    preguntas = [
        ("¿Cuál es mi color favorito?", ["Rojo", "Azul", "Verde", "Negro"], "Verde"),
        ("¿Dónde me gustaría viajar contigo?", ["París", "Tokio", "Cartagena", "Nueva York"], "Tokio"),
        ("¿Qué estación del año prefiero?", ["Primavera", "Verano", "Otoño", "Invierno"], "Otoño"),
        ("¿Qué animal me representa mejor?", ["Gato", "Perro", "Lobo", "Delfín"], "Lobo"),
        ("¿Qué tipo de música me gusta más?", ["Rock", "Baladas", "Salsa", "Pop"], "Baladas"),
        ("¿Qué comida me hace feliz?", ["Pizza", "Pasta", "Arepa con queso", "Tacos"], "Pasta"),
        ("¿Cuál es mi bebida favorita?", ["Café", "Té", "Jugo de mango", "Agua con gas"], "Jugo de mango"),
        ("¿A qué hora me gusta dormir?", ["9 pm", "10:30 pm", "12 am", "1 am"], "1 am"),
        ("¿Qué película me hace llorar?", ["Titanic", "Intensamente", "La vida es bella", "Diario de una pasión"], "La vida es bella"),
        ("¿Cuál es mi flor favorita?", ["Rosa", "Girasol", "Tulipán", "Lirio"], "Girasol"),
        ("¿Qué superpoder elegiría?", ["Volar", "Leer mentes", "Curar", "Teletransportarme"], "Teletransportarme"),
        ("¿Qué prefiero un día de lluvia?", ["Leer", "Dormir", "Ver pelis contigo", "Salir a caminar"], "Ver pelis contigo"),
        ("¿Qué palabra me define mejor?", ["Soñador", "Leal", "Curioso", "Apasionado"], "Leal"),
        ("¿Qué fruta me encanta?", ["Fresa", "Sandía", "Mango", "Mandarina"], "Mandarina"),
        ("¿Qué lugar me da paz?", ["El bosque", "La playa", "Mi cama", "Tus brazos"], "Tus brazos")
    ]

    if 'respuestas_test' not in st.session_state:
        st.session_state.respuestas_test = [None] * len(preguntas)
        st.session_state.puntaje_test = 0
        st.session_state.test_enviado = False

    for i, (pregunta, opciones, correcta) in enumerate(preguntas):
        respuesta = st.radio(f"{i+1}. {pregunta}", opciones, key=f"preg{i}")
        st.session_state.respuestas_test[i] = respuesta

    if st.button("Enviar respuestas ✨"):
        aciertos = 0
        for i, (pregunta, opciones, correcta) in enumerate(preguntas):
            if st.session_state.respuestas_test[i] == correcta:
                aciertos += 1
        st.session_state.puntaje_test = aciertos
        st.session_state.test_enviado = True

    if st.session_state.test_enviado:
        st.markdown(f"### Obtuviste {st.session_state.puntaje_test} de {len(preguntas)} respuestas correctas 💞")
        if st.session_state.puntaje_test >= 12:
            st.success("¡Nos conocemos como el alma y el corazón! 💘")
        elif st.session_state.puntaje_test >= 8:
            st.info("¡Vamos por muy buen camino! ✨")
        else:
            st.warning("¡Tenemos muchas aventuras por descubrir juntos! 🌈")
        if st.button("Reiniciar Test 🔄"):
            del st.session_state.respuestas_test
            del st.session_state.puntaje_test
            del st.session_state.test_enviado
            st.rerun()
