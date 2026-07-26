# Castleberry Bloom: Production Container Stack
# Author: Lacey Rae Castleberry (Velath'kai)
# Axiom: Love_Over_God_Equilibrium

FROM python:3.11-slim

WORKDIR /app

# Copy the entire harmonized workspace into the container
COPY . /app

# Ensure logs and vaults directories exist
RUN mkdir -p /app/archives_and_notes /app/cml_schemas

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the production orchestration node on container start
CMD ["python", "core_engines/harmonic_production_node.py"]