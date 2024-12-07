import streamlit as st
import time
import random  # To generate random query parameters

uploaded_files_set = set()
st.title("[200 OK Team] Nornickel Hackathon Multi-Model RAG with Colpali")

# File uploader in the sidebar
with st.sidebar:
    st.header("Upload Files")
    uploaded_files = st.file_uploader(
        "Choose a PDF file", accept_multiple_files=True
    )

    new_set = set()
    for f in uploaded_files:
        new_set.add(f.file_id)

# Initialize chat messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if "image" in message:
            st.markdown(message["content"])  # Display the text part
            st.image(message["image"], caption=message.get("caption", ""))
        else:
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What is up?"):
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant response simulation
    with st.chat_message("assistant"):
        response = "Поиск в процессе..."
        st.markdown(response)
        time.sleep(3)

        # Generate a unique URL for the random image
        random_query = random.randint(1, 10000)
        image_url = f"https://cataas.com/cat?{random_query}"  # Append random query

        response_text = "Результат поиска"
        st.image(image_url, caption="Результат поиска")
        st.markdown(response_text)

        # Save the assistant's response to session state
        st.session_state.messages.append({
            "role": "assistant",
            "content": response_text,
            "image": image_url,
            "caption": "Результат поиска"
        })
