# Futtatás: streamlit run /Users/zsoltbarczikay/git/chat-agentic-ai/app/tests_bzsolt/streamlit_example.py
# http://localhost:8501/

import streamlit as st

st.title("Hello :blue[World!] :speech_balloon:")
st.text("This is plan texht")
st.markdown("#This is header \n **This is bold text** \n - This is list item")
st.write('This is plain text')

# built in styles
data_ex = {"Name": "Alice", "Age": 30, "Occupation": "Engineeer"}
st.write(data_ex)

# mintha folyamatosan írna
with st.chat_message("user"):   # user, assistant, human, ai
    st.write("Hello there!")

prompt = st.chat_input("Type your message")
if prompt:
    st.write(f"User message: {prompt}")

# session state, mikor esemény történik a rendszer újrafuttatja a teljes kódot... ezt figyelmbe kell venni, session_state-t
# kell használni
if st.button("First Button"):
    st.session_state.show_second_button = True # session statebe le kell tárolni!!!!
    st.write("Revealed")
    if st.button("Second button"):
        st.write("Second button")