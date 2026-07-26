'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:55 UTC
=====================================================================
'''

from qiskit_ibm_runtime import QiskitRuntimeService
import config

if not config.IBM_CLOUD_API_KEY or not config.IBM_QUANTUM_CRN:
    print("[ERROR] IBM_CLOUD_API_KEY or IBM_QUANTUM_CRN not found in .env file.")
    exit()

# Authenticate with the API Key (token) and specify the service CRN (instance).
service = QiskitRuntimeService(channel="ibm_cloud", token=config.IBM_CLOUD_API_KEY, instance=config.IBM_QUANTUM_CRN)

print("[SYSTEM] Authentication successful.")
print("[INSTANCES] Available instances:", service.instances())