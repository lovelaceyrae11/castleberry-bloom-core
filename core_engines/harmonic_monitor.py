'''
=====================================================================
HARMONIC SEAL: Love over God. Protected by Lacey Rae Castleberry (Velath'kai)
AXIOM: Love_Over_God_Equilibrium
BASELINE FREQUENCY: 528.0 Hz
ORGANIZED BY: Remnant Workspace Auto-Organizer
TIMESTAMP: 2026-07-26 21:02:56 UTC
=====================================================================
'''

import json
import time
import random
import os

REGISTRY_FILE = "calibrated_vault.json"

def monitor_nodes():
    if not os.path.exists(REGISTRY_FILE):
        print(f"[ERROR] Registry file '{REGISTRY_FILE}' not found. Cannot simulate drift.")
        return

    while True:
        try:
            # Load the registry
            with open(REGISTRY_FILE, "r+", encoding="utf-8") as f:
                registry_data = json.load(f)

                # Select a random node to apply drift to
                if not registry_data:
                    print("[WARN] Registry is empty. Nothing to monitor.")
                    time.sleep(10)
                    continue

                target_node = random.choice(registry_data)
                # Ensure we are modifying the correct, unified structure
                if "lattice_topology" in target_node and "case_metadata" in target_node:
                    node_id = target_node["case_metadata"].get("case_id", "Unknown Node")
                    # Inject high entropy to simulate drift
                    target_node["lattice_topology"]["entropy"] = round(random.uniform(0.75, 0.99), 2)
                    target_node["status"] = "DRIFTING"
                    print(f"[DRIFT DETECTED] Node: {node_id} | Entropy set to: {target_node['lattice_topology']['entropy']}")

                # Write the modified data back to the file
                f.seek(0)
                json.dump(registry_data, f, indent=4)
                f.truncate()
        except (json.JSONDecodeError, IOError) as e:
            print(f"[ERROR] Could not process registry file: {e}")

        time.sleep(10) # Wait before causing the next drift event

if __name__ == "__main__":
    monitor_nodes()