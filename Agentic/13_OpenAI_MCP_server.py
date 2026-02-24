from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo_server")

@mcp.tool()
async def greeting(name: str) -> str:
    text = f"Nice to meet you {name}! It is a demo MCP server!"
    return(text)

@mcp.resource("people://getdata/{name}")
async def read_people_resource(name: str) -> str:
    number = 42
    return(number)

if __name__ == "__main__" :
    mcp.run(transport="stdio")

# futtatni pl 
# uv run 13_OpenAI_MCP_server.py 