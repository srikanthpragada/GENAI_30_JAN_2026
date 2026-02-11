from langchain_ollama import ChatOllama
 
llm = ChatOllama(model="gemma3:4b", temperature = 0, max_output_tokens = 200)
response = llm.invoke("Write an email to my boss asking for leave for 2 days due to an important personal work")
print(response.content)
 
