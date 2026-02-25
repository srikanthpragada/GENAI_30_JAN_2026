# pip install langchain-mcp-adapters

from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import asyncio

clients = MultiServerMCPClient(
    {"Math Server": {
        "url": "http://localhost:9999/mcp",
        "transport": "streamable_http"
      },
     "File Server:": {
         "url": "http://localhost:8888/mcp",
         "transport": "streamable_http"
      }
    }
)


async def process():
    tools = await clients.get_tools()
    for tool in tools:
        print(tool.name)


    model = init_chat_model("gemini-2.5-flash", model_provider="google-genai")
    #model = init_chat_model("gpt-4.1-nano", model_provider="openai")
    agent = create_agent(model, tools)
    prime_response = await agent.ainvoke({"messages": "is 383843 a prime number?"})
    for msg in prime_response['messages']:
        msg.pretty_print()

    # perfect_response = await agent.ainvoke({"messages": "is 28 a prefect number?"})
    # print(perfect_response["messages"][-1].content)

    file_response = await agent.ainvoke({"messages": "Get contents of test.txt file"})
    for msg in file_response['messages']:
        msg.pretty_print()


asyncio.run(process())
