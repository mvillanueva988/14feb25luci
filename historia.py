import streamlit as st
import base64
import time

# Configuración de la página
st.set_page_config(
    page_title="🏰 La perturbadora desventura de Luci ⚔️",
    page_icon="🐉",
    layout="centered"
)

# CSS personalizado con tema medieval mejorado
st.markdown("""
    <style>
    /* Fondo principal */
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                         url('https://cdnjs.cloudflare.com/ajax/libs/placeholders/4.0.0/img/1920x1080.png');
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* Contenedor principal */
    .main {
        background: rgba(28, 20, 15, 0.85);
        border-radius: 15px;
        padding: 30px;
        border: 3px solid #C19A6B;
    }
    
    /* Títulos */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Cinzel', serif;
        color: #FFD700 !important;
        text-shadow: 2px 2px 4px #000000, -1px -1px 0 #8B4513;
        border-bottom: 2px solid #8B4513;
        padding-bottom: 15px;
        margin-bottom: 25px;
        text-align: center;
        letter-spacing: 2px;
    }
    
    /* Texto normal */
    p, .stMarkdown {
        font-family: 'MedievalSharp', cursive;
        color: #FFF5E1 !important;
        font-size: 18px;
        line-height: 1.8;
        text-shadow: 1px 1px 2px #000000;
        margin-bottom: 20px;
    }
    
    /* Botones */
    .stButton button {
        background: linear-gradient(45deg, #8B4513, #A0522D) !important;
        color: #FFD700 !important;
        border: 2px solid #DAA520 !important;
        font-family: 'MedievalSharp', cursive !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        padding: 10px 25px !important;
        width: 100%;
        margin: 10px 0;
        border-radius: 8px !important;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #A0522D, #8B4513) !important;
        border-color: #FFD700 !important;
    }
    
    /* Radio buttons */
    .stRadio {
        background: rgba(139, 69, 19, 0.3);
        padding: 25px;
        border-radius: 10px;
        border: 2px solid #DAA520;
        margin: 20px 0;
    }
    
    .stRadio label {
        color: #FFD700 !important;
        font-family: 'MedievalSharp', cursive;
        font-size: 18px;
        text-shadow: 1px 1px 2px #000000;
    }
    
    /* Decoraciones */
    .chapter-decoration {
        text-align: center;
        font-size: 24px;
        color: #DAA520;
        margin: 20px 0;
    }
    
    /* Separadores */
    hr {
        border: none;
        height: 3px;
        background: linear-gradient(90deg, transparent, #DAA520, transparent);
        margin: 30px 0;
    }
    
    /* Contenedor de diálogo */
    .dialogue-box {
        background: rgba(0, 0, 0, 0.6);
        border: 2px solid #8B4513;
        border-radius: 10px;
        padding: 20px;
        margin: 20px 0;
        position: relative;
    }
    
    .dialogue-box::before {
        content: "📜";
        position: absolute;
        top: -15px;
        left: 20px;
        font-size: 24px;
    }
    
    /* Agregar fuentes personalizadas */
    @import url('https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
    </style>
""", unsafe_allow_html=True)

# Inicializar el estado de sesión si no existe
if "step" not in st.session_state:
    st.session_state["step"] = 0

def next_step():
    st.session_state["step"] += 1

def prev_step():
    if st.session_state["step"] == 11:
        st.session_state["step"] -= 2
    elif st.session_state["step"] > 0:
        st.session_state["step"] -= 1

def autoplay_audio(file_path, volume=1.0):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true" id="myAudio">
                <source src="data:audio/wav;base64,{b64}" type="audio/wav">
            </audio>
            <script>
                document.getElementById("myAudio").volume = {volume};
            </script>
            """
        st.markdown(md, unsafe_allow_html=True)

def show_decorated_title(title, emoji_start="", emoji_end=""):
    st.markdown(f"""
        <div style="text-align: center; margin: 40px 0;">
            <div class="chapter-decoration">{'⚜️' if not emoji_start else emoji_start}</div>
            <h2>{title}</h2>
            <div class="chapter-decoration">{'⚜️' if not emoji_end else emoji_end}</div>
        </div>
    """, unsafe_allow_html=True)

def show_dialogue(text, emoji="💭"):
    st.markdown(f"""
        <div class="dialogue-box">
            <p>{emoji} {text}</p>
        </div>
    """, unsafe_allow_html=True)

# Historia secuencial
if st.session_state["step"] == 0:
    show_decorated_title("Magicoaventura skibidi", "🏰", "⚔️")
    st.markdown("""
        <div style="text-align: center; padding: 30px 0;">
            <p style="font-size: 24px; font-style: italic;">Una historia medieval perturbadora</p>
        </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col2.button("📜 Comenzar la aventura", on_click=next_step)

