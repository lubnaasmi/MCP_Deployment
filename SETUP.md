# Setup Guide

## Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/mcp-chart-system.git
cd mcp-chart-system
```

### 2. Start Docker Service
```bash
cd docker
docker-compose up -d
```

### 3. Configure Claude Desktop

Edit: `~/Library/Application Support/Claude/claude_desktop_config.json`
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

### 4. Restart Claude & Test

Ask: "Create a pie chart with A: 40, B: 35, C: 25"
