"""
Basic MCP Chart Generation Example

Prerequisites:
1. Docker rendering service must be running on port 3000
2. MCP Python SDK installed: pip install mcp

Usage:
    python examples/basic_example.py
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def generate_simple_chart():
    """Generate a simple pie chart."""
    
    print("🔧 Connecting to MCP server...")
    
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@antv/mcp-server-chart"],
        env={"VIS_REQUEST_SERVER": "http://localhost:3000/generate"}
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            print("✅ Connected! Initializing...")
            await session.initialize()
            
            print("🎨 Generating pie chart...")
            result = await session.call_tool(
                "generate_pie_chart",
                arguments={
                    "data": [
                        {"category": "Python", "value": 45},
                        {"category": "JavaScript", "value": 35},
                        {"category": "Java", "value": 20}
                    ],
                    "title": "Programming Languages"
                }
            )
            
            chart_url = result.content[0].text
            print(f"\n🎉 Success!")
            print(f"📍 View your chart: {chart_url}")
            
            return chart_url


if __name__ == "__main__":
    asyncio.run(generate_simple_chart())
