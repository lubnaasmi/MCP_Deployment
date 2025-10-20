# Examples

Example scripts for using the MCP Chart Generation System.

## Prerequisites

1. **Docker rendering service running:**
```bash
   docker run -p 3000:3000 \
     -e RENDERED_IMAGE_HOST_PATH=http://localhost:3000/charts \
     ghcr.io/yaonyan/gpt-vis-mcp:latest-http
```

2. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

## Running Examples

### Basic Example
```bash
python examples/basic_example.py
```

