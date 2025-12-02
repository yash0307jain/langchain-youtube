from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

history = [
    ("human", "Hello"),
    ("ai", "Hello how are you"),
]
prompt_filled = prompt.invoke({"history": history, "input": "Hello world"})
print("=" * 50)
print(prompt_filled)
print("=" * 50)
