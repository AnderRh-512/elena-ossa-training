import streamlit as st
import time
import firebase_admin
from firebase_admin import credentials, db as fbdb

# ============================================================
# CONFIGURACION DE PAGINA
# ============================================================
st.set_page_config(
    page_title="Vektor Core - Elena Ossa Training Engine",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS - IDENTIDAD SC · VEKTOR CONSULTING
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;1,500&family=Outfit:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&display=swap');

:root {
    --bg: #0D1F1A; --panel: #13281F; --p2: #0A1A13; --line: #1F3B30;
    --green: #1D9E75; --gdim: #155A41; --gg: rgba(29,158,117,.13);
    --dark: #085041; --gold: #E0A458; --gol: rgba(224,164,88,.16);
    --text: #F4F4F0; --muted: #8FA89D; --m2: #3A5B4E; --danger: #D9694F;
    --r: 14px; --rs: 10px;
}
.stApp {
    background-color: var(--bg);
    background-image:
        radial-gradient(ellipse at 0% 0%, rgba(29,158,117,0.10) 0%, transparent 55%),
        radial-gradient(ellipse at 100% 0%, rgba(224,164,88,0.05) 0%, transparent 40%);
    font-family: 'Outfit', sans-serif;
    color: var(--text);
    line-height: 1.6;
}
h1, h2, h3, h4 { font-family: 'Playfair Display', serif !important; color: var(--text) !important; font-weight: 700 !important; letter-spacing: -0.01em; }
.stApp h2, .stApp h3 { color: var(--text) !important; }
.stApp .stMarkdown h3 { color: var(--gold) !important; font-size: 18px !important; }
p, span, label, div, li { font-family: 'Outfit', sans-serif; }

.vektor-card { background: var(--panel); border: 1px solid var(--line); padding: 22px 24px; border-radius: var(--r); margin-bottom: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.15); }
.vektor-quote { border-left: 3px solid var(--green); background: var(--gg); padding: 14px 18px; border-radius: 0 12px 12px 0; margin: 12px 0; font-style: italic; color: var(--text); font-size: 14px; line-height: 1.7; }
.comic-bad { background: rgba(217, 105, 79, 0.12); border-left: 3px solid var(--danger); padding: 12px 16px; border-radius: 0 10px 10px 0; margin: 8px 0; color: var(--text); font-size: 13.5px; line-height: 1.6; }
.comic-good { background: var(--gg); border-left: 3px solid var(--green); padding: 12px 16px; border-radius: 0 10px 10px 0; margin: 8px 0; color: var(--text); font-size: 13.5px; line-height: 1.6; }
.hook { border-left: 3px solid var(--gold); background: var(--gol); padding: 13px 16px; border-radius: 0 12px 12px 0; margin: 12px 0; color: var(--text); line-height: 1.65; font-size: 14px; }
.hlbl { display: block; font-size: 10px; letter-spacing: 2px; text-transform: uppercase; color: var(--gold); font-weight: 600; margin-bottom: 6px; }
.eyebrow { font-size: 10.5px; letter-spacing: 3px; text-transform: uppercase; color: var(--green); font-weight: 500; margin-bottom: 8px; }
.tag { display: inline-block; font-size: 10px; letter-spacing: 1.5px; text-transform: uppercase; font-weight: 600; padding: 3px 10px; border-radius: 20px; border: 1px solid var(--line); color: var(--muted); margin-right: 6px; }
.tag.gold { color: var(--gold); border-color: rgba(224,164,88,0.35); }
.tag.green { color: var(--green); border-color: var(--gdim); }
.hangman-word { text-align: center; font-family: 'Playfair Display', serif !important; font-size: 3rem; letter-spacing: 14px; color: var(--gold); margin: 20px 0 10px; text-shadow: 0 2px 12px rgba(224,164,88,0.15); }
.leaderboard-title { color: var(--gold) !important; font-family: 'Playfair Display', serif !important; font-weight: 700; text-align: center; letter-spacing: 3px; font-size: 16px !important; margin-bottom: 12px !important; }
.lb-row { display: flex; align-items: center; gap: 10px; padding: 8px 12px; border-radius: var(--rs); background: var(--p2); border: 1px solid var(--line); margin-bottom: 6px; }
.lb-rank { font-family: 'Playfair Display', serif; font-size: 16px; font-weight: 700; color: var(--gold); min-width: 24px; }
.lb-name { flex: 1; font-size: 13.5px; color: var(--text); font-weight: 500; }
.lb-pts { font-size: 13px; color: var(--green); font-weight: 600; }
.lb-last { font-size: 11.5px; color: var(--muted); padding: 0 12px 6px 46px; font-style: italic; margin-top: -4px; margin-bottom: 6px; }

