# pip install openai
# Create key using https://platform.openai.com/api-keys
# Set environment variable OPENAI_API_KEY to OpenAI key.

from openai import OpenAI

client = OpenAI()   # api_key = key 

response = client.responses.create(
    model = "gpt-4.1-nano",
    input="What is the capital of Spain? Just give only the name"
)

#print(response)
print(response.output_text)
