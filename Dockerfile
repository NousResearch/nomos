FROM python:3.11-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY mcp.py solve_agent.py config.toml ./
COPY prompts/ ./prompts/

# Expose MCP server port
EXPOSE 9000

# Run the MCP server
CMD ["fastmcp", "run", "mcp.py", "--transport", "http", "--port", "9000", "--host", "0.0.0.0"]