[data-testid="stSidebar"] { background: var(--panel); border-right: 1px solid var(--line); }
[data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 { color: var(--gold) !important; }
.vk-logo-fallback { font-family: 'Orbitron', sans-serif; font-size: 22px; font-weight: 900; letter-spacing: 8px; color: var(--gold); text-align: center; padding: 20px 0 4px; }
.vk-sub { text-align: center; font-family: 'Outfit', sans-serif; font-size: 10px; letter-spacing: 5px; color: var(--muted); margin-bottom: 14px; text-transform: uppercase; }

.stButton > button { background: transparent !important; color: var(--green) !important; border: 1px solid var(--green) !important; border-radius: var(--rs) !important; font-family: 'Outfit', sans-serif !important; font-weight: 600 !important; font-size: 13px !important; padding: 8px 16px !important; transition: background 0.15s, color 0.15s !important; box-shadow: none !important; }
.stButton > button:hover { background: var(--green) !important; color: #031009 !important; border-color: var(--green) !important; }
.stButton > button:disabled { opacity: 0.28 !important; cursor: not-allowed !important; }
.stFormSubmitButton > button { background: var(--green) !important; color: #031009 !important; border: none !important; font-weight: 700 !important; padding: 12px 24px !important; border-radius: 12px !important; }
.stFormSubmitButton > button:hover { background: var(--gold) !important; color: #1a1305 !important; }

.stTextInput input, .stTextArea textarea, .stNumberInput input { background: var(--p2) !important; color: var(--text) !important; border: 1px solid var(--line) !important; border-radius: 12px !important; font-family: 'Outfit', sans-serif !important; font-size: 14px !important; }
.stTextInput input:focus, .stTextArea textarea:focus, .stNumberInput input:focus { border-color: var(--green) !important; box-shadow: none !important; outline: none !important; }
.stSelectbox [data-baseweb="select"] > div { background: var(--p2) !important; border: 1px solid var(--line) !important; color: var(--text) !important; border-radius: 12px !important; }
.stRadio label, .stRadio p { color: var(--text) !important; font-family: 'Outfit', sans-serif !important; font-size: 14px !important; }
.stRadio [data-baseweb="radio"] { background: var(--p2); padding: 8px 12px; border-radius: 10px; border: 1px solid transparent; margin: 4px 0; transition: border-color 0.15s; }
.stRadio [data-baseweb="radio"]:hover { border-color: var(--gdim); }

.stTabs [data-baseweb="tab-list"] { background: transparent; border-bottom: 1px solid var(--line); gap: 6px; padding: 0 4px; }
.stTabs [data-baseweb="tab"] { background: transparent !important; color: var(--muted) !important; border-radius: 10px 10px 0 0 !important; padding: 12px 20px !important; font-family: 'Outfit', sans-serif !important; font-weight: 500 !important; font-size: 13px !important; letter-spacing: 0.5px !important; border: none !important; }
.stTabs [aria-selected="true"] { color: var(--gold) !important; background: var(--panel) !important; border-bottom: 2px solid var(--gold) !important; }

.stAlert { background: var(--p2) !important; border: 1px solid var(--line) !important; border-radius: var(--r) !important; color: var(--text) !important; font-family: 'Outfit', sans-serif !important; }
.stAlert [data-testid="stMarkdownContainer"] p { color: var(--text) !important; }
.stProgress > div > div > div { background: linear-gradient(90deg, var(--green), var(--gold)) !important; }
.stProgress > div > div { background: var(--p2) !important; border-radius: 4px !important; }
[data-testid="stExpander"] { background: var(--p2) !important; border: 1px solid var(--line) !important; border-radius: var(--rs) !important; }
[data-testid="stExpander"] summary { color: var(--gold) !important; font-family: 'Outfit', sans-serif !important; font-weight: 600 !important; }
.stCaption, [data-testid="stCaptionContainer"] { color: var(--muted) !important; font-family: 'Outfit', sans-serif !important; }
hr { border-color: var(--line) !important; opacity: 0.6 !important; }
[data-testid="stToast"] { background: var(--panel) !important; color: var(--text) !important; border: 1px solid var(--gold) !important; border-radius: var(--rs) !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# FIREBASE REALTIME DB - INIT
# ============================================================
ROOT = "elena-ossa"

INITIAL_PLAYERS = {
    "Karen":    {"score": 0, "last_answer": "—"},
    "Vanessa":  {"score": 0, "last_answer": "—"},
    "Elena":    {"score": 0, "last_answer": "—"},
    "Michelle": {"score": 0, "last_answer": "—"},
}

HANGMAN_BANK = [
    {"word": "VALORACION", "display": "VALORACIÓN",
     "replaces": "Consulta diagnóstica preliminar",
     "lesson": "Suena cálida, no clínica. La cliente entiende de inmediato que la vas a escuchar, no a diagnosticarla."},
    {"word": "CUIDADO", "display": "CUIDADO",
     "replaces": "Protocolo post-procedimiento",
     "lesson": "Habla de acompañamiento, no de una checklist médica. Refuerza la sensación de confianza."},
    {"word": "FRESCURA", "display": "FRESCURA",
     "replaces": "Revitalización dérmica",
     "lesson": "Vende un resultado visible y sensorial, no un tecnicismo que asusta o suena costoso."},
    {"word": "GUIA", "display": "GUÍA",
     "replaces": "Asesoría especializada",
     "lesson": "Posiciona al equipo como acompañante del proceso, no como vendedor externo."},
]


def init_firebase() -> bool:
    """Returns True if Firebase Admin is initialized and usable."""
    if firebase_admin._apps:
        return True
    if "firebase" not in st.secrets:
        return False
    try:
        cred_dict = {k: v for k, v in st.secrets["firebase"].items()}
        database_url = cred_dict.pop("databaseURL", None)
        if not database_url:
            st.error("Falta `databaseURL` en `st.secrets.firebase`.")
            return False
        cred = credentials.Certificate(cred_dict)
        firebase_admin.initialize_app(cred, {"databaseURL": database_url})
        return True
    except Exception as e:
        st.error(f"Error inicializando Firebase: {e}")
        return False


def render_setup_screen():
    st.title("🪐 Configuración pendiente")
    st.markdown(
        "<div class='vektor-card'>"
        "<div class='eyebrow'>Setup · Firebase Realtime DB</div>"
        "<h3>Conectá Firebase en 4 pasos</h3>"
        "<p style='color:var(--muted);font-size:13.5px;line-height:1.7;'>"
        "Esta app usa Firebase Realtime DB para sincronizar en vivo lo que las agentes escriben "
        "desde sus teléfonos con la pantalla del instructor. Necesitás configurar las credenciales una sola vez."
        "</p>"
        "</div>",
        unsafe_allow_html=True
    )
    st.markdown("""
    **1. Crear proyecto Firebase**
    - Entra a [console.firebase.google.com](https://console.firebase.google.com) → **Add project** → dale un nombre (ej. `elena-ossa-training`).

    **2. Activar Realtime Database**
    - En el sidebar del proyecto: **Build → Realtime Database → Create database**.
    - Elige la región más cercana (ej. `us-central1`).
    - En reglas: **Start in test mode** (permite lectura/escritura por 30 días — suficiente para capacitaciones).

    **3. Generar service account key**
    - **Project Settings** (⚙️) → **Service accounts** → **Generate new private key** → descarga el JSON.

    **4. Cargar credenciales en Streamlit Cloud**
    - En [share.streamlit.io](https://share.streamlit.io/) → tu app → **Settings → Secrets**.
    - Pega el siguiente bloque, reemplazando cada campo con lo del JSON descargado + el `databaseURL` de tu Realtime Database:

    ```toml
    [firebase]
    databaseURL = "https://<tu-proyecto>-default-rtdb.firebaseio.com"
    type = "service_account"
    project_id = "..."
    private_key_id = "..."
    private_key = "-----BEGIN PRIVATE KEY-----\\n...\\n-----END PRIVATE KEY-----\\n"
    client_email = "firebase-adminsdk-....iam.gserviceaccount.com"
    client_id = "..."
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
    client_x509_cert_url = "..."
    ```

    Guardá los secrets y la app se re-deploya sola. Al recargarla verás el dashboard live.
    """)


if not init_firebase():
    render_setup_screen()
    st.stop()


# ============================================================
# DB HELPERS
# ============================================================
def ref(path: str):
    return fbdb.reference(f"{ROOT}/{path}")


def db_get(path: str, default=None):
    val = ref(path).get()
    return val if val is not None else default


def db_set(path: str, value):
    ref(path).set(value)


def db_update(path: str, updates: dict):
    ref(path).update(updates)


def seed_if_missing():
    if not db_get("players"):
        db_set("players", INITIAL_PLAYERS)
    if not db_get("hangman"):
        db_set("hangman", {"index": 0, "guessed": [], "wrong_count": 0})


seed_if_missing()


# ============================================================
# SIDEBAR
# ============================================================
with st.sidebar:
    try:
        st.image("assets/vektor-lockup-light.png", width="stretch")
    except Exception:
        st.markdown(
            "<div class='vk-logo-fallback'>VEKTOR</div>"
            "<div class='vk-sub'>CONSULTING</div>",
            unsafe_allow_html=True
        )

    st.markdown("<div class='eyebrow'>Sesión Activa · SC · Elena Ossa</div>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "<div class='hook'><span class='hlbl'>🪐 Capacitación en curso</span>"
        "<b>Cliente:</b> Elena Ossa<br>"
        "<b>Módulos:</b> 4 y 5<br>"
        "<b>Foco:</b> Comunicación no presencial</div>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    @st.fragment(run_every="2s")
    def render_leaderboard():
        players = db_get("players", INITIAL_PLAYERS)
        st.markdown("<h3 class='leaderboard-title'>🏆 LEADERBOARD LIVE</h3>", unsafe_allow_html=True)
        ranked = sorted(players.items(), key=lambda x: x[1].get("score", 0), reverse=True)
        medals = ["🥇", "🥈", "🥉"]
        for i, (player, data) in enumerate(ranked):
            medal = medals[i] if i < 3 else "🎖️"
            score = data.get("score", 0)
            last = data.get("last_answer", "—")
            st.markdown(
                f"<div class='lb-row'>"
                f"<div class='lb-rank'>{medal}</div>"
                f"<div class='lb-name'>{player}</div>"
                f"<div class='lb-pts'>{score} pts</div>"
                f"</div>"
                f"<div class='lb-last'>↳ {last}</div>",
                unsafe_allow_html=True
            )

    render_leaderboard()

    st.markdown("---")
    st.markdown("<div class='eyebrow'>Sesión activa</div>", unsafe_allow_html=True)
    player_names = list(db_get("players", INITIAL_PLAYERS).keys())
    active_player = st.selectbox(
        "¿Quién está respondiendo?",
        player_names,
        key="active_player",
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("<div class='eyebrow'>Consola del instructor</div>", unsafe_allow_html=True)
    mod_score = st.selectbox("Asignar puntos a:", player_names, key="mod_target")
    points = st.number_input("Puntos", min_value=5, max_value=20, step=5, key="mod_points")
    if st.button("⚡ Otorgar puntos en vivo"):
        current = db_get(f"players/{mod_score}/score", 0)
        db_update(f"players/{mod_score}", {"score": current + points})
        st.toast(f"¡{points} puntos asignados a {mod_score}!")
        st.rerun()

    if st.button("🔄 Reset completo de sesión", key="reset_all"):
        db_set("players", INITIAL_PLAYERS)
        db_set("hangman", {"index": 0, "guessed": [], "wrong_count": 0})
        db_set("responses", {})
        db_set("quiz_scores", {})
        st.toast("Sesión reiniciada. Todos los datos borrados.")
        st.rerun()


# ============================================================
# NAVEGACION PRINCIPAL
# ============================================================
tab_hoy, tab_manana = st.tabs(["🚀 SESIÓN HOY · Módulos 4 y 5", "📊 SESIÓN MAÑANA · Evaluación"])

# ============================================================
# TAB 1 · SESIÓN HOY
# ============================================================
with tab_hoy:
    st.markdown("<div class='eyebrow'>SC · Sistema de Conversión Comercial</div>", unsafe_allow_html=True)
    st.title("Habilidades de Comunicación Virtual")
    st.markdown(
        "<p style='color:var(--muted);font-size:14px;line-height:1.65;margin-bottom:22px;'>"
        "Módulos 4 y 5 · Empatía escrita, blindaje en depósitos y cierre de compromiso perfecto."
        "</p>",
        unsafe_allow_html=True
    )

    # ---------- PILARES ----------
    st.markdown("<div class='vektor-card'>", unsafe_allow_html=True)
    st.markdown("<span class='tag green'>PILAR TEÓRICO</span>", unsafe_allow_html=True)
    st.markdown("### Pilares de la Comunicación Empática")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            "<div class='vektor-quote'>«Aquel que habla mucho te quiere vender, aquel que te pregunta mucho, te quiere ayudar.»</div>",
            unsafe_allow_html=True
        )
        st.caption("Deja de lanzar precios fríos en el chat. Quien pregunta lidera la conversación y demuestra interés genuino por el cutis o cuerpo del cliente.")
    with col2:
        st.markdown(
            "<div class='vektor-quote'>«Cuidado con lo que escribes, por como se puede interpretar.»</div>",
            unsafe_allow_html=True
        )
        st.caption("En el chat de un Spa, la falta de puntuación o el uso de palabras ambiguas pueden cambiar radicalmente el sentido de un mensaje de relajación profunda.")

    st.markdown("### 💬 3 Ejemplos Cómicos · Cómo NO escribir en WhatsApp")
    with st.expander("👀 Ver los 3 malentendidos clásicos y su corrección profesional"):
        st.markdown("**1. El 'profundo' que se malinterpreta**")
        st.markdown("<div class='comic-bad'>❌ Cliente: 'Quiero un masaje de relajación profunda'<br>Agente: 'Yo te lo doy bien profundo, no te preocupes 😉'</div>", unsafe_allow_html=True)
        st.markdown("<div class='comic-good'>✅ Corrección: 'Perfecto, nuestro masaje de relajación profunda dura 60 min y libera tensión de espalda y cervicales. ¿Qué día te acomoda?'</div>", unsafe_allow_html=True)

        st.markdown("**2. Piedras calientes con emoji equivocado**")
        st.markdown("<div class='comic-bad'>❌ Cliente: '¿Cuánto por el masaje de piedras calientes?'<br>Agente: 'Bien caliente, te va a encantar 🔥🔥'</div>", unsafe_allow_html=True)
        st.markdown("<div class='comic-good'>✅ Corrección: 'El masaje de piedras calientes tiene un costo de $XX. Usamos piedras de basalto a temperatura terapéutica para liberar tensión muscular. ¿Te reservo un cupo?'</div>", unsafe_allow_html=True)

        st.markdown("**3. Tono brusco por prisa**")
        st.markdown("<div class='comic-bad'>❌ Cliente: 'Necesito relajarme mucho'<br>Agente: 'Ven que yo te relajo completa'</div>", unsafe_allow_html=True)
        st.markdown("<div class='comic-good'>✅ Corrección: 'Entiendo la necesidad de un descanso profundo. Te recomiendo nuestro protocolo antiestrés de 90 min. ¿Prefieres mañana en la mañana o en la tarde?'</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- AHORCADO ----------
    st.markdown("<div class='vektor-card'>", unsafe_allow_html=True)
    st.markdown("<span class='tag gold'>JUEGO 1 · AHORCADO</span>", unsafe_allow_html=True)
    st.markdown("### El Ahorcado Orgánico (NY Latino Market)")

    @st.fragment(run_every="2s")
    def render_hangman():
        state = db_get("hangman", {"index": 0, "guessed": [], "wrong_count": 0})
        idx = state.get("index", 0)
        guessed = set(state.get("guessed", []))
        wrong_count = state.get("wrong_count", 0)
        current = HANGMAN_BANK[idx]

        st.markdown(
            f"<div style='color:var(--muted);font-size:13px;margin-bottom:6px;'>"
            f"Palabra {idx + 1} de {len(HANGMAN_BANK)} · "
            f"Reemplaza el tecnicismo: <b style='color:var(--gold)'>{current['replaces']}</b>"
            f"</div>",
            unsafe_allow_html=True
        )

        display_word = " ".join([l if l in guessed else "_" for l in current["word"]])
        st.markdown(f"<div class='hangman-word'>{display_word}</div>", unsafe_allow_html=True)
        st.progress(min(wrong_count / 6, 1.0), text=f"Errores: {wrong_count} / 6")

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cols = st.columns(13)
        for i, letter in enumerate(letters):
            col_idx = i % 13
            already = letter in guessed
            if cols[col_idx].button(letter, key=f"hang_{letter}_{idx}", disabled=already):
                new_guessed = sorted(list(guessed | {letter}))
                new_wrong = wrong_count + (0 if letter in current["word"] else 1)
                db_update("hangman", {"guessed": new_guessed, "wrong_count": new_wrong})
                if letter in current["word"]:
                    st.toast(f"¡Acertaste la letra {letter}!", icon="✨")
                else:
                    st.toast(f"Letra {letter} no está.", icon="❌")
                st.rerun()

        solved = "_" not in display_word
        lost = wrong_count >= 6
        active = st.session_state.get("active_player", list(INITIAL_PLAYERS.keys())[0])

        if solved:
            st.success(f"🎉 ¡Palabra correcta! **{current['display']}** reemplaza a *'{current['replaces']}'*.\n\n**Lección:** {current['lesson']}")
            if st.button("➕ +10 pts para el agente activo y siguiente palabra", key=f"solve_{idx}"):
                cur_score = db_get(f"players/{active}/score", 0)
                db_update(f"players/{active}", {
                    "score": cur_score + 10,
                    "last_answer": f"Resolvió '{current['display']}'"
                })
                next_idx = (idx + 1) % len(HANGMAN_BANK)
                db_set("hangman", {"index": next_idx, "guessed": [], "wrong_count": 0})
                st.toast(f"+10 pts para {active}", icon="⚡")
                st.rerun()
        elif lost:
            st.error(f"💀 Se agotaron los intentos. La palabra era **{current['display']}**.")
            if st.button("🔄 Reintentar palabra", key=f"retry_{idx}"):
                db_update("hangman", {"guessed": [], "wrong_count": 0})
                st.rerun()

    render_hangman()
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- ROLE-PLAY ----------
    st.markdown("<div class='vektor-card'>", unsafe_allow_html=True)
    st.markdown("<span class='tag green'>JUEGO 2 · ROLE-PLAY</span>", unsafe_allow_html=True)
    st.markdown("### Simulador en Tiempo Real · 4 Casos Críticos")
    st.markdown(
        "<p style='color:var(--muted);font-size:13.5px;line-height:1.6;'>"
        "El instructor activa un caso. Cada agente escribe su respuesta desde el celular y aparece en vivo en el tablero central."
        "</p>",
        unsafe_allow_html=True
    )

    caso = st.radio("Seleccionar caso de práctica:", [
        "Caso 1: El gancho comercial (Precio por Instagram)",
        "Caso 2: La barrera del depósito de $20 USD por Zelle (Miedo a Estafa)",
        "Caso 3: La barrera tecnológica (Adultos mayores sin Zelle)",
        "Caso 4: El cierre de compromiso perfecto"
    ], key="active_case")
    case_key = caso.split(":")[0].strip()

    if "Caso 1" in caso:
        st.markdown(
            "<div class='hook'><span class='hlbl'>🎯 Situación</span>"
            "Un prospecto de Queens escribe por Instagram: <em>'¿Precio del Botox?'</em>. "
            "El agente NO debe dar sólo el precio frío.</div>",
            unsafe_allow_html=True
        )
        st.info("**Estructura ganadora Vektor:** Saludo cálido + Pregunta de filtrado que activa la regla *'quien pregunta, ayuda'* (edad, primera vez, zona a tratar).")
    elif "Caso 2" in caso:
        st.markdown(
            "<div class='hook'><span class='hlbl'>🛡️ Situación · Objeción financiera</span>"
            "La clienta quiere agendar pero se resiste al depósito de <b>$20 USD por Zelle</b> por miedo a estafas de internet.</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<div class='vektor-quote'><b>Script de autoridad Vektor:</b><br>"
            "«Entiendo perfectamente tu cuidado, María. Elena Ossa es una clínica registrada en Nueva York. "
            "Este depósito de $20 garantiza que tu cabina y tu especialista queden reservados exclusivamente para ti, "
            "y se descuenta de tu tratamiento final. Al instante de recibirlo, nuestro sistema te enviará "
            "la confirmación digital oficial a tu celular.»</div>",
            unsafe_allow_html=True
        )
    elif "Caso 3" in caso:
        st.markdown(
            "<div class='hook'><span class='hlbl'>👵 Situación · Barrera tecnológica</span>"
            "Una clienta mayor de Manhattan no sabe usar Zelle, se abruma y dice <em>'Mejor no agendo nada'</em>. "
            "Hay que rescatar la cita.</div>",
            unsafe_allow_html=True
        )
        st.markdown(
            "<div class='vektor-quote'><b>Protocolo alternativo Vektor:</b><br>"
            "• Enlace telefónico seguro cifrado.<br>"
            "• Procesamiento manual de tarjeta por teléfono en 2 min.<br>"
            "• Reserva presencial anticipada en recepción con efectivo o tarjeta.<br><br>"
            "<b>Script:</b> «No te preocupes, corazón. No necesitas Zelle para visitarnos. "
            "Podemos hacer tu reserva con total seguridad procesando tu tarjeta directamente por teléfono, "
            "o te guardo un cupo especial si prefieres pasar por recepción.»</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div class='hook'><span class='hlbl'>🎁 Situación · Cierre perfecto</span>"
            "El depósito fue aceptado. Toca ejecutar el cierre asegurando la asistencia.</div>",
            unsafe_allow_html=True
        )
        st.info("**Estructura ganadora Vektor:** Confirmación de fecha/hora + Indicaciones previas (sin maquillaje, hidratada, sin cafeína) + Despedida cálida con nombre del especialista.")

    st.markdown("---")
    st.markdown(
        f"<div class='eyebrow'>Respuesta de <b style='color:var(--gold)'>{active_player}</b> · {case_key}</div>",
        unsafe_allow_html=True
    )
    response_text = st.text_area(
        "Escribe la respuesta y envíala al tablero central:",
        placeholder="Ej: ¡Hola! Qué gusto saludarte. Antes de contarte precios, ¿es tu primera vez con Botox o ya tienes alguna experiencia previa?",
        key=f"resp_input_{case_key}_{active_player}",
        label_visibility="collapsed"
    )
    submit_col, clear_col = st.columns([1, 1])
    with submit_col:
        if st.button("📡 Enviar al tablero (+15 pts)", key=f"send_{case_key}"):
            if response_text.strip():
                text = response_text.strip()
                db_set(f"responses/{case_key.replace(' ', '_')}/{active_player}", text)
                cur_score = db_get(f"players/{active_player}/score", 0)
                snippet = text[:60] + ("..." if len(text) > 60 else "")
                db_update(f"players/{active_player}", {
                    "score": cur_score + 15,
                    "last_answer": snippet
                })
                st.toast(f"Respuesta de {active_player} sincronizada. +15 pts", icon="📡")
                st.rerun()
            else:
                st.warning("Escribe una respuesta antes de enviar.")
    with clear_col:
        if st.button("🧹 Limpiar respuestas del caso", key=f"clear_{case_key}"):
            db_set(f"responses/{case_key.replace(' ', '_')}", {})
            st.rerun()

    # Tablero central autoactualizado
    @st.fragment(run_every="2s")
    def render_response_board():
        active_case = st.session_state.get("active_case", "")
        ck = active_case.split(":")[0].strip() if active_case else "Caso 1"
        st.markdown(f"### 📊 Tablero central · respuestas para {ck}")
        case_responses = db_get(f"responses/{ck.replace(' ', '_')}", {})
        if not case_responses:
            st.markdown(
                "<div style='color:var(--muted);font-size:13px;padding:12px;text-align:center;"
                "background:var(--p2);border-radius:10px;border:1px dashed var(--line);'>"
                "Aún no hay respuestas para este caso.</div>",
                unsafe_allow_html=True
            )
        else:
            for agent, text in case_responses.items():
                st.markdown(
                    f"<div style='background:var(--p2);border:1px solid var(--line);"
                    f"padding:12px 14px;border-radius:10px;margin-bottom:8px;'>"
                    f"<div style='color:var(--green);font-size:12px;font-weight:600;margin-bottom:4px;'>"
                    f"{agent}</div>"
                    f"<div style='color:var(--text);font-size:13.5px;line-height:1.55;'>{text}</div>"
                    f"</div>",
                    unsafe_allow_html=True
                )

    render_response_board()
    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# TAB 2 · SESIÓN MAÑANA
# ============================================================
with tab_manana:
    st.markdown("<div class='eyebrow'>SC · Cierre y seguimiento</div>", unsafe_allow_html=True)
    st.title("Monitoreo, Seguimiento y Evaluación")

    st.markdown("<div class='vektor-card'>", unsafe_allow_html=True)
    st.markdown("<span class='tag gold'>RESUMEN</span>", unsafe_allow_html=True)
    st.markdown("### Ciclo integral de capacitación")
    st.markdown("""
    - **Módulo 1:** ADN de marca y experiencia premium en el mercado NY.
    - **Módulo 2:** Estructura de protocolos comerciales y control de tiempos en cabina.
    - **Módulo 3:** Gestión de objeciones financieras y control de insumos.
    - **Módulos 4 y 5:** Comunicación virtual, empatía escrita y blindaje en depósitos de seguridad.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- QUIZ ----------
    st.markdown("<div class='vektor-card'>", unsafe_allow_html=True)
    st.markdown("<span class='tag green'>EVALUACIÓN FINAL</span>", unsafe_allow_html=True)
    st.markdown("### 10 preguntas · Control de comando")
    st.markdown(
        f"<div class='eyebrow'>Respondiendo como <b style='color:var(--gold)'>{active_player}</b></div>",
        unsafe_allow_html=True
    )

    QUIZ = [
        {"q": "1. ¿Cuál es el principal peligro de la comunicación escrita en canales virtuales?",
         "opts": ["Que los mensajes se demoran mucho en llegar.",
                  "La libre interpretación del tono y la falta de empatía visual si no se redacta con cuidado.",
                  "Que los clientes de Nueva York no leen español."],
         "correct": 1},
        {"q": "2. Si un cliente se niega a depositar por Zelle por temor a fraudes, la respuesta correcta es:",
         "opts": ["Decirle que si no deposita no lo podemos atender.",
                  "Explicarle que el depósito reserva su cabina exclusiva y se deduce del total, con confirmación inmediata.",
                  "Cancelar la interacción de inmediato."],
         "correct": 1},
        {"q": "3. ¿Cuál es la palabra orgánica para 'Consulta diagnóstica preliminar'?",
         "opts": ["Evaluación técnica", "Valoración", "Análisis dermatológico"], "correct": 1},
        {"q": "4. Un prospecto de Queens pregunta por Instagram '¿Precio del Botox?'. ¿Qué haces primero?",
         "opts": ["Enviar la lista de precios completa de inmediato.",
                  "Saludar cálidamente y hacer una pregunta de filtrado que active interés genuino.",
                  "Pedirle su dirección para enviarle catálogo impreso."],
         "correct": 1},
        {"q": "5. Palabra orgánica para 'Protocolo post-procedimiento':",
         "opts": ["Recuperación clínica", "Cuidado", "Régimen aftercare"], "correct": 1},
        {"q": "6. La filosofía 'Aquel que habla mucho te quiere vender...' implica que:",
         "opts": ["Nunca hay que hablar en el chat.",
                  "Preguntar activamente demuestra interés y guía la conversación hacia la solución.",
                  "Sólo debemos enviar audios largos."],
         "correct": 1},
        {"q": "7. Una clienta mayor dice 'mejor no reservo' porque no usa Zelle. ¿Qué haces?",
         "opts": ["Insistir hasta que instale la app.",
                  "Ofrecer alternativas cálidas: pago telefónico, enlace seguro o reserva en recepción.",
                  "Dejarla ir sin insistir."],
         "correct": 1},
        {"q": "8. Palabra orgánica para 'Revitalización dérmica':",
         "opts": ["Renovación celular", "Frescura", "Estimulación epidermal"], "correct": 1},
        {"q": "9. En el cierre perfecto de una cita virtual NO puede faltar:",
         "opts": ["Sólo la fecha.",
                  "Fecha, hora, indicaciones previas al tratamiento y despedida cálida.",
                  "Enviar la factura anticipada."],
         "correct": 1},
        {"q": "10. Palabra orgánica para 'Asesoría especializada':",
         "opts": ["Consultoría técnica", "Guía", "Coaching estético"], "correct": 1},
    ]

    with st.form(key="quiz_form"):
        answers = []
        for idx, item in enumerate(QUIZ):
            choice = st.radio(item["q"], item["opts"], key=f"q_{idx}", index=None)
            answers.append(choice)
        submitted = st.form_submit_button("📊 Procesar y guardar calificaciones en Firebase")

    if submitted:
        with st.spinner("Calculando promedios de adherencia teórica..."):
            time.sleep(1.2)
        score = 0
        detail = []
        for idx, item in enumerate(QUIZ):
            picked = answers[idx]
            correct_text = item["opts"][item["correct"]]
            if picked == correct_text:
                score += 1
                detail.append((idx + 1, True, picked, correct_text))
            else:
                detail.append((idx + 1, False, picked, correct_text))

        pct = int((score / len(QUIZ)) * 100)
        bonus = score * 2
        cur_score = db_get(f"players/{active_player}/score", 0)
        db_update(f"players/{active_player}", {
            "score": cur_score + bonus,
            "last_answer": f"Evaluación final: {score}/10 ({pct}%)"
        })
        db_set(f"quiz_scores/{active_player}", pct)

        st.success(f"✅ Evaluación consolidada. **{active_player}** obtuvo **{score}/10 ({pct}%)** — se sumaron **+{bonus} pts** al leaderboard.")

        with st.expander("🔍 Detalle por pregunta"):
            for num, ok, picked, correct in detail:
                icon = "✅" if ok else "❌"
                st.markdown(f"{icon} **P{num}** — Tu respuesta: `{picked}` · Correcta: `{correct}`")

    # Historial de evaluaciones (live desde Firebase)
    @st.fragment(run_every="3s")
    def render_quiz_history():
        quiz_scores = db_get("quiz_scores", {})
        if quiz_scores:
            st.markdown("### 📈 Historial de evaluaciones (Firebase)")
            for name, pct in sorted(quiz_scores.items(), key=lambda x: x[1], reverse=True):
                st.markdown(
                    f"<div class='lb-row'>"
                    f"<div class='lb-rank'>·</div>"
                    f"<div class='lb-name'>{name}</div>"
                    f"<div class='lb-pts'>{pct}%</div>"
                    f"</div>",
                    unsafe_allow_html=True
                )

    render_quiz_history()
    st.markdown("</div>", unsafe_allow_html=True)
