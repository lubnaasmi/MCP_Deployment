
# Local MCP Chart Generation System - 

> Privacy-first AI-powered chart visualization using Model Context Protocol and Docker

[![Docker](https://img.shields.io/badge/Docker-Ready-blue)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-1.0-orange)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🎯 Overview

A self-hosted chart generation system that enables AI assistants to create visualizations locally without external API dependencies. Built using the Model Context Protocol (MCP), Docker, and Python.

**Key Features:**
- ✅ 25+ chart types (pie, bar, line, scatter, radar, etc.)
- ✅ 100% local deployment - no external APIs
- ✅ Python SDK integration for custom agents
- ✅ Claude AI Desktop compatible
- ✅ Privacy-focused architecture

## 🏗️ Architecture 
```
┌─────────────────────────────────────┐
│   User / AI Assistant               │
│   (Claude Desktop / Python Agent)   │
└─────────────┬───────────────────────┘
              │
              ↓
┌─────────────────────────────────────┐
│   MCP Server (stdio protocol)       │
│   @antv/mcp-server-chart            │
└─────────────┬───────────────────────┘
              │ HTTP
              ↓
┌─────────────────────────────────────┐
│   Docker Container                  │
│   GPT-Vis-SSR Rendering Service     │
│   Port: 3000                        │
└─────────────┬───────────────────────┘
              │
              ↓
          Chart Image
```

## 🚀 Quick Start

### Prerequisites
- Docker Desktop installed
- Node.js & npm (for npx)
- Python 3.8+ (for Python integration)

### Step 1: Start Rendering Service
```bash
docker run -p 3000:3000 \
  -e RENDERED_IMAGE_HOST_PATH=http://localhost:3000/charts \
  ghcr.io/yaonyan/gpt-vis-mcp:latest-http
```

Keep this terminal running.

### Step 2: Configure MCP Client

**For Claude Desktop:**

Edit config file:
- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
```json
{
  "mcpServers": {
    "mcp-server-chart": {
      "command": "npx",
      "args": ["-y", "@antv/mcp-server-chart"],
      "env": {
        "VIS_REQUEST_SERVER": "http://localhost:3000/generate"
      }
    }
  }
}
```

Restart Claude Desktop.

**For Python:**
```bash
pip install mcp
```


### Step 3: Generate Charts!

Ask Claude: *"Create a pie chart showing: Apples 40%, Oranges 35%, Bananas 25%"*

Or use Python:
```python
python examples/generate_chart.py
```

## 🐍 Python Integration

### Installation
```bash
pip install mcp
```

### Example: Generate Chart
```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def generate_chart():
    server_params = StdioServerParameters(
        command="npx",
        args=["-y", "@antv/mcp-server-chart"],
        env={"VIS_REQUEST_SERVER": "http://localhost:3000/generate"}
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
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
            print(f"Chart URL: {chart_url}")
            return chart_url

asyncio.run(generate_chart())
```

## 📊 Supported Chart Types

| Chart Type | Description | Use Case |
|------------|-------------|----------|
| Pie | Proportional data | Market share, percentages |
| Bar | Horizontal comparisons | Category rankings |
| Column | Vertical comparisons | Time series, groups |
| Line | Trends over time | Stock prices, growth |
| Area | Cumulative trends | Total over time |
| Scatter | Correlations | Data relationships |
| Radar | Multi-dimensional | Performance metrics |
| Histogram | Distribution | Data frequency |
| Boxplot | Statistical summary | Data spread |
| Funnel | Process stages | Conversion rates |
| **+15 more** | | |

Full list: area, bar, boxplot, column, dual-axes, fishbone, flow, funnel, histogram, line, liquid, mind-map, network, organization, pie, radar, sankey, scatter, treemap, venn, violin, word-cloud

## 📁 Project Structure
```
mcp-chart-system/
├── README.md
├── examples/
│   ├── generate_chart.py          # Basic Python example
│   ├── advanced_examples.py       # Multiple chart types
│   └── generated_charts/          # Sample outputs
├── docker/
│   └── docker-compose.yaml        # Alternative deployment
└── docs/
    ├── architecture.md
    └── api-reference.md
```

## 🔧 Advanced Configuration

### Custom Port
```bash
docker run -p 8080:3000 \
  -e RENDERED_IMAGE_HOST_PATH=http://localhost:8080/charts \
  ghcr.io/yaonyan/gpt-vis-mcp:latest-http
```

Update config:
```json
{
  "env": {
    "VIS_REQUEST_SERVER": "http://localhost:8080/generate"
  }
}
```

### Docker Compose Deployment
```yaml
services:
  rendering:
    image: ghcr.io/yaonyan/gpt-vis-mcp:latest-http
    ports:
      - "3000:3000"
    environment:
      - RENDERED_IMAGE_HOST_PATH=http://localhost:3000/charts
```

## 🧪 Testing

### Test Rendering Service
```bash
curl -X POST http://localhost:3000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "type": "pie",
    "data": [
      {"category": "A", "value": 30},
      {"category": "B", "value": 70}
    ]
  }'
```

Expected response:
```json
{
  "success": true,
  "resultObj": "http://localhost:3000/charts/chart_xxxxx.png"
}
```

## 🛠️ Tech Stack

- **Containerization:** Docker
- **MCP Server:** @antv/mcp-server-chart (Node.js)
- **Rendering:** GPT-Vis-SSR (AntV visualization libraries)
- **Python SDK:** mcp (async/await)
- **Protocol:** Model Context Protocol (MCP)
- **API:** REST (HTTP/JSON)

## 📈 Performance

- **Chart Generation:** < 2 seconds
- **Memory Usage:** ~200MB (Docker container)
- **Concurrent Requests:** Supports multiple simultaneous generations
- **Output Format:** PNG images

## 🔒 Privacy & Security

- ✅ 100% local processing
- ✅ No external API calls
- ✅ No data sent to third parties
- ✅ Self-hosted rendering
- ✅ Open-source components


## 📚 Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [AntV GPT-Vis](https://github.com/antvis/GPT-Vis)
- [MCP Server Chart](https://github.com/antvis/mcp-server-chart)




---