elif st.session_state["step"] == 1:
    show_decorated_title("Esta historia no es un top", "📚", "🎭")
    show_dialogue("Es la perturbadora desventura de Luci, contra la celiaquía...")
    show_dialogue("Y su vomitivo, repelente, y cuanto menos perturbador, viaje por el Imperio Oriental Comunista Dictatorial de Perukistán", "🗺️")
    autoplay_audio("audios dross/audio1- esta historia no es un top.wav")
    col1, col2 = st.columns(2)
    col1.button("⬅️ Retroceder", on_click=prev_step)
    col2.button("Avanzar ➡️", on_click=next_step)

elif st.session_state["step"] == 2:
    show_decorated_title("Capítulo 1: El despertar", "🌅", "🛏️")
    show_dialogue("Todo comienza una hermosa mañana en la ciudad de CÓRDOBA", "🌞")
    show_dialogue("Hacían tan solo 39 grados, sin una puta nube sobre el cielo", "🌡️")
    show_dialogue("Luci se encontraba despertándose en su curioso departamento, lleno de fotos de patas en todas las paredes.", "🦶")
    autoplay_audio("audios dross/audio2- todo comienza.wav")
    col1, col2 = st.columns(2)
    col1.button("⬅️ Retroceder", on_click=prev_step)
    col2.button("🛏️ Haz click para despertar", on_click=next_step)

elif st.session_state["step"] == 3:
    show_dialogue("Bostezo atómico", "😪")
    autoplay_audio("audios dross/audio3- bostezo.wav")
    col1, col2 = st.columns(2)
    col1.button("⬅️ Retroceder", on_click=prev_step)
    col2.button("Continuar ➡️", on_click=next_step)

elif st.session_state["step"] == 4:
    show_dialogue("Coño de su madre pelotuda faltó que te cagues encima.", "😱")
    col1, col2 = st.columns(2)
    autoplay_audio("audios dross/audio4- coño de su madre.wav")
    col1.button("⬅️ Retroceder", on_click=prev_step)
    col2.button("Continuar ➡️", on_click=next_step)

elif st.session_state["step"] == 5:
    show_dialogue("*sonido de pedo atómico*", "💨")
    autoplay_audio("audios dross/audio5- Sonidos de Pedos Graciosos.wav")
    col1, col2 = st.columns(2)
    col1.button("⬅️ Retroceder", on_click=prev_step)
    col2.button("Continuar ➡️", on_click=next_step)

elif st.session_state["step"] == 6:
    show_decorated_title("Capítulo 2: La misión ANTI TACC", "🍞", "❌")
    show_dialogue("Lu finalmente se levantó de su cama, se dirigió a la heladera porque estaba recagadísima de hambre la carechimba y solo se encontró", "🚶‍♀️")
    show_dialogue("un limón sin exprimir tras ir de la cama al living por su incuantificable desesperación,  decidió enfrentar su atemorizante situación", "🍋")
    show_dialogue("Juntó sus cosas en un palito con una bolsita cual indigente venezolano y se dirigió a Sofi para comentarle", "🎒")
    show_dialogue("sobre su apoteósica holocáustica misión cristiana que asomaba por el horizonte, la cuál consistía en la alambicada obtención de bienes consumibles para celíacos amigables, es decir, libres de pecado, todo mal y gluten concebido.", "✝️")
    autoplay_audio("audios dross/audio6- se levanto de su cama.wav")
    col1, col2 = st.columns(2)
    col1.button("⬅️ Retroceder", on_click=prev_step)
    col2.button("Continuar ➡️", on_click=next_step)

elif st.session_state["step"] == 7:
    show_dialogue("Así emprendió su gesta ANTI TACC, esmerándose en su homofobia.", "⚔️")
    show_dialogue("Porque si no lo sabían, aparte de antisemillita, antisemita, anti-triguita y orgullosamente antipan y a su vez pansexual;", "🌟")
    show_dialogue("Es alérgica a los Transexuales Arcaicos Chilenos Chidos.", "🏳️‍⚧️")
    autoplay_audio("audios dross/audio7- gesta antitacc.wav")
    col1, col2 = st.columns(2)
    col1.button("⬅️ Retroceder", on_click=prev_step)
    col2.button("Continuar ➡️", on_click=next_step)

