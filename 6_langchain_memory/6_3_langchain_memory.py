"""
Multiple Conversation Sessions with Persistent Memory
Demonstrates handling multiple users/sessions simultaneously
"""

from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

# Load the env
load_dotenv()

# Global store for all sessions
session_store = {}


def get_session_history(session_id: str):
    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()
    return session_store[session_id]


# Create a conversational prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a personal assistant. Remember details about each user separately."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}"),
    ]
)

# Create the chain
model = ChatOpenAI(model="gpt-4", temperature=0.7)
chain = prompt | model

# Wrap with history
conversational_chain = RunnableWithMessageHistory(
    chain, get_session_history, input_messages_key="question", history_messages_key="history"
)


def chat(session_id: str, message: str):
    """Helper function to chat with a specific session"""
    config = {"configurable": {"session_id": session_id}}
    response = conversational_chain.invoke({"question": message}, config=config)
    return response.content


# Example: Multiple users having separate conversations
if __name__ == "__main__":

    # User Alice's conversation
    print("=== Alice's Conversation ===")
    print("Alice:", "Hi! I'm Alice, a teacher from New York.")
    print("AI:", chat("alice_123", "Hi! I'm Alice, a teacher from New York."))
    print()

    # User Bob's conversation
    print("=== Bob's Conversation ===")
    print("Bob:", "Hello! I'm Bob, a chef from Paris.")
    print("AI:", chat("bob_456", "Hello! I'm Bob, a chef from Paris."))
    print()

    # Alice continues
    print("=== Alice Continues ===")
    print("Alice:", "What do I do for work?")
    print("AI:", chat("alice_123", "What do I do for work?"))
    print()

    # Bob continues
    print("=== Bob Continues ===")
    print("Bob:", "Where am I from?")
    print("AI:", chat("bob_456", "Where am I from?"))
    print()

    # Alice adds more info
    print("=== Alice Adds Info ===")
    print("Alice:", "I teach mathematics to high school students.")
    print("AI:", chat("alice_123", "I teach mathematics to high school students."))
    print()

    # Bob asks for summary
    print("=== Bob Asks for Summary ===")
    print("Bob:", "Tell me everything you know about me.")
    print("AI:", chat("bob_456", "Tell me everything you know about me."))
    print()

    # Alice asks for summary
    print("=== Alice Asks for Summary ===")
    print("Alice:", "What do you know about me?")
    print("AI:", chat("alice_123", "What do you know about me?"))
    print()

    # Show session statistics
    print("=== Session Statistics ===")
    print(f"Total active sessions: {len(session_store)}")
    print(f"Alice's message count: {len(session_store['alice_123'].messages)}")
    print(f"Bob's message count: {len(session_store['bob_456'].messages)}")
