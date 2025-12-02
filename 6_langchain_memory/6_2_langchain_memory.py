"""
Simple In-Memory Chat with RunnableWithMessageHistory
Modern LangChain approach without LangGraph
"""

from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

# Load the env
load_dotenv()

# Dictionary to store chat histories for different sessions
chat_histories = {}


def get_chat_history(session_id: str):
    """Retrieve or create chat history for a given session"""
    if session_id not in chat_histories:
        chat_histories[session_id] = InMemoryChatMessageHistory()
    return chat_histories[session_id]


# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Remember user information from the conversation."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
    ]
)

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4", temperature=0)

# Create the chain using LCEL (pipe operator)
chain = prompt | llm

# Wrap the chain with message history
runnable_with_history = RunnableWithMessageHistory(
    chain,
    get_chat_history,
    input_messages_key="input",
    history_messages_key="chat_history",
)

# Example usage
if __name__ == "__main__":
    session_config = {"configurable": {"session_id": "user_session_1"}}

    print("=== Conversation 1 ===")
    response1 = runnable_with_history.invoke(
        {"input": "Hello! My name is John and I'm a software engineer."},
        config=session_config,
    )
    print(f"AI: {response1.content}\n")

    print("=== Conversation 2 ===")
    response2 = runnable_with_history.invoke(
        {"input": "What's my name and profession?"},
        config=session_config,
    )
    print(f"AI: {response2.content}\n")

    print("=== Conversation 3 ===")
    response3 = runnable_with_history.invoke(
        {"input": "I also love playing guitar in my free time."},
        config=session_config,
    )
    print(f"AI: {response3.content}\n")

    print("=== Conversation 4 ===")
    response4 = runnable_with_history.invoke(
        {"input": "Can you summarize everything you know about me?"},
        config=session_config,
    )
    print(f"AI: {response4.content}\n")

    # Display the full conversation history
    print("=== Full Message History ===")
    history = chat_histories["user_session_1"]
    for i, message in enumerate(history.messages, 1):
        role = "User" if message.type == "human" else "AI"
        print(f"{i}. {role}: {message.content}")
