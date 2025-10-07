import streamlit as st
import requests

# ---------------------- Estilos ----------------------
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

# ---------------------- Configuración ----------------------
YOUTUBE_API_KEY = "AIzaSyD_at-QNQ2WUGM0hKbcynogJqhc3E_jtvQ"  # <-- Coloca aquí tu API Key

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

if 'estado_activo' not in st.session_state:
    st.session_state['estado_activo'] = None

# ---------------------- Función para buscar canciones ----------------------
def buscar_canciones_youtube(estado, max_results=5):
    busqueda_map = {
        "feliz": "happy music", "triste": "sad music", "estresado": "relax music",
        "motivado": "motivational music", "enamorado": "love songs",
        "aburrido": "fun music", "nostalgico": "nostalgic songs", "enojado": "angry music",
        "relajado": "chill music", "agradecido": "thankful music", "melancolico": "melancholic music",
        "sorprendido": "surprise music", "divertido": "funny music", "concentrado": "focus music",
    }
    query = busqueda_map.get(estado, "music")
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={max_results}&q={query}&type=video&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    canciones = []
    if response.status_code == 200:
        data = response.json()
        for item in data['items']:
            canciones.append({
                "titulo": item['snippet']['title'],
                "artista": item['snippet']['channelTitle'],
                "url": f"https://www.youtube.com/watch?v={item['id']['videoId']}"
            })
    return canciones

# ---------------------- Interfaz ----------------------
st.title("Música según tu estado sentimental")
st.write("Haz clic en tu sentimiento actual:")

# Botones en columnas
col1, col2, col3 = st.columns(3)
columnas = [col1, col2, col3]

musica_por_estado = list(emojis.keys())  # solo para los botones

for i, estado in enumerate(musica_por_estado):
    col = columnas[i % 3]
    if col.button(estado.capitalize()):
        if st.session_state['estado_activo'] == estado:
            st.session_state['estado_activo'] = None
        else:
            st.session_state['estado_activo'] = estado

# Mostrar contenido solo si hay un estado activo
if st.session_state['estado_activo']:
    estado = st.session_state['estado_activo']
    canciones = buscar_canciones_youtube(estado)

    st.subheader(f"{emojis[estado]} Canciones para cuando te sientes {estado}")
    st.markdown(f"<div class='tip-box'>{tips[estado]}</div>", unsafe_allow_html=True)

    for c in canciones:
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
