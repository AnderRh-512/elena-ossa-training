import streamlit as st
import time

# ============================================================
# CONFIGURACION DE PAGINA - VEKTOR PREMIUM (SC3 IDENTITY)
# ============================================================
st.set_page_config(
    page_title="Vektor Core - Elena Ossa Training Engine",
    page_icon="🪐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# ESTILOS CSS - IDENTIDAD SC3 · VEKTOR CONSULTING
# Palette: Forest green + gold on deep bg. Outfit + Playfair Display.
# Sidebar logo fallback: Orbitron.
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,700;1,500&family=Outfit:wght@300;400;500;600;700&family=Orbitron:wght@400;700;900&display=swap');

:root {
    --bg: #0D1F1A;
    --panel: #13281F;
    --p2: #0A1A13;
    --line: #1F3B30;
    --green: #1D9E75;
    --gdim: #155A41;
    --gg: rgba(29,158,117,.13);
    --dark: #085041;
    --gold: #E0A458;
    --gol: rgba(224,164,88,.16);
    --text: #F4F4F0;
    --muted: #8FA89D;
    --m2: #3A5B4E;
    --danger: #D9694F;
    --r: 14px;
    --rs: 10px;
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

h1, h2, h3, h4 {
    font-family: 'Playfair Display', serif !important;
    color: var(--text) !important;
    font-weight: 700 !important;
    letter-spacing: -0.01em;
}

/* Streamlit block titles: subtle green accent hierarchy */
.stApp h2, .stApp h3 {
    color: var(--text) !important;
}
.stApp .stMarkdown h3 {
    color: var(--gold) !important;
    font-size: 18px !important;
}

p, span, label, div, li {
    font-family: 'Outfit', sans-serif;
}

/* ===================== CARDS ===================== */
.vektor-card {
    background: var(--panel);
    border: 1px solid var(--line);
    padding: 22px 24px;
    border-radius: var(--r);
    margin-bottom: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

/* ===================== QUOTES / PILLARS ===================== */
.vektor-quote {
    border-left: 3px solid var(--green);
    background: var(--gg);
    padding: 14px 18px;
    border-radius: 0 12px 12px 0;
    margin: 12px 0;
    font-style: italic;
    color: var(--text);
    font-size: 14px;
    line-height: 1.7;
}

/* ===================== COMIC EXAMPLES ===================== */
.comic-bad {
    background: rgba(217, 105, 79, 0.12);
    border-left: 3px solid var(--danger);
    padding: 12px 16px;
    border-radius: 0 10px 10px 0;
    margin: 8px 0;
    color: var(--text);
    font-size: 13.5px;
    line-height: 1.6;
}
.comic-good {
    background: var(--gg);
    border-left: 3px solid var(--green);
    padding: 12px 16px;
    border-radius: 0 10px 10px 0;
    margin: 8px 0;
    color: var(--text);
    font-size: 13.5px;
    line-height: 1.6;
}

/* ===================== HOOK / TIP ===================== */
.hook {
    border-left: 3px solid var(--gold);
    background: var(--gol);
    padding: 13px 16px;
    border-radius: 0 12px 12px 0;
    margin: 12px 0;
    color: var(--text);
    line-height: 1.65;
    font-size: 14px;
}
.hlbl {
    display: block;
    font-size: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--gold);
    font-weight: 600;
    margin-bottom: 6px;
}

/* ===================== EYEBROW / TAGS ===================== */
.eyebrow {
    font-size: 10.5px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--green);
    font-weight: 500;
    margin-bottom: 8px;
}
.tag {
    display: inline-block;
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 20px;
    border: 1px solid var(--line);
    color: var(--muted);
    margin-right: 6px;
}
.tag.gold { color: var(--gold); border-color: rgba(224,164,88,0.35); }
.tag.green { color: var(--green); border-color: var(--gdim); }

/* ===================== HANGMAN ===================== */
.hangman-word {
    text-align: center;
    font-family: 'Playfair Display', serif !important;
    font-size: 3rem;
    letter-spacing: 14px;
    color: var(--gold);
    margin: 20px 0 10px;
    text-shadow: 0 2px 12px rgba(224,164,88,0.15);
}

/* ===================== LEADERBOARD ===================== */
.leaderboard-title {
    color: var(--gold) !important;
    font-family: 'Playfair Display', serif !important;
    font-weight: 700;
    text-align: center;
    letter-spacing: 3px;
    font-size: 16px !important;
    margin-bottom: 12px !important;
}
.lb-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 8px 12px;
    border-radius: var(--rs);
    background: var(--p2);
    border: 1px solid var(--line);
    margin-bottom: 6px;
}
.lb-rank {
    font-family: 'Playfair Display', serif;
    font-size: 16px;
    font-weight: 700;
    color: var(--gold);
    min-width: 24px;
}
.lb-name { flex: 1; font-size: 13.5px; color: var(--text); font-weight: 500; }
.lb-pts { font-size: 13px; color: var(--green); font-weight: 600; }
.lb-last {
    font-size: 11.5px;
    color: var(--muted);
    padding: 0 12px 6px 46px;
    font-style: italic;
    margin-top: -4px;
    margin-bottom: 6px;
}

