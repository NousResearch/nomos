# Nomos Solver MCP - Docker

## Build
```bash
docker build -t nomos-solver-mcp .
```

## Run
```bash
docker run -p 9000:9000 nomos-solver-mcp
```

## With custom config
```bash
docker run -p 9000:9000 -v $(pwd)/config.toml:/app/config.toml nomos-solver-mcp
```

## Environment variables
Set `API_KEY` if needed:
```bash
docker run -p 9000:9000 -e API_KEY=your-key-here nomos-solver-mcp
```

---

## Docker Compose

### Quick start
```bash
docker-compose up -d
```

### Build and run
```bash
docker-compose up --build
```

### Stop
```bash
docker-compose down
```

### View logs
```bash
docker-compose logs -f nomos-solver-mcp
```

### Environment variables
Create a `.env` file:
```env
API_KEY=your-key-here
```

**Note**: Adjust `base_url` in `config.toml` to point to your model server (use host IP instead of localhost when running in Docker).
