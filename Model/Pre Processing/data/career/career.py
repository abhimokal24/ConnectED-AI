import streamlit as st
from groq import Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq

# Replace this with your actual Groq API key
GROQ_API_KEY = "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"
DEFAULT_MODEL_NAME = 'mixtral-8x7b-32768'  # Set a default model

def main():
    """
    Main function to set up the Streamlit interface and handle the chat interaction.
    """

    st.title("ConnectEd-AI : Career Roadmap")
    st.subheader("Plan Your Path to Success")

    # Introduction and chat history container
    st.write("Welcome to the Career Roadmap Generator! We are here to help you plan your path to success based on your interests and preferences.")

    chat_history_container = st.empty()

    memory = ConversationBufferWindowMemory(k=3)  # Set a reasonable memory size

    # Initialize chat history if not already initialized
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Dropdown menu for selecting preferred programming language
    preferred_language = st.selectbox("Select your preferred programming language:", options=["Python", "Java", "JavaScript", "C++", "Others"])

    # Radio buttons for selecting area of interest
    area_of_interest = st.radio("What is your primary area of interest?", ["Web Development", "Data Science", "Machine Learning", "Mobile App Development", "Game Development", "Others"])

    # Optional prompt bar for additional context
    optional_prompt = st.text_input("Optional: Provide any additional information or clarify your interests (optional)")

    # Submit button
    if st.button("Generate Roadmap"):
        # Initialize Groq Langchain chat object and conversation
        groq_chat = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=DEFAULT_MODEL_NAME)
        conversation = ConversationChain(llm=groq_chat, memory=memory)

        # Constructing the question based on user's inputs
        question = f"I'm interested in {area_of_interest.lower()} and prefer to work with {preferred_language.lower()}. Can you provide a career roadmap for me?"
        if optional_prompt:
            question += f" Additional context: {optional_prompt}"

        # Ask the question to the model
        response = conversation(question)

        # Constructing the message
        message = {'human': question, 'AI': response['response']}
        st.session_state.chat_history.insert(0, message)  # Insert new message at the beginning of chat history

    # Update chat history display
    chat_history_container.empty()  # Clear previous content
    for index, message in enumerate(st.session_state.chat_history):
        if index != 0:  # Add a partition for all results except the first one
            st.markdown("---")  # Add a horizontal line partition

        # Displaying the response
        st.write(f"\n\n**Your Query:** {message['human']}\n\n**Career Roadmap:** {message['AI']}")


if __name__ == "__main__":
    main()