/* ===================== SIDEBAR LOGO ===================== */
[data-testid="stSidebar"] {
    background: var(--panel);
    border-right: 1px solid var(--line);
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: var(--gold) !important;
}
.vk-logo-fallback {
    font-family: 'Orbitron', sans-serif;
    font-size: 22px;
    font-weight: 900;
    letter-spacing: 8px;
    color: var(--gold);
    text-align: center;
    padding: 20px 0 4px;
}
.vk-sub {
    text-align: center;
    font-family: 'Outfit', sans-serif;
    font-size: 10px;
    letter-spacing: 5px;
    color: var(--muted);
    margin-bottom: 14px;
    text-transform: uppercase;
}

/* ===================== STREAMLIT WIDGETS ===================== */

/* Buttons — ghost outline default */
.stButton > button {
    background: transparent !important;
    color: var(--green) !important;
    border: 1px solid var(--green) !important;
    border-radius: var(--rs) !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
    font-size: 13px !important;
    padding: 8px 16px !important;
    transition: background 0.15s, color 0.15s !important;
    box-shadow: none !important;
}
.stButton > button:hover {
    background: var(--green) !important;
    color: #031009 !important;
    border-color: var(--green) !important;
}
.stButton > button:disabled {
    opacity: 0.28 !important;
    cursor: not-allowed !important;
}

/* Form submit button = primary green solid */
.stFormSubmitButton > button {
    background: var(--green) !important;
    color: #031009 !important;
    border: none !important;
    font-weight: 700 !important;
    padding: 12px 24px !important;
    border-radius: 12px !important;
}
.stFormSubmitButton > button:hover {
    background: var(--gold) !important;
    color: #1a1305 !important;
}

/* Inputs / text area */
.stTextInput input,
.stTextArea textarea,
.stNumberInput input {
    background: var(--p2) !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    border-radius: 12px !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important;
}
.stTextInput input:focus,
.stTextArea textarea:focus,
.stNumberInput input:focus {
    border-color: var(--green) !important;
    box-shadow: none !important;
    outline: none !important;
}

/* Selectbox */
.stSelectbox [data-baseweb="select"] > div {
    background: var(--p2) !important;
    border: 1px solid var(--line) !important;
    color: var(--text) !important;
    border-radius: 12px !important;
}

/* Radio & radio labels */
.stRadio label, .stRadio p {
    color: var(--text) !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 14px !important;
}
.stRadio [data-baseweb="radio"] {
    background: var(--p2);
    padding: 8px 12px;
    border-radius: 10px;
    border: 1px solid transparent;
    margin: 4px 0;
    transition: border-color 0.15s;
}
.stRadio [data-baseweb="radio"]:hover {
    border-color: var(--gdim);
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    border-bottom: 1px solid var(--line);
    gap: 6px;
    padding: 0 4px;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: var(--muted) !important;
    border-radius: 10px 10px 0 0 !important;
    padding: 12px 20px !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 500 !important;
    font-size: 13px !important;
    letter-spacing: 0.5px !important;
    border: none !important;
}
.stTabs [aria-selected="true"] {
    color: var(--gold) !important;
    background: var(--panel) !important;
    border-bottom: 2px solid var(--gold) !important;
}

/* Alerts */
.stAlert {
    background: var(--p2) !important;
    border: 1px solid var(--line) !important;
    border-radius: var(--r) !important;
    color: var(--text) !important;
    font-family: 'Outfit', sans-serif !important;
}
.stAlert [data-testid="stMarkdownContainer"] p {
    color: var(--text) !important;
}

