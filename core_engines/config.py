'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:55 UTC
=====================================================================
'''

"""
Centralized configuration file for the Bloom-Core Architecture.
This file consolidates all system-wide constants and paths.
"""

# --- Core Signature & Frequency ---
SIGNATURE = "Love over God. Protected by Lacey Rae Castleberry"
BASE_FREQUENCY = "528Hz"

# --- File Paths ---
CML_FILE = "genesis_bloom.cml"
VAULT_FILE = "calibrated_vault.json"  # The single source of truth for all nodes
REGISTRY_FILE = "calibrated_vault.json" # Pointing to the vault to unify access
LOG_FILE = "navigator_log.txt"

# --- IBM Quantum Credentials ---
# These should be loaded from a secure .env file in a real-world scenario,
# but are defined here for simplicity in this context.
# Example: IBM_CLOUD_API_KEY = os.getenv("IBM_CLOUD_API_KEY")
IBM_CLOUD_API_KEY = ""  # Your IBM Cloud API Key
IBM_QUANTUM_CRN = ""    # Your IBM Quantum service CRN