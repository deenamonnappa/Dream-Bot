import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = 'YOUR_API_KEY_HERE'

def generate_text(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Your AI Assistant for All Needs Hi! I'm AstraBot, here to help with answers, task management, problem-solving, and learning support. Available 24/7, I’m friendly, adaptable, and always ready to assist with quick insights and helpful resources. Let’s make your day easier and more productive together.!"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60  # Adjust token length as needed
    )
    return response.choices[0].message['content'].strip()

# Streamlit app
st.title("AstraBot")

# Initialize chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    st.write(message)

# User input
user_input = st.text_input("You: ", "")

# Process user input
if st.button("Send"):
    if user_input:
        # Append user message to chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        
        # Generate bot response
        bot_response = generate_text(user_input)
        
        # Append bot response to chat history
        st.session_state.chat_history.append(f"Bot: {bot_response}")

        # Clear the input
        st.experimental_rerun()

# Optional: Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.experimental_rerun()
