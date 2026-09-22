from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever  

llm = OllamaLLM(model="llama3.2")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert assistant answering questions about a restaurant "
                "based on real customer reviews.\n\n"
                "Relevant reviews:\n{reviews}"),
    ("user", "{question}")
])

chain = prompt | llm

while True:
    print("\n--- New Question ---")
    question = input("Enter your question (or type 'q' to quit): ")
    if question.lower() == 'q':
        break

    reviews = retriever.invoke(question)
    print("\n--- Answer ---")
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)