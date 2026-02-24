import asyncio
from fastmcp import Client

client = Client("http://localhost:9999/mcp")

async def get_prompt():
    async with client:
        # get prompt
        result = await client.get_prompt("code_request",
        {
        "language": "python",
        "task": "Check whether a number is prime"
        })
         
        print(result.messages[0].content.text)

        result = await client.get_prompt("email_prompt", {
         "topic" : "A Request for sick leave of 3 days"
        })
         
        print(result.messages[0].content.text)

asyncio.run(get_prompt())