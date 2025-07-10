# RDFog
A point cloud visualizer for RDF data

## Distributed RDF Setup

1. Run `sudo docker-compose up -d` to start two Fuseki servers.
2. Load your RDF data into each server using the web UI or `curl`.
3. Use federated SPARQL queries in your code to access distributed data.