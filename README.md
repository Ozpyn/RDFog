# RDFog
A point cloud visualizer for RDF data with distributed storage.

## Quick Start

1. **Clone and install:**
   ```bash
   git clone https://github.com/yourusername/RDFog.git
   cd RDFog
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Start distributed RDF servers:**
   ```bash
   sudo docker-compose up -d
   ```

3. **Run the visualizer:**
   ```bash
   python3 main.py
   ```

## What It Does
- Starts two Fuseki RDF servers with sample data
- Queries data from both servers using federated SPARQL
- Visualizes the combined RDF graph as a point cloud

## Endpoints
- Server 1: `http://localhost:3030`
- Server 2: `http://localhost:3031`

## Troubleshooting
- **No data?** Check: `sudo docker logs fuseki1`
- **Permission error?** Make sure: `chmod +x entrypoint.sh`
- **Restart fresh:** `sudo docker-compose down -v && sudo docker-compose up --build -d`