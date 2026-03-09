import streamlit as st
import time

# Configuración de la página
st.set_page_config(page_title="AI Business Hub", page_icon="🚀", layout="wide")

# Estilo personalizado para un look "Premium"
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007BFF; color: white; }
    </style>
    """, unsafe_allow_html=True)

# BARRA LATERAL - Configuración del Cliente
with st.sidebar:
    st.title("🛠️ Panel de Control")
    st.info("Configura los parámetros de tu asistente de IA.")
    
    plan = st.selectbox("Nivel de Servicio", ["Básico (Rápido)", "Pro (Creativo)", "Enterprise (Máxima Precisión)"])
    temperatura = st.slider("Creatividad", 0.0, 1.0, 0.7)
    
    if st.button("Limpiar Historial"):
        st.session_state.messages = []

# CUERPO PRINCIPAL
st.title("🤖 AI Business Assistant")
st.caption(f"Conectado al motor: {plan}")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada del usuario
if prompt := st.chat_input("¿En qué puedo ayudar a tu negocio hoy?"):
    # Agregar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Simulación de respuesta de IA (Aquí conectarás tu API de OpenAI, Anthropic o Gemini)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Simulamos una respuesta "pensada"
        assistant_response = f"Como experto en {plan}, analicé tu consulta: '{prompt}'. Aquí tienes una estrategia optimizada..."
        
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    st.session_state.messages.append({"role": "assistant", "content": full_response})
