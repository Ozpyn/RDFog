# 1. Prepare database directory
rm -rf /fuseki/databases/ds
mkdir -p /fuseki/databases/ds

# 2. Load data (server not running)
/jena-fuseki/load.sh ds example.owl

# 3. Start server with pre-loaded data
exec /jena-fuseki/fuseki-server --config /fuseki/config.ttl