/* Progress bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--green), var(--gold)) !important;
}
.stProgress > div > div {
    background: var(--p2) !important;
    border-radius: 4px !important;
}

/* Expander */
[data-testid="stExpander"] {
    background: var(--p2) !important;
    border: 1px solid var(--line) !important;
    border-radius: var(--rs) !important;
}
[data-testid="stExpander"] summary {
    color: var(--gold) !important;
    font-family: 'Outfit', sans-serif !important;
    font-weight: 600 !important;
}

/* Caption */
.stCaption, [data-testid="stCaptionContainer"] {
    color: var(--muted) !important;
    font-family: 'Outfit', sans-serif !important;
}

/* Divider */
hr {
    border-color: var(--line) !important;
    opacity: 0.6 !important;
}

/* Toast */
[data-testid="stToast"] {
    background: var(--panel) !important;
    color: var(--text) !important;
    border: 1px solid var(--gold) !important;
    border-radius: var(--rs) !important;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# ESTADO GLOBAL (MOCK FIREBASE - session_state)
# ============================================================
if "players" not in st.session_state:
    st.session_state.players = {
        "Karen":    {"score": 0, "last_answer": "—"},
        "Vanessa":  {"score": 0, "last_answer": "—"},
        "Elena":    {"score": 0, "last_answer": "—"},
        "Michelle": {"score": 0, "last_answer": "—"},
    }

# HANGMAN - 4 palabras organicas rotan automaticamente
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

if "hangman_index" not in st.session_state:
    st.session_state.hangman_index = 0
    st.session_state.guessed_letters = set()
    st.session_state.wrong_count = 0

# RESPUESTAS ROLE-PLAY (Firebase mock)
if "responses" not in st.session_state:
    st.session_state.responses = {"Caso 1": {}, "Caso 2": {}, "Caso 3": {}, "Caso 4": {}}

# QUIZ SCORES
if "quiz_submitted" not in st.session_state:
    st.session_state.quiz_submitted = {}


# ============================================================
# SIDEBAR - CONSOLA VEKTOR CON LOGO TRY/EXCEPT
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
    st.markdown("<h3 class='leaderboard-title'>🏆 LEADERBOARD LIVE</h3>", unsafe_allow_html=True)
    ranked = sorted(st.session_state.players.items(), key=lambda x: x[1]["score"], reverse=True)
    medals = ["🥇", "🥈", "🥉"]
    for i, (player, data) in enumerate(ranked):
        medal = medals[i] if i < 3 else "🎖️"
        st.markdown(
            f"<div class='lb-row'>"
            f"<div class='lb-rank'>{medal}</div>"
            f"<div class='lb-name'>{player}</div>"
            f"<div class='lb-pts'>{data['score']} pts</div>"
            f"</div>"
            f"<div class='lb-last'>↳ {data['last_answer']}</div>",
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown("<div class='eyebrow'>Sesión activa</div>", unsafe_allow_html=True)
    active_player = st.selectbox(
        "¿Quién está respondiendo?",
        list(st.session_state.players.keys()),
        key="active_player",
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("<div class='eyebrow'>Consola del instructor</div>", unsafe_allow_html=True)
    mod_score = st.selectbox("Asignar puntos a:", list(st.session_state.players.keys()), key="mod_target")
    points = st.number_input("Puntos", min_value=5, max_value=20, step=5, key="mod_points")
    if st.button("⚡ Otorgar puntos en vivo"):
        st.session_state.players[mod_score]["score"] += points
        st.toast(f"¡{points} puntos asignados a {mod_score}!")
        st.rerun()


# ============================================================
# NAVEGACION PRINCIPAL
# ============================================================
tab_hoy, tab_manana = st.tabs(["🚀 SESIÓN HOY · Módulos 4 y 5", "📊 SESIÓN MAÑANA · Evaluación"])

# ============================================================
# TAB 1 - SESION HOY
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

    # ---------- NUCLEO TEORICO ----------
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

    # ---------- COMPONENTE A: AHORCADO ORGANICO ----------
    st.markdown("<div class='vektor-card'>", unsafe_allow_html=True)
    st.markdown("<span class='tag gold'>JUEGO 1 · AHORCADO</span>", unsafe_allow_html=True)
    st.markdown("### El Ahorcado Orgánico (NY Latino Market)")
    current = HANGMAN_BANK[st.session_state.hangman_index]
    st.markdown(
        f"<div style='color:var(--muted);font-size:13px;margin-bottom:6px;'>"
        f"Palabra {st.session_state.hangman_index + 1} de {len(HANGMAN_BANK)} · "
        f"Reemplaza el tecnicismo: <b style='color:var(--gold)'>{current['replaces']}</b>"
        f"</div>",
        unsafe_allow_html=True
    )

    display_word = " ".join([l if l in st.session_state.guessed_letters else "_" for l in current["word"]])
    st.markdown(f"<div class='hangman-word'>{display_word}</div>", unsafe_allow_html=True)
    st.progress(min(st.session_state.wrong_count / 6, 1.0), text=f"Errores: {st.session_state.wrong_count} / 6")

    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cols = st.columns(13)
    for i, letter in enumerate(letters):
        col_idx = i % 13
        already = letter in st.session_state.guessed_letters
        if cols[col_idx].button(letter, key=f"hang_{letter}_{st.session_state.hangman_index}", disabled=already):
            st.session_state.guessed_letters.add(letter)
            if letter in current["word"]:
                st.toast(f"¡Acertaste la letra {letter}!", icon="✨")
            else:
                st.session_state.wrong_count += 1
                st.toast(f"Letra {letter} no está.", icon="❌")
            st.rerun()

    solved = "_" not in display_word
    lost = st.session_state.wrong_count >= 6

    if solved:
        st.success(f"🎉 ¡Palabra correcta! **{current['display']}** reemplaza a *'{current['replaces']}'*.\n\n**Lección:** {current['lesson']}")
        if st.button("➕ +10 pts para el agente activo y siguiente palabra"):
            st.session_state.players[active_player]["score"] += 10
            st.session_state.players[active_player]["last_answer"] = f"Resolvió '{current['display']}'"
            st.session_state.hangman_index = (st.session_state.hangman_index + 1) % len(HANGMAN_BANK)
            st.session_state.guessed_letters = set()
            st.session_state.wrong_count = 0
            st.toast(f"+10 pts para {active_player}", icon="⚡")
            st.rerun()
    elif lost:
        st.error(f"💀 Se agotaron los intentos. La palabra era **{current['display']}**.")
        if st.button("🔄 Reintentar palabra"):
            st.session_state.guessed_letters = set()
            st.session_state.wrong_count = 0
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- COMPONENTE B: ROLE-PLAY ENGINE ----------
    st.markdown("<div class='vektor-card'>", unsafe_allow_html=True)
    st.markdown("<span class='tag green'>JUEGO 2 · ROLE-PLAY</span>", unsafe_allow_html=True)
    st.markdown("### Simulador en Tiempo Real · 4 Casos Críticos")
    st.markdown(
        "<p style='color:var(--muted);font-size:13.5px;line-height:1.6;'>"
        "El instructor activa un caso. Cada agente escribe su respuesta y ésta se sincroniza al tablero central."
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
                st.session_state.responses[case_key][active_player] = response_text.strip()
                st.session_state.players[active_player]["score"] += 15
                snippet = response_text.strip()[:60] + ("..." if len(response_text.strip()) > 60 else "")
                st.session_state.players[active_player]["last_answer"] = snippet
                st.toast(f"Respuesta de {active_player} sincronizada. +15 pts", icon="📡")
                st.rerun()
            else:
                st.warning("Escribe una respuesta antes de enviar.")
    with clear_col:
        if st.button("🧹 Limpiar respuestas del caso", key=f"clear_{case_key}"):
            st.session_state.responses[case_key] = {}
            st.rerun()

    # Tablero central de respuestas del caso activo
    st.markdown(f"### 📊 Tablero central · respuestas para {case_key}")
    case_responses = st.session_state.responses.get(case_key, {})
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
    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# TAB 2 - SESION MANANA
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

    # ---------- QUIZ FINAL 10 PREGUNTAS ----------
    st.markdown("<div class='vektor-card'>", unsafe_allow_html=True)
    st.markdown("<span class='tag green'>EVALUACIÓN FINAL</span>", unsafe_allow_html=True)
    st.markdown("### 10 preguntas · Control de comando")
    st.markdown(
        f"<div class='eyebrow'>Respondiendo como <b style='color:var(--gold)'>{active_player}</b></div>",
        unsafe_allow_html=True
    )

    QUIZ = [
        {
            "q": "1. ¿Cuál es el principal peligro de la comunicación escrita en canales virtuales?",
            "opts": [
                "Que los mensajes se demoran mucho en llegar.",
                "La libre interpretación del tono y la falta de empatía visual si no se redacta con cuidado.",
                "Que los clientes de Nueva York no leen español."
            ],
            "correct": 1
        },
        {
            "q": "2. Si un cliente se niega a depositar por Zelle por temor a fraudes, la respuesta correcta es:",
            "opts": [
                "Decirle que si no deposita no lo podemos atender.",
                "Explicarle que el depósito reserva su cabina exclusiva y se deduce del total, con confirmación inmediata.",
                "Cancelar la interacción de inmediato."
            ],
            "correct": 1
        },
        {
            "q": "3. ¿Cuál es la palabra orgánica para 'Consulta diagnóstica preliminar'?",
            "opts": ["Evaluación técnica", "Valoración", "Análisis dermatológico"],
            "correct": 1
        },
        {
            "q": "4. Un prospecto de Queens pregunta por Instagram '¿Precio del Botox?'. ¿Qué haces primero?",
            "opts": [
                "Enviar la lista de precios completa de inmediato.",
                "Saludar cálidamente y hacer una pregunta de filtrado que active interés genuino.",
                "Pedirle su dirección para enviarle catálogo impreso."
            ],
            "correct": 1
        },
        {
            "q": "5. Palabra orgánica para 'Protocolo post-procedimiento':",
            "opts": ["Recuperación clínica", "Cuidado", "Régimen aftercare"],
            "correct": 1
        },
        {
            "q": "6. La filosofía 'Aquel que habla mucho te quiere vender...' implica que:",
            "opts": [
                "Nunca hay que hablar en el chat.",
                "Preguntar activamente demuestra interés y guía la conversación hacia la solución.",
                "Sólo debemos enviar audios largos."
            ],
            "correct": 1
        },
        {
            "q": "7. Una clienta mayor dice 'mejor no reservo' porque no usa Zelle. ¿Qué haces?",
            "opts": [
                "Insistir hasta que instale la app.",
                "Ofrecer alternativas cálidas: pago telefónico, enlace seguro o reserva en recepción.",
                "Dejarla ir sin insistir."
            ],
            "correct": 1
        },
        {
            "q": "8. Palabra orgánica para 'Revitalización dérmica':",
            "opts": ["Renovación celular", "Frescura", "Estimulación epidermal"],
            "correct": 1
        },
        {
            "q": "9. En el cierre perfecto de una cita virtual NO puede faltar:",
            "opts": [
                "Sólo la fecha.",
                "Fecha, hora, indicaciones previas al tratamiento y despedida cálida.",
                "Enviar la factura anticipada."
            ],
            "correct": 1
        },
        {
            "q": "10. Palabra orgánica para 'Asesoría especializada':",
            "opts": ["Consultoría técnica", "Guía", "Coaching estético"],
            "correct": 1
        },
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
        st.session_state.quiz_submitted[active_player] = pct
        bonus = score * 2
        st.session_state.players[active_player]["score"] += bonus
        st.session_state.players[active_player]["last_answer"] = f"Evaluación final: {score}/10 ({pct}%)"

        st.success(f"✅ Evaluación consolidada. **{active_player}** obtuvo **{score}/10 ({pct}%)** — se sumaron **+{bonus} pts** al leaderboard.")

        with st.expander("🔍 Detalle por pregunta"):
            for num, ok, picked, correct in detail:
                icon = "✅" if ok else "❌"
                st.markdown(f"{icon} **P{num}** — Tu respuesta: `{picked}` · Correcta: `{correct}`")

    if st.session_state.quiz_submitted:
        st.markdown("### 📈 Historial de evaluaciones (mock Firebase)")
        for name, pct in sorted(st.session_state.quiz_submitted.items(), key=lambda x: x[1], reverse=True):
            st.markdown(
                f"<div class='lb-row'>"
                f"<div class='lb-rank'>·</div>"
                f"<div class='lb-name'>{name}</div>"
                f"<div class='lb-pts'>{pct}%</div>"
                f"</div>",
                unsafe_allow_html=True
            )

    st.markdown("</div>", unsafe_allow_html=True)
