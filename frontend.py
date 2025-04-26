import streamlit as st
import requests

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="LangGraph AI Chat",
    page_icon="💬",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Minimalist Apple-like Feel ---
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Helvetica Neue', sans-serif;
        color: black;
        background-color: white;
    }
    .main {
        padding: 2rem;
    }
    .stTextArea textarea {
        background-color: #f5f5f7;
        color: black;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: black;
        color: white;
        border-radius: 25px;
        height: 3rem;
        font-weight: 500;
    }
    .stChatMessage {
        border: 1px solid #e5e5e5;
        border-radius: 10px;
        padding: 1rem;
        background-color: #fafafa;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1 style='text-align: center;'>LangGraph AI Chat</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.1rem;'>Smart. Friendly. Powerful.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Model Selection ---
model_name = st.selectbox(
    "Choose a model",
    options=["llama3-70b-8192", "mixtral-8x7b-3278", "llama-3.3-70b-versatile", "gpt-4o-mini"]
)

provider = st.selectbox(
    "Choose provider",
    options=["Groq", "OpenAI"]
)

# --- System Prompt ---
system_prompt = st.text_area("System Prompt", value="Act as an AI chatbot who is smart and friendly")

# --- Messages Input ---
user_input = st.text_area("Your Message", height=100)

# --- Allow Search ---
allow_search = st.checkbox("Enable Search Tool", value=False)

# --- Submit ---
if st.button("Send"):
    if not user_input:
        st.warning("Please enter a message.")
    else:
        with st.spinner("Thinking..."):
            # --- Prepare API Request ---
            url = "http://127.0.0.1:8083/chat"
            payload = {
                "model_name": model_name,
                "model_provider": provider,
                "system_prompt": system_prompt,
                "messages": [user_input],
                "allow_search": allow_search
            }

            try:
                response = requests.post(url, json=payload)
                data = response.json()
                if data.get("message") == "success":
                    st.success("AI Response:")
                    st.markdown(f"""
                    <div style='
                        background-color: #f0f0f0;
                        padding: 1.5rem;
                        border-radius: 12px;
                        border: 1px solid #dcdcdc;
                        font-size: 1rem;
                        line-height: 1.6;
                        color: #111;
                    '>
                        <strong>You:</strong><br>{user_input}<br><br>
                        <strong>AI:</strong><br>{data['response']}
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.error(data.get("message"))
            except Exception as e:
                st.error(f"Error: {str(e)}")
