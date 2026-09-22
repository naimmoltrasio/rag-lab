from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

llm = OllamaLLM(model="llama3.2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

chain = prompt | llm

while True:
    print("\n--- New Question ---")
    question = input("Enter your question (or type 'q' to quit): ")
    if question.lower() == 'q':
        break
    print("\n--- Answer ---")
    result = chain.invoke({"input": question})
    print(result)