# Set environment variable OPENAI_API_KEY to OpenAI key.

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4.1-nano", model_provider="openai")
response = model.invoke("What is the capital of Spain. Just give name")
print(response)