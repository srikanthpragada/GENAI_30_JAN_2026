from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-nano",
    input="Who won IPL 2025? Just give team name"
)

print(response.output_text)
