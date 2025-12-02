from dotenv import load_dotenv
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI
from langsmith import uuid7

# Load the env
load_dotenv()

# Store for sessions
# store = {
#    "abc123": ChatMessageHistory(),
#    "user45": ChatMessageHistory(),
# }
store = {}


# Fetch or create session history
def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]


# Create chain
# MessagesPlaceholder - insert a list of chat messages here
# - used when we want to put conversation history
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

chain = prompt | ChatOpenAI(model="gpt-3.5-turbo")


# RunnableWithMessageHistory
# - add chat memory to any Runnable
# - without you having to manually manage history
# Wrap with message history
# - loads history before each call
# - save new messages after each call
with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
)

# Use it
# add this LLM invoke to this session id
# every session id is a unique chat

id = uuid7()
while True:
    print("=" * 50)
    user_input = input("Enter: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Bye")
        break

    response: AIMessage = with_message_history.invoke(
        {"input": user_input},
        config={
            "configurable": {"session_id": id},
        },
    )

    print(f"Response: {response.content}")

print("=" * 50)
print("====== HISTORY ======")
for messages in store[id]:
    for message in messages[1]:
        if isinstance(message, AIMessage):
            message_type = "AI"
        else:
            message_type = "Human"
        print(f"{message_type} - {message.content}")
