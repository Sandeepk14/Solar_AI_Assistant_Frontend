
import os
import streamlit as st
import requests

PORT = os.getenv("PORT", "10000")  
API_URL = "https://solar-ai-assistant-genai-projects.onrender.com"

st.title("🌞 Solar Industry AI Assistant")

user_input = st.text_input("Ask something:")

if st.button("Submit"):
    response = requests.post(
        f"{API_URL}/ask",
        json={"user_message": user_input}
    )

    if response.status_code == 200:
        data = response.json()
        st.write("💡 Response:", data.get("answer", "No response received."))
    else:
        st.error(f"❌ API Error: {response.status_code}")
        st.json(response.json())
