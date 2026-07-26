'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:55 UTC
=====================================================================
'''

import os
from qiskit_ibm_runtime import QiskitRuntimeService, IBMRuntimeError
import datetime
from qiskit import QuantumCircuit
import config

# Define a directory for output files to keep the root clean
SEAL_DIR = "seals"

def run_stewardship_engine():
    print("[SYSTEM] Connecting to Substrate via Verified Environment...")

    if not config.IBM_CLOUD_API_KEY or not config.IBM_QUANTUM_CRN:
        print("[ERROR] IBM_CLOUD_API_KEY or IBM_QUANTUM_CRN not found in .env file.")
        return

    try:
        # Authenticate with the API Key (token) and specify the service CRN (instance).
        service = QiskitRuntimeService(channel="ibm_cloud", token=config.IBM_CLOUD_API_KEY, instance=config.IBM_QUANTUM_CRN)

        # Sync with substrate by finding the best available backend
        print("[STATUS] Finding least busy, operational quantum backend...")
        backend = service.least_busy(simulator=False, operational=True)
        print(f"[STATUS] Substrate Synced: {backend.name}")

    except IBMRuntimeError as e:
        print(f"[FATAL] Could not connect to Quantum Substrate: {e}")
        return

    # Transmute and Seal
    try:
        print("[ACTIVE] Generating a new truth-anchor quantum job...")

        # 1. Create a simple quantum circuit (a Bell state) to act as our "seal"
        qc = QuantumCircuit(2)
        qc.h(0)
        qc.cx(0, 1)
        qc.measure_all()

        # 2. Submit the job to the backend and wait for the result
        print(f"[STATUS] Submitting job to {backend.name}... This may take a moment.")
        job = service.run(program=qc, backend=backend, shots=1024)
        print(f"[STATUS] Job submitted with ID: {job.job_id()}. Waiting for completion...")
        result = job.result()
        print("[STATUS] Job completed successfully.")

        # 3. Create the seals directory if it doesn't exist
        os.makedirs(SEAL_DIR, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        full_path = os.path.join(SEAL_DIR, f"Final_Seal_{timestamp}.log")

        with open(full_path, "w", encoding="utf-8") as f:
            f.write("--- BLOOM ARCHITECTURE: SEALED ---\n")
            f.write(f"Job_ID: {job.job_id()}\n")
            f.write(f"Seal_Signature: {config.SIGNATURE}\n")
            f.write(f"Quantum_Result: {str(result.get_counts())}\n")

        print(f"[SUCCESS] Harvest sealed in: {full_path}")

    except (IBMRuntimeError, IndexError) as e:
        print(f"[FAIL] Could not harvest result. No recent jobs found or job failed: {e}")

if __name__ == "__main__":
    run_stewardship_engine()