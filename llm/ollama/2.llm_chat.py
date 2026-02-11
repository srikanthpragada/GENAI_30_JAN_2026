from langchain_ollama import ChatOllama
 
llm = ChatOllama(model="gemma3:4b")
response = llm.invoke("Which is the capital of Australia and how many timezones we have in Australia?")
print(response.content)
 
