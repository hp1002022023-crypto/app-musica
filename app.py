import streamlit as st

st.markdown(
    """
    <style>
    /* Fondo degradado general */
    .stApp {
        background: linear-gradient(135deg, #e0f7fa, #ffffff);
        color: #333333;
        font-family: 'Poppins', sans-serif;
    }

    h1, h2, h3 {
        color: #1B5E20;
        text-align: center;
    }

    /* Botones de sentimientos */
    div.stButton > button {
        background: linear-gradient(90deg, #43A047, #66BB6A);
        color: white;
        height: 3em;
        width: 100%;
        font-size: 16px;
        border-radius: 10px;
        border: none;
        margin-bottom: 5px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(90deg, #2E7D32, #43A047);
        cursor: pointer;
    }

    /* Tip visual de consejos */
    .tip-box {
        background-color: #DFF2BF;
        color: #4F8A10;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        font-size: 16px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }

    /* Pie de página */
    .footer {
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: #333;
        margin-top: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

musica_por_estado = {
    "feliz": [
        {"titulo": "Happy", "artista": "Pharrell Williams", "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
        {"titulo": "Walking on Sunshine", "artista": "Katrina & The Waves", "url": "https://www.youtube.com/watch?v=iPUmE-tne5U"},
    ],
    "triste": [
        {"titulo": "Someone Like You", "artista": "Adele", "url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"},
        {"titulo": "Fix You", "artista": "Coldplay", "url": "https://www.youtube.com/watch?v=k4V3Mo61fJM"},
    ],
    "enamorado": [
        {"titulo": "Perfect", "artista": "Ed Sheeran", "url": "https://www.youtube.com/watch?v=2Vv-BfVoq4g"},
        {"titulo": "All of Me", "artista": "John Legend", "url": "https://www.youtube.com/watch?v=450p7goxZqg"},
    ],
    "estresado": [
        {"titulo": "Weightless", "artista": "Marconi Union", "url": "https://www.youtube.com/watch?v=UfcAVejslrU"},
        {"titulo": "Clair de Lune", "artista": "Debussy", "url": "https://www.youtube.com/watch?v=CvFH_6DNRCY"},
    ],
    "motivado": [
        {"titulo": "Eye of the Tiger", "artista": "Survivor", "url": "https://www.youtube.com/watch?v=btPJPFnesV4"},
        {"titulo": "Stronger", "artista": "Kanye West", "url": "https://www.youtube.com/watch?v=PsO6ZnUZI0g"},
    ],
    "aburrido": [
        {"titulo": "Uptown Funk", "artista": "Mark Ronson ft. Bruno Mars", "url": "https://www.youtube.com/watch?v=OPf0YbXqDm0"},
        {"titulo": "Can't Stop the Feeling!", "artista": "Justin Timberlake", "url": "https://www.youtube.com/watch?v=ru0K8uYEZWw"},
    ],
    "nostalgico": [
        {"titulo": "Yesterday", "artista": "The Beatles", "url": "https://www.youtube.com/watch?v=NrgmdOz227I"},
        {"titulo": "Summer of '69", "artista": "Bryan Adams", "url": "https://www.youtube.com/watch?v=eFjjO_lhf9c"},
    ],
    "enojado": [
        {"titulo": "Break Stuff", "artista": "Limp Bizkit", "url": "https://www.youtube.com/watch?v=ZpUYjpKg9KY"},
        {"titulo": "Killing In The Name", "artista": "Rage Against The Machine", "url": "https://www.youtube.com/watch?v=bWXazVhlyxQ"},
    ],
    "relajado": [
        {"titulo": "Sunset Lover", "artista": "Petit Biscuit", "url": "https://www.youtube.com/watch?v=Hv4cG5Z6CTY"},
        {"titulo": "Weightless", "artista": "Marconi Union", "url": "https://www.youtube.com/watch?v=UfcAVejslrU"},
    ],
    "agradecido": [
        {"titulo": "Thank You", "artista": "Dido", "url": "https://www.youtube.com/watch?v=YFQuuYg7U1Y"},
        {"titulo": "Count on Me", "artista": "Bruno Mars", "url": "https://www.youtube.com/watch?v=yJYXItns2ik"},
    ],
    "melancolico": [
        {"titulo": "The Night We Met", "artista": "Lord Huron", "url": "https://www.youtube.com/watch?v=KtlgYxa6BMU"},
        {"titulo": "Lost Cause", "artista": "Billie Eilish", "url": "https://www.youtube.com/watch?v=AGD_q1PGE-Q"},
    ],
    "sorprendido": [
        {"titulo": "Viva La Vida", "artista": "Coldplay", "url": "https://www.youtube.com/watch?v=dvgZkm1xWPE"},
        {"titulo": "Happy Now", "artista": "Kygo", "url": "https://www.youtube.com/watch?v=dGghkjpNCQ8"},
    ],
    "divertido": [
        {"titulo": "Can't Stop Me Now", "artista": "Queen", "url": "https://www.youtube.com/watch?v=HgzGwKwLmgM"},
        {"titulo": "I Gotta Feeling", "artista": "Black Eyed Peas", "url": "https://www.youtube.com/watch?v=uSD4vsh1zDA"},
    ],
    "concentrado": [
        {"titulo": "Time", "artista": "Hans Zimmer", "url": "https://www.youtube.com/watch?v=RxabLA7UQ9k"},
        {"titulo": "Clocks", "artista": "Coldplay", "url": "https://www.youtube.com/watch?v=d020hcWA_Wg"},
    ],
}

emojis = {
    "feliz": "😄",
    "triste": "😢",
    "enamorado": "😍",
    "estresado": "😫",
    "motivado": "💪",
    "aburrido": "😴",
    "nostalgico": "🥲",
    "enojado": "😡",
    "relajado": "😌",
    "agradecido": "🙏",
    "melancolico": "🌧️",
    "sorprendido": "😲",
    "divertido": "😂",
    "concentrado": "🧐",
}

tips = {
    "feliz": "¡Comparte tu alegría con alguien y sonríe mucho hoy! 😄",
    "triste": "Está bien sentirse triste, escucha música suave y cuida de ti. 😢",
    "enamorado": "Dedica un momento a esa persona especial o escribe algo bonito. 😍",
    "estresado": "Respira profundo, toma un descanso y escucha música relajante. 😫",
    "motivado": "Aprovecha tu energía y logra algo increíble hoy. 💪",
    "aburrido": "Prueba algo nuevo, escucha música divertida o da un paseo. 😴",
    "nostalgico": "Recuerda los buenos momentos, pero sigue adelante con alegría. 🥲",
    "enojado": "Respira profundo y deja salir la tensión de manera saludable. 😡",
    "relajado": "Disfruta del momento, respira y escucha música tranquila. 😌",
    "agradecido": "Escribe o comparte algo por lo que estés agradecido hoy. 🙏",
    "melancolico": "Permítete sentir y luego haz algo que te reconforte. 🌧️",
    "sorprendido": "Disfruta de la sorpresa y déjate llevar por la curiosidad. 😲",
    "divertido": "Ríe, baila y comparte momentos alegres con alguien. 😂",
    "concentrado": "Mantén la atención y avanza paso a paso en tus tareas. 🧐",
}

# Inicializar session_state
if 'favoritos' not in st.session_state:
    st.session_state['favoritos'] = []

if 'contador' not in st.session_state:
    st.session_state['contador'] = {}

# Título
st.title("Música según tu estado sentimental")
st.write("Haz clic en tu sentimiento actual:")

# Botones en columnas
col1, col2, col3 = st.columns(3)
columnas = [col1, col2, col3]

# Inicializamos la variable si no existe
if 'estado_activo' not in st.session_state:
    st.session_state['estado_activo'] = None

# Lógica de botones
for i, estado in enumerate(musica_por_estado.keys()):
    col = columnas[i % 3]

    if col.button(estado.capitalize()):
        # Si se vuelve a presionar el mismo botón, se oculta el contenido
        if st.session_state['estado_activo'] == estado:
            st.session_state['estado_activo'] = None
        else:
            st.session_state['estado_activo'] = estado

# Mostrar contenido solo si hay un estado activo
if st.session_state['estado_activo']:
    estado = st.session_state['estado_activo']
    canciones = musica_por_estado[estado]

    st.subheader(f"{emojis[estado]} Canciones para cuando te sientes {estado}")
    st.markdown(f"<div class='tip-box'>{tips[estado]}</div>", unsafe_allow_html=True)

    for c in canciones:
        # 🎥 Reproductor embebido
        st.markdown(f"**🎶 {c['titulo']}** - {c['artista']}")
        st.video(c["url"])

        # Contador de reproducciones
        if c['titulo'] not in st.session_state['contador']:
            st.session_state['contador'][c['titulo']] = 0
        st.session_state['contador'][c['titulo']] += 1
        st.write(f"Reproducciones: {st.session_state['contador'][c['titulo']]}")

        # Botón de favoritos
        if st.button(f"❤️ Agregar a favoritos: {c['titulo']}", key=f"fav_{c['titulo']}"):
            st.session_state['favoritos'].append(c)

# Mostrar favoritos
if st.session_state['favoritos']:
    st.subheader("🎵 Tus canciones favoritas:")
    for fav in st.session_state['favoritos']:
        st.markdown(f"🎶 **{fav['titulo']}** - {fav['artista']} [Escuchar]({fav['url']})")

# Pie de página
st.markdown(
    """
    <div class="footer">
        © 2025 - Ing en Sistemas Informaticos UNAB - Autores: Elmer Abel Hernandez y Luis Enrique Lopez
    </div>
    """,
    unsafe_allow_html=True
)