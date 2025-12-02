"""
Advanced Memory with Window Limiting and Custom Processing
Manages long conversations by keeping only recent messages
"""

from dotenv import load_dotenv
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import trim_messages
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

# Load the env
load_dotenv()

# Store for sessions
memory_store = {}


def get_memory(session_id: str):
    if session_id not in memory_store:
        memory_store[session_id] = InMemoryChatMessageHistory()
    return memory_store[session_id]


# Initialize LLM for token counting and generation
llm = ChatOpenAI(model="gpt-4", temperature=0)


# Create a message trimmer to limit history
# Keeps only the most recent messages to prevent token limit issues
def trim_chat_history(messages):
    """Trim messages to last 6 messages (3 exchanges) to manage context"""
    trimmed = trim_messages(
        messages,
        max_tokens=500,
        strategy="last",
        token_counter=llm,
        include_system=True,
    )
    return trimmed


# Create prompt with system message and history
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. You have access to recent conversation history."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

# Build chain with trimming logic
chain = RunnablePassthrough.assign(history=lambda x: trim_chat_history(x["history"])) | prompt | llm

# Wrap with message history
chat_with_limited_memory = RunnableWithMessageHistory(
    chain,
    get_memory,
    input_messages_key="input",
    history_messages_key="history",
)

# Example: Long conversation demonstrating trimming
if __name__ == "__main__":
    config = {"configurable": {"session_id": "demo_user"}}

    # Simulate a longer conversation
    messages = [
        "Hi, I'm Emma. I'm 28 years old.",
        "I work as a graphic designer in Seattle.",
        "I have two dogs named Max and Luna.",
        "I love hiking and photography.",
        "My favorite color is purple.",
        "I studied at UCLA.",
        "I speak English and Spanish.",
        "I enjoy Italian food, especially pasta.",
        "I'm planning a trip to Japan next year.",
        "What's my name and what do I do?",
    ]

    print("=== Demonstrating Conversation with Memory Trimming ===\n")

    for i, msg in enumerate(messages, 1):
        print(f"Turn {i}")
        print(f"User: {msg}")

        response = chat_with_limited_memory.invoke({"input": msg}, config=config)

        print(f"AI: {response.content}\n")
        print("-" * 60)

    # Check the actual stored history
    print("\n=== Memory Analysis ===")
    full_history = memory_store["demo_user"].messages
    print(f"Total messages stored: {len(full_history)}")
    print("(All messages are stored, but only recent ones are used in context)\n")

    # Test recall capabilities
    print("=== Testing Memory Recall ===")
    recall_test = chat_with_limited_memory.invoke(
        {"input": "List everything you remember about me from our conversation."},
        config=config,
    )
    print("User: List everything you remember about me from our conversation.")
    print(f"AI: {recall_test.content}\n")

    print("Note: AI may not recall earliest details due to message trimming,")
    print("but recent information should be accurately remembered.")

    # Show what's actually in the trimmed context
    print("\n=== Last Few Messages in Context ===")
    recent_messages = full_history[-6:]  # Show last 6 messages
    for i, msg in enumerate(recent_messages, 1):
        role = "User" if msg.type == "human" else "AI"
        print(f"{i}. {role}: {msg.content[:80]}...")
