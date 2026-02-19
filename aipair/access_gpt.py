import os
from langchain_openai import ChatOpenAI

def main():
	api_key = os.environ.get("OPENAI_API_KEY")
	if not api_key:
		print("OPENAI_API_KEY not found in environment.")
		return
	llm = ChatOpenAI(
		openai_api_key=api_key,
		model="gpt-4.1-nano"
	)
	user_input = input("Enter your prompt: ")
	response = llm.invoke(user_input)
	print("Response:", response.content)

if __name__ == "__main__":
	main()