elif st.session_state["step"] == 8:
    show_decorated_title("Encuentro con Milei", "👨‍👦", "🦁")
    show_dialogue("Al bajar por la calle se encontró con Milei, su archienemigo número 1...", "😈")
    show_dialogue("Él estaba clausurando el Carrefour Express tras haber desmantelado una secta hippie comandada por Germán un yihadista proveniente de Tero Violado, reconocido vendedor de chipá en su pueblo.", "🏪")
    show_dialogue("Germán le advirtió que el presidente la estaba buscando para hacerla reconocer públicamente que River Plate es mejor que el Bosta Juniors de Fernando Gago", "⚽")
    show_dialogue("También le contó que Mateo la esperaba en Santiago del Estero para partir al Perúkistán, ya que toda la comida del país había sido infectada de un virus fabricado en los laboratorios del grupo TACC, dicha bacteria aumenta la proliferación de enzimas diabólicas TACCsicas que se encargan de la desintegración de la materia chida", "🗺️")
    autoplay_audio("audios dross/audio8- milei carrefour german.wav")
    time.sleep(2.7)
    autoplay_audio("audios dross/audio9- pianoterrorifico.wav", volume=0.2)
    col1, col2 = st.columns(2)
    col1.button("⬅️ Retroceder", on_click=prev_step)
    col2.button("Continuar ➡️", on_click=next_step)

elif st.session_state["step"] == 9:
    show_decorated_title("¿Qué quieres hacer?", "🤔", "🎯")
    opcion = st.radio("Elige tu destino:", ["🌟 Teletransportarte a Santiago", "🚌 Tomarse el colectivo"], key="choice")
    if st.button("🎲 Confirmar elección"):
        if opcion == "🌟 Teletransportarte a Santiago":
            st.session_state["step"] = 10
        else:
            st.session_state["step"] = 11
    st.button("⬅️ Retroceder", on_click=prev_step)

elif st.session_state["step"] == 10:
    show_dialogue("Salió mal y fuiste enviada a la República Chaqueña en una tribu mapuche fanática de Tan Biónica", "❌")
    show_dialogue("Por suerte pudiste volver tras ser reconocida como la Chamán Biónica al contar todas las veces que Chano tuvo un desvarío neurótico.", "🧙‍♀️")
    autoplay_audio("audios dross/audio10- teletransporte a santiago.wav")
    st.button("Continuar ➡️", on_click=next_step)

elif st.session_state["step"] == 11:
    show_decorated_title("Final: La revelación", "🎭", "❤️")
    show_dialogue("Luego de recuperar tu bolsa del linyera, lograste bajar en Santiago del Estero para encontrarte con Mateo...", "🎒")
    show_dialogue("Te confesó que el capítulo dos no fue desarrollado por falta de presupuesto", "💰")
    show_dialogue("Se gastó toda la plata en contratar a Dross como narrador y tras un accidente exótico en un recreo, fue demandado por derechos de Copyright.", "🎙️")
    show_dialogue("Aunque no por eso no te va a decir lo enamorado que está de tí, lo agradecido que está de tenerte como compañera y lo feliz que es al rededor tuyo, que este mamarracho gerontofílico vomitivo intento de originalidad fue mucho más dificil de completar de lo que parecía, pero que espera que te haya hecho reír un poco aunque sea, que te ama y te deja una cartita más seria a continuación. Se despide, Dross.", "❤️")
    autoplay_audio("audios dross/audio11- fin dross se despide.wav")
    
    # Añadimos una sección final decorativa
    st.markdown("""
        <div style="text-align: center; margin-top: 50px; padding: 30px; background: rgba(0,0,0,0.6); border: 3px solid #DAA520; border-radius: 15px;">
            <h3 style="color: #FFD700 !important; text-shadow: 2px 2px 4px #000000;">🏰 Fin de la Aventura 🏰</h3>
            <p style="font-size: 20px; color: #FFF5E1;">Gracias por jugar</p>
            <div style="font-size: 24px; margin: 20px;">
                ⚔️ 🛡️ 🏹 🗡️
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Botón para reiniciar la aventura
    if st.button("🔄 Repetir la súper experiencia hiper sensitiva e inmersiva"):
        st.session_state["step"] = 0