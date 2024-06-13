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

    st.title("ConnectEd-AI")
    st.subheader("Where Learning Meets Intelligence")

    # Introduction and chat history container
    st.write("Welcome to ConnectEd-AI! We are here to help you with your studies and answer any questions you have.")

    chat_history_container = st.empty()

    memory = ConversationBufferWindowMemory(k=3)  # Set a reasonable memory size

    # Initialize chat history if not already initialized
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Dropdown menu for selecting semester
    selected_semester = st.selectbox("Select your semester:", options=["Semester 3", "Semester 4", "Semester 5", "Semester 6", "Semester 7", "Semester 8"])

    # Subjects for each semester
    if selected_semester == "Semester 3":
        subjects = ["Engineering Mathematics - 3 (M3)", "Discrete Structure and Graph Theory (DSGT)", "Data Structure (DS)", "Digital Logic and Computer Architecture (DLCA)", "Computer Graphics (CG)"]
    elif selected_semester == "Semester 4":
        subjects = ["Engineering Mathematics - 4 (M4)", "DataBase Management System (DBMS)", "Analysis of Algorithm (AOA)", "Operating System (OS)", "MicroProcessor (MP)"]
    elif selected_semester == "Semester 5":
        subjects = ["Computer Network (CN)", "Web Computing (WC)", "Artificial Intelligence (AI)", "Data Warehouse and Mining (DWM)", "Statistics"]
    elif selected_semester == "Semester 6":
        subjects = ["Data Analysis and Visualization (DAV)", "Cryptography and System Security (CSS)", "Software Engineering and Project Management (SEPM)", "Machine Learning (ML)", "Image and Video Processing (IVP)"]
    elif selected_semester == "Semester 7":
        subjects = ["Deep Learning (DL)", "Big Data Analytics (BDA)", "Natural Language Processing (NLP)", "Blockchain Technology (BT)", "Disaster Management and Mitigation Measures (DMMM)"]
    elif selected_semester == "Semester 8":
        subjects = ["Reinforcement Learning (RL)", "Advanced Artificial Intelligence (AAI)", "Social Media Analytics (SMA)", "Entrepreneurship and Development Management (EDM)"]

    # Dropdown menu for selecting the tough subject
    tough_subject = st.selectbox("Which subject do you find tough?", options=subjects)

    # Dropdown menu for selecting desired performance
    desired_performance = st.selectbox("Desired performance in the exam:", options=["Passing only", "Average Grades", "Good Grades", "Excellent Grades"])

    # Radio buttons for selecting the type of help needed
    help_needed = st.radio("What help do you need from ConnectEd-AI?", ["Important Topics", "Study Plan"])

    # Optional prompt bar for additional context
    optional_prompt = st.text_input("Optional: Provide additional context or clarify your query (optional)")

    # Submit button
    if st.button("Submit"):
        # Initialize Groq Langchain chat object and conversation
        groq_chat = ChatGroq(groq_api_key=GROQ_API_KEY, model_name=DEFAULT_MODEL_NAME)
        conversation = ConversationChain(llm=groq_chat, memory=memory)

        # Constructing the question based on user's inputs
        question = f"I'm preparing for {selected_semester} and I find {tough_subject} tough. My desired performance in the exam is {desired_performance}. Can you provide {help_needed.lower()}?"
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
        st.write(f"\n\n**Your Query:** {message['human']}\n\n**ConnectEd-AI's Response:** {message['AI']}")


if __name__ == "__main__":
    main()
