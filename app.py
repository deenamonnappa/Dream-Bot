import openai
import streamlit as st

# Set your OpenAI API key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Function to generate text with continuous stream
def generate_text(prompt):
    # Initialize an empty string for the response
    response_text = ""

    # Start the chat message display
    chat_message = st.chat_message("bot", "Thinking...")

    # Simulate streaming response by breaking response into chunks
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a well-read journalist aware of India's recent performance in the 2024 Paralympics."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,  # Adjust token length as needed
        stream=True
    )

    # Update the response in chunks to simulate streaming
    for chunk in response:
        # Extract and append the latest part of the response
        response_text += chunk['choices'][0]['delta'].get('content', '')
        chat_message.update(response_text)

    # Return final response text
    return response_text

# Streamlit UI setup
st.title("AstraBot")
st.write("Hi! I'm AstraBot, here to help with answers, task management, problem-solving, and learning support. Available 24/7, I’m friendly, adaptable, and always ready to assist with quick insights and helpful resources. Let’s make your day easier and more productive together!")

# User input
user_input = st.text_input("You:", placeholder="Type your question here...")

# If there's a user input, get the response from the chatbot
if user_input:
    st.chat_message("user", user_input)
    generate_text(user_input)
