from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
import asyncio

# Basic connection
transport = StreamableHttpTransport(url="http://localhost:9999/mcp")
client = Client(transport)

async def add_todo(todo : str, importance : str = 'normal'):
    async with client:
        # Call add
        result = await client.call_tool("add_todo",
            {"todo": todo,
             "importance" : importance
             })
        print(result)
 

async def list_todos_by_importance(importance):
    async with client:
        # Call add
        result = await client.call_tool("get_todos_by_importance", {"importance": importance})
        for todo in result.structured_content['result']:
            print(todo['todo'])
            print(todo['addedon'])
            print('-'  * 50)

#asyncio.run(add_todo('Work with ollama and tool calling', 'high'))
#asyncio.run(add_todo('Pay Electricity Bill'))

asyncio.run(list_todos_by_importance('high'))

