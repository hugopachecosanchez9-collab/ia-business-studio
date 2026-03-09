import streamlit as st
from openai import OpenAI

# Configuración visual
st.set_page_config(page_title="AI Business Studio", page_icon="💼")
st.title("🤖 Consultor Pro para PYMES")

# --- CONEXIÓN CON EL CEREBRO (API KEY) ---
# Esto busca la llave que pusiste en los 'Secrets' de Streamlit
if "OPENAI_API_KEY" in st.secrets:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
else:
    st.error("⚠️ Falta configurar la API KEY en los Secrets de Streamlit.")
    st.stop()

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrada de usuario
if prompt := st.chat_input("¿En qué puedo ayudar a tu negocio?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Respuesta de la IA en tiempo real (Streaming)
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "system", "content": "Eres un consultor experto en sistemas y procesos para PYMES. Das respuestas estructuradas, profesionales y con pasos a seguir."},
                *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
